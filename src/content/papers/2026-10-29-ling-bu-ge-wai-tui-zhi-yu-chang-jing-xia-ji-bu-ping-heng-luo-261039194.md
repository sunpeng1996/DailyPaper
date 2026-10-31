---
title: 'Zero-Complement Extrapolation: Parameter Recovery and Classification in Severely
  Imbalanced Logistic Regression under Rank-Deficient Regimes'
title_zh: 零补格外推：秩亏场景下极不平衡逻辑回归的参数恢复与分类
authors:
- Chongsun Park
affiliations:
- Sungkyunkwan University
arxiv_id: '2610.39194'
url: https://arxiv.org/abs/2610.39194
pdf_url: https://arxiv.org/pdf/2610.39194
published: '2026-10-29'
collected: '2026-10-31'
category: Other
direction: 极不平衡分类 · 秩亏逻辑回归优化
tags:
- Imbalanced Classification
- Logistic Regression
- Rank Deficiency
- Oversampling
- Parameter Estimation
one_liner: 提出自校准零补格估计器，解决少数类样本数小于特征维度的极不平衡逻辑回归问题
practical_value: '- 电商高转化、欺诈检测等极稀有样本建模场景，n1远小于特征维度时，可复用多数类边缘外推合成样本思路，替代SMOTE避免子空间坍塌

  - 推荐冷启少样本分类（如新类目点击预测）任务，可借鉴多数类三阶偏度混合校准方法，降低截距偏差

  - CVR/CTR极端不平衡预估场景，可尝试外推合成少数类样本的trick，提升模型F1得分与训练稳定性'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
二分类任务少数类样本数$n_1$小于特征维度$p$时，传统逻辑回归出现准完全分离，惩罚似然方法存在严重截距偏差，SMOTE等插值过采样会陷入$n_1-1$维仿射子空间坍塌，模型效果骤降。
### 方法关键点
1. 范式从少数类插值转为多数类边缘外推，基于Stein引理，马氏白化后利用多数类$Y=0$的逻辑截断条件期望偏移唯一识别真实超平面法向量
2. 沿共轭方向从多数类分布高密分位数边缘向外外推合成少数样本，保持协方差满秩
3. 融合多数类固有三阶偏度和位置不变零边界截距校准，适配半监督/全监督场景
### 关键结果
极端稀有场景$n_1 \in \{3,5\}$时，相比Firth回归、SMOTE，F1得分与估计稳定性大幅提升，可高保真恢复最优超平面，避免参数发散
