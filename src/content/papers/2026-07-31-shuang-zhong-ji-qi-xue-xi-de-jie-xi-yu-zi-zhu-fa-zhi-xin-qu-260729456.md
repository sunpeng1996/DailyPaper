---
title: 'Analytical and Bootstrap Confidence Intervals of Double Machine Learning:
  Simulation studies and an application to rural-urban difference in obesity prevalence'
title_zh: 双重机器学习的解析与自助法置信区间：模拟研究及城乡肥胖率差异应用
authors:
- Haozheng Xu
- Siyuan Ma
- Qingyan Xiang
affiliations:
- Department of Biostatistics, Vanderbilt University Medical Center
arxiv_id: '2607.29456'
url: https://arxiv.org/abs/2607.29456
pdf_url: https://arxiv.org/pdf/2607.29456
published: '2026-07-31'
collected: '2026-08-04'
category: Other
direction: 因果推断 · DML置信区间评估
tags:
- DML
- Causal Inference
- Confidence Interval
- Bootstrap
- Treatment Effect Estimation
one_liner: 通过模拟与真实数据验证了干扰模型选择对DML置信区间覆盖性能的关键影响
practical_value: '- 电商策略uplift评估用DML时，优先测试树模型（LightGBM/随机森林）作为干扰项估计器，避免置信区间覆盖度不足导致的效果误判

  - 大样本下DML解析与bootstrap置信区间覆盖度均会下降，策略效果显著性判断建议结合多组干扰模型结果交叉验证

  - 需高可靠DML效应推断时，可同时计算两类置信区间，取交集作为显著性判断的参考依据'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
DML是因果处理效应估计的主流方案，支持灵活选择机器学习方法估计干扰参数并保留有效推断，但当前干扰模型选型对DML方差估计、置信区间有效性的影响尚未被充分验证，从业者缺乏明确的选型参考。

### 方法关键点
覆盖OLS、LASSO、随机森林、LightGBM、神经网络五类常用干扰模型，在多组数据生成设置下，对比DML理论推导的解析置信区间、bootstrap置信区间的偏差、区间宽度、核心指标覆盖概率；补充美国县域城乡肥胖率真实数据集验证结论普适性。

### 关键结果
不同模型的置信区间覆盖性能存在显著差异，学习者选型是DML推断可靠性的核心影响因素；多数场景下样本量提升时，两类置信区间的覆盖概率均出现下降；真实数据验证了模型选型的性能差异，同时证实乡村化程度对县域肥胖率存在统计显著的正向效应。
