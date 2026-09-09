---
title: 'Q2D-Web: A Large-Scale Benchmark for Retrieval in Agentic RAG Systems'
title_zh: Q2D-Web：面向智能体RAG系统的大规模检索基准数据集
authors:
- Maximilian Schall
- Sedigheh Eslami
- Markus Krimmel
- Antoine Chaffin
- Louis Milliken
- Bo Wang
- Denis Bykov
affiliations:
- Perplexity AI
arxiv_id: '2609.08887'
url: https://arxiv.org/abs/2609.08887
pdf_url: https://arxiv.org/pdf/2609.08887
published: '2026-09-08'
collected: '2026-09-09'
category: Eval
direction: Agentic RAG 检索性能评测基准
tags:
- Agentic-RAG
- Retrieval-Benchmark
- Multilingual
- Large-Scale
- RRF
one_liner: 构建含190M网页文档、70k智能体重写查询的多语言Agentic RAG检索基准并配套公开榜单
practical_value: '- 构建RAG召回标签体系时，可融合Agent引用、生产排序结果、LLM打分三类信号，降低单源标注偏置，减少假阴性

  - 大规模召回评测成本过高时，采用RRF融合多召回模型top结果采样子语料，保留30%语料即可复现全量语料的模型相对排名，评测成本降低60%+

  - 召回层架构设计中可保留BM25+多架构召回模型的组合：BM25整体召回率最低，但贡献的独有正样本是最优稠密模型的16倍以上，融合可大幅提升总召回

  - 面向Agent的RAG系统需针对性优化支持查询的召回效果：神经召回模型在支持查询上的表现比主查询低2-4pct，可微调模型或提升BM25权重适配该类查询'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agentic RAG检索基准存在三大缺陷：语料规模普遍小于100M，查询数量不足1万，无法模拟工业级大规模检索场景；查询多为人类手写，和生产中LLM重写的查询分布差异大；标注浅，单查询正样本不足10个，假阴性率高，无法准确评估第一阶段召回的真实性能。

### 方法关键点
- 数据集：从9个月去PII的生产流量中采样70k多语言LLM重写查询（含17.7%主查询、82.3%支持查询），合并每个查询top5000召回结果去重得到190M网页语料
- 标签体系：构建三类标签集：Agent引用高精准标签、生产链路排序结果、融合前两类+LLM标注未标注候选的组合标签，平均单查询99.6个正样本
- 高效评测：用RRF融合多召回模型top结果采样子语料，仅保留31.7%语料即可完全复现全量语料的模型相对排名

### 关键结果
评测13个词法、稠密、晚交互召回模型：pplx-embed-v1-4b在组合标签下Recall@1000达69.11%为最优；神经召回模型在支持查询上的Recall@1000比主查询低2-4pct，仅BM25在支持查询上表现略优；BM25整体Recall@1000最低仅44.77%，但贡献的独有正样本是最优稠密模型的16倍以上。

### 核心结论
召回层的效果上限不取决于单模型的最高召回率，而取决于不同架构召回模型的多样性，词法召回即使整体表现差也有不可替代的价值。
