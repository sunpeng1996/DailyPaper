---
title: 'Bar-JEPA: Extracting Values from Bar Chart with Joint-Embedding Predictive
  Architecture'
title_zh: Bar-JEPA：基于联合嵌入预测架构的柱状图数值提取方法
authors:
- Poonam Poonam
- Alexander Epple
- Timo Ropinski
affiliations:
- Institute of Media Informatics, Visual Computing Group, Ulm University, Germany
arxiv_id: '2608.06062'
url: https://arxiv.org/abs/2608.06062
pdf_url: https://arxiv.org/pdf/2608.06062
published: '2026-08-06'
collected: '2026-08-08'
category: Multimodal
direction: 多模态文档理解 · 图表数值抽取
tags:
- JEPA
- Self-supervised Learning
- Multimodal Understanding
- Chart Information Extraction
- Document Analysis
one_liner: 基于JEPA自监督架构的柱状图数值提取方案，仅需少量标注即可实现高性能数值还原
practical_value: '- 电商/广告行业研报、竞品公开数据自动抓取场景，可复用JEPA自监督预训练+轻量微调的结构，解决图表标注数据不足问题，大幅降低标注成本

  - 多模态特征抽取类任务可优先采用JEPA类自监督架构预训练编码器，下游仅需微调轻量Decoder即可快速上线，显著降低训练算力与时间开销

  - 运营端多源数据汇总场景可接入该柱状图抽取能力，自动同步竞品销量、营收等公开图表数据，补充现有推荐系统的外部特征池'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
柱状图是应用最广的数据可视化形式，现有机器自动提取其底层数值的方案依赖大量标注实采数据，标注耗时久、公开标注样本稀缺，端到端监督训练泛化性差、训练成本高。

### 方法关键点
1. 采用JEPA自监督架构预训练编码器，无需标注即可学习高语义质量的柱状图隐层特征；
2. 下游对接极轻量的Decoder，仅需少量标注微调即可输出坐标轴刻度、柱体坐标，可直接换算得到每根柱对应的数值；
3. 整套pipeline支持端到端推理，无需额外OCR或规则后处理模块。

### 关键结果
相比端到端监督基线，自监督微调后模型数值提取准确率显著更优，Decoder训练速度提升70%以上，整套方案已开源代码、数据集与预训练checkpoint。
