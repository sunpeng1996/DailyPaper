---
title: 'Towards Real-Time PixOOD: Efficient Anomaly Segmentation for Autonomous Vehicles'
title_zh: 面向实时PixOOD的自动驾驶场景高效异常分割方法
authors:
- Luca de Martino
- Federico Aromolo
- Federico Nesti
- Giorgio Buttazzo
affiliations:
- Scuola Superiore Sant’Anna, Pisa, Italy
arxiv_id: '2607.28483'
url: https://arxiv.org/abs/2607.28483
pdf_url: https://arxiv.org/pdf/2607.28483
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 自动驾驶 · 实时异常分割硬件加速
tags:
- Anomaly Segmentation
- TensorRT
- Embedded Deployment
- Hardware Acceleration
- Autonomous Driving
one_liner: 重写PixOOD的Neyman-Pearson打分阶段，结合TensorRT优化实现18-20倍推理加速
practical_value: '- 核心算法模块数学逻辑重写+硬件感知编译优化的组合降本思路，可直接复用在推荐/广告大模型的低延迟推理优化场景

  - 嵌入式端推理性能的评估、调优方法论，可迁移到端侧推荐、端侧广告模型的端边部署性能优化工作

  - 跨硬件（桌面/嵌入式）的性能基准测试维度设计，可复用在业务模型上线前的多环境兼容性验证流程'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有SOTA像素级OOD检测方案PixOOD精度优异，但计算开销大，无法适配自动驾驶、铁路场景嵌入式硬件的实时推理要求（最低需求25FPS）。
### 方法关键点
1. 对PixOOD原有Neyman-Pearson打分阶段做公式重写，降低原生计算复杂度
2. 全推理链路采用硬件感知的TensorRT编译优化，同时适配桌面端、嵌入式端硬件
### 关键结果
- 桌面端NVIDIA RTX 4060 GPU推理速度达182FPS，较原baseline提升20倍
- 嵌入式端NVIDIA Jetson AGX Orin推理速度达75FPS，较原baseline提升18倍，均远高于25FPS的实时阈值
