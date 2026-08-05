---
title: Why Large Language Models Fail at Tabular Prediction
title_zh: 大语言模型表格预测任务性能不佳的原因探究
authors:
- Marta Garnelo
- Wojciech M. Czarnecki
affiliations:
- Fundamental Technologies
- Voylab
arxiv_id: '2608.02412'
url: https://arxiv.org/abs/2608.02412
pdf_url: https://arxiv.org/pdf/2608.02412
published: '2026-08-03'
collected: '2026-08-05'
category: LLM
direction: 大语言模型能力边界 · 表格预测
tags:
- LLM
- Tabular Prediction
- Dimensionality
- Model Capability
- Inference
one_liner: 通过控制变量实验验证LLM表格预测失效核心原因是输入维度过高，排除其余四类常见假设
practical_value: '- 做电商/广告用户/商品特征相关的LLM推理任务时，先做特征降维（特征筛选、PCA等），避免高维输入直接喂给LLM导致性能骤降

  - 处理结构化表格类任务（用户消费预测、商品动销预判等）时，优先让LLM调用传统树模型/SQL等工具做计算，不要依赖纯prompt原生推理做表格预测

  - 低维特征场景（仅用2-3个核心特征做简单规则匹配）可直接用LLM推理，性能接近传统距离类模型，无需额外训练小模型'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
LLM在文本、代码等多类任务上已成为通用底座，但在工业界广泛使用的表格预测任务上表现远不如传统基线，其失效原因始终缺乏系统性验证结论。
### 方法关键点
针对无微调、无工具调用、无Agent脚手架的纯推理场景，控制变量验证5类常见失效假设：无法处理噪声/非线性可分数据、CSV线性格式掩盖列结构、数值tokenization缺陷、单query测试点数量、输入维度。
### 关键结果数字
- 排除前4类假设，仅输入维度是核心影响因素：31个基准数据集上，9类对比方法中仅LLM准确率随维度升高持续下降，其余传统基线均持平或提升
- 2维场景下LLM预测行为与局部距离类模型网格匹配度达91.6%，高维场景下其失效模式无任何经典模型（含加维度依赖噪声的模型）可复现
