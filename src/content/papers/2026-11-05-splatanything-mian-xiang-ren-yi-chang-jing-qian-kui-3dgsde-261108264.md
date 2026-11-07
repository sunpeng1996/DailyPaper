---
title: 'SplatAnything: Gaussian Spacing Normalization for Feed-forward 3DGS across
  Arbitrary Scenes'
title_zh: SplatAnything：面向任意场景前馈3DGS的高斯间距归一化方法
authors:
- Hao Yu
- Zhenwei Wang
- Yongzhen Hu
- Yuning Gong
- Junta Wu
- Xiaowei Zhou
- Hujun Bao
- Tengfei Wang
- Chunchao Guo
- Sida Peng
affiliations:
- Zhejiang University
- Tencent Hunyuan
- Causa Robotics
arxiv_id: '2611.08264'
url: https://arxiv.org/abs/2611.08264
pdf_url: https://arxiv.org/pdf/2611.08264
published: '2026-11-05'
collected: '2026-11-07'
category: Other
direction: 3D高斯重建 · 跨场景泛化
tags:
- 3DGS
- Normalization
- Cross-Scene Generalization
- 3D Reconstruction
- Novel View Synthesis
one_liner: 提出高斯间距归一化解决前馈3DGS跨场景尺度视角泛化差问题，性能达SOTA
practical_value: '- 电商3D商品建模场景可复用GSNorm归一化思路，解决不同尺寸商品（小配饰/大家电）3D重建时的尺度不一致问题，提升跨品类建模精度

  - 多视图商品3D重建管线可参考其前馈3DGS架构，替代传统逐场景优化方案，将单商品重建耗时从分钟级压缩到秒级

  - 跨尺度特征建模任务可借鉴其场景级鲁棒统计量归一化思路，替代全局径向归一化，减少分布偏移带来的监督歧义'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有前馈3DGS方法采用径向距离归一化，仅规范全局径向统计量，相邻高斯中心间距仍会随场景尺度、相机配置大幅波动，导致高斯尺度目标系统偏移，监督信号存在歧义，跨场景泛化性能差。
### 方法关键点
1. 核心引入高斯间距归一化（GSNorm），通过规范场景级高斯间距的鲁棒统计量，为高斯预测提供一致空间参考，消除尺度偏移带来的监督歧义
2. 构建覆盖多数据集、多输入稀疏度、外推视角的系统评测基准，覆盖实际落地的多种复杂场景
### 关键结果
所有评测设置下达到SOTA，在场景尺度、视角存在大幅变化的极端场景下性能提升尤为显著，仅需数秒即可完成任意场景的前馈3DGS重建
