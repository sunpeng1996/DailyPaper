---
title: To Retain or to Adapt? Generalizing Continual Learning
title_zh: 保留还是适配？面向泛化的持续学习通用框架
authors:
- Giulia Lanzillotta
- Mandana Samiei
- Doina Precup
- Razvan Pascanu
- Claire Vernade
affiliations:
- ETH Zürich
- Mila - Quebec AI Institute
- McGill University
- University of Technology Nuremberg
arxiv_id: '2607.05609'
url: https://arxiv.org/abs/2607.05609
pdf_url: https://arxiv.org/pdf/2607.05609
published: '2026-07-06'
collected: '2026-07-09'
category: Training
direction: 持续学习 · 记忆与自适应平衡优化
tags:
- Continual Learning
- Catastrophic Forgetting
- Online Optimization
- Transfer Efficiency
- Predictive Learning
one_liner: 打破持续学习优先保留历史知识的假设，提出可自适应平衡记忆与适配的通用持续学习范式
practical_value: '- 推荐系统应对用户兴趣/商品分布漂移时，可参考Critical Task Duration阈值判断是否遗忘过时历史特征/样本，无需盲目保留全量知识降低适配延迟

  - 电商大促/季节营销场景的模型迭代，可引入Transfer Efficiency指标量化历史经验的正负迁移收益，平衡热启动速度与新场景适配精度

  - 可复用文中Window算法思路，动态调整训练样本窗口大小，在多轮活动序列的推荐模型持续训练中同时优于全量联合训练与单任务独立训练效果'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有持续学习(CL)默认以缓解灾难性遗忘、对齐联合任务学习(JTL)效果为目标，默认需保留全部历史知识，但在非稳态环境下过度保留会阻碍实时适配能力，现有指标未覆盖全生命周期平均误差。

### 方法关键点
1. 以平均终身误差(ALE)为核心目标，将CL形式化为环境与学习动态交互的在线优化问题；
2. 提出Transfer Efficiency指标，量化历史经验带来的偏差（不稳定性）与从零学习新任务的优化成本（瞬态误差）的trade-off；
3. 推导得到Critical Task Duration闭值，超过阈值后保留历史知识会从热启动优势变为优化负担；
4. 提出Predictive Continual Learning范式，基于动态更新的未来任务预测模型优化长期性能，给出可在JTL和独立任务学习(ITL)间插值的Window算法作为验证。

### 关键结果
在图像分类、强化学习基准上验证了理论推导的正确性，提出的Window算法在可控分布漂移场景下效果同时优于JTL和ITL
