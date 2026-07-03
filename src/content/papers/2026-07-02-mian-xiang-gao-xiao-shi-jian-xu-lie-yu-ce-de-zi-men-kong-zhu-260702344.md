---
title: Self-Gating Attention for Efficient Time Series Forecasting
title_zh: 面向高效时间序列预测的自门控注意力机制
authors:
- Dezheng Wang
- Tong Chen
- Wei Yuan
- Congyan Chen
- Shihua Li
- Hongzhi Yin
arxiv_id: '2607.02344'
url: https://arxiv.org/abs/2607.02344
pdf_url: https://arxiv.org/pdf/2607.02344
published: '2026-07-02'
collected: '2026-07-03'
category: Other
direction: 时间序列预测 · 高效注意力机制优化
tags:
- Attention Mechanism
- Time Series Forecasting
- Efficient Inference
- Plug-and-Play
- Linear Complexity
one_liner: 提出可插拔自门控注意力SGA，将时间序列预测注意力复杂度降至线性同时保持SOTA级性能
practical_value: '- 电商销量、流量、库存等时间序列预测任务可直接替换原有Transformer的注意力模块为SGA，线性降低推理延迟，适配高吞吐在线预测场景

  - 可复用「公共模式共享矩阵+输入相关残差」的注意力设计思路，优化推荐系统用户长行为序列建模的注意力效率

  - 高吞吐低资源约束的在线系统中，可参考SGA的可插拔设计，无需修改原有模型主干即可做性能优化，降低改造成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Transformer用于时间序列预测时，标准自注意力随历史回溯长度呈二次时间与内存复杂度，无法适配资源受限、高吞吐的工业级在线预测需求；且观测到真实时序数据的注意力图存在大量跨时间戳冗余模式，源于时序模式重复、相关性稳定的特性。
### 方法关键点
提出可插拔自门控注意力SGA，用共享可学习矩阵捕捉通用注意力模式，搭配输入依赖的残差组件捕捉个性化波动；去掉标准注意力计算中的Q、K投影步骤，实现随回溯长度线性的时间与内存复杂度。
### 关键结果
在电力、金融、气象等9个公开真实数据集上测试，相比现有SOTA轻量注意力变体，SGA推理效率显著提升，同时预测性能保持竞争力，支持直接部署落地
