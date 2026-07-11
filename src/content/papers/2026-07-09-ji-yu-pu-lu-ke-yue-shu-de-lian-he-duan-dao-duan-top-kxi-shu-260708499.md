---
title: Cross-seed explainability using Procrustes-conditioned Joint End-to-end Top-K
  Sparse Autoencoders
title_zh: 基于普鲁克约束的联合端到端Top-K稀疏自编码器跨种子可解释性方法
authors:
- Bendegúz Váradi
- Zoltán Kmetty
affiliations:
- Centre for Social Sciences, CSS-RECENS Research Group, Budapest, Hungary
- Department of Sociology, Faculty of Social Sciences, Eötvös Loránd University, Budapest,
  Hungary
arxiv_id: '2607.08499'
url: https://arxiv.org/abs/2607.08499
pdf_url: https://arxiv.org/pdf/2607.08499
published: '2026-07-09'
collected: '2026-07-11'
category: LLM
direction: LLM可解释 · 跨模型特征对齐
tags:
- SAE
- BERT
- Procrustes Alignment
- Mechanistic Interpretability
- XAI
one_liner: 通过普鲁克预对齐+改进SAE从独立训练BERT中提取跨种子通用可解释特征
practical_value: '- 多版本微调LLM/embedding模型的特征对齐场景可复用正交Procrustes旋转方法，解决不同初始化导致的特征空间错位问题

  - 训练SAE做语义特征提取时，可复用Top-K稀疏约束+死特征复活损失的组合，提升特征稀疏性与有效率

  - 跨模型通用语义特征挖掘方案可用于多场景召回特征对齐、跨域推荐的语义表征统一'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
独立训练的同架构LLM因随机初始化，特征空间存在错位，跨种子提取通用可解释特征是机制可解释性的核心痛点，现有后对齐方案效果有限。
### 方法关键点
1. 联合训练SAE前，先对不同种子BERT的激活空间做正交Procrustes旋转预对齐
2. 融合Top-K稀疏约束、端到端下游任务优化、死特征复活辅助损失三类优化点
3. 跨种子联合训练SAE提取通用可解释特征
### 关键结果数字
在SST-2、斯坦福礼貌度、TweetEval情感三个数据集，5组共10个独立种子BERT上测试，跨种子特征皮尔逊相关系数≥0.70，全面优于后对齐基线，高通用性特征可对应可解释的社会语言模式
