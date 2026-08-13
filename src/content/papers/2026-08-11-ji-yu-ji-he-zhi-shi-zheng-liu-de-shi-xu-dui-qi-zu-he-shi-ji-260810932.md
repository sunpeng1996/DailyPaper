---
title: Temporally Grounded Compositional Camera Motion Understanding via Geometric
  Knowledge Distillation
title_zh: 基于几何知识蒸馏的时序对齐组合式相机运动理解
authors:
- Dazhao Du
- Shiyan Du
- Jian Liu
- Yongjian Yu
- Bohai Gu
- Tao Han
- Hualuo Liu
- Eric Liu
- Yujia Zhang
- Xi Chen
affiliations:
- The Hong Kong University of Science and Technology
- Tencent
arxiv_id: '2608.10932'
url: https://arxiv.org/abs/2608.10932
pdf_url: https://arxiv.org/pdf/2608.10932
published: '2026-08-11'
collected: '2026-08-12'
category: Multimodal
direction: 多模态大模型 · 视频几何感知知识蒸馏
tags:
- MLLM
- Knowledge Distillation
- Video Perception
- Camera Motion
- Geometric Perception
one_liner: 提出时序组合相机运动识别框架CamDistill及标注基准CamChoreo，性能追平3D特征注入方案且推理更轻量
practical_value: '- 电商短视频内容理解场景可借鉴该知识蒸馏思路，将笨重的3D几何模型知识蒸馏为轻量token，大幅降低推理阶段算力开销

  - 时序分段标注思路可复用在电商短视频看点识别、商品动态片段定位等场景，提升细粒度内容理解精度

  - 复合标签建模方法可迁移到多属性视频内容分类任务，解决同一时段多个语义/属性共存的识别问题'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有MLLM做相机运动识别仅支持整片段粗粒度标注，忽略单镜头内运动动态变化、多运动同时发生的真实场景特性；且MLLM视觉编码器侧重语义而非几何特征，直接注入3D模型特征的方案推理成本过高。

### 方法关键点
1. 定义时序对齐的组合式相机运动识别任务，要求定位运动一致区间并识别区间内所有并发运动
2. 开源CamChoreo基准，包含4229个真实单镜头片段，人工标注20类方向感知标签，近半片段含复合运动
3. 提出CamDistill蒸馏方案，训练阶段将冻结3D基础模型的几何知识蒸馏到轻量相机token，推理阶段无需加载3D教师模型。

### 关键结果
CamDistill精度与直接注入3D特征的基线方案持平，推理成本大幅降低，推动相机运动理解从片段级标注升级为时域对齐的组合式识别。
