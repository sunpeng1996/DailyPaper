---
title: Using Hierarchical Controlled Vocabularies to Understand CLIP Retrieval Failures
  in Historical Photo Collections
title_zh: 基于分层受控词表解析历史照片集合中CLIP的检索失效问题
authors:
- Ratan Sebastian
- Anett Hoppe
- Christoph Rippe
- Ralph Ewerth
affiliations:
- TIB – Leibniz Information Centre for Science and Technology, Hannover, Germany
- L3S Research Center, Leibniz University Hannover, Germany
- Marburg University, Germany
- Hessian Center for Artificial Intelligence (hessian.AI), Germany
- Goethe University Frankfurt, Germany
arxiv_id: '2607.19836'
url: https://arxiv.org/abs/2607.19836
pdf_url: https://arxiv.org/pdf/2607.19836
published: '2026-07-22'
collected: '2026-07-24'
category: Multimodal
direction: 跨模态检索 · CLIP失效与优化分析
tags:
- CLIP
- Cross-Modal Retrieval
- Controlled Vocabulary
- Fine-tuning
- Failure Analysis
one_liner: 通过分层受控词表的结构属性解释CLIP检索失效模式及微调增益的分布规律
practical_value: '- 跨模态商品检索场景下，可将类目体系的层级深度、根类目类型作为先验特征，预判CLIP检索的效果边界，提前过滤低质量召回结果

  - CLIP微调优化时，优先对齐层级更浅的高频类目可获得更高投入产出比，长尾深层类目可搭配RAG补充召回能力

  - 拆分「视觉特征聚类一致性」「文本-特征对齐度」两个独立指标定位跨模态检索失效根因，比单一召回指标更易归因迭代'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
GLAM机构（画廊、图书馆、档案馆、博物馆）采用受控词表管理图像资源，CLIP类跨模态检索模型性能波动大，现有研究未结合词表的结构化属性解释失效原因。

### 方法关键点
基于AAT分层受控词表的两个结构属性（根facet类型、层级深度），拆分「视觉 coherence（同类目图像在CLIP嵌入空间的聚类紧密度）」「text-image alignment（类目文本嵌入与图像聚类中心的距离）」两个独立维度，在3套标注AAT的历史照片数据集上分析CLIP失效模式及微调效果。

### 关键结果
1. 视觉 coherence与text-image alignment几乎无相关性，可拆分4类失效模式，其中「图像聚类紧密但文本对齐差」的类目检索效果最差，在2/3数据集上比两类指标都差的类目表现更差；
2. 根facet类型可显著区分不同视觉 coherence的类目，常规检索指标与两个结构属性无显著相关性；
3. 微调整体提升检索效果，增益集中在层级更浅的类目，其text-image alignment提升最明显，不受概念频率影响。
