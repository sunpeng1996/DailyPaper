---
title: 'RealMe: Immersive Volumetric Video from Minimal Captures'
title_zh: RealMe：基于少量采集数据生成沉浸式体视频
authors:
- Chenxu Zhou
- Zhiyuan Yu
- Yudong Jin
- Yinji Shentu
- Yu Zhang
- Jiaming Sun
- Xiaowei Zhou
affiliations:
- State Key Laboratory of CAD&CG, Zhejiang University
- 4DV.ai
arxiv_id: '2610.30023'
url: https://arxiv.org/abs/2610.30023
pdf_url: https://arxiv.org/pdf/2610.30023
published: '2026-10-20'
collected: '2026-10-23'
category: Other
direction: 生成式4D体视频重建
tags:
- Diffusion Model
- Volumetric Video
- 4D Reconstruction
- Sparse View Synthesis
one_liner: 基于视频扩散模型从稀疏低清采集生成2K、4D一致的沉浸式体视频
practical_value: '- 电商XR购物、3D/4D商品内容生成场景，可借鉴稀疏输入下用扩散模型做高分辨率多视角一致内容增强的架构思路

  - 跨视角/时序一致性优化可复用「因子化时空注意力适配输入布局」「隐空间频域损失」两个算法trick

  - 普通搜索推荐、Agent业务无直接复用价值，仅适用于3D内容生产相关的电商垂直场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有沉浸式体视频生成方案要么依赖昂贵的密集多视角采集设备，落地门槛高；要么基于生成模型的方案存在分辨率低、4D时空一致性差的缺陷。
### 方法关键点
1. 基于高分辨率视频扩散模型搭建统一框架，从原始采集视频构建辅助数据，结合布局感知位置编码共同编码为隐向量
2. 采用适配多视角采集布局的因子化时空注意力，跨视角与时序维度去噪后解码为增强视频，优化4D表征一致性
3. 新增隐空间频域损失，缩小生成视频与真实采集的数据分布差距
### 关键结果
在公开DNA-Rendering基准与自建RealVV数据集上，视觉保真度、4D一致性均超越SOTA，可生成2K分辨率的沉浸式体视频
