---
title: 'DS@GT-ARC at eRisk 2026 Task 3: Sparse, Semantic, and LLM Reranking for ADHD
  Symptom Sentences'
title_zh: eRisk 2026任务3方案：融合稀疏、语义与LLM重排的ADHD症状句子排序
authors:
- David Guecha
affiliations:
- Georgia Institute of Technology
arxiv_id: '2608.03883'
url: https://arxiv.org/abs/2608.03883
pdf_url: https://arxiv.org/pdf/2608.03883
published: '2026-08-04'
collected: '2026-08-06'
category: RAG
direction: RAG检索优化 · 多阶段重排
tags:
- BM25
- LLM Reranking
- Zero-shot Retrieval
- Query Expansion
- Semantic Embedding
one_liner: 零样本无标注场景下提出多阶段分级检索方案，融合稀疏、语义与LLM重排提升相关性排序效果
practical_value: '- 零样本冷启动检索/排序场景可直接复用「BM25粗筛 + 语义/LLM重排」的多阶段架构，在无标注数据时平衡召回效率与排序精度

  - 搜索召回阶段可引入query原型扩展技巧，补充语义相关特征，有效提升低资源场景下的召回准确率

  - 针对电商UGC（评论、问答、晒单）的相关性排序任务，可新增自指类内容的证据感知重打分规则，提升排序贴合度'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
eRisk 2026 Task 3要求针对18项成人ADHD自评量表症状，对Reddit候选句子做相关性排序，任务首次发布无标注训练数据，需适配零样本/弱监督的检索排序方案。
### 方法关键点
采用多阶段分级检索架构：1. 用BM25做大规模候选粗召，兼顾召回效率与覆盖度；2. 叠加证据感知重打分规则，对自指类症状报告做权重倾斜；3. 可选语义嵌入重排+query原型扩展，或端到端LLM重排做精排。
### 关键结果
LLM重排版本取得官方最优得分，其次为query原型扩展版本；人工Top10分析结果与专家评分趋势高度一致，验证了多阶段重排架构的有效性。
