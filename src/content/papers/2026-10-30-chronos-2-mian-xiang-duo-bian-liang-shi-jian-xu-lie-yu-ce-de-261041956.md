---
title: 'Chronos-2: A foundation model for multivariate time series forecasting'
title_zh: Chronos-2：面向多变量时间序列预测的基础模型
authors:
- Abdul Fatir Ansari
- Oleksandr Shchur
- Jaris Küken
- Andreas Auer
- Boran Han
- Pedro Mercado
- Syama Sundar Rangapuram
- Huibin Shen
- Lorenzo Stella
- Xiyuan Zhang
affiliations:
- Amazon Web Services
- University of Freiburg
- Amazon
- Rutgers University
- Max Planck Institute for Biogeochemistry
arxiv_id: '2610.41956'
url: https://arxiv.org/abs/2610.41956
pdf_url: https://arxiv.org/pdf/2610.41956
published: '2026-10-30'
collected: '2026-11-02'
category: Other
direction: 多变量时序预测 · 零样本基础模型
tags:
- Time Series Forecasting
- Foundation Model
- Zero-shot Learning
- Multivariate Time Series
- Probabilistic Forecasting
one_liner: 提出支持多变量时序与异质协变量交互建模的零样本时序预测基础模型，精度与推理效率均显著领先
practical_value: '- 电商销量、流量、库存、大促GMV等多变量时序预测场景可直接试用开源Chronos-2，无需单独训练领域专属模型，大幅降低落地成本

  - 多因素联动预测场景可复用其「从历史上下文直接推理多时序+异质协变量交互关系」的建模思路，替代传统的人工特征工程耦合方案

  - 实时预测场景可参考其高推理效率优化方案，单中端GPU即可实现1秒内输出100条时序预测结果，满足大促等低延迟需求

  - 库存调拨、动态定价等需要风险评估的场景可复用其自带的概率预测能力，输出带不确定性的预测结果辅助决策'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有时间序列基础模型多独立处理单条时序，无法建模多时序及外部驱动因素的交互，不同领域仍需单独训练专属模型，落地成本高。
### 方法关键点
- 支持建模多变量时序与异质协变量的交互关系，可直接从历史上下文推理时序间关联
- 无需任务特定适配即可输出带不确定性的概率预测结果，支持跨领域零样本预测
### 关键结果
- 基准测试平均精度达SOTA，相对最强基线技能分数提升5.2个百分点，胜率提升10个百分点
- 推理效率极高，单中端GPU 1秒内可生成100条时序预测结果，端到端速度较最优任务特定点预测模型快50倍，较概率预测模型快1000倍
- 在传染病预测、宏观经济建模等多科学领域效果匹配或超过领域专属模型
