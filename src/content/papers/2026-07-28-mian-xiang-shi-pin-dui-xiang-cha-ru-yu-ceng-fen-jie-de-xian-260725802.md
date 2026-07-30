---
title: Explicit Layer Modeling for Video Object Insertion and Layer Decomposition
title_zh: 面向视频对象插入与层分解的显式层建模
authors:
- Kyujin Han
- Seungjoo Shin
- Sunghyun Cho
affiliations:
- POSTECH, Republic of Korea
arxiv_id: '2607.25802'
url: https://arxiv.org/abs/2607.25802
pdf_url: https://arxiv.org/pdf/2607.25802
published: '2026-07-28'
collected: '2026-07-30'
category: Multimodal
direction: 多模态生成 · 视频分层编辑
tags:
- Diffusion Model
- Video Editing
- Layered Representation
- Object Insertion
- Video Decomposition
one_liner: 构建TriLayer三元组视频数据集，提出双分支扩散框架实现高质量视频对象插入与层分解
practical_value: '- 短视频广告商品植入场景可复用DBL-Insert双分支扩散思路，直接生成带RGBA层的商品素材完成合成，省去逐帧抠图步骤，大幅提升广告素材生产效率

  - 可借鉴TriLayer三元组标注范式，构建电商场景专属（背景+商品前景+合成视频）数据集，优化自有视频素材生成模型的效果

  - 做UGC内容的同款商品召回时，可复用DBL-Decompose层分解方法，自动提取UGC视频中的商品前景层，提升同款匹配准确率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前主流视频编辑系统缺乏显式分层视频表示，难以支撑高真实度合成、对象复用和一致性编辑；视频对象插入、层分解任务缺少显式前景层监督，现有方法依赖隐式推理或单场景优化，效果受限。
### 方法关键点
1. 构建TriLayer大规模三元组视频数据集，包含对齐的合成、背景、前景视频，前景层同时覆盖物体外观和关联视觉效果，提供显式监督信号；
2. 提出DBL-Diffusion双分支扩散框架，通过共享去噪模块和跨分支交互机制，联合建模RGB合成视频与RGBA前景层；
3. 框架适配两个核心任务：DBL-Insert实现分层对象插入，生成支持灵活后期编辑的RGBA层；DBL-Decompose基于三元组监督实现视频层分解，恢复前景、背景层。
### 关键结果
显式层建模相比基线方法，视频对象插入保真度、层分解质量均实现大幅提升。
