---
title: 'SACHA: Semantic-Aware Compression for 3D Gaussian Head Avatars'
title_zh: SACHA：面向3D高斯头 Avatar 的语义感知压缩框架
authors:
- Zihan Zhang
- Shanzhi Yin
- Xinju Wu
- Bolin Chen
- Ru-Ling Liao
- Jie Chen
- Shiqi Wang
- Yan Ye
affiliations:
- City University of Hong Kong
- DAMO Academy, Alibaba Group
arxiv_id: '2608.23133'
url: https://arxiv.org/abs/2608.23133
pdf_url: https://arxiv.org/pdf/2608.23133
published: '2026-08-24'
collected: '2026-08-29'
category: Other
direction: 3D数字人 · 高斯头Avatar压缩
tags:
- 3D Gaussian Splatting
- Avatar Compression
- Semantic-aware Pruning
- Motion Decomposition
- Rate-distortion Optimization
one_liner: 提出语义感知控制+外观运动分解的3D高斯头Avatar压缩框架，降存储传输成本且保渲染质量
practical_value: '- 语义感知自适应剪枝逻辑可复用到电商3D商品、数字人主播模型压缩场景，降低端侧渲染算力门槛

  - 外观-运动分解降时序冗余的思路可迁移到直播数字人动作序列传输优化，削减带宽成本

  - 区域自适应高斯基元分配方法可借鉴到虚拟试穿场景，优先保障面部、上身服装等高关注区域的渲染精度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
可动画3D高斯头Avatar支持高保真灵活人脸渲染，但海量高斯基元带来极高存储与传输成本；现有方法既未利用头部不同语义区域的视觉显著性优化基元分配，也未针对训练后的头Avatar序列做高效压缩。
### 方法关键点
1. 语义感知密度控制：通过区域自适应增密与剪枝策略，引导高斯基元向面部等高显著性区域倾斜，实现计算存储资源最优分配；
2. 外观-运动分解压缩：仅传输头部先验参数表征Avatar运动，大幅压缩序列时序冗余，降低传输负载。
### 关键结果
相比现有同类高斯头Avatar表征与压缩方法，SACHA取得更优率失真性能，同时保持高质量的新视角、新表情渲染效果。
