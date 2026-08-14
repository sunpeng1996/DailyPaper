---
title: Query Translation vs. Cross-Lingual Embeddings for Sinhala-Tamil E-Government
  Information Retrieval
title_zh: 僧伽罗语-泰米尔语电子政务检索的查询翻译与跨语言嵌入对比
authors:
- Dharshi Balasubramaniyam
- Tiroshan Madushanka
affiliations:
- University of Kelaniya, Sri Lanka
arxiv_id: '2608.12820'
url: https://arxiv.org/abs/2608.12820
pdf_url: https://arxiv.org/pdf/2608.12820
published: '2026-08-13'
collected: '2026-08-14'
category: RAG
direction: 跨语言RAG · 低资源语言检索方案对比
tags:
- CLIR
- Cross-Lingual Embedding
- Query Translation
- BGE-M3
- RAG
- Low-Resource Language
one_liner: 对比低资源语言跨语言检索两类方案，验证BGE-M3性能优于翻译方案且无额外开销
practical_value: '- 跨境多语言搜索/ RAG 场景优先测试BGE-M3等跨语言嵌入方案，相比调用翻译API成本更低、召回准确率更高

  - 小语种低资源跨语言检索场景，无需优先投入定制翻译模型，直接选用SOTA多语言嵌入模型即可获得更优效果

  - 跨语言检索效果评估可优先采用Recall@k作为核心指标，快速对齐业务侧检索准确率的诉求'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
低资源语言用户查询英文语料时存在语言 mismatch，现有多语言检索方案缺乏低资源垂直场景的对比验证；斯里兰卡政务场景中，用户常用僧伽罗语、泰米尔语查询，而官方政务语料以英语为主，检索体验差。
### 方法关键点
对比两类跨语言检索（CLIR）范式：1）Query Translation（QT）：包含Google Translate、NLLB、mBART50；2）Cross-Lingual Embeddings（CLE）：包含LaBSE、多语言E5、BGE-M3，以单语英文检索为基线，在斯里兰卡政务标注benchmark（500条三语QA对、1699条分割上下文）上测试，用Recall@k评估效果。
### 关键结果
单语基线Recall@15<10%，所有CLIR方案均大幅提升检索准确率；其中BGE-M3性能最优，僧伽罗语-英语Recall@15达96.2%，泰米尔语-英语达95.6%，比最优QT方案（Google Translate）分别高3.8、2.6个百分点，且无翻译延迟开销，更适合低资源场景跨语言RAG落地。
