---
title: Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting
title_zh: 基于Koopman生成算子的高效概率时间序列预测框架
authors:
- Raz Marshanski
- Liran Nochumsohn
- Mayank Jauhari
- Boris N. Oreshkin
- Omri Azencot
affiliations:
- Ben-Gurion University of the Negev
- Amazon Science
arxiv_id: '2611.04760'
url: https://arxiv.org/abs/2611.04760
pdf_url: https://arxiv.org/pdf/2611.04760
published: '2026-11-03'
collected: '2026-11-05'
category: Other
direction: 概率时序预测 · 生成式推理效率优化
tags:
- Time-Series-Forecasting
- Koopman-Operator
- Flow-Matching
- Probabilistic-Forecasting
- Generative-Models
one_liner: 融合三类核心模块的KGO概率时序预测框架，兼具SOTA精度与超25倍迭代模型推理速度
practical_value: '- 电商场景销量、流量、用户活跃度等时序预测任务可复用KGO单步生成逻辑，替换原有迭代式生成预测模型，推理速度提升25倍以上，适配高QPS在线推理需求

  - 可直接复用Adaptive Uncertainty Gate(AUG)模块，无人工调参下自动适配不同预测变量、预测周期的不确定性估计，优化库存备货、大促流量预判等决策的鲁棒性

  - Koopman Patch Embedding(KoPE)的时序一致性隐轨迹外推思路可迁移到用户行为序列建模，提升长周期用户兴趣预测的稳定性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有概率时序预测方案无法同时满足时序结构建模、不确定性表达、高效推理三类需求：隐式动力学模型生成机制受限，扩散、流匹配等现代生成方法依赖迭代采样，推理延迟高。
### 方法关键点
Koopman Generative Operator(KGO)框架融合三类核心组件：
1. Koopman Patch Embedding(KoPE)：实现时序一致的隐轨迹外推
2. Koopman Flow Matching(KoFM)：在Koopman隐空间通过闭式矩阵指数实现单步生成，无需迭代采样
3. Adaptive Uncertainty Gate(AUG)：逐变量、逐预测周期自适应调整不确定性，无人工调参即可完成随机不确定性的学习分解
### 关键结果
在17个ProbTS基准测试中，CRPS指标SOTA占比13/17，NMAE指标SOTA占比16/17；推理速度相比迭代生成模型至少提升25倍，大幅优化精度-效率权衡。
