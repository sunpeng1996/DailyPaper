---
title: 'StitchRAG: Constructing Compact and Evidence-Preserving Contexts for RAG with
  Diffusion-Based Stitching'
title_zh: StitchRAG：基于扩散拼接构建RAG紧凑且保留证据的上下文
authors:
- Minsang Kim
- Junpyo Lim
- Heeje Cho
- Seungjun Baek
affiliations:
- Korea University
- SK Telecom
arxiv_id: '2611.22766'
url: https://arxiv.org/abs/2611.22766
pdf_url: https://arxiv.org/pdf/2611.22766
published: '2026-11-17'
collected: '2026-11-18'
category: RAG
direction: RAG上下文压缩 · 文本扩散
tags:
- RAG
- Context Compression
- Text Diffusion
- Open-domain QA
- Information Retrieval
one_liner: 提出融合动态预算分配、混合锚点筛选、扩散拼接的RAG上下文压缩框架，在多QA基准上优于现有基线
practical_value: '- 可直接复用动态压缩预算分配方法：用LLM判断query与检索片段的相关性，通过效用最大化公式计算每个片段的保留比例，替代固定压缩比，适配电商商品检索、客服RAG等场景的异质检索质量，降本同时保留关键信息

  - 混合锚点筛选策略（语义答案候选+TF-IDF关键词）可迁移到RAG证据保留环节，避免商品属性、用户意图等关键实体丢失，大幅降低电商场景RAG的事实幻觉

  - 扩散拼接方案可优化跨片段多跳推理场景的上下文连贯性，比如商品多属性组合查询、售后问题多轮溯源，相比自回归拼接准确率更高、延迟更低

  - StitchRAG在检索深度从Top10提升到Top30时效果无衰减，可用于需要高召回覆盖的搜索推荐场景的RAG后置处理，解决长上下文噪声问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG系统检索到的长上下文存在大量冗余噪声，不仅推高推理成本，还会干扰LLM判断导致效果下降；传统上下文压缩方法多采用固定比例，忽略query与检索片段的相关性差异，且容易破坏原文语义连贯性，压缩后上下文可读性差，反而拉低RAG表现。
### 方法关键点
- 动态预算分配：构建效用最大化目标（相关性对数效用减去平方计算成本），为每个检索片段计算最优保留比例r*，高相关片段保留更多内容，低相关片段大幅压缩，平均压缩率约73%
- 混合锚点提取：融合推理型锚点（LLM基于query+片段生成的答案候选）和查询型锚点（TF-IDF提取的query相关关键词），优先保留包含锚点的完整句子作为事实骨架，剩余预算补充高优先级非锚点句子
- 扩散拼接：根据相邻句子的语义重叠度动态分配拼接token数，用文本扩散模型仅填充拼接位置的掩码token，完全保留原始证据不变，解决碎片化句子的连贯性问题
### 关键实验
在HotpotQA、NQ、TriviaQA、PopQA、2WikiMultiHopQA 5个公开QA基准上测试，对比标准RAG、多步RAG（DRAG、IRCoT等）、压缩基线（LongLLMLingua、RECOMP等），6/10的EM/F1指标排名第一，比标准RAG在HotpotQA上EM提升2.4、F1提升2.3；当检索Top-K从10提升到30时，标准RAG平均F1下降3，StitchRAG效果完全稳定；延迟仅比标准RAG高47%，远低于多步RAG（IRCoT、DRAG延迟是其2-3倍）。
### 核心结论
RAG上下文优化的核心不是盲目增加检索量，而是在固定计算预算下最大化关键证据的密度与可读性，扩散模型的双向建模能力比自回归模型更适合证据保留型的上下文编辑
