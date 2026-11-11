---
title: 'FERN: Cross-Benchmark Table Retrieval for Text-to-SQL with Frozen Retrievers
  and Learned Ranking'
title_zh: FERN：面向Text-to-SQL的跨基准表检索，基于冻结检索器与学习排序
authors:
- Arjun Rao
- Nishant Gopinath
affiliations:
- SAP
arxiv_id: '2611.14477'
url: https://arxiv.org/abs/2611.14477
pdf_url: https://arxiv.org/pdf/2611.14477
published: '2026-11-10'
collected: '2026-11-11'
category: RAG
direction: RAG检索优化 · 混合召回轻量排序
tags:
- Table Retrieval
- Learning to Rank
- Hybrid Retrieval
- Text-to-SQL
- LightGBM
one_liner: 提出无生成式LLM的FERN表检索框架，跨基准性能接近Claude 3.5方案且延迟极低
practical_value: '- 多冻结检索器融合召回+轻量GBM排序的架构可替代昂贵的生成式LLM检索方案，大幅降低推理成本与延迟，适合电商大库语义召回、Agent工具检索等场景

  - 排序阶段在检索匹配特征外加入非检索类特征，可显著提升Top N准确率，该思路可直接复用在商品/广告召回排序、Query推荐等业务

  - 单数据集训练的排序模型可跨基准泛化，无需重复适配多场景数据，降低多品类电商、多业务线通用召回架构的迭代成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
大表库场景下Text-to-SQL的前置表检索是核心瓶颈，现有基于生成式LLM的检索方案调用成本高、延迟高，跨基准泛化性不足。
### 方法关键点
FERN完全不依赖生成式LLM，先融合3个冻结检索器输出Top 100候选表，为每个候选构造120维特征，使用仅在BIRD训练集拟合的LightGBM排序器完成重排。
### 关键结果
- Spider数据集上Top15召回达98.0，与Claude 3.5驱动的RASL持平；complete@5从83.9%提升至95.6%，Top5召回96.7仅比RASL低0.3个点
- BIRD带证据提示场景下Top5召回96.6，仅比RASL低0.9个点
- 单A100上单query中位数延迟仅208ms，无远程模型调用开销
