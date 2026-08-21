---
title: 'DeltaMomentum: A Key-Value based Anisotropic Momentum Update via Delta Rule'
title_zh: DeltaMomentum：基于KV结构与Delta规则的各向异性动量更新方法
authors:
- Euijin Hong
- Guannan Qu
affiliations:
- Carnegie Mellon University
arxiv_id: '2608.19491'
url: https://arxiv.org/abs/2608.19491
pdf_url: https://arxiv.org/pdf/2608.19491
published: '2026-08-19'
collected: '2026-08-21'
category: Training
direction: 深度模型训练 · 优化器动量更新
tags:
- Optimizer
- Momentum
- LLM Training
- Delta Rule
- Computer Vision
one_liner: 提出基于KV结构与Delta规则的即插即用动量更新方法，显著降低各类模型训练步数
practical_value: '- 可直接替换现有LLM4Rec、搜索推荐排序模型训练时的优化器动量模块，无需改其他代码即可降低训练步数，节省算力成本

  - 训练垂域电商/广告LLM时可尝试引入DeltaAdamW，同等训练预算下可获得更低验证损失，提升模型生成/排序效果

  - 对于训练数据分布极度各向异性的用户行为序列建模场景，该动量更新规则可更快清除stale梯度方向，提升模型收敛稳定性'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有优化器动量均采用固定遗忘率的EMA，无法适配训练数据各向异性的特点（少量方向高频出现、多数方向极少出现），现有方案仅对动量缓存做额外处理，未修改动量更新逻辑本身。

### 方法关键点
1. 利用线性层梯度可拆分为作为key的输入、作为value的输出侧误差的KV结构，采用Delta规则更新动量缓存，每个梯度方向的遗忘率由其出现频率动态决定；
2. 无需矩阵求逆即可实现输入侧曲率校正，比EMA更快清除 stale 方向，可即插即用替换任意优化器的动量缓存，额外计算量仅为gated-MLP块线性层成本的22.2%-25%，无额外持久化内存开销。

### 关键结果
FineWeb-Edu预训练中，DeltaAdamW相比AdamW，67M模型训练步数最多减少46.39±4.32%，370M模型减少22.12±0.80%，1B参数模型下增益仍保持，效果优于同调参的Muon基线，在SGD、ResNet-18、ViT-Tiny等模型与CV任务上均有稳定增益
