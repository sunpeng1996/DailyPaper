---
title: Conformal Bayes for Two-Sided Censored Gaussian Regression under Label Shift
title_zh: 标签偏移下双侧截断高斯回归的共形贝叶斯方法
authors:
- Seungjin Choi
affiliations:
- CROID Research
- aSSIST University, Korea
arxiv_id: '2607.02173'
url: https://arxiv.org/abs/2607.02173
pdf_url: https://arxiv.org/pdf/2607.02173
published: '2026-07-02'
collected: '2026-07-06'
category: Other
direction: 截断回归 · 标签偏移校准方法
tags:
- Conformal Prediction
- Label Shift
- Censored Regression
- Bayesian Inference
- Tobit Model
one_liner: 针对双侧截断高斯回归的标签偏移场景，提出融合后验倾斜与加权共形校准的混合空间共形贝叶斯方法
practical_value: '- 做用户消费能力、营销预算等存在上下截断的预测任务时，可借鉴混合密度校准思路修正标签偏移带来的预测偏差

  - CTR/CVR预测的置信区间校准场景，尤其是极端样本存在截断时，可复用三成分归一化的后验倾斜方法提升预测集覆盖度

  - 新场景冷启动出现样本分布偏移时，可参考加权共形校准思路，无需重训模型即可适配目标域分布，降低上线成本'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
标签偏移场景下，当响应存在上下截断（低于下限L记为L、高于上限U记为U）时，传统预测方法无法适配观测值的混合分布（边界离散原子+区间连续密度）的校准需求，现有共形方法无法直接处理截断带来的观测空间密度比不匹配问题。
### 方法关键点
1. 融合后验预测倾斜与加权共形校准，适配双侧截断高斯模型的混合空间预测需求；
2. 采用双侧Tobit高斯贝叶斯预测头+拉普拉斯后验近似，得到左原子、中间区间、右原子三成分的倾斜预测分布，具备闭式三范式归一化项；
3. 引入隐式指数倾斜生成截断边界的尾平均原子权重，结合中间区间密度比构造混合观测空间校准权重，修正校准度量。
### 关键结果
合成实验显示，加权倾斜共形贝叶斯方法恢复边缘覆盖度的同时，预测集大小比加权源分数校准更小，同时存在边缘覆盖度与原子/区间样本分组件性能的权衡。
