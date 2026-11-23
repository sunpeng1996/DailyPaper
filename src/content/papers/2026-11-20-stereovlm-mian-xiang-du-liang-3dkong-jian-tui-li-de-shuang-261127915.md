---
title: 'StereoVLM: Binocular Vision-Language Models for Metric 3D Spatial Reasoning'
title_zh: StereoVLM：面向度量3D空间推理的双目视觉语言模型
authors:
- Chi Yan
- Guoyang Zhao
- Wentao Yuan
- Yixiao Ge
- Yanning Zhou
- Dan Xu
affiliations:
- The Hong Kong University of Science and Technology
- XPENG Robotics
arxiv_id: '2611.27915'
url: https://arxiv.org/abs/2611.27915
pdf_url: https://arxiv.org/pdf/2611.27915
published: '2026-11-20'
collected: '2026-11-23'
category: Multimodal
direction: 多模态大模型 · 3D空间推理
tags:
- VLM
- 3D Reasoning
- Stereo Vision
- Multimodal
- Spatial Perception
one_liner: 提出首个几何感知双目VLM StereoVLM与3D推理基准Stereo3D-Bench，解决VLM度量3D推理歧义
practical_value: '- 电商AR试穿/3D商品展示场景可借鉴双目几何约束的3D感知思路，解决单目深度估计的尺度歧义问题，提升虚拟商品与真实场景的适配精度

  - 实体导购Agent、仓储巡检Agent的3D空间感知模块可复用分层几何监督范式，优先用视差监督替代直接深度监督，提升未知环境下的感知泛化性

  - 多模态空间推理任务的评估可参考Stereo3D-Bench的分层评估逻辑，从点级几何到对象级推理分维度验证效果，避免仅靠语义先验的伪性能'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM语义理解能力优异，但无相机标定、无跨视图几何约束的3D推理存在固有度量尺度歧义，无法区分预测来自视觉证据还是语义先验，度量3D空间推理性能受限。
### 方法关键点
1. 提出首个几何感知的双目VLM StereoVLM，采用分层学习范式，从跨视图匹配、视差估计，到标定条件下的度量深度感知、语义空间推理逐步学习
2. 验证视差监督相比直接双目深度监督，在未知环境下的泛化性显著更优
3. 推出三层结构的Stereo3D-Bench基准，覆盖点级几何到对象级空间推理的全维度评估
### 关键结果
StereoVLM-8B在Stereo3D-Bench上深度精度δ₁达95.17%，对象级平均得分66.98；分层几何监督在5个空间基准上平均提升3.54分，RoboCasa操纵成功率提升4.3pct
