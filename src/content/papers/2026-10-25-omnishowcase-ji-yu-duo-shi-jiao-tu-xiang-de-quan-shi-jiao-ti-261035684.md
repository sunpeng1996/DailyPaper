---
title: 'OmniShowcase: Omnidirectional Subject-Consistent Video Generation from Multi-View
  Images'
title_zh: OmniShowcase：基于多视角图像的全视角主体一致性视频生成
authors:
- Junyeong Ahn
- Geonwoo Kim
- Kinam Kim
- Gihwi Kim
- Hoonjin Jung
- Hyojin Jang
- Jaegul Choo
affiliations:
- KAIST AI
- Inha University
- FLIPTION
arxiv_id: '2610.35684'
url: https://arxiv.org/abs/2610.35684
pdf_url: https://arxiv.org/pdf/2610.35684
published: '2026-10-25'
collected: '2026-10-29'
category: Multimodal
direction: 多模态生成 · 3D一致视频合成
tags:
- VideoGeneration
- 3DConsistency
- MultiViewImage
- DataSynthesis
- GeometryConditioning
one_liner: 提出自动数据合成管线与几何条件模块，基于多视角输入生成全视角3D一致的主体视频
practical_value: '- 电商商品详情页可直接复用该方案，仅需3~5张商品多视角实拍图即可生成360°旋转、螺旋升降等动态展示视频，替代高成本的专业3D建模

  - 广告/种草短视频素材生产场景，可基于已有商品图批量生成多视角展示素材，大幅降低素材制作成本与周期

  - 虚拟直播间、AR试穿等互动场景，可快速生成任意视角切换的商品3D视频流，提升用户交互展示体验'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多视角输入的主体视频生成方法未显式建模关联多观测的3D结构，且训练数据无法保证视角变化时底层主体3D结构一致，易出现主体畸变、身份漂移等问题。
### 方法关键点
1. 搭建全自动数据合成管线，生成基于3D主体几何驱动的多相机轨迹训练视频，支持360°全轨道视角变化；
2. 提出几何条件模块，输入参考视图重建的表面法向图转盘作为生成条件，无需与生成帧做时序对齐；
3. 构建包含12种相机运动、88种轨迹配置的4K 3D资产视频数据集Showcase-4K，以及带源网格与相机参数的评估集ShowcaseBench。
### 关键结果
在主体身份一致性、3D一致性指标上达到SOTA，同时视频质量与运动自然度保持业内竞争水平。
