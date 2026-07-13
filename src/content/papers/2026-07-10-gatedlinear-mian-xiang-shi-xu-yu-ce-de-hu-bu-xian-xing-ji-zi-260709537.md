---
title: 'GatedLinear: Adaptive Routing of Complementary Linear Bases for Time Series
  Forecasting'
title_zh: 《GatedLinear：面向时序预测的互补线性基自适应路由框架》
authors:
- Qitai Tan
- Ruiwen Gu
- Yilin Su
- Mo Li
- Xu Lin
- Xiao-Ping Zhang
affiliations:
- Shenzhen Key Laboratory of Ubiquitous Data Enabling
- Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2607.09537'
url: https://arxiv.org/abs/2607.09537
pdf_url: https://arxiv.org/pdf/2607.09537
published: '2026-07-10'
collected: '2026-07-13'
category: Other
direction: 时序预测 · 轻量模型自适应路由
tags:
- Time Series Forecasting
- Gating Mechanism
- Adaptive Routing
- Lightweight Model
- Linear Basis
one_liner: 提出轻量时序预测框架，通过三因子门控路由三种互补线性基，精度达SOTA且参数量显著降低
practical_value: '- 电商销量、流量、库存等时序预测场景可直接复用三种互补线性基（趋势季节性、非平稳漂移、周期复用）的设计，替代单一大模型backbone降本提效

  - 三因子分解门控（通道偏好、预测horizon偏移、时间相位偏移）的路由思路可迁移到多通路召回/排序的多信号融合场景，实现细粒度软路由

  - 低延时要求的时序特征建模场景可借鉴该轻量设计思路，无需堆叠大模型也能达到接近SOTA的精度，适配端侧或高吞吐推理需求'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有深度学习时序预测模型普遍采用单一计算骨干，受固定归纳偏置（如self-attention、谱滤波）限制，难以适配真实时序数据的强异质性：不同变量、预测周期需要完全不同的预测逻辑，大模型堆叠也带来高成本、可解释性差的问题。
### 方法关键点
1. 构建三种互补专用线性基：全局趋势-季节性基适配平滑投影、差分增量基适配非平稳漂移、相位对齐循环基适配显式周期复用
2. 设计三因子融合门，将路由决策拆分为通道专属偏好、horizon感知偏移、基于未来时间标识的相位索引偏差三个独立维度，实现逐点细粒度软路由，无需堆叠重神经网络模块
### 关键结果
在标准时序基准数据集上精度达到SOTA或与复杂大模型相当，同时具备显式可解释的路由模式，参数量相比同类复杂基模型大幅缩减。
