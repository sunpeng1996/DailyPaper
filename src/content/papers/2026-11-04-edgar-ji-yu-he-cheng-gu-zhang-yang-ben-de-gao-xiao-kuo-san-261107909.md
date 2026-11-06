---
title: 'EDGAR: Efficient Diffusion-Driven Gaussian Avatar Refinement via Synthetic
  Failure'
title_zh: EDGAR：基于合成故障样本的高效扩散驱动高斯头雕优化
authors:
- Kwan Yun
- Minhyeok Bang
- Colette Suhjung Koo
- Junyong Noh
affiliations:
- KAIST Visual Media Lab, South Korea
arxiv_id: '2611.07909'
url: https://arxiv.org/abs/2611.07909
pdf_url: https://arxiv.org/pdf/2611.07909
published: '2026-11-04'
collected: '2026-11-06'
category: Other
direction: 3D数字人优化 · 条件扩散模型
tags:
- Gaussian Splatting
- Diffusion Model
- MoE
- 3D Avatar
- Pseudo Label
one_liner: 提出带MoE结构的条件扩散框架EDGAR，修复高斯头雕伪影同时保留身份一致性
practical_value: '- 电商虚拟主播/3D商品展示数字人场景可复用MoE适配不同降级类型的思路，针对性修复模糊、拉伸、表情失真等常见伪影

  - 可借鉴合成退化三元组数据集构造方法，针对业务bad case自动生成配对训练样本，大幅降低真实样本标注成本

  - 伪标签迭代优化思路可迁移：先用轻量优化模块生成高质量结果作为伪目标，再训练底层生成模型，避免推理时逐帧调用重模块'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有基于单目视频/图像的高斯头雕重建方法几何、纹理约束不足，易出现模糊、拉伸、时序不稳定等伪影，无法直接用于高要求的数字人落地场景。

### 方法关键点
1. 构造EDGAR-SET混合三元组数据集，配对退化渲染图、真值、参考图，模拟真实高斯头雕的各类故障场景
2. 基于单步扩散骨干+自监督Sapiens模型提取的身份特征注入融合块，兼顾去伪影效率与身份保真度
3. 引入MoE结构适配不同退化类型与严重程度；生成的多视角优化渲染图作为伪标签优化底层高斯头雕，推理阶段无需逐帧调用EDGAR

### 关键结果
在3种主流高斯头雕重建方法、3种实验设置下，感知与重建指标均显著优于原始输出与SDEdit基线，跨视角一致性明显提升，大偏航、张嘴等极端场景鲁棒性得到验证
