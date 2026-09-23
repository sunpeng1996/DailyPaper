---
title: 'Agensh: Scaling Organizational Intelligence to 1,024 Agents'
title_zh: Agensh：可扩展至1024个Agent的自组织多智能体框架
authors:
- Zhihao Zhan
- Ting Song
- Li Dong
- Shaohan Huang
- Jianxun Lian
- Yan Xia
- Furu Wei
affiliations:
- Microsoft Research
arxiv_id: '2609.26781'
url: https://arxiv.org/abs/2609.26781
pdf_url: https://arxiv.org/pdf/2609.26781
published: '2026-09-22'
collected: '2026-09-23'
category: MultiAgent
direction: 多智体 · 无中心大规模自组织协作
tags:
- Multi-Agent
- Self-Organized
- Decentralized Coordination
- Scalable Agent
- Organizational Intelligence
one_liner: 无中心编排的自组织多Agent框架，支持千级规模协作，提升复杂任务效率与效果
practical_value: '- 复杂多Agent任务可放弃中心化编排架构，采用「共享工作空间+消息接口+共享上下文」三板斧的自组织模式，解决中心化调度的性能瓶颈，可直接迁移到电商大促智能客服集群、广告素材批量生成等高并发Agent任务场景

  - 可复用标准化共享上下文设计：定义OBSERVED/FACT/FAIL/CLAIM/PATCH_SUMMARY等固定格式的可复用条目，避免多Agent重复劳动，适配推荐系统多Agent做用户调研、竞品分析、素材生成的协作场景

  - Agent数量是可落地的优化维度：底层模型能力固定时，增加合法协作的Agent数量可同时提升任务完成率和完成速度，可用于电商活动规则校验、商品合规审核等重时效、高复杂度任务的横向扩容'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多Agent框架普遍采用中心化编排器- worker架构，系统规模上限受编排器的任务分配、协同调度能力约束，无法支撑大规模Agent并行协作，难以满足低时延、高复杂度长周期任务的需求。

### 方法关键点
- 无中心自组织架构：所有Agent地位平等，无统一调度节点，每个Agent独立执行异步协作循环：收集上下文→认领子任务→执行动作→验证结果→合并进度
- 三层协作基础设施：1）共享工作空间（基于Git实现）：存储待办、进行中、已完成的工作，支持版本管理和冲突合并；2）消息接口：支持全局公告和一对一私信，解决子任务认领冲突、依赖协商问题；3）共享上下文：基于Append-only日志存储标准化的观察、事实、失败尝试、任务认领、变更摘要等信息，支持全局搜索复用
- 兼容现有单Agent框架：仅通过Prompt植入协作规则，无需修改底层单Agent的推理逻辑，可快速对接不同LLM Agent底座

### 关键实验
在ProgramBench的5个最难代码复现任务上测试，底层统一用GPT-5.6-sol，时间预算6小时：
1. 规模从1→128个Agent：平均测试通过率从19.31%提升到28.78%，相对提升49%；同等通过率下，128Agent耗时仅为8Agent的1/3
2. pandoc任务规模从1→1024个Agent：测试通过率从33.89%提升到55.06%，千级规模下仍有稳定性能收益

### 核心结论
Agent数量是多智能体组织的新 scaling 维度，自组织协作是突破大规模多Agent系统性能瓶颈的可行路径
