---
title: Domain-Specific Text Embedding Models for Entity Resolution
title_zh: 面向实体解析的领域专属文本嵌入模型
authors:
- Khajesh Sapram
- Srivardhani Raju
- Kishore Konda
affiliations:
- Sodhana
- Nexus IQ Solutions
arxiv_id: '2608.16161'
url: https://arxiv.org/abs/2608.16161
pdf_url: https://arxiv.org/pdf/2608.16161
published: '2026-08-17'
collected: '2026-08-18'
category: Training
direction: 实体解析 · 领域专属嵌入微调优化
tags:
- Text Embedding
- Entity Resolution
- Triplet Learning
- Fine-tuning
- Dense Retrieval
one_liner: 采用领域专属三元组微调通用嵌入模型，显著提升实体解析场景真假匹配区分能力
practical_value: '- 电商商品/商家/用户去重场景可复用三元组微调方案，构造同实体同义变体、高相似负样本对通用嵌入做轻量微调，提升去重准确率

  - RAG的实体级召回环节可针对业务领域用该方法微调嵌入，避免召回语义相近但实体不同的内容，降低RAG幻觉

  - 构造训练数据时可参考合成数据思路，自动生成同实体多变体（别名、拼写错误）和高相似负样本，降低标注成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
通用预训练文本嵌入仅优化广义语义相似性，未适配实体解析场景的身份判断需求：文本微小差异既可能是不改变实体身份的变体（如拼写误差、别名），也可能对应完全不同的实体，直接使用会导致实体去重、重复记录检索效果不达预期。
### 方法关键点
1. 合成面向商业、个人实体的训练数据集，覆盖同实体的身份保留变体、高相似非匹配难负例；
2. 基于margin的三元组损失对两类主流通用嵌入模型做领域专属微调，重塑向量空间分布；
3. 采用基于margin的相似度指标评估模型区分真假匹配的能力。
### 关键结果
微调后模型对真匹配与高相似非匹配的区分能力得到显著提升，验证了领域专属三元组微调可高效适配通用嵌入到身份敏感的实体检索场景，可直接落地到数据质量管理、信息检索类业务。
