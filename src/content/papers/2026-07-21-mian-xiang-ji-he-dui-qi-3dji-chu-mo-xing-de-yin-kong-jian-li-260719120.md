---
title: Latent Riemannian Flow Matching for Geometry-Grounded 3D Foundation Models
title_zh: 面向几何对齐3D基础模型的隐空间黎曼流匹配方法
authors:
- Lisa Weijler
- Irene Ballester
- Guofeng Mei
- Tolga Birdal
- Pedro Hermosilla
affiliations:
- TU Wien
- Fondazione Bruno Kessler
- Imperial College London
arxiv_id: '2607.19120'
url: https://arxiv.org/abs/2607.19120
pdf_url: https://arxiv.org/pdf/2607.19120
published: '2026-07-21'
collected: '2026-07-23'
category: Other
direction: 3D基础模型 · 隐空间流匹配生成
tags:
- 3D Foundation Model
- Flow Matching
- Riemannian Manifold
- Latent Generation
- Geometric Prior
one_liner: 在3D基础模型VGGT的超球乘积隐空间实现黎曼流匹配，提升稀疏输入下的3D场景生成效果
practical_value: '- 若业务用到的预训练大模型（如LLM、多模态大模型）隐空间存在非欧几何结构，不要直接套用欧氏空间生成算法，需适配对应流形设计匹配逻辑，避免生成结果脱离有效分布

  - 下游生成任务可冻结预训练基础模型的解码头，仅在隐空间做适配优化，大幅降低微调成本的同时保留基础模型的强先验能力，可复用在生成式推荐、文案生成等场景

  - 多尺度编码器与生成框架对齐的设计思路，可迁移至多粒度商品语义ID生成、分层召回等推荐任务，保证不同层级生成结果的一致性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有几何对齐3D基础模型（如VGGT）为前馈确定性范式，仅能生成输入视图直接支撑的几何内容；而3D场景生成模型需依赖强几何先验才能从稀疏输入生成连贯结果，两类范式存在天然gap。
### 方法关键点
1. 直接在VGGT隐空间执行流匹配，复用其预训练3D先验，无需绑定高斯、网格、video-VAE隐向量等显式下游表示；
2. 针对VGGT token所在的高维超球乘积空间下欧氏流匹配失效的问题，提出适配4个超球乘积流形的黎曼流匹配框架，与VGGT多尺度编码器对齐，确保生成token落在冻结解码头要求的有效数据流形范围内。
### 关键结果
在RealEstate10K、ScanNet++、ETH3D三个公开数据集上，单视图外观、聚合3D几何指标均优于当前主流场景生成基线，验证了几何基础模型上做隐空间流匹配的可行性。
