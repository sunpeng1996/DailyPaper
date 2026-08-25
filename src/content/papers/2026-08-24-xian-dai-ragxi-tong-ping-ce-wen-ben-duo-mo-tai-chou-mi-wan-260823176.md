---
title: 'Evaluating Modern RAG: Textual, Multimodal, Dense, and Late Interaction Pipelines'
title_zh: 现代RAG系统评测：文本/多模态、稠密/晚交互架构的权衡指南
authors:
- Emre Kuru
- Mehmet Onur Keskin
affiliations:
- Özyeğin University, Türkiye
arxiv_id: '2608.23176'
url: https://arxiv.org/abs/2608.23176
pdf_url: https://arxiv.org/pdf/2608.23176
published: '2026-08-24'
collected: '2026-08-25'
category: RAG
direction: RAG架构选型 · 多模态与效率权衡
tags:
- RAG
- Multimodal Retrieval
- Late Interaction
- Dense Retrieval
- System Evaluation
one_liner: 量化对比四类主流RAG检索架构的效果与资源开销，给出业务场景下的选型指导
practical_value: '- 业务中含大量带表格/图片的商品/售后/合同类文档的RAG场景，优先选Visual-Dense架构，FinReport场景下nDCG@5比文本稠密架构高43.5%，同时内存开销低12.8%，端到端索引速度快44%

  - 若场景对召回精度要求极高且能容忍高延迟（比如内部运营知识库查询），可选Visual-Late Interaction架构，Recall@5比文本稠密架构高48%，但内存开销是前者的13倍，检索
  latency 超20s

  - 纯文本类低复杂度文档场景，直接用Text-Dense架构即可，Text-Late Interaction不仅效果低30%+，还会带来2倍以上的内存开销和8倍的检索延迟

  - BM25仅适合无query重写的精准匹配场景，一旦query存在语义改写，效果下降幅度是语义检索的3倍以上，不适合C端用户查询类场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG架构选型缺乏系统的效果与效率对比指导：文本类架构处理带布局/表格/图片的复杂文档时OCR误差大、语义丢失，多模态架构效果好但资源开销不明确，同时稠密和晚交互架构的trade-off也缺乏量化数据，无法支撑业务落地选型。

### 方法关键点
- 沿两个维度划分四类核心RAG检索架构：模态（文本/视觉）、检索架构（稠密/晚交互），分别为Text-Dense、Text-Late Interaction、Visual-Dense、Visual-Late Interaction
- 统一在H100 80G环境下测试，控制硬件、向量数据库（Qdrant）等无关变量，同时测试检索效果（nDCG@5、MRR@5等）和QoS指标（内存、索引延迟、检索延迟）
- 引入4级query重写机制测试鲁棒性，同时按文档视觉占比、答案模态（文本/视觉）拆分效果分析

### 关键实验
在REAL-MM-RAG的FinReport（金融财报多表格）、TechReport（技术文档多图表）两个数据集上测试，对比BM25及四类SOTA架构：Visual-Late Interaction效果最优，FinReport nDCG@5达0.74，比Text-Dense高60.9%，但内存开销达5GB，检索延迟超27s；Visual-Dense是性价比最优选项，FinReport nDCG@5达0.66，内存仅340MB，端到端索引速度比文本架构快40%+；BM25在3级query重写下效果下降58.1%，远高于语义检索的平均17%降幅。

**最值得记住的一句话**：没有通用最优的RAG架构，Visual-Dense是绝大多数带复杂结构文档场景的性价比首选。
