---
title: 'InstantHand: Feed-Forward 3D Gaussian Splatting for Animatable Hand Avatar
  Reconstruction from a Single Image'
title_zh: 单图生成可动画3D高斯手化身的前馈框架InstantHand
authors:
- Chanho Kim
- Muhammad Salman Ali
- Kyeonghwan Gwak
- Muhammad Shaheryar
- Incheol Park
- Jeongwan On
- Seungryul Baek
affiliations:
- UNIST, South Korea
arxiv_id: '2611.08330'
url: https://arxiv.org/abs/2611.08330
pdf_url: https://arxiv.org/pdf/2611.08330
published: '2026-11-05'
collected: '2026-11-07'
category: Other
direction: 3D数字人 · 单图可动画手化身重建
tags:
- 3D Gaussian Splatting
- Avatar Reconstruction
- Feed-Forward
- Digital Human
- Single Image Reconstruction
one_liner: 仅用单张图像无需测试时优化，2.84s生成可动画3D高斯手avatar，性能媲美逐样本优化基线
practical_value: '- 内容生成边缘优化：做商品/数字人生成时，可借鉴Soft Alpha Band正则，将监督权重集中在轮廓边缘，解决细配件、手指等薄结构生成过粗/模糊问题

  - 多模态内容补全：做图像补全/风格迁移时，可复用Reliability-gated机制，按渲染贡献度保留观测区原始特征，未观测区用先验补全，平衡保真度与完整性

  - 实时交互场景架构：做AR/VR电商试戴、数字人交互业务时，可参考无测试时优化的前馈管线，实现秒级生成、百帧以上渲染的实时体验'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有手化身重建依赖多视图采集或逐主体优化，扩展性差；图像平均损失对alpha泄露监督不足，导致手指轮廓过粗；回归颜色易向预训练先验漂移，观测区域保真度低

### 方法关键点
1. 端到端前馈框架，复用成熟MANO、相机、掩码预训练模型输出，无需测试时优化
2. 提出Soft Alpha Band正则，将监督集中在轮廓边界，解决薄手指轮廓过粗问题
3. 设计可靠性门控外观迁移模块，按每个高斯的渲染贡献度迁移源图像颜色保观测区保真，未观测区用全局身份条件的先验补全

### 关键结果
单图生成手avatar仅需2.84s，渲染帧率达161FPS，在InterHand2.6M数据集上性能匹配逐主体优化基线，HanCo零样本评估表现具备竞争力
