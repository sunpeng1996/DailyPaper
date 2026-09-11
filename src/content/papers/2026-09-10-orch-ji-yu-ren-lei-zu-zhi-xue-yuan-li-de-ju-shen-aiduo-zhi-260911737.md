---
title: 'ORCH: Organizational Principles Enable Collective Intelligence in Embodied
  AI'
title_zh: ORCH：基于人类组织学原理的具身AI多智能体协作框架
authors:
- Zhengran Ji
- Jonathan Hyun
- Boyuan Chen
affiliations:
- Duke University
arxiv_id: '2609.11737'
url: https://arxiv.org/abs/2609.11737
pdf_url: https://arxiv.org/pdf/2609.11737
published: '2026-09-10'
collected: '2026-09-11'
category: MultiAgent
direction: 多智能体协作 · 组织层级自适应生成
tags:
- MultiAgent
- CollectiveIntelligence
- LLM
- OrganizationalDesign
- EmbodiedAI
one_liner: 将人类组织学依赖关系原理落地，构建任务自适应的多智能体层级协作结构，大幅提升复杂任务性能
practical_value: '- 多Agent系统架构可复用混合依赖设计：并行任务用水平管理器分配、有前置依赖的串行任务用垂直管理器管控，适配电商大促、多链路运营等混合需求场景

  - 层级组织生成可复用critic迭代优化机制：生成初始组织架构后用critic校验角色匹配、层级冗余度，减少无效管理层，降低多Agent通信/计算开销

  - LLM选型不用盲目追大参数：中等规模LLM在角色遵守、状态上报、任务对齐等多Agent协作场景表现可能优于大模型，可降低业务落地成本

  - 多Agent故障归因可参考本文分类：按执行层、任务分配层、协调层、规划层拆解失败原因，快速定位系统瓶颈'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有具身多智能体系统多采用固定组织结构，无法适配不同任务的差异化协调需求，团队规模扩大后易出现通信冗余、中心管理器过载、串行/并行任务协调混乱等问题，大规模异构多智能体的长周期复杂任务协作性能瓶颈突出。
### 方法关键点
- 借鉴人类组织学的两类依赖关系设计管理器：水平管理器协调可并行的共享依赖任务，分配并发子任务、汇总进度；垂直管理器协调有前置依赖的串行任务，拆解为有序阶段、管控阶段切换
- 支持人工/LLM生成任务专属层级组织：LLM生成时加入critic模块，迭代校验角色-能力匹配度、层级冗余度，避免无效管理层
- 执行阶段采用双向通信机制：自底向上逐层汇总进度，自顶向下逐层下发调整后的任务，保持层级间信息对齐的同时降低全局通信量
### 关键结果
在扩展的25个野火响应任务（覆盖侦察、救援、灭火等多场景，最多支持50个异构Agent）上，对比CAMON、COELA等4种主流多智能体框架，测试8款不同规模LLM：人工设计的ORCH组织相对基线平均最终得分提升63.97%、执行效率提升74.29%；LLM自动生成的ORCH组织对应提升43.63%、52.53%；中等规模模型（如Gemma-4-it、Qwen-3.6）的多Agent协作表现优于ChatGPT-5.4等大参数模型。

> 最值得记住的一句话：多智能体的集体性能不仅取决于单个Agent的能力，更取决于适配任务的组织结构设计，合理的组织架构可同时提升任务效果与资源使用效率
