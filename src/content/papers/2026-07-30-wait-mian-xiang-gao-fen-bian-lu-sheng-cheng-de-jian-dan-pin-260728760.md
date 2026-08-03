---
title: 'WaiT for the Signal: Simple Frequency-Aware Flow-Matching'
title_zh: WaiT：面向高分辨率生成的简单频率感知流匹配方法
authors:
- Krunoslav Lehman Pavasovic
- Théophane Vallaeys
- Stéphane Mallat
- Giulio Biroli
- Luke Zettlemoyer
- Brian Karrer
- Jakob Verbeek
affiliations:
- Meta FAIR
- École Normale Supérieure, Paris
- Sorbonne University, Paris
arxiv_id: '2607.28760'
url: https://arxiv.org/abs/2607.28760
pdf_url: https://arxiv.org/pdf/2607.28760
published: '2026-07-30'
collected: '2026-08-03'
category: Multimodal
direction: 多模态生成 · 频率感知流匹配
tags:
- Flow-Matching
- Wavelet
- Image Generation
- Video Generation
- Transformer
one_liner: 基于小波分解的高低频分步生成策略，大幅提升图像视频生成质量并降低采样算力
practical_value: '- 电商商品图/短视频广告生成可复用高低频分步生成逻辑，先输出符合要求的轮廓结构再补纹理细节，在提升生成质感的同时降低最多50%采样算力

  - 生成内容评估可借鉴三轴评估思路，在FID等全局指标外补充局部细节、纹理保真度专项评估，避免商品图的细节瑕疵被粗粒度评估指标掩盖

  - 分层调度生成的思路可迁移到生成式推荐场景：先返回粗粒度的推荐结果骨架（如品类、价格区间），再异步补全商品属性、卖点文案等细粒度内容，降低用户等待感知时长'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
高分辨率图像/视频生成需兼顾全局一致性、局部细节、纹理保真度，传统流匹配对所有空间频率统一处理，忽略高频信号比粗结构更早与噪声难区分的天然频率层级，且标准FID评估通过下采样会丢失细粒度细节。
### 方法关键点
1. 提出WaiT小波感知Transformer，通过无损小波将生成过程拆分为粗、细双频段；
2. 高频段延迟启动：粗结构完全生成前保持纯噪声状态，结构成型后再加入流联合优化；
3. 提出覆盖全局质量、局部细节、纹理保真度的三轴原生分辨率评估协议。
### 关键结果
ImageNet 512×512像素级FID最高达1.3（SOTA），采样算力最高降低50%，三轴评估均为帕累托最优；无需算法修改直接适配视频生成，Kinetics-600上FVD达0.84（SOTA），纹理保真度优于现有潜空间模型
