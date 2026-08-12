---
title: 'TSDS-Toolbox: A Toolbox for Measuring Time-Series Dataset Similarity'
title_zh: TSDS-Toolbox：时序数据集相似度度量工具包
authors:
- Yen-Ku Liu
- Hongjie Chen
- Ryan A. Rossi
- Franck Dernoncourt
affiliations:
- National Yang Ming Chiao Tung University
- Dolby Laboratories
- Adobe Research
arxiv_id: '2608.08119'
url: https://arxiv.org/abs/2608.08119
pdf_url: https://arxiv.org/pdf/2608.08119
published: '2026-08-07'
collected: '2026-08-12'
category: Other
direction: 时序数据集相似度 · 基准评测框架
tags:
- Time-Series
- Similarity Measurement
- Benchmark
- Open Source
- Time Series Analysis
one_liner: 开源统一可扩展的时序数据集相似度度量框架，支持自定义组件与多维度一致评估
practical_value: '- 做电商用户行为时序、销量时序等业务时序跨域相似匹配时，可直接复用工具包内置度量方法，减少重复开发

  - 微调销量预测、用户行为预测类时序大模型时，可通过该工具匹配最相似的源数据集做微调，提升下游业务效果

  - 针对点击序列、转化序列等自定义业务时序数据，可扩展工具包自定义接口快速适配场景化相似度评测需求'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
时序分析（预测、分类、生成）领域发展迅速，尤其时序大模型微调高度依赖数据集相似度匹配筛选源域数据，但现有时序相似度度量实现碎片化、可扩展性差，评测结果难以复现、难以定制适配业务需求。
## 方法关键点
推出统一框架TSDS-Toolbox，核心能力包括：1）支持各类时序数据集相似度方法的系统化、可复现对比；2）支持自定义数据集、相似度算法、下游任务的灵活扩展；3）内置时序数据reducer模块，可统一完成数据集级、序列级两类相似度方法的一致性评估。
## 关键结果
在多类实验设置下完成框架有效性验证，工具包已完全开源，支持工业界/学术界直接使用或二次开发。
