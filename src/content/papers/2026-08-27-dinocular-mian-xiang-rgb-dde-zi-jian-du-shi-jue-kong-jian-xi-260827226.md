---
title: 'DINOcular: Self-Supervised Visuospatial Representations'
title_zh: DINOcular：面向RGB-D的自监督视觉空间表征学习框架
authors:
- Farkhat Almukhamedov
- Sami Azirar
- Hermann Blum
affiliations:
- University of Bonn
- Robot Perception and Learning Lab
arxiv_id: '2608.27226'
url: https://arxiv.org/abs/2608.27226
pdf_url: https://arxiv.org/pdf/2608.27226
published: '2026-08-27'
collected: '2026-08-28'
category: Multimodal
direction: 多模态表征 · RGB-D自监督学习
tags:
- Self-Supervised Learning
- RGB-D
- Visuospatial Representation
- 3D Perception
- Vision Foundation Model
one_liner: 融合深度几何先验与视觉特征的自监督框架，学习兼顾语义与3D空间信息的RGB-D联合表征
practical_value: '- AR/VR电商商品3D展示、虚实融合导购场景可借鉴inter/intra patch融合策略，将深度信息融入现有视觉表征模型，提升3D商品识别、空间摆放推荐精度

  - 实体机器人导购、线下门店智能推荐Agent可复用该框架融合深度传感器与RGB数据，增强空间感知能力，降低环境理解错误率

  - 业务涉及RGB-D语义分割需求时可直接尝试该轻量表征方案，在不显著增加模型规模的前提下保证效果竞争力'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视觉基础模型几乎仅基于RGB数据训练，存在3D空间感知能力短板，而机器人、AR/VR等实体系统普遍自带深度传感器，可提供单目RGB无法恢复的几何信息，但深度数据稀缺、异质性高，此前难以高效融入大模型训练流程。
### 方法关键点
DINOcular自监督框架通过patch内、patch间两级融合策略，将深度生成的几何先验融入视觉backbone，无需大量标注即可高效编码视觉外观语义与空间结构双重信息。
### 关键结果
同参数量下在多个3D几何基准任务上超过现有SOTA，同时标准RGB-D语义分割任务效果保持竞争力，3D感知能力显著提升的同时未损失语义迁移能力。
