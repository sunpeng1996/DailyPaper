---
title: Weakly-Supervised RGB-D Salient Object Detection via SAM-driven Pseudo Annotation
  and State Space Interaction-based Diffusion
title_zh: 基于SAM驱动伪标注与状态空间交互扩散的弱监督RGB-D显著目标检测
authors:
- Wenqi Si
- Gongyang Li
- Shixiang Shi
- Weisi Lin
arxiv_id: '2607.15041'
url: https://arxiv.org/abs/2607.15041
pdf_url: https://arxiv.org/pdf/2607.15041
published: '2026-07-16'
collected: '2026-07-18'
category: Other
direction: 弱监督显著目标检测 · SAM+扩散模型
tags:
- Weakly Supervised Learning
- SAM
- Diffusion Model
- State Space Model
- RGB-D SOD
one_liner: 用SAM扩充分散标注+状态空间交互扩散模型，实现媲美全监督的弱监督RGB-D SOD性能
practical_value: '- 稀疏标注转稠密伪标注的思路可复用：推荐场景下可借助通用大模型扩充用户点击、少量人工标注等稀疏监督信号，降低标注成本

  - 跨模态特征融合的频域集成+显隐状态空间交互trick，可迁移到图文多模态推荐的特征交互模块，提升全局特征捕捉能力

  - 扩散模型迭代优化生成结果的思路，可用于生成式推荐的候选结果精炼阶段，抑制噪声提升生成内容质量'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
弱监督RGB-D显著目标检测（SOD）可大幅降低像素级标注成本，但现有涂鸦标注缺乏对象结构与细节，导致输出的显著性图精度偏低，难以落地。
### 方法关键点
1. 设计SAM-PAG模块：基于SAM通过双分支结构与分割掩码一致性约束，将稀疏涂鸦标注扩充为稠密像素级伪标注，解决监督信息稀疏问题
2. 提出S²Diff条件扩散模型：通过频域集成+显隐状态空间交互的跨模态条件生成模块提取全局条件特征，搭配上下文注入模块抑制噪声、增强目标信息，迭代优化带噪显著性图生成高精度结果
### 关键结果
在7个公开数据集上性能优于所有同类涂鸦监督方法，达到与全监督方法相当的竞争水平
