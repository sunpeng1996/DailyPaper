---
title: A Scalable Framework for Automated NER Annotation Correction in Low-Resource
  Languages
title_zh: 面向低资源语言的可扩展NER标注自动修正框架
authors:
- Toqeer Ehsan
- Thamar Solorio
affiliations:
- VTT Technical Research Centre of Finland Ltd.
- Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)
arxiv_id: '2609.18739'
url: https://arxiv.org/abs/2609.18739
pdf_url: https://arxiv.org/pdf/2609.18739
published: '2026-09-16'
collected: '2026-09-17'
category: LLM
direction: 低资源语言 · LLM NER标注优化
tags:
- NER
- Low-Resource
- Self-Training
- LLM
- Data-Annotation
one_liner: 提出多步骤自动修正框架，通过自训练+双阈值提升低资源语言NER标注质量
practical_value: '- 电商多语言站点的低资源语种场景（如小语种商品属性抽取、用户Query实体识别）可直接复用双阈值+自训练的标注清洗流程，大幅降低人工标注成本

  - 业务侧已有噪声标注数据集无需重新标注，可参考该框架用小样本LLM+规则迭代补全缺失标注，快速提升下游模型性能

  - 多语言商品/内容理解任务中，可优先用该标注修正框架预处理小语种数据集后再微调模型，性价比远高于直接全量人工标注'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
低资源语言NER数据集普遍存在标注缺失、噪声大问题，严重制约监督模型性能，现有LLM在这类任务上表现弱于监督方案，亟需高效的标注质量优化方法。

### 方法关键点
1. 构建多步可扩展自动标注修正框架，采用基于词频的迭代策略
2. 融合自训练机制+双阈值置信度过滤，提升实体识别推理可靠性
3. 结合生成式LLM能力适配低资源语言NER场景

### 关键结果数字
在乌尔都语MK-PUCIT数据集上总实体标注量提升19.9%，其中ORG类实体标注量提升39.1%；旁遮普语Shahmukhi数据集总实体标注量提升7.3%，修正后的数据集可显著提升后续NER模型的基准性能。
