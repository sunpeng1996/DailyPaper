---
title: 'Human-JEPA: A Human-Centric Vision Model that Perceives and Anticipates'
title_zh: Human-JEPA：支持感知与预测的以人为中心的视觉模型
authors:
- Hui Wei
- Licai Sun
- Guoying Zhao
affiliations:
- ELLIS Institute Finland
- Center for Machine Vision and Signal Analysis, University of Oulu
arxiv_id: '2608.21160'
url: https://arxiv.org/abs/2608.21160
pdf_url: https://arxiv.org/pdf/2608.21160
published: '2026-08-21'
collected: '2026-08-24'
category: Other
direction: 以人为中心的视觉预训练 · 多任务统一
tags:
- Human-Centric Vision
- Pre-training
- Video Understanding
- JEPA
- Action Anticipation
one_liner: 提出基于锚定预测训练的Human-JEPA，兼顾人体静态感知与未来动作预测能力
practical_value: '- 直播电商场景可复用该模型做用户动作预判，优化实时商品弹窗推送时机

  - 短视频电商的人体姿态/重识别任务可直接用该轻量预训练模型微调，降低推理成本

  - 线下无人零售场景可结合该模型预判用户取货动作，优化结算链路与商品推荐优先级'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有以人为中心的视觉模型均基于静态图像预训练，仅支持静态密集感知，无法覆盖动作时序建模与未来预测需求，两类任务此前需要独立模型适配，部署与训练成本高。
### 方法关键点
提出基于锚定预测的视频预训练范式Human-JEPA：1）将密集预测目标锚定到初始化的冻结副本，避免密集感知能力塌缩；2）用纯过去-未来时序分割替代块掩码，消除5点动作税与17点重识别塌缩问题；支持单一模型适配静态感知与未来预测双任务。
### 关键结果
参数量比像素锚定专用模型少2.7倍，在人体姿态估计、行人重识别任务上性能领先，是首个预测头不降低预判性能的模型，仅在高分辨率密集解析任务上性能稍逊。
