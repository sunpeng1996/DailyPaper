---
title: 4D Human-Scene Reconstruction from Low-Overlap Captures
title_zh: 低重叠采集条件下的4D人体与场景重建
authors:
- Minhyuk Hwang
- Sangmin Kim
- Seunguk Do
- Daneul Kim
- Jaesik Park
affiliations:
- Seoul National University
arxiv_id: '2607.09125'
url: https://arxiv.org/abs/2607.09125
pdf_url: https://arxiv.org/pdf/2607.09125
published: '2026-07-10'
collected: '2026-07-15'
category: Other
direction: 4D人体场景重建 · 低重叠采集优化
tags:
- 4D_Reconstruction
- Video_Diffusion
- Gaussian_Splatting
- Novel_View_Synthesis
one_liner: 提出StudioRecon管线，通过背景人体解耦等方案实现低重叠相机下SOTA 4D人体场景重建
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有动态人体4D高保真重建依赖密集相机阵列，真实场景中仅能获取低重叠稀疏相机采集数据，会导致重建质量差、未观测区域存在大量伪影，现有低重叠重建方案、视频扩散模型均存在几何一致性差、伪影明显的问题。

### 方法关键点
1. 提出StudioRecon管线，解耦背景与人体独立重建；
2. 用视频扩散模型生成数百个相机可控新视角，增密背景监督信号；
3. 基于跨视角身份关联与多视角关键点三角拟合，鲁棒初始化可变形高斯人体；
4. 引入带运动自适应一致性注入的递归增强模块，消除输出残留伪影。

### 关键结果
在4个真实世界数据集上实现新视角合成效果SOTA，支持新轨迹渲染、人物替换等下游应用。
