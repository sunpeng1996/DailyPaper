---
title: 'HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness'
title_zh: HarnessVLN：基于Agent调度层的免训练统一具身导航框架
authors:
- Yang Chen
- Lirong Che
- Zhenyu Huang
- Wenbo Fu
- Chuang Wang
- Xu Cao
- Daqi Liu
- Yuzhe Yang
- Jian Su
- Lan-Zhe Guo
affiliations:
- Nanjing University
- AGIBOT
- Tsinghua University
arxiv_id: '2609.15195'
url: https://arxiv.org/abs/2609.15195
pdf_url: https://arxiv.org/pdf/2609.15195
published: '2026-09-13'
collected: '2026-09-16'
category: Agent
direction: Agent 具身导航免训练框架设计
tags:
- Embodied Navigation
- Training-free
- MLLM
- Agent Orchestration
- Spatiotemporal Graph
- Zero-shot
one_liner: 提出免训练具身导航框架HarnessVLN，通过统一Agent调度接口协调多模块，性能超现有免训练SOTA
practical_value: '- 多模块Agent协调逻辑可复用：统一工具接口+规划结果三重校验的方案，可迁移到电商导购Agent、线下零售机器人场景，解决LLM生成动作/回复不符合业务约束的问题

  - 分层记忆设计可借鉴：分层事件记忆+持久化时空图谱的存储方案，可用于推荐系统用户行为序列建模、线下到店用户动线留存分析

  - 跨场景适配思路可参考：可替换执行器的设计，可复用到跨触点推荐Agent，无需重新训练即可适配直播、货架、私域不同场景的内容/动作输出要求'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
具身导航任务中训练类方法泛化性差，现有免训练MLLM方案缺乏动作与空间证据、任务进度、执行失败的对齐机制，落地受限。

### 方法关键点
1. 采用零样本免训练架构，Agent Harness层通过统一工具接口协调感知、检索、grounding、导航、故障恢复、终止全流程
2. 对规划器生成的动作做空间证据、几何可行性、子目标一致性三重校验，结构化工具反馈闭环迭代决策
3. 分层事件记忆跟踪任务进度，持久化Spatiotemporal Graph存储可复用空间证据与失败标注，支持校验与故障恢复
4. 可替换Navigation Executor将验证后的目标转化为可执行动作，同时支持指令跟随、物体目标两类导航任务

### 关键结果
在R2R、RxR、HM3D-v2、HM3D-OVON四个基准数据集上成功率分别达60.8%、53.9%、76.0%、59.3%，超越此前免训练SOTA，已完成人形机器人真实环境部署验证。
