---
title: 'SSMB: Self-Supervised Local Feature Detection under Motion Blur'
title_zh: SSMB：运动模糊场景下的自监督局部特征检测
authors:
- Zhenjun Zhao
- Fabio Bellavia
- Wenting Wang
- Fan Zhu
- Jiajun Wu
- Suryansh Kumar
- Mingqiang Wei
- Haoang Li
- Javier Civera
arxiv_id: '2608.27181'
url: https://arxiv.org/abs/2608.27181
pdf_url: https://arxiv.org/pdf/2608.27181
published: '2026-08-27'
collected: '2026-08-28'
category: Other
direction: 自监督学习 · 运动模糊局部特征检测
tags:
- Self-supervised Learning
- Keypoint Detection
- Motion Blur
- Local Feature
- Computer Vision
one_liner: 提出无去模糊、无手工依赖的自监督运动模糊关键点检测器SSMB，性能全面超现有SOTA
practical_value: '- 两阶段自监督训练范式可迁移至模糊商品图的特征提取任务，先合成数据预训练再真实数据微调，大幅降低标注成本

  - Local Discriminability Enhancement模块可复用在多模态召回的全局特征融合后，增强细粒度特征区分度

  - 跨域一致性+几何对齐+空间覆盖的多组件损失设计，可参考用于多模态特征对齐任务的目标函数优化'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
运动模糊会扭曲图像局部结构，降低特征定位重复性；现有方案要么走先去模糊再检测的流程，算力开销高且易引入恢复伪影，要么回归清晰图像上提取的手工关键点，受手工检测器假设限制，无法适配模糊场景下的真实可重复特征需求。
### 方法关键点
SSMB是无去模糊流程、无需手工检测器/外部伪标签的自监督关键点检测器；引入LDE模块，在全局特征混合后恢复细粒度局部区分度；采用两阶段训练：第一阶段基于合成形状做几何预训练，仅靠渲染几何信息即可得到空间判别性关键点，无需外部检测器；第二阶段基于真实清晰-模糊图像对做多组件自监督的模糊感知训练，约束跨域一致性、几何对齐、空间覆盖三个目标。
### 关键结果
在运动模糊场景下的关键点检测、图像匹配、相对位姿估计、视觉定位任务上均达到SOTA，全面超越有监督、自监督基线。
