---
title: 'ScaleVid: Geometry-Aware Video Object Scaling with Mesh-Free Inference'
title_zh: ScaleVid：基于无网格推理的几何感知视频对象缩放方法
authors:
- Youze Huang
- Penghui Ruan
- Bojia Zi
- Xianbiao Qi
- Shihao Zhao
- Rong Xiao
affiliations:
- University of Electronic Science and Technology of China
- The Hong Kong Polytechnic University
- The Chinese University of Hong Kong
- Intellif Inc.
- The University of Hong Kong
arxiv_id: '2608.12232'
url: https://arxiv.org/abs/2608.12232
pdf_url: https://arxiv.org/pdf/2608.12232
published: '2026-08-12'
collected: '2026-08-13'
category: Other
direction: 视频可控生成 · 几何感知对象编辑
tags:
- Video Editing
- Diffusion Model
- Geometry-Aware Generation
- Mesh-Free Inference
- Controllable Generation
one_liner: 提出两阶段无网格几何感知视频对象缩放框架，无需显式3D重建即可实现高保真时序一致的缩放效果
practical_value: '- 电商商品短视频批量生产可复用该无网格推理方案，跳过高成本3D重建流程，大幅降低商品缩放/形变类特效的计算开销

  - 基于真实数据构造几何扰动伪标签的训练思路可迁移到其他可控生成任务，无需成对标注即可实现精准几何变换效果

  - 前景背景解耦编辑的框架可直接应用于电商短视频的商品尺寸调整/场景植入场景，保障背景一致性与时序连贯性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有几何感知视频对象缩放方案存在显著缺陷：文本引导方法仅在2D平面操作缺乏几何合理性，深度引导方法控制精度低，网格类方法依赖高成本3D重建，且普遍缺少成对真实缩放标注支撑训练。
### 方法关键点
提出渐进式两阶段训练框架，推理阶段无需网格像素对齐与显式3D重建；两阶段均基于真实视频构造几何扰动的伪源数据，以原始完整视频为重建目标，无需成对真实缩放标注；第一阶段用平面变换学习鲁棒前后景合成能力，第二阶段引入以对象为中心的3D形变引导，实现几何感知的精准缩放。
### 关键结果
在自建的配对几何基准、真实背景基准及野生视频上测试，几何一致性、前景保真度、背景保留效果均显著优于现有基线，推理速度远高于需显式3D重建的方案，落地性更强。
