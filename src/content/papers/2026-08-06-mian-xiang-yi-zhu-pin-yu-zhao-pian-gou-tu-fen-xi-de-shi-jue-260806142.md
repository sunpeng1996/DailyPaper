---
title: Learning visual representations for compositional analysis of artworks and
  photographs
title_zh: 面向艺术品与照片构图分析的视觉表征学习
authors:
- Fatemeh Behrad
- Tinne Tuytelaars
- Johan Wagemans
affiliations:
- KU Leuven University
arxiv_id: '2608.06142'
url: https://arxiv.org/abs/2608.06142
pdf_url: https://arxiv.org/pdf/2608.06142
published: '2026-08-06'
collected: '2026-08-09'
category: Multimodal
direction: 多模态视觉表征 · 构图分析与美学评估
tags:
- visual representation
- computational aesthetics
- graph attention network
- object-centric learning
- image retrieval
one_liner: 对比两类视觉构图分析范式，明确不同场景下性能、可解释性与泛化性的trade-off
practical_value: '- 电商/广告图美学评分场景选型参考：小样本冷启动优先用人启发的object-centric+GAT方案，兼顾可解释性与跨域泛化性

  - 大样本商品海报/主图构图优化场景，优先微调自监督大模型，可获得显著性能提升

  - 多模态召回的构图相似商品检索任务，可复用GAT建模视觉元素空间关系的trick，提升跨域召回准确率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视觉理解体系缺乏形式化的构图表征建模，存在语义偏差，难以兼顾性能、可解释性与跨域泛化性，在美学评估、图像检索等场景落地受限。
### 方法关键点
对比两类构图分析范式：1）人启发范式：基于object-centric模型做区域级分解，用GAT建模元素间空间关系，编码器全程冻结；2）大模型范式：基于大规模构图数据集微调自监督基础模型。在三类任务上统一评测：构图分数/类别预测、构图相似图像检索、视觉显著性检测。
### 关键结果
冻结编码器时，人启发范式性能达到竞争力水平且可解释性强；数据充足时，微调自监督大模型性能显著更优，但可解释性、跨域泛化性出现明显下降。
