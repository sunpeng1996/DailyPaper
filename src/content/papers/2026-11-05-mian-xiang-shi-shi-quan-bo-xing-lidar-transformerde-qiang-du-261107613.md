---
title: Towards Real-Time Full-Waveform LiDAR Transformers via Intensity-Guided Token
  Reduction and Physics-Aware Augmentation
title_zh: 面向实时全波形LiDAR Transformer的强度引导Token缩减与物理感知增强
authors:
- Kotaro Oishi
- Kazuma Ikeda
- Ryosei Hara
- Ryo Yoshida
- Mariko Isogawa
- Kentaro Yoshioka
affiliations:
- Keio University
arxiv_id: '2611.07613'
url: https://arxiv.org/abs/2611.07613
pdf_url: https://arxiv.org/pdf/2611.07613
published: '2026-11-05'
collected: '2026-11-07'
category: Other
direction: LiDAR感知 · Transformer效率优化
tags:
- Transformer
- Token Reduction
- Data Augmentation
- Real-time Inference
- LiDAR
one_liner: 提出强度引导Token剪枝与物理感知增强方案，实现首个高精度实时全波形LiDAR Transformer
practical_value: '- 基于特征重要性的token剪枝思路可迁移至长序列推荐Transformer提速，例如按用户交互权重裁剪低价值历史行为token，兼顾精度与推理速度。

  - 保留核心业务约束的数据增强思路可复用，推荐场景做增强时需不破坏用户行为时序逻辑、商品属性关联规则，避免引入噪声。'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
全波形LiDAR可解决常规激光雷达在恶劣天气、透明物体、低反射面等场景的感知缺陷，但现有Transformer类方案存在两大瓶颈：低强度背景区域的冗余token带来极高计算开销，标注数据稀缺导致模型泛化能力不足。
### 方法关键点
1. 提出FWL-ToPM token剪枝合并机制，基于强度分布选择性缩减token，仅保留关键波形内容；
2. 提出FWLAug物理感知数据增强框架，保留每条射线的飞行时间波形与视锥几何结构，提升未知场景泛化性。
### 关键结果
在Ghost-FWL基准上，FWL-ToPM实现超8倍推理提速，相比现有SOTA F1值提升近9个点，是首个同时提升精度的实时全波形LiDAR Transformer；FWLAug可进一步提升基准集与OOD测试集的性能。
