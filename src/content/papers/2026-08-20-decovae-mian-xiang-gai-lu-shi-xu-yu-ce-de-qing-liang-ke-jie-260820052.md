---
title: 'DecoVAE: a Lightweight Interpretable Trend-Seasonal VAE Framework for Efficient
  Probabilistic Time Series Forecasting'
title_zh: DecoVAE：面向概率时序预测的轻量可解释趋势-季节性VAE框架
authors:
- Alexander Marusov
- Dmitry Anikin
- Alexey Zaytsev
affiliations:
- Applied AI Institute, Moscow, Russia
arxiv_id: '2608.20052'
url: https://arxiv.org/abs/2608.20052
pdf_url: https://arxiv.org/pdf/2608.20052
published: '2026-08-20'
collected: '2026-08-21'
category: Other
direction: 概率时序预测 · 轻量可解释建模
tags:
- Time Series Forecasting
- VAE
- Trend-Seasonal Decomposition
- Lightweight Model
- Interpretable Model
one_liner: 显式拆分趋势-季节性双支路的轻量VAE，实现精度效率可解释性兼顾的概率时序预测
practical_value: '- 电商销量、流量、库存、大促GMV等时序预测场景可直接复用显式趋势-季节性双支路拆分架构，兼顾精度和业务可解释性要求

  - 趋势支路引入Hodrick-Prescott类光滑正则、季节支路采用频域复高斯VAE的设计，可直接替换现有时序预测模块的特征提取层，降低参数量

  - 对推理速度、模型体积有要求的实时预测/端侧部署场景，可参考其轻量化设计思路，参数量最高压缩93%的同时精度不降反升'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有概率时序预测方法难以同时捕捉趋势、季节性的不同结构特征，普遍存在可解释性差、内存和推理开销高的问题，无法兼顾精度和落地效率。
### 方法关键点
DecoVAE显式拆分双支路建模：趋势支路对隐轨迹施加微分正则，类Hodrick-Prescott滤波器保证结构光滑性；季节支路通过复高斯VAE在频域建模，原生捕获周期模式的振幅与相位，结合领域归纳偏置提升可解释性。
### 关键结果
在7个真实基准上全面优于基线，短时序预测CRPS最高降14.96%、NMAE最高降23.30%；长时序预测CRPS最高降52.68%、NMAE最高降26.51%；相比次优方法参数量最高减93%，推理速度最高提74%
