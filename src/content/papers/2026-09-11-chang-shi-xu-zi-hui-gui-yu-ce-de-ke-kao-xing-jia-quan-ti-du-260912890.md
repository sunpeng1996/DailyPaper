---
title: 'Large Distant Gradients Need Not Be Reliable: reliability-weighted credit
  assignment for long-horizon autoregressive forecasting'
title_zh: 长时序自回归预测的可靠性加权梯度信用分配方法
authors:
- Junhao Zhao
- David Michael Simberg
- Jacob Kang
- Colin Connor Kurniawan
- Nan Xu
affiliations:
- University of Maryland, College Park
arxiv_id: '2609.12890'
url: https://arxiv.org/abs/2609.12890
pdf_url: https://arxiv.org/pdf/2609.12890
published: '2026-09-11'
collected: '2026-09-14'
category: Training
direction: 长时序自回归训练 · 梯度优化
tags:
- Gradient_Optimization
- Autoregressive_Forecasting
- BPTT
- Long_Horizon
- Credit_Assignment
one_liner: 提出仅反向干预的Internal-DW梯度路由方法，解决长时序自回归预测远梯度不可靠问题
practical_value: '- 长序列用户行为建模的自回归训练场景，可借鉴Internal-DW梯度加权思路替代梯度裁剪、TBPTT，降低远梯度噪声带来的训练不稳定

  - 搭建生成式推荐/序列预测训练框架时，可复用残差块的Wiener增益计算逻辑，按梯度信噪比动态分配不同反向路径权重

  - 历史数据充足的长时序广告库存预测、用户LTV预测场景，可尝试引入Internal-DW实现5%以上的预测误差降低'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
长时序自回归预测中，BPTT会将远步长损失的梯度经过多步回传，重复雅可比乘积会同时放大梯度中的信号和噪声，大梯度不一定携带可靠学习信号，反而可能主导参数更新降低模型效果。

### 方法关键点
提出仅在反向传播阶段干预的Internal-DW路由：完全保留前向传播逻辑和全步长损失，在每个残差块为恒等、非线性路径推导有界Wiener增益，平衡可预测信号保留与不可预测噪声抑制，增益从路径级梯度统计和显式噪声模型估计得到。

### 关键结果
1. 4个历史主导、弱驱动测试集上，相对全量BPTT预测误差降低5.2%-13.8%，全部优于梯度裁剪、雅可比正则化，3个测试集优于验证集选择的截断BPTT
2. 可扩展或保持最优训练步长范围，仅在可用历史有限、采样器无法表征主导变异时效果下降
