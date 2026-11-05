---
title: Balance-Guided Forest for Causal Effect Estimation
title_zh: 用于因果效应估计的平衡引导森林算法
authors:
- Feiyang Yi
- Jelena Bradic
affiliations:
- Cornell University
arxiv_id: '2611.05723'
url: https://arxiv.org/abs/2611.05723
pdf_url: https://arxiv.org/pdf/2611.05723
published: '2026-11-03'
collected: '2026-11-05'
category: Other
direction: 因果效应估计 · 协变量平衡树模型
tags:
- Causal Inference
- Covariate Balancing
- Tree-based Model
- Observational Study
- Effect Estimation
one_liner: 提出耦合协变量平衡与树表示学习的平衡引导森林，提升观察性研究因果效应估计精度
practical_value: '- 可迁移到电商广告Uplift建模场景，用BGF的分裂得分规则优化树结构，减少混淆变量导致的增益估计偏差

  - 解决观察性用户行为数据的协变量不平衡问题，替代现有森林类Uplift模型的分裂逻辑，提升干预效果预估准确率

  - 针对推荐系统AB实验数据补全场景，用BGF耦合平衡与表示学习的思路，降低非随机分流带来的实验效果评估误差'
score: 7
source: arxiv-stat.ML
depth: abstract
---

## 动机
现有森林核平衡方法采用先学习树表示、再构造平衡权重的两步流程，存在结构不匹配问题：有限的树容量易浪费在已经表征良好的特征上，导致因果效应估计偏差较高。
## 方法关键点
1. 提出Balance-Guided Forest（BGF），用当前平衡权重引导后续树构造，将表示学习与协变量平衡深度耦合，而非将平衡作为下游独立步骤；
2. 设计全新分裂得分函数，融合残差不平衡与outcome对比指标，优先选择可分割仍存在不平衡的outcome相关区域的分裂点；
3. 理论上证明了关联迭代构造过程与加权误差、因果偏差的oracle-type边界。
## 关键结果
仿真实验中因果估计效果显著优于现有森林核方法，多个真实观察研究数据集验证了算法的实际有效性。
