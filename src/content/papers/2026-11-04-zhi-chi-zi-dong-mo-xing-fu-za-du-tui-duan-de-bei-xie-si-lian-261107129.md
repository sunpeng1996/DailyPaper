---
title: Bayesian Tensor Train Kernel Machines with Automatic Model Complexity Inference
title_zh: 支持自动模型复杂度推断的贝叶斯张量链核机器
authors:
- Afra Kilic
- Kim Batselier
affiliations:
- Delft University of Technology
- Delft Center for Systems and Control
arxiv_id: '2611.07129'
url: https://arxiv.org/abs/2611.07129
pdf_url: https://arxiv.org/pdf/2611.07129
published: '2026-11-04'
collected: '2026-11-07'
category: Other
direction: 张量网络核机器 · 自动超参推断
tags:
- Tensor Network
- Tensor Train
- Kernel Method
- Variational Inference
- Automatic Model Selection
one_liner: 将贝叶斯张量网络核机器扩展到张量链分解，可自动从数据推断张量秩与特征维度
practical_value: '- 推荐系统中用张量分解建模用户-物品-上下文多维交互时，可借鉴分层ARD先验自动推断张量秩，省去人工调参成本

  - 张量链相邻核心仅局部耦合的更新逻辑，可迁移至高维稀疏特征的大规模排序模型轻量化，不额外增加计算开销

  - 均值场变分推断得到的闭式预测分布，可用于推荐系统不确定性估计，支撑冷启动、探索性推荐场景'
score: 6
source: arxiv-stat.ML
depth: abstract
---

## 动机
张量网络核机器通过低秩分解降低高维场景计算与内存开销，但现有确定性方法需手动调优张量秩、特征维度，已有的贝叶斯版本仅支持CP分解，所有模式共享单一秩，适用场景受限。

## 方法关键点
将贝叶斯张量网络核机器框架扩展到张量链（TT）分解，提出BTT-KM：在TT核心上施加分层ARD型先验，可从数据直接推断TT秩与特征维度；基于均值场变分推理推导贝叶斯交替最小二乘算法，计算复杂度与确定性TT核机器一致，同时支持闭式预测分布输出。

## 关键结果
合成实验验证，BTT-KM可从过参数化初始化中精准恢复真实TT秩与特征维度，无需人工超参调优。
