---
title: 'T-RoPE: Time-Aware Rotary Position Embedding for Sequential Recommendation'
title_zh: 面向序列推荐的时间感知旋转位置编码T-RoPE
authors:
- Yang Liu
- Noel Loo
- Ali Khanafer
- Shuying Sun
- Akshay Soni
- Zhong Wu
- Linjun Yang
affiliations:
- Shopify
- Massachusetts Institute of Technology
- Liquid AI
arxiv_id: '2609.30576'
url: https://arxiv.org/abs/2609.30576
pdf_url: https://arxiv.org/pdf/2609.30576
published: '2026-09-24'
collected: '2026-09-28'
category: RecSys
direction: 序列推荐 · 时间感知位置编码优化
tags:
- RoPE
- Sequential Recommendation
- Positional Encoding
- Temporal Modeling
- Transformer
one_liner: 提出兼容原生RoPE接口的时间感知位置编码，适配序列推荐的时序间隔、周期与季节性特征
practical_value: '- 可直接替换现有Transformer/生成式推荐模型的RoPE为T-RoPE，兼容原生接口，几乎无需改动架构即可获得时序建模增益

  - 多尺度频率银行设计可复用：用几何间隔的时间频率覆盖业务常见的用户行为周期，结合可学习系数自适应选择核心周期，无需手动做时间特征分桶

  - Shifted Query对齐trick可直接落地：训练时将query时间偏移到下一交互时间，推理时替换为当前请求时间，同一模型可无缝适配不同季节、促销期的上下文需求

  - 工业场景下可与Time RAB等现有时间偏置方案叠加使用，两者信号互补，进一步提升时序推荐效果，线上实测可带来CVR、订单量的正向提升'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前序列推荐大量复用LLM的Transformer技术栈，包括RoPE位置编码，但传统RoPE仅基于序列索引编码，只保留交互先后顺序，完全丢失真实时间间隔、用户行为多尺度周期、日历季节相位三类核心时序信号；现有时间增强方案要么仅做时间分桶偏置，要么仍保持时间平移不变性，无法区分不同季节的相同行为序列，导致时序信号利用不足。

### 方法关键点
- 替换序列索引为真实Unix时间戳计算旋转角度，采用几何间隔的多尺度频率银行覆盖10²~10⁸秒的时间周期，匹配从小时到跨年的用户行为规律
- 新增query和key独立的可学习时间系数，自适应调整不同时间尺度的权重，不同层可学习差异化的时序敏感度
- 采用Shifted Query对齐：训练时query的时间偏移到下一个交互的时间戳，推理时替换为当前请求时间，同一历史序列可适配不同预测时间的上下文
- 引入非平稳key旋转：对key使用旋转矩阵的转置，打破RoPE的时间平移不变性，让模型可感知日历季节等绝对时间相位

### 关键实验
在5个公开基准数据集上全指标优于所有基线，稀疏PixelRec数据集HR@10较最优基线提升78~130%，Amazon Books数据集全指标提升8~12%；在Shopify 60亿交互的工业数据集上，较HSTU+Time RAB基线全指标提升13~82%，消融显示多尺度频率银行贡献最大（NDCG@50提升56%）；线上A/B测试实现CVR+0.33%、订单量+0.63%的正向收益，额外开销仅随序列长度和头维度线性增长。

### 核心结论
把位置编码的锚点从序列顺序改为真实时间，是适配电商等强时序推荐场景的低成本高收益优化方案
