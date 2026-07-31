---
title: 'CCFormer: Efficient Cross-Field Interaction and Hierarchical Sequence Compression
  for Industrial Recommendation at Tencent'
title_zh: CCFormer：面向工业推荐的高效跨域交互与层级序列压缩框架
authors:
- Yunlong Wang
- Huizhe Zhang
- Haonan Hu
- Yudong Li
- Bing Wen
- Jianchao Tu
- Chengxiang Zhuo
- Zang Li
affiliations:
- Tencent Platform and Content Group
arxiv_id: '2607.28070'
url: https://arxiv.org/abs/2607.28070
pdf_url: https://arxiv.org/pdf/2607.28070
published: '2026-07-30'
collected: '2026-07-31'
category: RecSys
direction: 工业级长序列推荐排序优化
tags:
- Long-sequence Recommendation
- CTR Prediction
- Transformer
- Token Mixing
- Sequence Compression
one_liner: 提出兼顾跨域特征交互与长序列压缩的推荐Backbone，训练提速2.21倍，业务指标显著提升
practical_value: '- 可复用特征域分离交叉注意力设计，拆分用户、行为序列、候选Item三个域做定向交叉，减少全量自注意力冗余计算，提升长序列建模效率

  - 层级序列压缩+子空间Token Mixing组合可直接落地长序列排序场景，用卷积下采样逐步扩大感受野，几乎无损前提下训练速度提升2倍以上

  - 在线推理时复用用户/序列特征，批量打分同请求的多个候选Item，实测可提升30%峰值QPS，适配高吞吐的广告/电商推荐场景

  - 稀疏参数INT8量化+双哈希压缩的工程trick可直接复用，能减少约70%的Embedding表存储开销，无明显效果损失'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业长序列推荐中Transformer自注意力平方复杂度带来极高训练推理延迟，传统序列截断/压缩方案要么丢失细粒度行为信号，要么丢弃长期兴趣，难以平衡效果与效率。
### 方法关键点
- 特征域分离交叉注意力：拆分用户、行为序列、候选Item三个语义域，仅做定向交叉（用户检索序列、候选检索序列与用户），规避全量自注意力冗余计算
- 子空间相对时空编码：序列按时间分组，组内加入时间衰减系数与相对位置编码，时序依赖建模复杂度降至O(L*m)
- 长序列子空间Token Mixing：将序列按时间与特征维度分组，组内用MLP做Token混合替代自注意力，大幅降低计算开销
- 层级序列压缩：每层用1D卷积下采样，逐步扩大Token感受野，浅层捕捉短期细粒度兴趣、深层提取长期抽象偏好
### 关键结果
在Taobao、KuaiRec公开数据集与腾讯40亿样本工业数据集上，对比HSTU、STCA等工业SOTA基线，工业场景下AUC相对HSTU提升1.01%、GAUC提升2.40%，训练速度快2.21倍；在线A/B测试视频推荐场景CTR涨3.57%、广告收入涨1.64%，广告排序场景广告收入涨1.71%，已全量上线服务主流量。
> 长序列建模无需盲目堆长度，分层压缩+定向交叉可在更低算力成本下获得更优业务收益
