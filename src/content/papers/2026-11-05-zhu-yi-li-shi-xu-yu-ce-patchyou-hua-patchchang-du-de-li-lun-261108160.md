---
title: 'Patch Attention Wisely: Understanding Patch Length in Attention-Based Forecasting'
title_zh: 注意力时序预测Patch优化：Patch长度的理论解释与选择框架
authors:
- Junyu Chen
- Likai Chen
- Weining Wang
affiliations:
- University of Groningen
- Washington University in St. Louis
- University of Bristol
arxiv_id: '2611.08160'
url: https://arxiv.org/abs/2611.08160
pdf_url: https://arxiv.org/pdf/2611.08160
published: '2026-11-05'
collected: '2026-11-07'
category: Other
direction: 时序预测 · 注意力Patch长度优化
tags:
- TimeSeriesForecasting
- AttentionMechanism
- PatchTuning
- TheoreticalAnalysis
- ModelOptimization
one_liner: 为注意力时序预测的Patch长度选择提供可解释理论框架与量化准则
practical_value: '- 电商时序预测场景（销量/流量/库存/用户活跃度预估）用Patch类注意力模型时，可直接复用论文的Patch选择准则，替代盲目网格调参，平衡预测效果与计算开销

  - 训练样本量少、序列存在强长程依赖时，优先选择中等长度Patch，避免表示误差、估计误差双高

  - 注意力头数与Patch长度可联动调整：头数不足时选更短Patch提升表示能力，头数充足时可拉长Patch降低训练与推理成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
注意力时序预测模型普遍采用连续观测分Patch的设计，Patch长度对预测性能影响极大，但当前选型完全依赖经验调参，缺乏理论支撑。
### 方法关键点
1. 针对线性状态空间模型，推导预测系数矩阵的精确分解形式，分离预测动态与滤波动态，证明长预测周期下单一预测成分占优不代表秩一表示，解释了长预测周期不一定降低表示复杂度的现象
2. 结合分解结果与估计边界，提出时序依赖下平衡表示误差、估计误差的Patch选择准则，明确预测结构、注意力头数、训练样本量、长程依赖四个核心影响因子
### 关键结果
给出了均衡Patch设置的适用边界，可量化输出最优Patch长度区间，相比经验调参降低80%以上的调参成本，预测精度显著优于经验选型基线
