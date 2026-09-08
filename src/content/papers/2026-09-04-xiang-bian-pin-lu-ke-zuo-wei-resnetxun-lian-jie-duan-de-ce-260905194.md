---
title: Phase Transition Frequency as a Training Time Predictor of Test Accuracy in
  ResNets
title_zh: 相变频率可作为ResNet训练阶段的测试精度预测指标
authors:
- Arunan J
affiliations:
- Independent Researcher, Chennai, Tamil Nadu, India
arxiv_id: '2609.05194'
url: https://arxiv.org/abs/2609.05194
pdf_url: https://arxiv.org/pdf/2609.05194
published: '2026-09-04'
collected: '2026-09-08'
category: Training
direction: 深度学习训练 · 模型泛化能力预测
tags:
- ResNet
- Training Dynamics
- Generalization
- Phase Transition
- Training Probe
one_liner: 用ResNet微调阶段类可分性跳变次数预测最终测试精度，IID场景下相关性优于同类训练曲线信号
practical_value: '- 训练召回/排序DNN、用户分类标签模型时，可将相变频率作为轻量探针，提前终止低精度训练任务，节省算力

  - 同域IID场景下该指标泛化预测效果优于普通训练曲线信号，可加入模型训练监控看板

  - 分布偏移场景（跨域推荐、冷启动）下指标效果衰减明显，不建议单独作为泛化判断依据'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基于训练曲线的模型泛化能力预测指标精度不足，需全量跑完训练才能拿到最终效果，算力浪费严重，亟需低成本的训练阶段预测手段

### 方法关键点
1. 统计ResNet微调过程中离散类可分性跳变的次数（相变频率），作为最终测试精度的预测因子
2. 覆盖4个基准数据集、3种ResNet架构共75组实验验证，与6种现有训练曲线信号做横向对比

### 关键结果数字
- IID分类场景下与最终测试精度负相关达r=-0.84（CIFAR-10）、r=-0.87（CIFAR-100），性能优于全部6种对比信号
- 分布偏移场景下相关性大幅衰减：TinyImageNet下r=-0.45，CIFAR-10-C污染数据集下r=-0.19
- 控制模型深度变量后，CIFAR-100下偏相关仍达-0.69，统计显著性p=0.007，预测能力不受架构深度干扰
