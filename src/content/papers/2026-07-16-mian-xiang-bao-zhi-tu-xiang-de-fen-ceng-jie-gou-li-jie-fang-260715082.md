---
title: Towards Hierarchical Structure Understanding of Newspaper Images
title_zh: 面向报纸图像的分层结构理解方法研究
authors:
- William Mocaër
- Solène Tarride
- Thomas Constum
- Merveilles Agbeti-Messan
- Tom Simon
- Clément Chatelain
- Stéphane Nicolas
- Pierrick Tranouez
- Sébastien Cretin
- Thierry Paquet
affiliations:
- LITIS UR4108, University of Rouen Normandy, France
- LITIS UR4108, INSA of Rouen Normandy, France
- Teklia, Paris, France
- Bibliothèque nationale de France, Paris, France
arxiv_id: '2607.15082'
url: https://arxiv.org/abs/2607.15082
pdf_url: https://arxiv.org/pdf/2607.15082
published: '2026-07-16'
collected: '2026-07-18'
category: Multimodal
direction: 多模态文档分层结构理解
tags:
- Document Understanding
- Layout Detection
- Transformer
- Dataset
- Semantic Segmentation
one_liner: 提出模块化pipeline与端到端Tiramisu架构两类报纸结构理解方案，同步开源专用评估数据集
practical_value: '- 电商商家海报、商品详情页的结构化信息提取，可复用YOLO+LayoutReader的模块化pipeline，兼顾落地成本与可解释性

  - Tiramisu分层Transformer显式建模层级结构的思路，可迁移用于长图文、商品评价的层级语义拆解任务

  - 合成样本生成方案可复用在低资源多模态结构化任务中，降低人工标注成本'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
报纸图像存在嵌套分层结构、密集异构布局的特点，结构理解难度高，现有方案难以同时兼顾准确性、灵活性与可解释性，无法支撑大规模文档数字化需求。

### 方法关键点
1. 模块化自底向上pipeline：组合开源SOTA组件，YOLO做布局检测、LayoutReader预测阅读顺序、自研算法完成文章分割，灵活性与可解释性强
2. 端到端Tiramisu架构：基于分层Transformer设计，通过迭代分层过程显式建模文档层级，用高并行注意力机制一站式完成栏目/文章分割、块定位、语义分类、阅读顺序预测全任务
3. 开源Finlam La Liberté数据集，专门用于历史报纸分层信息检索任务评估

### 关键结果
两类方案均能有效还原复杂报纸的层级结构，对比实验明确了模块化方案适合快速迭代场景、端到端方案适合高吞吐大规模数字化场景的各自优势。
