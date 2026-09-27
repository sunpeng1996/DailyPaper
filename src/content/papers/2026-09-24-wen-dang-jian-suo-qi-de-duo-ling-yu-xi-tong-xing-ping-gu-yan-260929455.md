---
title: A Systematic Multi-Domain Evaluation of Document Retrievers
title_zh: 文档检索器的多领域系统性评估研究
authors:
- Valentin Velev
- Andreas Spitz
affiliations:
- University of Konstanz
arxiv_id: '2609.29455'
url: https://arxiv.org/abs/2609.29455
pdf_url: https://arxiv.org/pdf/2609.29455
published: '2026-09-24'
collected: '2026-09-27'
category: Eval
direction: 文档检索器 多领域性能与延迟评估
tags:
- DocumentRetrieval
- RAG
- Evaluation
- SparseRetrieval
- DenseRetrieval
one_liner: 覆盖3类33种开箱即用文档检索器，跨7个数据集做统一评估，给出性能延迟选型参考
practical_value: '- 业务选型RAG/Agent的检索模块时，可直接参考本文开箱评估结论匹配场景：通用场景选NV-Embed-v2，低延迟要求选SPLADE-v3，指令类场景选GritLM

  - 内部做检索器横向对比时，需统一计算预算、采用开箱配置做基准测试，避免单数据集、额外调优带来的选型偏差

  - 可参照本文的失败点分析框架，对业务落地的检索器做bad case分类，定向优化召回准确率'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有文档检索器的对比研究普遍局限于单领域、单基准或单模型族，碎片化结论无法支撑可靠的选型判断，难以适配RAG、搜索推荐等下游业务的检索需求。
### 方法关键点
统一采用开箱即用配置、相同计算预算，覆盖稀疏、稠密、扩展型3大类共33个检索器，跨7个IR数据集，从检索质量、运行耗时、失败点三个维度做系统性评测。
### 关键结果
- NV-Embed-v2在7个数据集中的4个取得最优性能，但查询延迟显著高于其他模型
- 稀疏检索器SPLADE-v3延迟远低于稠密类SOTA，性能媲美头部方案，在MS MARCO数据集上得分最高
- 指令遵循类数据集上GritLM表现最优
