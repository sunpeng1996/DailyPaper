---
title: 'Not all world models can doubt: how training objective and architecture shape
  epistemic uncertainty in JEPA and RSSM world models'
title_zh: 训练目标与架构对JEPA和RSSM世界模型认知不确定性的影响
authors:
- Simon Baur
- Wojciech Samek
- Jackie Ma
affiliations:
- Fraunhofer Heinrich-Hertz-Institut
arxiv_id: '2611.34830'
url: https://arxiv.org/abs/2611.34830
pdf_url: https://arxiv.org/pdf/2611.34830
published: '2026-11-25'
collected: '2026-11-27'
category: Agent
direction: Agent 世界模型认知不确定性优化
tags:
- World Model
- Epistemic Uncertainty
- JEPA
- RSSM
- Agent
one_liner: 实证对比JEPA与RSSM世界模型的认知不确定性差异，揭示架构和训练目标的影响机制
practical_value: '- 搭建决策类Agent（如电商导购Agent、广告投放优化Agent）时，若需精准感知分布外输入的不确定性，优先选择JEPA类无解码的联合嵌入架构，相比RSSM可减少小幅度/小目标输入偏差的漏检

  - 若采用RSSM类循环状态空间模型搭建世界模型，需额外补充小特征、单帧变化的感知旁路，规避循环平均和重建目标导致的不确定性漏报，降低决策风险

  - 两类世界模型的不确定性估计可直接复用last-layer Laplace或集成法的后验估计方案，无需改动原有模型训练流程，落地成本低'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
世界模型是Agent决策的核心基础，其认知不确定性（EU）是标记分布外输入、规避不可靠决策的核心信号，但不同架构和训练目标对EU估计的影响机制尚未被系统性验证。
### 方法关键点
控制变量对比两类主流世界模型的后验EU（last-layer Laplace、集成法）：无解码器的JEPA架构LeWorldModel，带循环隐状态重建的RSSM架构DreamerV3；在10个仿真视觉控制环境下追踪状态扰动从输入到EU输出的全链路传递过程，同时在5个不确定性相关下游任务验证性能差异。
### 关键结果
RSSM通过循环上下文平均、重建目标像素加权两个机制衰减扰动：单帧变化输入到隐状态时幅度被大幅削弱，小目标特征易被丢失；JEPA无上述衰减机制，扰动可全链路传递到不确定性输出；下游任务中RSSM会漏检自身后验已捕捉到的偏差，JEPA的不确定性输出与模型实际感知完全对齐。
