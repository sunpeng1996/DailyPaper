---
title: Goodness-of-Fit Tests and Calibration Machine-Learning Algorithms for Logistic
  Regression with Sparse Data
title_zh: 稀疏数据下逻辑回归的拟合优度检验与校准机器学习算法
authors:
- Ebrahim Khaled Ebrahim
affiliations:
- Alexandria University
arxiv_id: '2608.11140'
url: https://arxiv.org/abs/2608.11140
pdf_url: https://arxiv.org/pdf/2608.11140
published: '2026-08-11'
collected: '2026-08-13'
category: Eval
direction: 模型评估 · 稀疏数据逻辑回归校准检验
tags:
- Logistic Regression
- Goodness-of-Fit Test
- Sparse Data
- Model Calibration
- Statistical Evaluation
one_liner: 对比30余种稀疏数据下逻辑回归GOF检验与校准算法，给出最优评估方案
practical_value: '- 做LR CTR/广告点击率模型校准评估时，优先选用GiViTI、McCullagh、Osius-Rojek等5种检验方法，兼顾低假阳性率和高缺陷识别能力

  - 稀疏连续特征场景下需弃用传统卡方、偏差检验做GOF评估，避免得到错误检验结论

  - LR模型评估不能仅依赖统计指标，需搭配校准曲线可视化分析，捕捉统计检验漏检的拟合缺陷'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
逻辑回归是电商CTR预估、广告点击率预测等场景的常用模型，稀疏数据下传统卡方、偏差等拟合优度（GOF）检验的渐近分布假设不成立，常输出无效评估结果。
### 方法关键点
覆盖分组、稀疏数据两类场景，对比共30余种经典GOF检验、ML校准算法，包含卡方/Hosmer-Lemeshow变体、标准化皮尔逊统计量、协变量空间分区、平滑类方法、bootstrap校准流程等类别。
### 关键结果
固定检验规模下，GiViTI、McCullagh等5种检验表现最优，平衡高拟合缺陷识别能力与低假阳性率；仅依赖正式统计检验不足，校准图等可视化手段可捕捉检验漏检的模型缺陷；真实数据集验证多数检验在复杂真实数据下结论无效，最终建议采用「多强效力统计检验+可视化校准检查」的组合评估方案。
