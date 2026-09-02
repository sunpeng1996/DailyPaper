---
title: 'The First Token Is a Clue: Verbalizing Multi-Token Concepts from the J-lens'
title_zh: 首token为线索：从Jacobian Lens中提取多token概念表示
authors:
- Xijie Gong
- Tonghan Wang
affiliations:
- College of AI, Tsinghua University
arxiv_id: '2608.31084'
url: https://arxiv.org/abs/2608.31084
pdf_url: https://arxiv.org/pdf/2608.31084
published: '2026-08-31'
collected: '2026-09-02'
category: LLM
direction: LLM可解释 · 多token概念提取
tags:
- LLM Interpretability
- Jacobian Lens
- Multi-token Concept
- Frozen LLM
- Hidden State Representation
one_liner: 基于J-lens首token线索结合冻结LLM，实现无微调的多token概念及对应向量高效恢复
practical_value: '- 生成式推荐候选生成可复用「首token召回+冻结LLM补全」的流程，无需微调即可降低候选生成成本，提升多token实体/商品召回准确率

  - RAG场景下抽取多token业务概念（如商品属性、用户意图短语）时，可直接套用该方法，避免预定义短语库的覆盖度不足问题

  - 电商广告文案/客服话术定向干预场景，可直接用该方法提取的多token概念向量做因果替换，无需重新微调LLM即可实现精准内容修改'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有Jacobian Lens（J-lens）仅能将LLM隐状态映射为单token词汇排序，无法直接表示多token概念；原有多token表示方案要么依赖预定义固定短语库，要么需要微调组件，成本高泛化性差。
### 方法关键点
1. 验证多token概念的首token可被J-lens有效识别，冻结LLM在给定正确首token+源prompt的前提下，双token场景下第二token恢复准确率达88.3%
2. 用J-lens输出候选首token，冻结LLM补全多token候选，单次前向传播从后续隐状态恢复完整概念向量，与全词表统一打分排序
### 关键结果
在Gemma-3-12B-IT、Llama-3.1-8B、Qwen3-14B共496个多跳完形任务上，平均Rank@10达43.1%，较Template Lens提升15.5pp；因果概念替换succ@10达61.4%，是Template Lens的2.3倍；移除首token线索后性能降至21.6%。
