---
title: Worth Another Look:Constrained World-Model Planning for Visual Inspection
title_zh: 重检优化：面向视觉检测的约束世界模型规划方法
authors:
- Ziyue Kang
- Zixi Qi
- Yuchen Dai
- Nana Lv
- Xirong Cheng
- Liang Liu
- Ying Li
- Haoyan Wei
- Haiyang Yao
affiliations:
- Shaanxi University of Science and Technology
arxiv_id: '2611.24187'
url: https://arxiv.org/abs/2611.24187
pdf_url: https://arxiv.org/pdf/2611.24187
published: '2026-11-18'
collected: '2026-11-22'
category: Agent
direction: 视觉检测Agent · 世界模型约束规划
tags:
- World Model
- Planning
- Visual Inspection
- Neuro-Symbolic
- Budget-Aware
one_liner: 无需重训冻结检测器，结合轻量世界模型与符号约束实现预算感知的自适应视觉检测规划
practical_value: '- 冻结基座+轻量世界模型+符号约束的架构可复用在电商广告/推荐的预算控制场景，无需重训大模型即可适配动态配额约束，降低调优成本

  - 滚动时域波束搜索+在线重规划的调度逻辑可迁移到多目标召回/多模态内容审核的算力分配场景，在紧 latency 约束下提升整体效果

  - slack感知影子定价策略可直接复用在大模型调用成本管控场景，预算充足时自动扩展能力边界，预算紧张时优先保障核心任务'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现场机器人、环境监测等场景的视觉检测需在严格算力、感知预算下定位多目标，现有穷举策略浪费检测资源，短视无搜索策略难以适配异构成本规则，无法感知二次查询的潜在价值。

### 方法关键点
1. 将冻结检测器的检测任务建模为部分可观测下的神经符号观测规划问题，解耦轻量循环世界模型与精确符号可行性、成本规则；
2. 采用带在线重规划的滚动时域波束搜索，联合调度类别查询、裁剪、增强、终止动作，大预算场景搭配松弛感知影子定价与合法 fallback 策略。

### 关键结果
8个陆地、光学、声呐基准测试中，紧预算下多步前瞻比静态优先级策略在RUOD数据集AP提升28.4个点，ARIS数据集提升15.1个点；动态定价策略在所有8个场景大预算下均提升性能，单次规划仅11ms。
