---
title: Cost-Pragmatic Quality Gating and Selection-Fusion Multi-Model Combiners for
  BioASQ Phases A+ and B
title_zh: 面向BioASQ A+/B阶段的成本务实型质量门控与选择融合多模型组合器
authors:
- Dima Galat
- Marian-Andrei Rizoiu
affiliations:
- University of Technology Sydney, Australia
arxiv_id: '2607.13551'
url: https://arxiv.org/abs/2607.13551
pdf_url: https://arxiv.org/pdf/2607.13551
published: '2026-07-15'
collected: '2026-07-16'
category: RAG
direction: 检索增强生成 · 重检索策略与多模型融合
tags:
- RAG
- Cross-Encoder
- Retrieval Policy
- LLM-as-judge
- Model Ensemble
one_liner: 提出成本感知的选择性重检索策略与多模型回答融合框架，在生物医学问答任务登顶多榜单
practical_value: '- 可复用BGE cross-encoder做弱检索结果识别的质量门控策略，仅对低置信度query触发重检索，适配电商搜索/大模型导购RAG链路降本

  - 多模型结果的选择-融合拆分思路可迁移到生成式推荐ensemble：LLM-as-judge做选择适配精度指标，同义词union融合适配召回类指标

  - 成本务实型重检索政策可复用到搜索suggestion、广告召回链路，相比全量重检索可降低约12%成本同时提升F1和精度'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有RAG系统要么盲目全量重检索导致成本过高，要么多模型回答融合无指标适配性，专业领域问答难以兼顾效果与成本。
### 方法关键点
1. 双路并行检索：混合检索（BGE稠密+BM25稀疏+RRF融合）+ Agent驱动多数据源（PubMed、Europe PMC、iCite）问题拆解检索，用BGE cross-encoder做质量门控，仅对弱支持query触发选择性重检索
2. 多模型回答拆分为选择+融合模块：选择模块用LLM-as-judge适配精确类指标，融合模块用同义词union resolver适配召回类指标
### 关键结果
12B验证集上重检索成本降低12%，list F1、list precision显著优于严格基线；13B测试集list F1绝对提升0.132；2026 BioASQ 14B初步榜单位居3个阶段/批次综合精确指标第一，4个问题类型单项第一，Phase B b3理想指标第一
