---
title: Prediction-Powered Smoothing and Validation for Disaggregated AI Evaluation
title_zh: 面向细粒度AI评估的预测驱动平滑与验证方法
authors:
- Sho Kawano
- Zehang Richard Li
- Paul A. Parker
affiliations:
- Department of Statistics, University of California, Santa Cruz
arxiv_id: '2609.20758'
url: https://arxiv.org/abs/2609.20758
pdf_url: https://arxiv.org/pdf/2609.20758
published: '2026-09-17'
collected: '2026-09-18'
category: Eval
direction: 细粒度AI评估 · 小样本性能估计
tags:
- disaggregated evaluation
- prediction-powered inference
- cross-validation
- small area estimation
- AI evaluation
one_liner: 提出预测驱动平滑方法与无偏交叉验证评分，解决小样本下细粒度AI评估精度不足问题
practical_value: '- 做推荐/Agent的细粒度效果评估（分用户群、分商品类目、分query类型）时，可复用PP-S方法借用跨域信息提升小样本域的评估精度，减少标注成本

  - 评估多estimator选型时，可直接复用文中提出的近似无偏设计型CV评分，不用额外采独立验证集，同等标注预算下评估误差更准

  - 对LLM Agent对话效果分场景评测的场景，可直接套用本文的「预测驱动估计+跨taxonomy信息增强」框架，降低人工标注量'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
AI系统尤其是LLM/Agent需要分域细粒度评估，但全量标注成本极高，现有直接估计方法（含PPI）仅用单域标签，小样本域的点估计、区间估计精度极低，无法满足评估需求。
### 方法关键点
1. 提出预测驱动平滑（PP-S），基于贝叶斯模型拟合每个域的PPI估计值，扩展版PP-TS可跨报告分类体系借用其他域的信息增强小样本域估计；
2. 设计近似无偏的基于设计的交叉验证评分，可在直接估计、平滑估计器之间做最优选型。
### 关键结果
在人工标注benchmark与真实部署Agent流量数据集上，PP-S/PP-TS比直接估计的点、区间估计效果显著提升，区间覆盖率接近标称值；同等采样预算下，新CV评分的选型效果与独立验证集相当，对选中估计器的误差估计精度远高于baseline。
