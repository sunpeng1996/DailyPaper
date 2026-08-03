---
title: 'PaletteID: Prototype-Composed Semantic Identifiers for Multimodal CTR Prediction'
title_zh: PaletteID：面向多模态CTR预测的原型组合语义标识符
authors:
- Huanyu Liu
- Baining Chen
- Hui Liu
- Zengyang Li
- Ziyi Huang
affiliations:
- Huazhong University of Science and Technology
- Central China Normal University
arxiv_id: '2607.29000'
url: https://arxiv.org/abs/2607.29000
pdf_url: https://arxiv.org/pdf/2607.29000
published: '2026-07-31'
collected: '2026-08-03'
category: GenRec
direction: 生成式推荐 · 多模态语义ID优化
tags:
- Semantic ID
- CTR Prediction
- Multimodal Recommendation
- Prototype Learning
- DPP
one_liner: 提出基于真实商品原型软组合的语义ID，提升多模态CTR效果与长尾泛化能力
practical_value: '- 多模态语义ID构建可放弃硬量化思路，改用真实商品作为原型锚点的软组合方案，既保留细粒度语义相似度，又大幅提升ID分配稳定性，避免商品多模态信息小修改导致ID突变

  - 原型集构建可复用SQ-DPP方法，同时兼顾局部语义密度和全局多样性，避免孤立低价值样本占用原型配额，实测比随机、KMeans选原型的下游效果更好

  - 原型组合聚合用独立sigmoid加权效果优于softmax，不需要强制权重和为1，允许多个互补原型同时贡献语义信号，尤其适合长尾商品的语义补全

  - 工程部署友好：原型选择、ID序列生成全离线预计算，在线仅需嵌入查表+轻量加权聚合，额外开销极低，可直接插入现有CTR排序pipeline'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态CTR方案直接输入预训练嵌入或硬量化Semantic ID存在两大瓶颈：一是硬码本分配丢失原始嵌入空间的连续语义相似度信号，无法区分不同程度的语义关联；二是残差分层ID的深层编码高度依赖前缀，同索引在不同前缀下语义不一致，参数共享会引入冲突，且深层量化有效信息增益极低，同时硬ID对多模态输入扰动敏感、可解释性差，长尾商品语义表示效果尤其差。

### 方法关键点
1. 用SQ-DPP离线选择真实商品构建原型调色板：设计Cosine-RBF核避免嵌入维度的秩天花板，加入局部语义密度的质量得分，同时兼顾全局语义多样性和局部代表性，无需训练
2. 每个目标商品检索Top-K相似原型，用独立sigmoid门控加权聚合原型嵌入，保留细粒度相似度，加入单调正则约束高排名原型权重不低于低排名原型
3. 生成的PaletteID可直接作为额外特征接入任意CTR backbone，部署时ID序列离线预存，在线仅需查表和轻量计算

### 关键结果
在淘宝多模态广告数据集（1M商品、7.2M用户、25.9M样本）和KuaiRec短视频数据集上测试，对比VQ-VAE、RQ-VAE、RQ-KMeans等语义ID方案：淘宝数据集DCNV2+DIN backbone下AUC比RQ-VAE高0.0017，长尾商品AUC提升0.0042；KuaiRec数据集RankMixer+DIN backbone下AUC比RQ-VAE高0.0018，GAUC提升0.0072；ID分配稳定性比RQ-SID高30%以上，语义面覆盖率超过85%。

最值得记住的一句话：语义ID不需要用抽象码本，基于真实商品的软组合方案在效果、稳定性、可解释性和工程落地性上全面优于传统硬量化方案
