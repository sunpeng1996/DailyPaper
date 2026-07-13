---
title: Taste-aware music retrieval from audio embeddings
title_zh: 基于音频嵌入的味觉感知音乐检索
authors:
- Matteo Spanio
- Antonio Rodà
affiliations:
- University of Padua
arxiv_id: '2607.03296'
url: https://arxiv.org/abs/2607.03296
pdf_url: https://arxiv.org/pdf/2607.03296
published: '2026-07-03'
collected: '2026-07-13'
category: Multimodal
direction: 跨模态音乐检索 · 声味关联挖掘
tags:
- Multimodal Retrieval
- Audio Embedding
- Crossmodal Learning
- Content-based Retrieval
- Music Recommendation
one_liner: 构建音频预测味觉的音乐检索基准，验证多编码器融合效果优于SOTA与普通标注者
practical_value: '- 食品广告、线下餐饮BGM推荐场景可直接复用验证过的声-味关联特征，提升背景音乐与场景的匹配度

  - 跨模态标签预测场景可采用「冻结预训练编码器+轻量多任务回归头」的低成本方案，无需全量微调大模型

  - 检索/推荐排序优化可引入异构编码器门控晚融合策略，在不增加预测误差的前提下显著提升排序相关性'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
心理学已证实声音与味觉存在稳定跨模态关联，但该关联未被应用到内容类多媒体检索中，食品广告、餐饮场景的音乐匹配缺乏标准化落地基准。

### 方法关键点
1. 构建经过感知验证的多源语料，将音频预测味觉任务标准化为音乐信息检索基准；
2. 对比4类HEAR系列共10个冻结音频编码器，共用多任务回归头，支持门控晚融合可选配置；
3. 采用绝对误差、秩相关评估效果，搭配岭探针、音频阻带 knockout 验证声味关联有效性。

### 关键结果
最优系统五类味觉预测宏RMSE达0.134，较前SOTA的0.219下降39%；真实音乐集上RMSE仅0.13，不到普通标注者偏差（0.28）的一半；门控晚融合宏Pearson相关系数达0.724，比单VGGish的0.666提升8.7%；基于预测味觉空间的309条音乐排序效果远优于随机水平的CLAP-text基线。
