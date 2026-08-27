---
title: 'WarpSAC: Towards the Pinnacle of Scalable Off-policy RL by Rethinking Exploration
  and Exploitation'
title_zh: WarpSAC：重思探索利用的高可扩展离线策略强化学习算法
authors:
- Zihao Wu
- Hongyao Tang
- Yi Ma
- Huizhong Song
- Pengyi Li
- Yifu Yuan
- Fei Ni
- Jinyi Liu
- Wei Wei
- Jianrong Wang
affiliations:
- Tianjin University
- Shanxi University
- Imperial College London
arxiv_id: '2608.24479'
url: https://arxiv.org/abs/2608.24479
pdf_url: https://arxiv.org/pdf/2608.24479
published: '2026-08-24'
collected: '2026-08-27'
category: Training
direction: 可扩展离线策略强化学习训练优化
tags:
- Off-policy RL
- Scalable Training
- SAC
- Data Regime Adaptation
- Reinforcement Learning
one_liner: 提出适配不同数据量场景的双版本WarpSAC离线RL算法，全场景性能显著优于SOTA FlashSAC
practical_value: '- 大规模离线RL训练的推荐/Agent场景可借鉴数据域适配思路：数据量有限时开参数归一化+clipped double-Q，数据充足时关归一化用单Q，平衡训练稳定性与拟合效率

  - 复用Age-biased replay weighting/Sample Weight Decay技巧，给旧样本加权重衰减，提升Replay Buffer利用效率，小模型训练场景收益更显著

  - 电商模拟环境下的推荐策略RL优化可直接复用WarpSAC双版本架构，根据算力/数据规模选择对应变种，加速策略收敛'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有离线策略RL的稳定器（参数归一化、clipped double-Q等）均针对数据受限场景设计，大规模并行仿真带来的高吞吐量充足数据场景下，原有稳定器反而限制模型值拟合效果，缺乏适配不同数据域的通用可扩展RL框架。

### 方法关键点
1. 经过8类基准测试验证，传统RL稳定器效果强依赖数据域：参数归一化在小数据域提效但大数据域限制值拟合，clipped double-Q在高吞吐量场景可放宽，年龄偏置重放加权全场景有效
2. 提出WarpSAC系列算法，通用组件采用Sample Weight Decay提升利用效率，分两个场景变种：WarpSAC-L（Norm ON+clipped double-Q）适配CPU级小数据训练，WarpSAC-A（Norm OFF+single-Q）适配GPU级大数据并行训练

### 关键结果数字
相比SOTA FlashSAC，9个CPU环境下归一化得分步长AUC提升4.5%，14个GPU并行环境提升23.1%；UnitreeG1机器人搬运任务成功率从19.8%提升至96.4%，MuJoCo Playground平均归一化wall-time AUC提升19.1%，sim-to-real部署速度快36.4%
