---
title: 'DP-Rec: Towards Dynamic Patching for Efficient Long-Sequence Recommendation'
title_zh: DP-Rec：面向高效长序列推荐的动态补丁架构
authors:
- Dwipam Katariya
- Thomas Caputo
- Akshat Shreemali
- Juan Manuel Origgi
- Nikita Seleznev
- Pranab Mohanty
- Kalanand Mishra
- Nam Nguyen
- James Montgomery
affiliations:
- Capital One
arxiv_id: '2609.32215'
url: https://arxiv.org/abs/2609.32215
pdf_url: https://arxiv.org/pdf/2609.32215
published: '2026-09-26'
collected: '2026-09-29'
category: RecSys
direction: 长序列推荐 · 动态序列压缩
tags:
- SequentialRecommendation
- LongSequenceModeling
- DynamicCompression
- Transformer
- EfficiencyOptimization
one_liner: 通过对比熵驱动的动态序列分块实现长序列推荐的效率-精度帕累托最优
practical_value: '- 序列压缩可放弃固定分块方案，改用对比熵惊喜度检测用户意图跳转点做动态分块，既保留关键信号又降低算力开销，尤其适合行为稀疏的电商/内容推荐场景

  - 可直接复用Time-RoPE方案，将绝对时间戳转换为旋转位置编码，让注意力天然适配行为间隔，比相对位置编码更贴合真实用户行为规律

  - 算力受限场景下，可通过调整目标分块数M灵活控效：哪怕压缩到2个分块也能保留94%以上的性能，适合低算力端的推荐服务部署

  - 动态分块的边界检测器可预训练后冻结，仅用极小hidden size（如8）就能实现不错的分块效果，几乎不会增加额外推理开销'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Transformer长序列推荐受自注意力O(N²)复杂度限制，要么做固定长度截断损失长期兴趣信号，要么用固定分块压缩忽略不同用户行为的信息密度差异，在长序列场景下效率和精度难以平衡，工业界亟需适配信息密度的动态压缩方案。

### 方法关键点
- 提出**对比熵惊喜度**作为分块边界判定指标：用极小尺寸的预训练冻结Transformer输出正负样本对比熵，熵值峰值对应意图跳转点，避免全词表softmax的高昂开销
- 分块阈值自适应优化：训练时用batch级统计确定阈值实现算力跨序列动态分配，推理时用单序列阈值保证推理耗时稳定
- 引入Time-RoPE将绝对时间戳转换为旋转位置编码，让模型天然感知行为间隔，提升分块和建模的时序合理性
- 整体架构采用「分块检测-局部编码- Latent Transformer建模-局部解码」四段式，Latent层仅处理压缩后的分块序列，算力开销随分块数而非原始序列长度缩放

### 关键实验
在ML-1M、ML-10M-L、KuaiRand三个数据集对比SASRec、LONGER等基线，同等FLOPs预算下NDCG@10相对最优基线分别提升16.0%、21.1%、11.0%；达到同等精度时算力最多降低7倍，哪怕极高度压缩到2个分块也能保留94%以上的峰值性能。

### 核心结论
长序列推荐的算力分配应该匹配用户行为的信息密度，而非固定长度或分块规则。
