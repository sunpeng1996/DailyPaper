---
title: 'Confidence matters: Leveraging Multi-view Geometric Priors for GS-based Reconstruction'
title_zh: 置信度优先：引入多视角几何先验优化3D高斯溅射重建效果
authors:
- Hongyu Zhou
- Zorah Lähner
affiliations:
- University of Bonn
- Lamarr Institute for Machine Learning and Artificial Intelligence
arxiv_id: '2608.06117'
url: https://arxiv.org/abs/2608.06117
pdf_url: https://arxiv.org/pdf/2608.06117
published: '2026-08-06'
collected: '2026-08-07'
category: Other
direction: 3D重建 · 3D高斯溅射优化
tags:
- 3D Gaussian Splatting
- Multi-view Reconstruction
- Geometric Prior
- Confidence Weighting
- Novel View Synthesis
one_liner: 将带置信度的多视角法向、深度几何先验引入3DGS框架，显著提升高反光等复杂场景重建质量
practical_value: '- 电商3D商品建模场景可直接复用该框架，引入多视角几何先验+置信度加权优化3DGS重建效果，解决美妆、3C等高反光商品建模失真问题

  - 多模态召回/多模型结果融合场景可迁移置信度加权思路，利用模型自带的预测置信度过滤低质量结果，降低负向干扰

  - 3D内容生成场景可采用该方案提升物体重建几何精度，减少后续3D内容二次编辑的人工成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
3D Gaussian Splatting（3DGS）是当前主流新视角合成方案，依赖运动恢复结构初始化与光度优化，在高反光等复杂材质场景下几何重建精度差，无法满足高精度3D建模需求。
### 方法关键点
1. 将多视角视觉几何 grounded Transformer（VGGT）输出的法向、深度预测作为几何先验，引入3DGS优化流程；
2. 复用多视角模型自带的预测置信度图作为权重，对不同质量的先验预测加权，避免低质量先验干扰优化过程；
3. 验证多视角几何先验的优化效果显著优于单视角预测方案。
### 关键结果
在标准基准测试集上重建质量实现稳定提升，高反光等复杂场景重建效果增益尤为显著，提取网格的几何保真度大幅改善。
