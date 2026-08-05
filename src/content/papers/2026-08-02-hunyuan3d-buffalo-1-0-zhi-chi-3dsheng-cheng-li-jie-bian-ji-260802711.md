---
title: 'Hunyuan3D-Buffalo 1.0: A Unified Multimodal Model for Scalable 3D Generation,
  Understanding, and Editing'
title_zh: Hunyuan3D-Buffalo 1.0：支持3D生成、理解、编辑的统一多模态模型
authors:
- Junliang Ye
- Kenkun Liu
- Guocun Wang
- Yang Li
- Yansong Qu
- Chunshi Wang
- Jingwei Xu
- Yunhan Yang
- Zibo Zhao
- Jiachen Xu
affiliations:
- Tencent Hunyuan
arxiv_id: '2608.02711'
url: https://arxiv.org/abs/2608.02711
pdf_url: https://arxiv.org/pdf/2608.02711
published: '2026-08-02'
collected: '2026-08-05'
category: Multimodal
direction: 多模态大模型 · 3D统一生成与编辑
tags:
- Multimodal-LLM
- 3D-Generation
- 3D-Editing
- Diffusion
- VLM
one_liner: 基于87M规模3D多模态语料，单架构覆盖3D理解、生成、编辑、部件生成全能力
practical_value: '- 电商3D商品展示、虚拟试穿场景可复用Nano3D-v2 Agent化数据流水线，低成本规模化生成/定制修改3D商品素材

  - 多任务统一训练的协同思路可迁移至多模态商品理解+生成场景：理解模块为生成提供语义约束，生成能力反哺编辑精度

  - 层级化prompt构造+多维度质量过滤的数据集构建方法，可直接复用至AIGC商品素材生成的训练语料加工流程'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前3D领域缺乏统一多模态框架，核心瓶颈是大规模几何一致的3D编辑数据稀缺，理解、生成、编辑模块割裂，无法实现能力协同迁移。

### 方法关键点
- 数据：构建87M规模3D多模态语料，包含25M理解样本、50M文本-3D对、12M编辑对；推出Nano3D-v2 Agent化数据构造流水线，通过锚点视图选择、3D编辑区域定位、体素级编辑、精细化几何纹理优化、VLM过滤，生成高质量几何一致的编辑配对数据
- 架构：采用双模块混合设计，Hunyuan3D-VLM负责3D细粒度语义、结构、空间理解，输出多模态语义条件；Hunyuan3D DiT基于扩散架构负责高保真3D合成；编辑/部件生成任务额外引入源对象表征作为扩散条件，保留未编辑区域结构
- 训练：分四阶段训练，先预训练3D-VLM，再预训练文本到3D生成能力，随后做多任务统一预训练，最后分任务持续微调，训练中保持VLM权重冻结避免破坏理解能力

### 关键结果
- 3D理解：UniPart-Bench基准中，SBERT得分85.47，比SOTA UniVerse3D高2.36；物体caption任务SBERT得分72.94，领先SOTA 7.76
- 文本到3D生成：用户调研中文本对齐偏好率55.2%、几何质量偏好率57.1%、整体偏好率56.6%，是最强基线Omni123的3倍以上
- 3D编辑：Edit3D-Bench基准平均CD低至0.0091，比最强基线Omni123降低86.7%；平均F1达0.6515，是SOTA Steer3D的2.39倍

### 核心结论
3D理解、生成、编辑任务的统一训练不是简单的能力叠加，而是存在明确的协同效应：生成能力提升编辑的几何自然度，理解能力提升编辑的区域定位精度与指令遵循度。
