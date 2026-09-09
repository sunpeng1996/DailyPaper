---
title: Compact Neural Appearance Models for Efficient Gaussian Splatting
title_zh: 面向高效高斯泼溅的紧凑神经外观模型
authors:
- Florian Hahlbohm
- Jorge Condor
- Linus Franke
- Martin Eisemann
- Marcus Magnor
affiliations:
- TU Braunschweig
- Università della Svizzera italiana
- University of Würzburg
- University of New Mexico
arxiv_id: '2609.05255'
url: https://arxiv.org/abs/2609.05255
pdf_url: https://arxiv.org/pdf/2609.05255
published: '2026-09-04'
collected: '2026-09-09'
category: Other
direction: 3D重建 · 高斯泼溅外观优化
tags:
- 3D Gaussian Splatting
- Neural Radiance Field
- Spherical Harmonics
- MLP
- Efficient Rendering
one_liner: 对比多种球面外观模型，提出共享小MLP解码隐码的紧凑表示，优化3DGS存储与性能
practical_value: '- 「共享轻量MLP+低维隐码」替换独立高维参数的压缩思路，可迁移到电商Item/用户Embedding降存储场景，大幅降低内存开销

  - 将前向/反向传播融合进自定义算子的工程优化方法，可复用在推荐大模型的训练、推理加速环节

  - 多模型统一pipeline的对比评估框架，可借鉴用于业务中不同模型方案的性能-效率tradeoff量化对比'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
3D Gaussian Splatting（3DGS）常用低阶球谐函数（SH）做视图依赖外观表示，SH系数占单基元存储与内存吞吐的主要部分，且带宽受限会限制角向细节表达，现有方案缺乏端到端统一对比框架。
### 方法关键点
1. 搭建统一优化pipeline，将SH与近年球面外观模型的前向、反向传播融合进可微CUDA光栅器，同时提供适配笔记本、移动端GPU的跨端WebGL渲染器；
2. 提出隐式外观表示方案，用tiny共享MLP解码每个基元的紧凑隐码生成外观，替代独立SH系数。
### 关键结果
提出的神经表示相比三阶SH，单基元外观存储从192字节降至28字节，优化速度提升1.3×，同时重建质量更高；近年球面模型整体的质量-效率tradeoff最优；还分析了不同外观参数化对几何恢复、非静态内容拟合的影响，给出SH替换的实践指导。
