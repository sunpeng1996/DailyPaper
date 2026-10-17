---
title: 'SelectPFN: Amortized Bayesian Variable Selection for Sparse Nonlinear Regression
  with Prior-Data Fitted Networks'
title_zh: SelectPFN：面向稀疏非线性回归的摊销贝叶斯变量选择方法
authors:
- Bin Luo
affiliations:
- Kennesaw State University
arxiv_id: '2610.21950'
url: https://arxiv.org/abs/2610.21950
pdf_url: https://arxiv.org/pdf/2610.21950
published: '2026-10-15'
collected: '2026-10-17'
category: Other
direction: 稀疏非线性回归 · 贝叶斯变量选择
tags:
- PFN
- Bayesian Variable Selection
- Sparse Regression
- Amortized Inference
- Tabular Foundation Model
one_liner: 提出面向稀疏非线性回归的SelectPFN，可单前向传播联合完成贝叶斯变量选择与预测
practical_value: '- 可复用SelectPFN的快速特征选择思路，筛选电商推荐/广告场景高维用户/物品特征的有效子集，降低下游模型训练与推理开销

  - 列置换等变+仿冒列随机交错的设计可迁移，用于特征重要性评估的FDR控制，避免误筛业务核心特征

  - 摊销预训练模式可借鉴，预训练通用特征选择模型，无需每次新增业务数据集都重新做特征选择调优'
score: 6
source: arxiv-stat.ML
depth: abstract
---

## 动机
现有基于PFN的表格基础模型仅能通过单次前向传播完成预测，无法输出预测依赖的输入特征，可解释性不足；高维稀疏非线性回归场景下传统变量选择方法存在效率低、精度差、误筛率高的问题。
## 方法关键点
1. 提出SelectPFN，单次前向传播即可输出每个变量的后验包含概率，仅基于采样的变量子集做预测，可证明排除的特征不会影响预测结果，完全符合贝叶斯模型要求
2. 基于组spike-and-slab稀疏输入神经网络构造元先验，仅需在合成任务上完成一次预训练，无需针对单数据集做适配拟合
3. 采用列置换等变架构+原始/仿冒列随机交错设计，实现有限样本下精确的FDR控制，不受元先验错误影响
## 关键结果
在特征数最高500的先验外非线性任务上，PR-AUC比Lasso、BART、DART等基线高0.23-0.28，FDP约0.07，单数据集推理仅需0.04s，比DART快300倍以上；真实数据集上PR-AUC比基线高0.17-0.26
