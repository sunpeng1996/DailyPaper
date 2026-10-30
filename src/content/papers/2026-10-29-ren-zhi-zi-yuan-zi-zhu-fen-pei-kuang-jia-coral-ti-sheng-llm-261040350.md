---
title: 'Don''t Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive
  Resource Self-Allocation'
title_zh: 认知资源自主分配框架CORAL：提升长程LLM Agent推理能力
authors:
- Zheng Zhu
- Xiaozhuan Liang
- Xi Chen
- Bei Yu
- Jiaya Jia
affiliations:
- The Chinese University of Hong Kong
- Tencent
- The Hong Kong University of Science and Technology
arxiv_id: '2610.40350'
url: https://arxiv.org/abs/2610.40350
pdf_url: https://arxiv.org/pdf/2610.40350
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: Agent 长程推理 · 工作记忆管理
tags:
- LLM Agent
- Long-Horizon Reasoning
- Working Memory
- Reinforcement Learning
- Context Optimization
one_liner: 提出认知资源自主分配框架CORAL，让Agent自主管理工作记忆，大幅提升长程任务性能并降低推理成本
practical_value: '- 电商导购Agent、多轮商品检索Agent等长交互场景可直接复用MM+CO工具设计：让Agent自主记录已验证的用户需求、商品属性等核心信息，上下文冗余时主动重置，既降低KV
  cache占用，避免历史无效交互干扰推理，还可降低6~7倍的token推理成本

  - 可迁移Multi-episode ARPO训练思路：训练长交互Agent时，将长轨迹拆分为独立的上下文重置片段，把全局奖励广播到所有片段，解决长程任务奖励稀疏、credit分配难的问题，适合多轮推荐Agent、多跳商品检索Agent的RL训练

  - 工程实现上无需依赖规则触发上下文压缩，将内存管理封装为Agent可调用工具，仅需千级样本SFT即可让基础模型掌握调用逻辑，业务端可快速落地迭代'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长程任务中LLM Agent的上下文会持续累积冗余的推理轨迹、工具返回结果，引发认知过载，导致推理精度与规划能力持续下降；现有上下文优化方案多依赖固定间隔、窗口即将占满等规则触发，易丢失关键信息，也无法打破「规划失效→冗余上下文→规划进一步失效」的恶性循环。
### 方法关键点
- 设计两套Agent可自主调用的工具：Memory Management（MM）持久化存储任务进度、已验证事实两类 checkpoint；Context Optimization（CO）主动重置上下文，仅保留系统提示、原始任务、MM存储的 checkpoint 作为新推理episode的初始输入，将长推理链拆分为多个独立短episode
- 两阶段训练：第一阶段SFT，将带CO拆分的多episode轨迹拆为独立样本训练，让模型掌握工具调用、checkpoint记录与上下文重置时机判断能力；第二阶段Multi-episode ARPO，将整条轨迹的最终奖励广播到所有关联episode，解决跨episode的credit分配问题，优化 checkpoint 策略
### 关键结果
- GAIA基准上，8B参数版平均精度达42.8%，Level 2/3长程任务精度显著领先同规模baseline，输入token消耗仅为ReAct Agent的1/6~1/7，LLM调用次数减少2/3
- BrowseComp长浏览任务上，无额外训练的CORAL直接将Claude Sonnet 4精度提升8.0个百分点，多跳Knowledge QA任务上也全面优于同期同类Agent

对于长程Agent，高效的注意力管理不是精度提升的额外成本，而是精度提升的核心来源
