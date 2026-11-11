---
title: Guiding Data Allocation for Robust Subpopulation Generalization
title_zh: 面向子群体鲁棒泛化的训练数据分配优化方法
authors:
- Zhaoying Pan
- Yipei Wang
- Shenyu Lu
- Xiaoqian Wang
affiliations:
- Elmore Family School of Electrical and Computer Engineering, Purdue University
arxiv_id: '2611.12884'
url: https://arxiv.org/abs/2611.12884
pdf_url: https://arxiv.org/pdf/2611.12884
published: '2026-11-09'
collected: '2026-11-11'
category: Training
direction: 训练鲁棒性 · 子群体分布偏移优化
tags:
- Subpopulation Shift
- Data Allocation
- Training Robustness
- Generalization
- Worst-group Performance
one_liner: 理论验证非平衡训练数据可实现子群体鲁棒泛化，给出梯度驱动的子组数据配比优化方案
practical_value: '- 电商推荐长尾用户/冷门品类子群优化无需强制平衡数据，可通过梯度导向调整训练集子群配比，降低数据采集、重采样的人力与算力成本

  - 模型训练时可复用本文梯度调整策略，在保证大盘推荐效果的前提下，针对性提升低活用户、小众品类等最差子群的推荐准确率

  - 应对大促、新品期等流量/商品结构突变的子群偏移场景时，可灵活调整训练集子群占比，无需全量重构平衡训练集，大幅缩短模型迭代周期'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
机器学习模型易受训练-测试子群体分布偏移影响，出现整体训练精度高但长尾子群泛化表现差的问题，传统强制子群数据平衡方案成本高、落地可行性差，且并非实现鲁棒泛化的必要条件。
### 方法关键点
1. 扩展高斯特征模型框架，从理论层面刻画任意训练子群分布对应的模型性能空间，证明包括显著非平衡配置在内的多种数据配比，均可达到与完全平衡配置相当的鲁棒泛化效果
2. 推导基于梯度的子群数据配比调整方向，可更高效优化校准精度与最差子群精度
### 关键结果
实验验证策略化数据分配相比简单强制平衡方案，可在大幅降低数据处理成本的前提下实现同等甚至更优的子群体鲁棒泛化效果，最差子群精度优化效率显著提升
