---
title: 'Gauss What You Need: Compact Gaussian Splatting Across Scene Scales'
title_zh: 按需生成高斯：适配多场景尺度的紧凑3D高斯溅射方法
authors:
- Afif Boudaoud
- Jiayi Liu
- Alexandru Calotoiu
- Torsten Hoefler
affiliations:
- ETH Zurich
arxiv_id: '2609.31248'
url: https://arxiv.org/abs/2609.31248
pdf_url: https://arxiv.org/pdf/2609.31248
published: '2026-09-25'
collected: '2026-09-28'
category: Other
direction: 3D重建 · 高斯溅射规模自适应
tags:
- 3D Gaussian Splatting
- Density Control
- Adaptive Sizing
- Scene Reconstruction
- Model Compression
one_liner: 提出TangoGS自适应高斯溅射方法，跨场景尺度实现最优重建质量与模型体积平衡
practical_value: '- 电商3D商品建模场景可复用「采集先验+训练反馈」的自适应参数调节思路，避免跨不同尺寸商品反复调优高斯数量

  - 复用去重重复观测视角的像素统计方法，降低多视角商品扫描数据的冗余计算开销

  - 质量引导的高斯增删策略可直接迁移到3D商品模型轻量化流程，在不损失渲染画质的前提下压缩模型存储体积'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
3D高斯溅射重建时，高斯基元数量直接决定重建质量、存储与渲染成本，现有固定阈值方法无法适配不同尺度采集场景，跨场景需反复调参，大场景易出现高斯不足丢失细节的问题。
### 方法关键点
1. 预训练阶段统计采集数据总像素，去重重复观测同一场景点的视角，计算模型生长学习配额，确定模型规模上限；
2. 训练阶段基于重建质量动态控制高斯增删，在配额内确定最终高斯数量。
### 关键结果
13个标准基准场景下，与最优基线LeGS PSNR持平，高斯数量减少48%；8个大场景采集数据下，无需重调配置自动适配规模，平均PSNR比次优方法高0.54dB，高斯数量仅为次优的1/2.3。
