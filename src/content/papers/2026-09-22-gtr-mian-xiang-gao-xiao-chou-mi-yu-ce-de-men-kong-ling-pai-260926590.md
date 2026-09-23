---
title: 'GTR: Gated Token Recurrence for Efficient Dense Prediction'
title_zh: GTR：面向高效稠密预测的门控令牌循环架构
authors:
- Zhe Feng
- Longfei Liu
- Wei Liu
- Kai Chen
- Jiangjiang Kong
- Wei Zhou
- Yifeng Qian
- Dexiong Chen
- Xuanlong Yu
- Xi Shen
affiliations:
- Didi International Business Group
- Intellindust AI Lab
- Institute of Automation, Chinese Academy of Sciences
- The Hong Kong University of Science and Technology (Guangzhou)
- Didi Research
arxiv_id: '2609.26590'
url: https://arxiv.org/abs/2609.26590
pdf_url: https://arxiv.org/pdf/2609.26590
published: '2026-09-22'
collected: '2026-09-23'
category: Other
direction: 高效视觉骨干 · 稠密预测推理优化
tags:
- Vision Backbone
- Dense Prediction
- Efficient Inference
- Knowledge Distillation
- CUDA Optimization
one_liner: 无softmax门控令牌循环视觉骨干，大幅降低高分辨率稠密预测推理延迟
practical_value: '- 电商多模态理解（商品检测、拍照搜货）场景可复用门控线性注意力+交替空间扫描设计，替换softmax自注意力降低高分辨率图像推理开销，适配边缘端部署

  - 视觉小骨干蒸馏可参考仅对齐最后层patch token的轻量方案，无需中间层监督即可完成大模型向小骨干的能力迁移，降低蒸馏成本

  - 高吞吐token处理场景可复用chunkwise CUDA算子优化思路，相比通用算子可获得数倍性能提升，适配大流量多模态召回底层加速'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
基于自注意力的视觉骨干在稠密预测任务上表现优异，但全局softmax注意力的二次计算开销随图像分辨率升高快速增长，限制了高分辨率场景和端侧部署的可行性。
### 方法关键点
无softmax的门控令牌循环（GTR）视觉骨干融合门控线性注意力、交替空间扫描方向、空间增强SwiGLU模块；蒸馏策略仅通过线性投影和平方$ℓ_2$损失对齐检测专用DINOv3教师模型的最后层patch token，无需掩码令牌预测或中间层监督。
### 关键结果
经Objects365预训练的GTR-L在COCO val2017上达到58.9 box AP，RTX 4090上单样本FP16推理中位延迟仅1.908ms；定制的chunkwise CUDA算子在1.6K token场景下比FLA v0.5.0快4倍；DRIVE AGX Thor上TensorRT部署单样本延迟2.282-8.769ms，可直接迁移至实例分割、语义分割等多类稠密预测任务。
