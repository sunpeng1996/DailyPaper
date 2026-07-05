---
title: Learning Spectral and Polarimetric Clues for One-to-Multimodal Novel View Synthesis
title_zh: 融合光谱与偏振特征的单模态到多模态新视角合成方法
authors:
- Federico Lincetto
- Gianluca Agresti
- Mattia Rossi
- Piergiorgio Sartor
- Pietro Zanuttigh
affiliations:
- University of Padova
- Sony Semiconductor Solutions Europe
arxiv_id: '2607.02372'
url: https://arxiv.org/abs/2607.02372
pdf_url: https://arxiv.org/pdf/2607.02372
published: '2026-07-02'
collected: '2026-07-05'
category: Multimodal
direction: 多模态神经渲染 · 跨模态内容生成
tags:
- Neural Rendering
- Multimodal Learning
- Cross-Modality Mapping
- Novel View Synthesis
one_liner: 提出SPoILeR框架，仅用RGB或少量多模态样本即可生成多视角一致的特殊模态渲染结果
practical_value: '- 电商商品3D/AR展示场景可复用该跨模态预训练范式，仅用常规RGB拍摄即可低成本生成多光谱/红外等特殊模态的商品展示内容，省去专业多模态采集成本

  - 「跨模态关联预训练+单模态监督微调」的范式可迁移至多模态商品内容生成任务，无需逐场景采集昂贵的多模态标注数据

  - 多视角一致性生成逻辑可复用在商品AR/VR展示场景的多模态内容渲染环节，保证不同视角下特殊模态显示效果统一'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态神经渲染方案需逐场景通过昂贵专业传感器采集校准后的多模态数据，落地门槛高，无法仅依托易得的RGB数据生成红外、偏振、多光谱等特殊模态的新视角内容。

### 方法关键点
1. 提出Spectral and Polarimetric Implicit Learned Representation（SPoILeR）隐式表征框架，先通过多模态预训练阶段学习RGB与各类特殊成像模态之间的关联映射规律
2. 微调阶段仅需RGB单模态监督，即可为仅提供RGB数据或极少量特殊模态样本的场景，生成多视角一致的多模态新视角渲染结果

### 关键结果
可在无任何红外、偏振、多光谱传感器输入样本的场景下，高精度生成对应模态的渲染内容
