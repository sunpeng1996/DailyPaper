---
title: 'Ambient Discrete Diffusion: Using the Wrong Data at the Right Time for Data
  Efficient Learning'
title_zh: 环境离散扩散：在合适阶段利用异分布数据实现数据高效学习
authors:
- Julian Kleutgens
- Mauricio Tec
- Claudio Battiloro
- Francesca Dominici
- Giannis Daras
affiliations:
- ETH Zürich
- Harvard University
- MIT
arxiv_id: '2610.12340'
url: https://arxiv.org/abs/2610.12340
pdf_url: https://arxiv.org/pdf/2610.12340
published: '2026-10-08'
collected: '2026-10-10'
category: Training
direction: 离散扩散模型 · 少样本训练优化
tags:
- Discrete Diffusion
- Few-shot Learning
- Out-of-distribution
- Efficient Training
- Generative Model
one_liner: 提出RefineMix框架，基于离散扩散阶段特性引入OOD数据实现少样本无偏高效训练
practical_value: '- 生成式推荐少样本微调可借鉴阶段式引入OOD数据思路，低噪声阶段加入通用域用户行为/物品文本数据，既提泛化性又不引入偏置

  - 离散扩散用于生成商品文案、搜索Query等离散序列任务时，可复用分阶段训练策略，解决垂类场景训练数据不足问题

  - 跨域推荐生成式召回场景，可参考该方法的理论边界，明确不同噪声水平下跨域数据使用范围，避免分布偏移'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
离散扩散模型在文本、分子生成等场景表现优异，但垂类场景普遍存在训练数据稀缺问题，直接混合OOD数据训练易导致生成结果分布偏移，现有连续扩散的OOD利用方案无法直接适配离散扩散场景。

### 方法关键点
提出RefineMix框架，仅在离散扩散低噪声阶段引入OOD数据训练，此时不同域数据分布支撑集互不重叠，既能让模型学习通用特征，又不会导致采样分布偏置；高噪声阶段仅用域内数据训练，避免掩码保留的域信息带来的偏置影响，同时给出完整理论支撑。

### 关键结果
5个域偏移实验中效果持平或优于域内微调、直接数据混合方案；蛋白质生成任务仅用197个域内样本微调时，同时满足新颖、可折叠、属目标家族的生成蛋白占比相比标准微调提升近1倍。
