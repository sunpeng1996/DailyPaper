---
title: 'TimeLineXR: An Interactive Exploration of Time in Vision-Language Models'
title_zh: TimeLineXR：视觉语言模型中时间维度的交互式探索
authors:
- Nidham Tekaya
- Markus Passecker
- Matthias Zeppelzauer
affiliations:
- Univ. of Applied Sciences St. Pölten
- TU Wien
arxiv_id: '2610.37349'
url: https://arxiv.org/abs/2610.37349
pdf_url: https://arxiv.org/pdf/2610.37349
published: '2026-10-27'
collected: '2026-10-29'
category: Multimodal
direction: 多模态VLM · 时间推理交互系统
tags:
- VLM
- CLIP
- WebXR
- Temporal Reasoning
- Interactive System
one_liner: 基于VLM内在时间编码能力，搭建Web/WebXR双端工具实现图像首次出现年份的可视化查询
practical_value: '- 可复用CLIP+cosine核KPCA的时间特征映射pipeline，用于二手/复古电商场景的商品年代自动识别，提升年代定向推荐的准确率

  - 预缓存时间索引的架构设计可直接复用，降低多模态时间推理的响应延迟，适配高并发检索业务需求

  - 3D交互式时间轴的展示思路可迁移到电商商品演进导购、用户消费时间线可视化等C端交互场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有研究已证明VLM具备内在时间理解能力，可估计物体的时间起源，但其嵌入空间内的非线性时间流形无法被普通用户直接查询、可视化，缺乏可解释的交互入口。
### 方法关键点
1. 搭建双端交互系统：Web端支持上传/选择图像，将其映射到色标编码的3D时间轴；WebXR端支持房间级3D时间轴交互，可拖拽缩放、投掷图像卡片完成查询
2. 统一推理pipeline：用CLIP编码查询图像，经cosine核KPCA投影后映射到贝塞尔时间轴，全程复用预缓存的时间索引降低延迟
### 关键结果
系统可自动输出图像对应物体的首次出现年份，支持多图像时间位置对比，全部代码已开源，可直接复现整套流程。
