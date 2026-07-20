---
title: 'Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours
  of Real-World Trajectories'
title_zh: 小米机器人1：基于10万+小时真实轨迹的规模化视觉-语言-动作模型
authors:
- Xiaomi Robotics Team
- Jun Guo
- Piaopiao Jin
- Jason Li
- Peiyan Li
- Yingyan Li
- Futeng Liu
- Wanli Peng
- Optimus Qin
- Yifei Su
affiliations:
- Xiaomi Robotics Team
arxiv_id: '2607.15330'
url: https://arxiv.org/abs/2607.15330
pdf_url: https://arxiv.org/pdf/2607.15330
published: '2026-07-15'
collected: '2026-07-20'
category: Other
direction: 机器人VLA模型 规模化训练
tags:
- VLA
- Foundation Model
- Auto-labeling
- Scaling Law
- Robot Learning
one_liner: 提出两阶段训练的VLA基础模型，基于10万+小时真实轨迹训练，泛化性强且下游微调效率高
practical_value: '- 两阶段（预训练+后对齐训练）范式可直接迁移至多模态业务Agent训练：预训练先学习通用跨模态能力，后训练对齐业务场景指令，大幅提升零样本泛化性能

  - 可扩展自动标注流水线思路可复用：对电商/推荐场景海量用户行为轨迹做自然语言标注，用于多模态生成式推荐模型训练，降低人工标注成本

  - Scaling Law验证结论可指导模型迭代：算力充足时，优先提升预训练数据规模、模型大小可直接带来下游少样本/零样本性能提升，明确迭代优先级'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有机器人VLA模型零样本泛化性弱，下游新任务微调数据需求量大，缺乏大规模真实世界轨迹数据支撑规模化能力升级。
### 方法关键点
1. 两阶段训练范式：预训练阶段基于UMI设备采集的10万+小时真实世界操作轨迹训练，配套可扩展自动标注流水线，用描述场景状态转移的自然语言标注轨迹片段，为动作学习提供精准监督；
2. 后训练阶段对齐预训练能力与机器人本体、人类自然指令，将状态转移理解映射为可执行的任务指令。
### 关键结果
RoboCasa365基准成功率达57.6%，超此前SOTA 11个百分点；RoboDojo基准平均分20.07，超此前SOTA 53.7%；模型性能随预训练数据量、模型规模提升单调上涨，该缩放效应可直接迁移到后训练阶段，少样本微调效率提升显著。
