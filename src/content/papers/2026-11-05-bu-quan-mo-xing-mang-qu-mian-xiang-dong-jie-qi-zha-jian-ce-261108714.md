---
title: 'Patching the Blind Spots: Reversible LLM Rule Overlay for Frozen Fraud Detectors'
title_zh: 补全模型盲区：面向冻结欺诈检测器的可逆LLM规则叠加框架
authors:
- Bo Qu
- Zhurong Wang
- Frank Zahradnik
- Ming Ouyang
affiliations:
- eBay
arxiv_id: '2611.08714'
url: https://arxiv.org/abs/2611.08714
pdf_url: https://arxiv.org/pdf/2611.08714
published: '2026-11-05'
collected: '2026-11-09'
category: LLM
direction: LLM 增强冻结模型欺诈检测能力
tags:
- LLM
- Fraud Detection
- SHAP
- Model Patching
- Tabular Data
- Ensemble LLM
one_liner: 无需修改已部署冻结树模型，通过LLM生成可逆规则叠加层补全欺诈检测盲区
practical_value: '- 线上已部署的冻结模型（如推荐召回/排序、风控模型）出现效果退化或盲区时，可直接叠加LLM生成的规则层，无需重训/重新上线，避免上线风险

  - 用SHAP定位现有模型权重偏低的特征，锚定LLM规则生成方向，可大幅降低无效规则产出比例，减少后续筛选成本

  - 单LLM输出效果方差大时，可采用多异质LLM的logit等权融合策略，牺牲部分峰值增益换稳定的效果下限，适配生产环境稳定性要求

  - 所有叠加规则均采用可读谓词形式，可追溯可回滚，完全满足合规要求，适合电商风控、交易链路等强监管场景'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
工业界表格类分类任务（如电商欺诈检测）多采用梯度提升树方案，已部署的冻结模型存在分布漂移、样本选择偏差导致的盲区，直接重训不仅有上线风险，还可能因训练样本偏差出现效果退化。
### 方法关键点
1. 用SHAP定位现有模型权重偏低的特征，锚定LLM规则生成方向，产出的规则池先做实证有效性筛选，再校准为可加、可逆的log-lift叠加层，直接在生产截断阈值处生效；
2. 采用3个异质LLM骨干的logit等权平均融合，降低单模型效果方差，保障最坏case下的效果下限。
### 关键结果
在eBay真实电商欺诈检测数据集上，相比重训方案的效果退化，叠加层在等精度下平均提升召回2.26%，等召回下平均提升精度1.60%；在7个公共偏差漂移基准变体上，所有变体的等召回精度均有提升，等精度召回基本保持中性。
