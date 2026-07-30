---
title: 'Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through
  Latent Guidance'
title_zh: Reinformed Dreamer：基于隐空间引导高效训练的非对称世界模型
authors:
- Gaspard Lambrechts
- Adrien Bolland
- Daniel Ebi
- Damien Ernst
affiliations:
- McGill University
- Mila Québec Artificial Intelligence Institute
- Université de Liège
- Karlsruhe Institute of Technology
arxiv_id: '2607.26040'
url: https://arxiv.org/abs/2607.26040
pdf_url: https://arxiv.org/pdf/2607.26040
published: '2026-07-28'
collected: '2026-07-30'
category: Training
direction: 强化学习 · 非对称世界模型训练优化
tags:
- World Model
- Asymmetric RL
- Latent Guidance
- Model-based RL
- Representation Learning
one_liner: 针对Informed Dreamer特权信息表征缺陷，提出隐空间引导的非对称表征学习目标，稳定提升基于模型RL性能
practical_value: '- 针对推荐/Agent系统中多源特权信息（如用户侧未暴露行为标签、商家侧运营数据）的表征学习，可复用隐空间引导对齐目标，在推理侧无需特权信息的前提下提升表征质量

  - 构建模拟用户行为/电商环境的世界模型时，可采用非对称训练范式，训练阶段接入全量信息做引导，部署阶段仅用可观测特征输入，兼顾效果和部署成本

  - 可借鉴特权信息表征缺陷的分析思路，排查现有多模态/多源特征融合方案中存在的隐空间对齐不足、信息泄露等问题'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
非对称强化学习范式可在训练阶段引入额外特权信息提升效果，但现有基于模型的非对称RL算法Informed Dreamer存在特权信息表征缺陷，效果提升不稳定，无法充分释放非对称学习的收益。
### 方法关键点
1. 定位Informed Dreamer特权信息表征学习的核心瓶颈，明确此前方案信息对齐逻辑的不足；
2. 设计基于隐空间引导的新型非对称表征学习目标，训练阶段用特权信息引导观测表征的隐空间对齐，推理阶段无需接入特权信息，输出Reinformed Dreamer算法。
### 关键结果
在多个基准测试集上，相比原始Dreamer算法，效果提升的稳定性显著优于所有此前的非对称改进方案，无负向性能波动案例。
