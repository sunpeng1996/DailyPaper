---
title: When Is Complex Chunking Worth It? A Multi-Objective Evaluation of Chunking
  Methods at Scale
title_zh: 大规模分块方法多目标评估：复杂分块何时值得投入？
authors:
- Laura Caspari
- Kanishka Ghosh Dastidar
- Michael Dinzinger
- Jelena Mitrović
- Michael Granitzer
affiliations:
- University of Passau
- Interdisciplinary Transformation University Linz
arxiv_id: '2608.16586'
url: https://arxiv.org/abs/2608.16586
pdf_url: https://arxiv.org/pdf/2608.16586
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: RAG系统 · 文档分块策略多目标评估
tags:
- Chunking
- RAG
- Dense Retrieval
- Embedding
- Evaluation
- Operational Efficiency
one_liner: 多维度评估8种分块策略的检索效果与运营成本，给出不同场景的分块选型参考
practical_value: '- 大规模检索场景默认选用token-based分块，简单、索引速度快、内存效率高，性能足够能打；需要保留语义边界可选sentence分块，注意权衡索引吞吐量。

  - 有文档标题的场景优先用Enriched (Title)分块，几乎无额外成本，在大部分检索指标下都能获得稳定收益，性价比远高于复杂的summary enrichment方案。

  - 分块选型要对齐业务目标：单阶段检索优先试enriched类分块提升Top N排序效果；一阶段召回用简单token/sentence分块足够，不要盲目上语义分块、上下文分块等高成本方案。

  - 语料规模大、更新频繁的业务（如电商实时商品索引、广告素材库）要把索引吞吐量、内存开销纳入早期评估，依赖LLM的复杂分块方案很难适配高频重索引需求。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG分块策略对比大多仅关注检索效果，忽略索引吞吐量、查询延迟、内存占用等运营成本，且未验证不同语料规模下的效果差异，工业界选型缺乏可落地的多维度参考。

### 方法关键点
- 覆盖8种典型分块策略：无额外模型调用的Token、Sentence、Late、Enriched (Title)，需额外LLM/Embedding调用的Enriched (Summary)、Contextual、Summary、Semantic分块
- 双维度评估：检索效果（NDCG@10、Recall@100）+ 运营成本（文档索引吞吐量、查询吞吐量、峰值内存占用）
- 跨3款开源Embedding模型、2类可扩展语料（CoRE、KILT-NQ）、4种语料规模（10K~10M）做对照测试

### 关键结果
复杂分块很少能持续优于简单方案：Enriched (Summary)在NDCG@10上赢过Late分块的概率仅71%，语义/上下文/摘要分块在绝大多数场景下无显著优势；成本差距显著，Token分块索引吞吐量达69.2doc/s，是Contextual分块（~1-5doc/s）的10倍以上，内存占用仅为Late分块的1/3；语料越大分块影响越显著，1M规模语料下分块方法的效果差异是10K规模的2倍以上。

### 核心结论
简单分块是绝大多数工业场景的最优默认，复杂分块的额外成本很少能匹配对应的检索收益，选型必须结合业务指标与部署约束做多目标权衡。
