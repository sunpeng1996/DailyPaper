---
title: 'ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space'
title_zh: ABot-3DWorld 0：支持任意3D空间探索的通用世界模型
authors:
- Mingchao Sun
- Luyang Tang
- Yu Liu
- Xu Yan
- Zhan Li
- Yunwei Zhang
- Fei Yu
- Zengye Ge
- Yumin Liu
- Jiacheng Zhang
affiliations:
- AMAP CV Lab
- Alibaba Group
arxiv_id: '2607.11673'
url: https://arxiv.org/abs/2607.11673
pdf_url: https://arxiv.org/pdf/2607.11673
published: '2026-07-13'
collected: '2026-07-15'
category: Multimodal
direction: 多模态3D世界模型 · 3D内容生成
tags:
- Multimodal Generation
- 3D World Model
- 3D Gaussian Splatting
- Spatial Primitive
- Content Creation
one_liner: 提出基于统一空间生成基元SGP的多模态3D世界模型，生成高保真可探索3D场景效果超现有开源方案
practical_value: '- 电商场景可复用SGP统一表示思路，把商品多模态信息（图/文/视频）压缩为统一紧凑空间基元，支撑3D商品展示快速生成

  - 本地生活/到店业务可接入该3D生成管线，基于门店实拍图/短视频自动生成可漫游3D门店场景，提升用户探店决策效率

  - 具身Agent场景可将该3D世界作为运行环境，支撑导购、导览类Agent的空间感知与路径规划能力落地'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有AI 3D生成多停留在物体级别，无法支撑场景级沉浸式体验、虚拟探店、游戏场景生产等高价值业务需求，多模态输入到可探索3D世界的转换管线缺乏统一高效方案。
### 方法关键点
1. 核心定义统一Spatial Generative Primitive（SGP），由全景图+空间点云构成，可高效表征任意3D空间
2. 管线分三步：多模态输入先映射为SGP，3D一致全景视频生成器沿规划轨迹探索SGP，最后通过全景视频重建引擎输出高保真3D Gaussian Splatting（3DGS）可探索世界
3. 支持两类输入范式：多视角图/视频等丰富输入走几何严谨重建链路，单图/文本输入走生成式补全链路
### 关键结果
在开源方案中达到SOTA，丰富多模态输入下场景保真度优于Marble，可对接地理POI实现面向C端的地图原生空间探索能力
