---
title: Faithful or Findable? Evaluating LLM-Generated Metadata for RDF Dataset Search
title_zh: 兼顾可信性与可检索性：RDF数据集搜索的LLM生成元数据评估
authors:
- Riccardo Terrenzi
- Serkan Ayvaz
affiliations:
- University of Southern Denmark
arxiv_id: '2607.05970'
url: https://arxiv.org/abs/2607.05970
pdf_url: https://arxiv.org/pdf/2607.05970
published: '2026-07-07'
collected: '2026-07-08'
category: Eval
direction: 检索系统 · LLM生成元数据效果评估
tags:
- Synthetic Metadata
- LLM Evaluation
- Information Retrieval
- Faithfulness
- Dataset Search
one_liner: 对比6种LLM生成RDF数据集元数据方案，量化检索效果与信息可信性的权衡关系
practical_value: '- 电商商品/短视频内容搜索的元数据（如商品短标题、内容摘要）生成场景，低敏感品类可优先用无约束改写最大化召回效率

  - 美妆、医药等合规要求高的品类，采用profile-grounded改写方案，平衡检索效果与事实可信性，避免虚假宣传风险

  - 生成式元数据落地的评估体系需同时覆盖检索效果、事实一致性、合规性三类指标，不能仅以搜全率作为唯一优化目标'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
数据集搜索高度依赖元数据质量，LLM自动生成元数据可补全稀疏描述、提升检索效果，但容易引入无依据的虚假信息，当前缺乏对不同生成方案的检索效果与可信性的系统性量化对比。
### 方法关键点
共测试6种LLM生成RDF数据集元数据的方案，覆盖无约束改写、基于属性profile的grounded改写、Agent 图结构生成三类范式，同时评估检索有效性、信息可信性两个核心维度。
### 关键结果
无约束改写相比原始元数据检索增益最高，但可信性最低，其性能提升主要来自无事实依据的语义扩充；基于profile的grounded改写在两个维度间取得最优平衡，落地性价比最高。
