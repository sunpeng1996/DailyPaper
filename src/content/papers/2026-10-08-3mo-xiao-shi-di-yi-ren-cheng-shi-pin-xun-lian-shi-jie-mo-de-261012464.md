---
title: What 30,000 Hours of Ego-centric Video Does Not Teach
title_zh: 3万小时第一人称视频训练世界模型的能力边界分析
authors:
- Jiahua Dong
- Anurag Bagchi
- Yash Jangir
- Muhammad Zubair Irshad
- Sergey Zakharov
- Martial Hebert
- Homanga Bharadhwaj
- Yu-Xiong Wang
- Vitor Campagnolo Guizilini
- Pavel Tokmakov
affiliations:
- University of Illinois Urbana-Champaign
- Carnegie Mellon University
- Johns Hopkins University
- Toyota Research Institute
arxiv_id: '2610.12464'
url: https://arxiv.org/abs/2610.12464
pdf_url: https://arxiv.org/pdf/2610.12464
published: '2026-10-08'
collected: '2026-10-11'
category: Agent
direction: 世界模型 · Agent交互保真度评估
tags:
- World Model
- Ego-centric Video
- Agent Modeling
- Fidelity Evaluation
- Data Scaling
one_liner: 通过3万小时第一人称视频实验，验证世界模型缩放中智能体建模先饱和、物体交互保真度提升滞后
practical_value: '- 数据缩放并非提升模型效果的唯一路径，可优先优化视觉条件注入等架构设计，用少量数据即可达到核心任务的饱和效果

  - 多目标建模时可通过监督方案调整模型容量分配，比如将分配给非核心场景外观的容量转移到核心动态交互任务上，提升核心指标

  - 模型评估不要只依赖黑盒下游指标，可针对核心子任务设计单独的保真度评估维度，更易定位性能瓶颈'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
世界模型是物理模拟器的潜在替代方案，但距离落地差距较大，第一人称视频数据缩放对世界模型的能力提升边界尚不明确。
### 方法关键点
- 采用覆盖1000+场景、1.4万贡献者的3万小时第一人称视频数据集训练世界模型
- 放弃黑盒下游指标，直接在分布外基准上评估智能体建模、物体交互两个维度的保真度
- 设计优化视觉条件注入模块，以及将模型容量从场景外观转移到物体动态的监督方案
### 关键结果
- 训练数据扩容100倍后两类指标均提升，但不均衡：智能体保真度接近饱和，物体保真度仅缓慢提升且差距显著
- 优化视觉条件后仅用少量数据即可达到智能体建模饱和效果，容量转移方案可提升物体保真度但仍有明显gap，结论可迁移到人形建模任务
