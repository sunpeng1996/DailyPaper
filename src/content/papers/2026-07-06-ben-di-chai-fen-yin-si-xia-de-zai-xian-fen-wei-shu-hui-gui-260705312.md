---
title: 'Locally Private Online Quantile Regression: Estimation and Inference'
title_zh: 本地差分隐私下的在线分位数回归：估计与推断
authors:
- Yi Liu
- Qirui Hu
affiliations:
- York University
- Shanghai University of Finance and Economics
arxiv_id: '2607.05312'
url: https://arxiv.org/abs/2607.05312
pdf_url: https://arxiv.org/pdf/2607.05312
published: '2026-07-06'
collected: '2026-07-09'
category: Training
direction: 隐私保护 · 在线回归模型训练
tags:
- LDP
- Quantile Regression
- Online Learning
- Privacy Preserving
- Stochastic Approximation
one_liner: 提出基于有限字母信道的LDP在线分位数回归方案，实现无偏推断且效果优于主流隐私机制
practical_value: '- 电商用户敏感数据建模可借鉴支持感知随机量化+随机响应的LDP方案，降低用户行为数据泄露风险

  - 无偏解码的在线分位数回归逻辑可复用到动态定价、配送时长预测等需分位数估计的业务场景

  - 无需Hessian的自归一化推断方法可降低隐私保护在线模型的工程实现复杂度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
在线分位数回归适用于偏态、异质性数据的分布估计，但用户敏感数据流场景下需满足LDP隐私约束，标准估计方程的协变量与残差耦合特性导致服务端无法直接用私有化数据做在线更新。
### 方法关键点
1. 构建有限字母信道，用户本地计算贡献后对选中块做支持感知随机量化+随机响应，仅上报单条结果；
2. 公共解码器矫正随机响应失真，重构条件均值无偏的估计方程输入；
3. 结合投影Polyak-Ruppert平均做在线更新，支持无Hessian的自归一化推断。
### 关键结果
仿真及纽约出租车行程数据集验证：隐私预算越高，私有模型输出越接近非私有在线基准；相同隐私约束下效果优于直接拉普拉斯、面指数几何发布机制
