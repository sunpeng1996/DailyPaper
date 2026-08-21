---
title: 'TinyCast: Probabilistic Zero-Shot Forecasting with Computed Periodicity'
title_zh: TinyCast：基于计算周期的概率式零样本时序预测模型
authors:
- Armin Steinhauser
affiliations:
- RA WS Labs
arxiv_id: '2608.15767'
url: https://arxiv.org/abs/2608.15767
pdf_url: https://arxiv.org/pdf/2608.15767
published: '2026-08-15'
collected: '2026-08-21'
category: Other
direction: 轻量零样本时序概率预测
tags:
- Time Series Forecasting
- Zero-Shot
- Lightweight Model
- Probabilistic Prediction
- Edge Deployment
one_liner: 仅146k参数的无注意力轻量架构，实现零样本概率时序预测最优尺寸-精度 tradeoff
practical_value: '- 电商流量、销量、库存等时序预测场景可复用「先计算周期再建模残差」的框架，大幅降低模型参数量

  - 端侧个性化推荐/时序预测需求可参考其全卷积+矩阵乘的结构，支持INT8量化部署，无需端侧重训

  - 不确定性感知的推荐决策（如库存备货、营销预算分配）可复用其分位数解码器输出概率分布的设计，替代单点预测提升决策鲁棒性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有零样本时序预测模型参数量大，难落地边缘端场景，且小参数模型仅能输出单点预测，无法提供不确定性估计，无法满足风控、决策类场景需求。

### 方法关键点
1. 放弃用注意力/大模型学习周期规律，改用零参数频谱检测器直接计算时序主导周期，将上下文按相位折叠
2. 用膨胀卷积编码器+块自回归分位数解码器建模周期外的残差特征，全结构仅用卷积和矩阵乘，无注意力模块

### 关键结果数字
仅146.5k参数，是GIFT-Eval榜单最小的零样本概率预测模型；在无测试数据泄露的模型中，是唯一1.4M参数以下可输出预测分布的模型，效果更优的模型参数量至少是其28倍；支持静态INT8导出，可直接在嵌入式设备端到端运行，无需单信号适配。
