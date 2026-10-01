---
title: 'Re-ranking and Late Interaction Drive Retrieval Quality: A Controlled Comparison
  of RAG Strategies for Scientific Question Answering'
title_zh: 科学问答RAG策略对比：重排序与晚交互是检索质量核心驱动
authors:
- Bhagyesh Rathi
- Eshan Chawla
- William B. Andreopoulos
affiliations:
- San Jose State University
arxiv_id: '2609.38473'
url: https://arxiv.org/abs/2609.38473
pdf_url: https://arxiv.org/pdf/2609.38473
published: '2026-09-29'
collected: '2026-10-01'
category: RAG
direction: RAG策略优化与效果对比
tags:
- RAG
- ColBERT
- Retrieval
- LLM-as-judge
- QuestionAnswering
one_liner: 控制变量下对比6种RAG检索策略，明确晚交互与重排序对检索质量的提升作用
practical_value: '- RAG选型优先级参考：优先落地ColBERT类晚交互检索方案，算力/存储受限场景优先选择「query改写 + LLM 重排」的单向量架构，性价比远高于多查询RRF、单步工具调用类复杂方案

  - 不要盲目叠加复杂组件：未经针对性优化的多查询融合、单步agent检索等复杂pipeline效果可能弱于经典RAG基线，额外增加的算力成本不会带来对应收益

  - 资源投入向召回侧倾斜：RAG效果差异90%以上来自召回是否命中目标文档，生成端优化对效果提升的贡献远小于召回侧，电商/广告场景可优先迭代商品/内容召回逻辑，再优化生成话术'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前RAG已成为LLM领域知识落地的标配方案，但不同检索策略的成本效果 tradeoff 缺乏统一的大规模对比结论，现有研究多评测孤立组件或基于小数据集，无法给从业者提供明确的选型指导，尤其在科学文献等领域语料场景下的参考性不足。

### 方法关键点
- 严格控制变量：所有6种检索策略共用Llama-3.1-8B-Instruct作为生成器、相同prompt、统一评测协议；5种单向量方案共用SPECTER2 embedding与Chroma向量库，仅检索逻辑不同
- 对比策略覆盖主流方案：经典Top-k稠密检索、LLM query改写、改写+LLM重排、多查询RRF融合、单步agent工具调用检索、ColBERTv2晚交互检索
- 双维度评测：用跨模型族的Qwen2.5-32B作为LLM-as-judge评估回答质量，同时统计Hit@1/Hit@3/MRR@3等硬检索指标

### 关键实验
评测基于46.4万篇2024-2025年arXiv论文，合成19484条问题-金文档对，以经典RAG为基线：ColBERT晚交互方案效果最优，整体打分3.94/5，Hit@3达92.8%~94.8%，比基线高0.37分；改写+重排是最优单向量方案，整体打分3.77/5，比基线高0.18分；多查询融合、单步agent检索效果均低于基线。

### 核心结论
RAG的效果瓶颈几乎完全来自召回侧是否能拿到正确的证据，而非生成端对上下文的利用能力，复杂度更高的pipeline不必然带来效果提升。
