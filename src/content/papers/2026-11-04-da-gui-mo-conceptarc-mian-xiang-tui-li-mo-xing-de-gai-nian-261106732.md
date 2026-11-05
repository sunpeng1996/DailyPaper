---
title: 'ConceptARC at Scale: Studying Conceptual Understanding in Reasoning Models'
title_zh: 大规模ConceptARC：面向推理模型的概念理解能力研究
authors:
- Philipp Mondorf
- Adrien Deliège
- Solim LeGris
- Claas Beger
- Ryan Yi
- Barbara Plank
- Brenden M. Lake
- Todd M. Gureckis
affiliations:
- LMU Munich & MCML
- University of Liège
- New York University
- Santa Fe Institute
- Princeton University
arxiv_id: '2611.06732'
url: https://arxiv.org/abs/2611.06732
pdf_url: https://arxiv.org/pdf/2611.06732
published: '2026-11-04'
collected: '2026-11-05'
category: Reasoning
direction: 大模型推理能力评测 · 抽象概念泛化
tags:
- Reasoning
- Benchmark
- Concept Abstraction
- LRM
- Evaluation
one_liner: 构建10倍规模的概念级ARC推理评测数据集，验证大推理模型可形成跨任务通用操作抽象
practical_value: '- 做Agent推理能力评测时可复用「按核心概念分组生成批量测试用例」的方法，避免小样本评测的偶然性

  - 推荐/搜索系统的规则抽象建模可参考论文结论，优先对改写、过滤、排序等核心操作做语义对齐，提升跨场景泛化性

  - 大模型微调做多任务推理时，可按操作语义聚类任务组，提升训练效率与跨任务迁移能力'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有ARC类推理基准仅含少量人工构造任务，无法可靠验证大推理模型（LRM）是否能在跨概念相关任务上形成可泛化的抽象能力，评测结果偶然性高。
### 方法关键点
1. 提出ConceptARC at Scale任务生成器，可针对特定空间/语义概念批量生成ARC风格的二维网格推理任务
2. 构建ConceptARC-100数据集，含16个概念各100个共1600个人工审核的推理任务，规模是原基准的10倍
3. 评测多款主流LRM与从零训练的模型，同时分析模型内部表征的语义聚类特征
### 关键结果数字
- 模型内部表征会按重着色、删除、平移等对象操作类型聚类，即使对应规则和场景差异极大
- 验证了现有LRM确实能形成稳定的变换操作抽象，可跨不同任务泛化
