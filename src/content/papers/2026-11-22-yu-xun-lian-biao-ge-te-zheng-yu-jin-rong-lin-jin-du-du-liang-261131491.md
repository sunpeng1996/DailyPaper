---
title: Pretrained Tabular Features and the Measurement of Financial Proximity
title_zh: 预训练表格特征与金融邻近度度量
authors:
- Marcus Gawronsky
arxiv_id: '2611.31491'
url: https://arxiv.org/abs/2611.31491
pdf_url: https://arxiv.org/pdf/2611.31491
published: '2026-11-22'
collected: '2026-11-28'
category: Other
direction: 表格基础模型 · 金融结构度量
tags:
- Tabular Foundation Model
- Financial Proximity
- Asset Pricing
- Representation Learning
- SEC Filing
one_liner: 利用表格基础模型冻结表征衡量企业金融相似度，提升空间资产定价模型效果
practical_value: '- 可复用冻结预训练模型的中间表征作为实体（商品/商家/用户）相似度计算特征，无需微调即可降低业务适配成本

  - 结构化任务中引入对应非结构化补充数据（如商品详情/用户评论），可显著提升预训练表征的下游效果增益

  - 黑盒预训练模型除预测输出外，其内部表征的业务语义挖掘可拓展相似品召回、竞品匹配等新应用场景'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
空间套利定价理论（S-APT）的效果高度依赖企业间金融邻近度的度量精度；现有表格基础模型（TFM）预测性能优异但可解释性差，难以应用于强监管的金融场景，而大模型内部表征可用于探针学习内容与相似度度量。
### 方法关键点
冻结4类TFM的内部表征作为企业金融差异度的度量指标，接入2011-2025年美股S-APT模型，对比基于同披露数据的直接距离度量效果，额外引入SEC全量filing数据做特征补充。
### 关键结果
纳入SEC全量数据后，TFM表征的度量效果较直接距离的增益持续为正，可将TFM从黑盒预测器转化为经济结构度量工具，直接适配同行选择、风险归因、网络资产定价等场景。
