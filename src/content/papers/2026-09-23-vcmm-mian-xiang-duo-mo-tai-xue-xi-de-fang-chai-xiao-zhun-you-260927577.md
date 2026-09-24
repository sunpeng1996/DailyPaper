---
title: 'VCMM: Variance-Calibrated Momentum for Multimodal Learning'
title_zh: VCMM：面向多模态学习的方差校准动量优化方法
authors:
- Zhongjing Gu
- Chenyang Huang
- Yufa Feng
- Chong He
- Qinxu Ding
- Yiming Cui
arxiv_id: '2609.27577'
url: https://arxiv.org/abs/2609.27577
pdf_url: https://arxiv.org/pdf/2609.27577
published: '2026-09-23'
collected: '2026-09-24'
category: Multimodal
direction: 多模态训练 · 模态不平衡优化
tags:
- Multimodal Learning
- Modality Imbalance
- Momentum Optimizer
- Training Optimization
- Gradient Dynamics
one_liner: 方差校准动量VCMM通过模态自适应梯度记忆缓解多模态训练的模态不平衡问题
practical_value: '- 做多模态召回/多模态推荐模型训练时，可直接复用VCMM替换原有AdamW等动量优化器的动量计算模块，低开销缓解图文/音视频模态不平衡问题，无需修改模型结构

  - 对于电商场景多任务训练的任务不平衡问题，可借鉴VCMM的卡尔曼控制器思路，为不同任务定制自适应动量系数，无需额外学习率调优

  - 可迁移VCMM在线估计小批量噪声+时序漂移的方法，动态调整LLM+推荐场景下不同特征域的梯度更新权重，降低特征域不平衡带来的效果衰减'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
多模态联合训练普遍存在模态不平衡问题，主导模态会压制其他模态的优化过程，最终限制多模态融合效果；现有平衡方法仅聚焦当前步梯度调制，未覆盖动量优化器中积累的历史梯度信息，无法从长期维度解决模态不平衡问题。

### 方法关键点
1. Variance-Calibrated MomentuM (VCMM)为不同模态的梯度动态特性定制自适应梯度记忆权重
2. 在线估计小批量梯度噪声与时序漂移，通过类卡尔曼控制器计算模态专属动量系数
3. 跨模态归一化控制信号，对时变一阶矩做精确偏差校正，无需额外前向传播或显式学习率缩放

### 关键结果
在4个多模态基准数据集上取得稳定效果提升，仅引入极低训练开销。
