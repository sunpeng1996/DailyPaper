---
title: 'ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any
  Device'
title_zh: ZipDepth：可跨任意设备部署的轻量化零样本单目深度估计模型
authors:
- Fabio Tosi
- Luca Bartolomei
- Matteo Poggi
- Stefano Mattoccia
affiliations:
- University of Bologna
arxiv_id: '2607.08771'
url: https://arxiv.org/abs/2607.08771
pdf_url: https://arxiv.org/pdf/2607.08771
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: 端侧轻量化 · 知识蒸馏 · 零样本视觉感知
tags:
- Monocular Depth Estimation
- Knowledge Distillation
- Edge Deployment
- Zero-Shot
- Lightweight Model
one_liner: 基于大模型知识蒸馏的6.1M参数单目深度网络，兼顾零样本精度与端侧推理效率
practical_value: '- 电商AR试穿/3D商品建模场景可复用大模型蒸馏+重参数化编解码的轻量化方案，在低功耗端侧设备上实现实时3D深度感知

  - 多域训练的知识蒸馏思路可迁移至端侧推荐/广告小模型优化，解决单域训练的跨场景泛化差问题

  - 端侧模型落地可参考其精度-能耗-FPS三维权衡的评估框架，更贴合实际业务部署约束'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有大模型零样本单目深度估计泛化性好，但计算量过高无法适配嵌入式/移动等功耗受限的端侧设备；已有的轻量化方案多为单域自监督训练，跨域泛化能力差，易在场景切换时失效。

### 方法关键点
采用可重参数化的高效编解码结构，基于多域大规模训练集，从大深度估计 foundation model 做知识蒸馏，压缩得到极小参数量的端侧模型。

### 关键结果数字
最终模型参数量仅6.1M，在5个基准数据集上取得轻量化模型中最优的零样本精度与部署效率权衡；15W Jetson Orin NX上FP32推理达34FPS、FP16 TensorRT推理达77FPS，单帧能耗低于400mJ，精度接近参数量50倍的大模型水平。
