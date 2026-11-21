---
title: 'Direct3D-V3: Latent-Free Diffusion Transformers in the Native Voxel Domain'
title_zh: Direct3D-V3：原生体素域无隐空间扩散Transformer框架
authors:
- Shuang Wu
- Jiachen Qian
- Youtian Lin
- Feihu Zhang
- Philip Torr
- Yao Yao
- Xun Cao
affiliations:
- Nanjing University
- The University of Hong Kong
- DreamTech
- University of Oxford
arxiv_id: '2611.26511'
url: https://arxiv.org/abs/2611.26511
pdf_url: https://arxiv.org/pdf/2611.26511
published: '2026-11-18'
collected: '2026-11-21'
category: Other
direction: 3D原生生成 · 无隐空间扩散Transformer
tags:
- 3D Generation
- Diffusion Transformer
- Voxel Domain
- SDF Modeling
- Latent-Free
one_liner: 丢弃VAE直接在原生体素域建模SDF网格，生成高细节几何可靠的3D网格
practical_value: '- 电商3D商品建模/虚拟展示场景可复用无VAE直接建模思路，避免隐空间压缩丢失商品纹理、结构细节

  - 可借鉴邻域体素隐式流形正则化+渲染法向损失的监督策略，提升3D生成结果的几何一致性与水密性

  - 辅助任务预测输入条件对应相机参数的设计，可迁移至多模态条件生成任务，优化输入与输出的对齐度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有原生3D生成方案均依赖VAE将几何压缩到隐空间再建模，存在两个核心缺陷：VAE重构过程会提前丢失精细几何细节，两阶段训练目标存在 mismatch（VAE面向重构、扩散模型面向分布匹配）。

### 方法关键点
1. 无隐空间设计，完全丢弃VAE，训练与采样阶段直接在原生体素域建模原始SDF体素网格
2. 引入邻域体素隐式流形正则化抑制非水密表面，通过Marching Cubes将预测SDF网格转为网格，用渲染法向损失直接监督模型输出
3. 新增条件图像的相机参数预测辅助任务，强化图像观测到3D形状的映射学习

### 关键结果
消除VAE重构瓶颈，生成网格的局部细节丰富度大幅提升；原生SDF输出+相机预测能力可扩展至生成式重建任务，兼顾观测视角对齐与未观测区域补全
