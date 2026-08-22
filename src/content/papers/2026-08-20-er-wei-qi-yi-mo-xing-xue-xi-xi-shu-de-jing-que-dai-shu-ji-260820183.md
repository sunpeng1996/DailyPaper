---
title: Exact Algebraic Computation of Learning Coefficients for Two-Dimensional Singular
  Models
title_zh: 二维奇异模型学习系数的精确代数计算
authors:
- Grégoire Sergeant-Perthuis
- Elias Tsigaridas
- Jules Tsukahara
affiliations:
- CQSB, Sorbonne Université
- Ouragan team, Inria Paris
arxiv_id: '2608.20183'
url: https://arxiv.org/abs/2608.20183
pdf_url: https://arxiv.org/pdf/2608.20183
published: '2026-08-20'
collected: '2026-08-22'
category: Training
direction: 模型选择 · 奇异模型学习系数计算
tags:
- Model Selection
- Singular Models
- RLCT
- WBIC
- Deterministic Algorithm
one_liner: 提出首个确定性算法精确计算二维奇异模型局部RLCT，填补WBIC学习系数通用精确求解空白
practical_value: '- 浅层小模型（二维参数空间）选型场景，可复用该确定性算法替代采样法计算RLCT，提升WBIC校准效率

  - 多项式神经网络结构优化场景，可用该方法获得学习系数精确真值，校准原有采样估计的偏差

  - 大规模推荐/LLM等超二维高维模型场景目前暂不适用，仅可作为理论参考优化奇异模型信息准则设计'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
经典BIC依赖正则性假设，在深度学习等奇异模型场景下失效，会输出错误的模型选择结果；WBIC依赖的局部学习系数λ（对应KL散度的局部实对数正则阈值RLCT）此前仅能通过采样法估计，无通用精确求解方案。
### 方法关键点
首个确定性算法可针对KL散度与多项式接触等价的任意二维模型精确计算局部RLCT，同时推导得到了算法的复杂度上界。
### 关键结果
算法在含多项式神经网络在内的广泛模型类别上验证有效，既可为采样估计器提供校准真值，还能挖掘采样法无法发现的学习系数代数结构，浅层模型场景下计算速度显著优于采样法。
