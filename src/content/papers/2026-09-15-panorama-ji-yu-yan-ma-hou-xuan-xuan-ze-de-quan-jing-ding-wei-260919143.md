---
title: 'PANORAMA: Panoptic Grounded Captioning via Mask Proposal Selection'
title_zh: PANORAMA：基于掩码候选选择的全景定位图像描述模型
authors:
- Sara Pieri
- Evangelos Kazakos
- Shizhe Chen
- Josef Sivic
- Cordelia Schmid
affiliations:
- Inria, École normale supérieure, CNRS, PSL Research University
- Czech Institute of Informatics, Robotics and Cybernetics, Czech Technical University
  in Prague
arxiv_id: '2609.19143'
url: https://arxiv.org/abs/2609.19143
pdf_url: https://arxiv.org/pdf/2609.19143
published: '2026-09-15'
collected: '2026-09-17'
category: Multimodal
direction: 多模态视觉语言 · 像素级文本定位分割
tags:
- VLM
- Panoptic Segmentation
- Image Captioning
- Grounding
- Multimodal Model
one_liner: 提出全景定位描述基准PanoCaps与掩码选择式VLM，像素级定位任务性能最优
practical_value: '- 电商商品图属性/文案生成场景，可复用短语-掩码匹配方法，自动关联描述词与商品部件/背景区域，提升商品文案准确性

  - 多模态搜索的query grounding任务，可借鉴短语条件掩码选择思路，快速定位query对应图像区域，提升多模态召回精度

  - 多模态内容审核场景，可复用gPQ评估指标，联合衡量描述文本与像素区域的匹配度，优化审核模型评估流程'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM生成的图像描述无法可靠关联像素，稠密描述+像素定位的现有方案要么描述覆盖不全，要么分割掩码精度不足，缺乏统一的训练评估基准和高效的文本-像素对齐方案。
### 方法关键点
1. 构建人工标注基准PanoCaps，提供近全像素覆盖的稠密描述和实体级图文对齐，同时提出广义全景质量gPQ指标，联合评估文本内容与掩码的匹配一致性；
2. 将短语定位转化为短语条件的掩码候选选择任务，基于预训练分割器输入上下文短语表征生成候选掩码，联合训练掩码选择与描述生成模块，支持单区域/多实例的短语指代。
### 关键结果
在PanoCaps基准上取得最优整体定位效果，在多个像素级定位任务上性能持平或超过专用模型，生成的实体级分割精度高，且描述文本与掩码一致性强。
