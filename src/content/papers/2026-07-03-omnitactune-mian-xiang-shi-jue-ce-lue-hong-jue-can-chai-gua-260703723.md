---
title: 'OmniTacTune: Policy-Agnostic Real-World RL for Tactile Residual Adaptation
  of Visual Policies'
title_zh: OmniTacTune：面向视觉策略触觉残差适配的策略无关现实世界RL方法
authors:
- Kelin Yu
- Haode Zhang
- Harish Ravichandar
- Yunhai Han
- Ruohan Gao
affiliations:
- University of Maryland, College Park
- Georgia Institute of Technology
arxiv_id: '2607.03723'
url: https://arxiv.org/abs/2607.03723
pdf_url: https://arxiv.org/pdf/2607.03723
published: '2026-07-03'
collected: '2026-07-12'
category: Other
direction: 机器人视触策略适配 现实世界强化学习
tags:
- Reinforcement Learning
- Tactile Sensing
- Visual Policy
- Residual Learning
- Robot Manipulation
one_liner: 提出两阶段策略无关RL管线，通过触觉残差校正大幅提升预训练视觉策略接触任务成功率
practical_value: '- 核心为机器人操作领域技术方案，电商/搜推/Agent业务直接可复用场景有限

  - 预训练base模型适配新模态信号时采用残差增量微调的思路，可迁移到搜推场景预训练排序模型适配新特征的需求，降低重训成本

  - 两阶段适配范式（先base策略自主采样warmstart再在线微调）可参考用于降低新特征/新策略上线的冷启动成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
预训练视觉策略在强接触类机器人操作任务中表现极差，触觉信号可补充局部力与接触几何信息，但触觉数据采集成本高、跨传感器/机器人/任务泛化难，缺乏高效将触觉信号适配到现有视觉策略的方案。

### 方法关键点
1. 提出策略无关的两阶段RL管线OmniTacTune，通过残差校正实现触觉信号对预训练视觉策略的适配，无需重训base视觉模型；
2. 第一阶段通过base策略自主rollout采样数据，完成触觉感知学习的warmstart，降低对标注触觉数据的依赖；
3. 第二阶段通过在线交互学习轻量级触觉残差策略，快速适配不同任务需求。

### 关键结果
在4个真实世界强接触任务中，仅需40-80分钟微调，即可将原视觉策略的成功率从5%-40%提升至85%-100%，兼容不同架构的base视觉策略、不同类型的触觉表征。
