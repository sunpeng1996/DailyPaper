---
title: 'AnyCam: Anything Can Represent Camera for Video Generation'
title_zh: AnyCam：任意物体均可作为视频生成的相机表征
authors:
- Weijie Lyu
- Zhixin Shu
- Yuntian Ke
- Ming-Hsuan Yang
affiliations:
- University of California, Merced
- Adobe Research
- University of Pennsylvania
arxiv_id: '2611.34944'
url: https://arxiv.org/abs/2611.34944
pdf_url: https://arxiv.org/pdf/2611.34944
published: '2026-11-25'
collected: '2026-11-27'
category: Multimodal
direction: 可控相机视频生成 · 3D锚点表征
tags:
- Video Generation
- Diffusion Model
- 3D Reconstruction
- Camera Control
- Novel View Synthesis
one_liner: 用场景锚点物体表征相机，实现大视角变化下的可控相机视频生成
practical_value: '- 电商商品展示短视频可复用锚点物体3D表征思路，围绕核心商品生成不同视角的展示视频，无需复杂相机参数标定

  - H-Concat时序对齐+小模型蒸馏的方案可迁移至实时短内容生成场景，比如AR试穿/试看的实时渲染

  - 大视角变化下的内容一致性生成方法可复用在商品3D建模的低成本批量内容生产流程'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有可控相机视频生成方法要么依赖单目视频中存在尺度歧义的相机参数，要么依赖显式几何表征，大视角变化下生成效果骤降，无法满足物体中心场景的视角切换需求。

### 方法关键点
1. 用场景中的锚点物体表征相机，先对锚点做3D重建，沿目标轨迹渲染获得具备尺度感知、视角完整的相机信号；
2. 采用视频扩散模型将源视频的内容与动态迁移到新视角，通过H-Concat布局实现源帧与目标帧的时序对齐；
3. 可蒸馏为AnyCam-AR少步流式生成器，支持实时相机控制；
4. 基于多相机视频、静态场景采集的像素对齐锚点渲染配对视频训练。

### 关键结果
在多数据集、多轨迹的实验中，相机控制精度、生成视觉质量均优于现有可控视频生成及3D重建SOTA方法。
