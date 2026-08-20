---
title: 'GreekBarRetrieval: A Benchmark for Greek Statutory Retrieval'
title_zh: GreekBarRetrieval：希腊法定条文检索基准数据集
authors:
- Ernest Beta
- Odysseas S. Chlapanis
- Dimitrios Galanis
- Ion Androutsopoulos
affiliations:
- Athens University of Economics and Business, Greece
- Archimedes, Athena Research Center, Greece
- Institute for Language and Speech Processing, Athena Research Center, Greece
arxiv_id: '2608.18752'
url: https://arxiv.org/abs/2608.18752
pdf_url: https://arxiv.org/pdf/2608.18752
published: '2026-08-19'
collected: '2026-08-20'
category: RAG
direction: 检索评测 · LLM查询改写优化
tags:
- Retrieval Benchmark
- Query Reformulation
- BM25
- ReAct
- Legal NLP
one_liner: 推出希腊法律条文检索公开基准，验证类ReAct多轮LLM查询改写可显著提升BM25检索效果
practical_value: '- 稀疏检索（如BM25）搭配多轮LLM查询改写的方案，可替代成本更高的稠密检索或稀疏-稠密融合方案，降低电商搜索、商品召回链路部署成本

  - 类ReAct的多轮查询改写迭代逻辑，可直接迁移到电商搜索query优化、商家咨询RAG问答、商品文案检索等场景，提升召回准确率

  - 低资源垂直领域检索优化可优先尝试LLM查询改写方案，效果优于伪相关反馈、跨语言翻译等常用baseline'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
法律问答需基于法条检索输出可解释、可验证的 grounded 回答，但希腊语领域法条检索缺乏公开基准，且日常口语化查询与法条正式术语存在语义鸿沟，案件中的无关事实也会干扰检索效果。
### 方法关键点
构建包含283道希腊律师资格考试题、6308条候选法条的公开检索基准GreekBarRetrieval；对比3种BM25变体、9种稠密检索器的检索效果，提出10轮类ReAct的LLM查询改写迭代流程，同时对比伪相关反馈、稀疏-稠密融合、英语翻译等基线方案。
### 关键结果
原生稠密检索Recall@100远优于原生稀疏检索；LLM查询改写可大幅缩小BM25与稠密检索的差距，同时提升稠密检索效果；10轮ReAct式改写后的BM25取得所有测试模型最优的nDCG和MAP，Recall@100进一步提升，效果优于所有对比基线。
