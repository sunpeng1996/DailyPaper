---
title: Towards Clinically Faithful Medical Image Captioning via Enhanced Vision-Language
  Alignment
title_zh: 基于增强视觉-语言对齐的临床可信医学图像描述生成
authors:
- Yunseo Lee
- Hyun Jun Kim
- Heeseung Shin
- Changwon Lim
affiliations:
- Chung-Ang University
arxiv_id: '2608.19825'
url: https://arxiv.org/abs/2608.19825
pdf_url: https://arxiv.org/pdf/2608.19825
published: '2026-08-20'
collected: '2026-08-22'
category: Multimodal
direction: 多模态生成 · 跨模态对齐优化
tags:
- Vision-Language Alignment
- Multimodal Generation
- Reinforcement Learning
- Reranking
- Medical AI
one_liner: 拆分训练推理双阶段对齐，结合多编码器、RL奖励和重排序提升医学图像字幕临床一致性
practical_value: '- 跨模态生成场景可复用「训练+推理双阶段对齐」框架：比如电商商品图文案生成任务，训练侧加商品属性/类目预测辅助损失，推理侧加业务规则/语义重排序，提升生成内容和商品的匹配度

  - 多模态特征提取可采用多编码器互补设计：比如同时使用通用CLIP和电商领域微调CLIP提取商品图特征，覆盖通用语义与领域特定特征，提升表征有效性

  - 领域定制生成任务可设计专属RL奖励：比如针对电商文案生成，引入点击率、转化率相关的奖励信号，直接优化生成分布贴合业务目标'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
医学图像描述生成需满足临床可信要求，但通用多模态模型输出仅保证流畅度，存在临床概念对齐度低、难以捕捉灰度图像细微解剖特征、专业术语匹配度差、数据质量波动大等问题。
### 方法关键点
1. 拆分训练、推理双阶段独立优化对齐效果；
2. 训练侧融合BioMedCLIP、SigLIP2双视觉编码器+Q-Former+LLaMA解码器结构，新增UMLS医学概念预测辅助任务，提出MedPAIR-SCST算法引入临床相关RL奖励，引导生成分布向临床对齐方向偏移；
3. 推理侧基于单嵌入重排序，从候选输出中筛选最优结果。
### 关键结果
多编码器互补特征+概念级辅助学习可有效保留临床关键信息；推理重排序无需额外训练即可提升语义与临床对齐度；双阶段对齐方案在数据受限场景下也可实现更可信的生成效果。
