---
title: 'Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders'
title_zh: 《超越特征袋：稀疏自动编码器的集合级不稳定性研究》
authors:
- Nikolai Bolik
- Lennart Stöpler
- Artur Andrzejak
affiliations:
- Heidelberg University
arxiv_id: '2608.11197'
url: https://arxiv.org/abs/2608.11197
pdf_url: https://arxiv.org/pdf/2608.11197
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: LLM表征解析 · SAE语义性质研究
tags:
- SAE
- Sparse Autoencoder
- LLM Representation
- Semantic Similarity
- Concept Alignment
one_liner: 揭示非理想场景下SAE激活集合不遵循特征袋语义，匹配人类概念的表现未优于稠密嵌入
practical_value: '- 业务中若用SAE做LLM可解释性、语义匹配，不要直接用SAE激活集合重叠度作为语义相似度度量，其匹配人类语义判断的表现劣于传统稠密embedding余弦相似度

  - 不要假设SAE特征可按简单特征袋规则组合，在电商query、商品标题等非理想业务文本场景下，SAE特征组合计算的语义会存在明显偏差

  - 面向用户的语义召回、意图识别等场景，优先选择成熟的稠密embedding方案，SAE集合级相似度当前暂不适合落地到生产环境'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
此前研究用LLM稠密表征余弦相似度度量语义相似度，发现仅能匹配人类大类概念边界，无法反映类内细粒度典型性；业界预期SAE稀疏激活集合重叠度作为可解释度量能优化这一问题。
### 方法关键点
1. 先在受控玩具模型、自然文本场景验证SAE激活集合度量的基础有效性
2. 对比SAE集合相似度、稠密嵌入余弦相似度、残差流状态三类度量与人类概念边界、类内典型性的对齐程度
3. 通过受控语义修改实验探查SAE集合度量与人类判断的差异来源
### 关键结果
- 理想场景下SAE激活集合可还原类union的组合结构，生成语义一致的邻域
- 对齐人类概念的表现未优于稠密嵌入/残差流，仅能匹配模型内部相似度结构
- 受控语义修改场景下，SAE激活集合变化与人类概念变化判断存在显著错配，非理想场景下SAE特征不遵循简单特征袋语义
