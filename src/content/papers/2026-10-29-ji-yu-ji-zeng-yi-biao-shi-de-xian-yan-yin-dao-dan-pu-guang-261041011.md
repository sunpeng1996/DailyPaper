---
title: Prior-Guided Single-Exposure HDR Novel View Synthesis via Base-Gain Representation
title_zh: 基于基增益表示的先验引导单曝光HDR新视角合成方法
authors:
- Armin Shafiee Sarvestani
- Sheyang Tang
- Jialu Xu
- Zhou Wang
affiliations:
- Department of Electrical and Computer Engineering, University of Waterloo
arxiv_id: '2610.41011'
url: https://arxiv.org/abs/2610.41011
pdf_url: https://arxiv.org/pdf/2610.41011
published: '2026-10-29'
collected: '2026-11-02'
category: Other
direction: HDR新视角合成 · 3D高斯喷涂
tags:
- 3D Gaussian Splatting
- Novel View Synthesis
- HDR Reconstruction
- Camera Response Function
- Base-Gain Representation
one_liner: 提出PriorGS 3D高斯喷涂框架，实现无真值约束的单曝光HDR新视角合成
practical_value: '- 电商3D商品建模/AR展示场景可复用3D基增益表示方法，基于单曝光普通素材即可生成高保真HDR多视角商品内容，降低素材采集成本

  - 虚拟直播间/实景商品渲染场景可借鉴伪监督+闭环校正范式，解决无HDR真值情况下的高动态范围内容重建问题，提升渲染真实感

  - 商品内容生成管线可复用CRF单调正则化先验，保证不同曝光参数下渲染的商品素材色彩一致性，降低后期调优成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
单曝光HDR新视角合成任务存在两大约束缺陷：一是仅以单曝光LDR视图为监督信号，无HDR真值时重建保真度不足；二是单曝光LDR对相机响应函数（CRF）的监督范围有限，超范围重曝光效果不可靠。此外独立生成的伪HDR跨视图不一致，会严重影响直接编码的HDR场景重建效果。
### 方法关键点
1. 提出PriorGS 3D Gaussian Splatting框架，引入2D单曝光HDR重建方法生成的伪HDR作为监督信号，搭配闭环重建链路锚定输入LDR视图，保证重建一致性；
2. 引入可学习先验正则化CRF建模，强制保证单调性，提升响应合理性；
3. 提出3D基增益HDR表示，将HDR辐射度分解为LDR基底+叠加3D增益场，缓解跨视图伪标签不一致问题，同时支持3D HDR外观编辑。
### 关键结果
在公开数据集上的大量实验验证，PriorGS相对现有基线方法取得显著性能提升
