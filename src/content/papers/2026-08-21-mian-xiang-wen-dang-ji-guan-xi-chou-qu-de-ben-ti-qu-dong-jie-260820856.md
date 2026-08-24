---
title: Ontology-Driven Structural Regularization for Document-Level Relation Extraction
title_zh: 面向文档级关系抽取的本体驱动结构正则化方法
authors:
- Laura Menotti
- Stefano Marchesin
- Gianmaria Silvello
affiliations:
- Department of Information Engineering, University of Padua, Italy
arxiv_id: '2608.20856'
url: https://arxiv.org/abs/2608.20856
pdf_url: https://arxiv.org/pdf/2608.20856
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: 知识抽取 · 本体驱动结构正则化
tags:
- Relation Extraction
- Ontology
- Distant Supervision
- Structural Regularization
- Knowledge Graph
one_liner: 提出本体驱动的结构正则框架，解决远监督DocRE数据的结构噪声问题，提升模型泛化性能
practical_value: '- 电商知识图谱构建场景，可引入本体约束对远监督自动标注的商品/用户/行为三元组做批量清洗，大幅降低人工标注成本的同时提升KG质量

  - 训练领域知识抽取模型时，可将结构一致性作为辅助监督信号加入损失函数，减少模型输出的逻辑错误，提升下游召回/排序特征的可靠性

  - RAG系统的知识库预处理环节，可复用该框架校验抽取的结构化知识合法性，避免错误知识流入检索池，提升问答/个性化推荐的准确率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
文档级关系抽取（DocRE）高度依赖昂贵的人工标注数据，规模更大的远监督数据集因噪声问题未被充分利用，此前研究普遍忽视了三元组违反本体约束、存在逻辑矛盾这类结构噪声的负面影响，且噪声会进一步传导到模型预测结果中。

### 方法关键点
1. 提出本体驱动框架，量化DocRE数据集内三元组的结构一致性，自动识别不符合本体规则的结构噪声
2. 训练阶段加入结构正则约束，强制模型输出符合逻辑与本体规则的关系三元组，阻断噪声传导路径

### 关键结果
验证DocRED远监督数据集存在大量结构噪声；加入结构正则后，模型预测的逻辑矛盾显著减少，泛化性能稳定提升，结构一致性可作为DocRE的新增监督维度。
