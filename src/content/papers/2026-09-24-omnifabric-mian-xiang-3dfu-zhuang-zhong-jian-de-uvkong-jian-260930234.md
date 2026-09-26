---
title: 'OmniFabric: Coherent UV Space Texture Synthesis for 3D Garment Reconstruction'
title_zh: OmniFabric：面向3D服装重建的UV空间连贯纹理合成
authors:
- Ding-Jiun Huang
- Yuanhao Wang
- Cheng Zhang
- Hugo Bertiche
- Alexandru-Eugen Ichim
- Thabo Beeler
- Fernando De la Torre
affiliations:
- Carnegie Mellon University
- University of Washington
- Texas A&M University
- Google
arxiv_id: '2609.30234'
url: https://arxiv.org/abs/2609.30234
pdf_url: https://arxiv.org/pdf/2609.30234
published: '2026-09-24'
collected: '2026-09-26'
category: Other
direction: 3D服装重建 · UV纹理合成
tags:
- 3D_Reconstruction
- Texture_Synthesis
- Diffusion_Transformer
- VLM
- Digital_Content_Creation
one_liner: 提出UV空间连贯纹理合成框架OmniFabric，实现单张图像生成生产级3D服装资产
practical_value: '- 电商虚拟试穿、3D商品展示场景可直接复用该方案，仅需单张商品图即可生成无光照、无阴影的纯净3D服装纹理，大幅降低3D资产制作成本

  - 可借鉴「粗粒度初始化+特定域扩散模型精修」的两阶段生成架构，解决折叠、多视角商品的纹理全局一致性生成问题

  - 业务侧需要大量领域内训练数据时，可复用其自动合成数据引擎的搭建思路，降低人工标注成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
单图生成生产就绪的3D服装资产是数字内容创作核心痛点，现有3D重建方案几何生成能力已成熟，但高质量纹理合成仍是瓶颈：生成的纹理常嵌入环境光照、阴影伪影，且全局结构一致性差，无法用于物理仿真与重光照。
### 方法关键点
1. 直接在2D缝纫图案UV空间做全局连贯纹理合成，避免3D到2D映射带来的畸变；
2. 两阶段流水线：基于估计的3D网格+VLM生成粗纹理初始化，覆盖所有展开的缝纫图案；
3. 采用自动合成数据引擎训练的专用扩散Transformer，以3D位置特征为条件，在标准UV域直接精修纹理，去除伪影的同时保留原始服装设计。
### 关键结果
大量实验验证OmniFabric显著优于现有SOTA基线，生成的3D服装纹理真实感强、全局结构连贯，可直接用于生产场景。
