---
title: 'HELIX: Purified and Unified - Rethinking Feature Interaction and Sequence
  Modeling for Large-Scale Recommendation'
title_zh: HELIX：面向大规模推荐的特征交互与序列建模统一提纯架构
authors:
- Yuntao Zheng
- Miao Zhang
- Yadong Ding
- Yanchuan Tang
- Lixiyu Chen
- Hao Wang
- Quan Li
- Shiying Cai
- Yue Lin
- Jiayu Li
affiliations:
- ByteDance
- TikTok Global E-Commerce Recommendation Video Team
arxiv_id: '2609.37183'
url: https://arxiv.org/abs/2609.37183
pdf_url: https://arxiv.org/pdf/2609.37183
published: '2026-09-29'
collected: '2026-09-30'
category: RecSys
direction: 大规模推荐排序 · 特征交互与序列建模联合优化
tags:
- Ranking
- FeatureInteraction
- SequenceModeling
- KVCache
- E-commerce
one_liner: 提出联合优化特征交互与序列建模的HELIX架构，在TikTok电商推荐获近6%GMV提升
practical_value: '- 特征交互模块可直接替换为MPTF（Mixup-PerToken-FFN），相比自注意力更适配异构特征，相同算力下可获得CTR/CVR
  AUC提升，同时降低显存占用

  - 落地时采用三流Token化+单向信息流设计，用户侧U-only序列产出的K/V缓存可跨候选复用，结合M-FALCON和用户级训练，最高可获得10倍以上训练/推理加速

  - 序列编码采用金字塔压缩策略，按特征重要度分配各序列Token预算，优先保留最近行为，可在降低序列计算成本的同时不损失排序效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐排序模型长期沿特征交互、序列建模两个独立方向迭代，单独缩放任一方向都存在明显性能天花板，现有统一架构存在特征交互算子效率低、用户侧计算无法跨候选复用等问题，难以匹配大规模电商推荐的效果与算力要求。
### 方法关键点
- 三流Token化设计：将非序列特征、候选依赖的U×C序列特征、候选无关的U-only序列特征分别编码为独立Token流
- 交错式双分支架构：SeqFormer编码器独立处理U-only序列生成可复用K/V缓存，MixFormer/SeqFormer解码器交错执行序列检索与MPTF特征交互，严格控制信息仅从序列分支流向特征交互分支
- 工程优化：采用金字塔序列压缩、可变长无Padding执行、用户侧计算跨候选/训练样本摊销策略，大幅降低训练推理成本
### 关键实验
在TikTok电商内部数据集验证，对比RankMixer+Transformer基线，HELIX-L参数量相当的情况下，CTR AUC相对提升0.21%、CVR AUC相对提升0.17%，推理FLOPs更低；在线A/B测试实现人均电商GMV提升5.99%、人均支付订单提升6.10%。缩放实验显示HELIX效果随算力增长呈稳定幂律提升，无饱和迹象。
### 核心结论
推荐模型要同时获得效果提升与算力收益，需联合优化特征交互与序列建模，并通过架构设计最大化用户侧公共计算的复用率。
