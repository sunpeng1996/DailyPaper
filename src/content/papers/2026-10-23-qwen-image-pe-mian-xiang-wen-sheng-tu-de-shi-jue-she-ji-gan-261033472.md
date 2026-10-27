---
title: 'Qwen-Image-PE: Learning Visual Design for Text-to-Image Prompt Enhancement'
title_zh: Qwen-Image-PE：面向文生图的视觉设计感知提示增强模型
authors:
- Zekai Zhang
- Yanran Zhang
- Shengming Yin
- Yan Shu
- Zhening Liu
- Bingxuan Zhao
- Chenyang Zhu
- Donghao Zhou
- Jiahao Li
- Jiahao Wang
affiliations:
- Alibaba Cloud Qwen Team
- Peking University
arxiv_id: '2610.33472'
url: https://arxiv.org/abs/2610.33472
pdf_url: https://arxiv.org/pdf/2610.33472
published: '2026-10-23'
collected: '2026-10-27'
category: Multimodal
direction: 多模态大模型 · 文生图提示增强
tags:
- Text-to-Image
- Prompt Enhancement
- Visual Design
- Reinforcement Learning
- Supervised Fine-Tuning
one_liner: 提出两阶段训练的文生图提示增强模型，显式优化细粒度视觉设计维度，性能超越现有基线
practical_value: '- 电商商品广告图生成场景可复用CRD反向蒸馏方案，收集优质商用素材做密集标注作为SFT目标，比零样本写提示的生成效果更符合设计规范，可有效提升素材点击率

  - 生成类任务RL优化可复用Groupwise Design Reward机制，同请求下的多候选联合打分能降低单样本评估偏差，提升优化效率与人类偏好对齐度

  - 做prompt增强时需优先保证增强后内容的信息密度，达到阈值后才能获得稳定收益，避免低信息密度的增强反而劣化原始生成效果

  - 通用视觉设计原则具备跨T2I底座迁移性，无需为每个文生图模型单独训练提示增强器，可大幅降低多模型部署的训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有文生图提示增强方法大多只关注语义对齐和整体美观，缺乏对光照、构图、布局、细节等细粒度视觉设计维度的显式优化，用户输入的短提示往往缺失这些关键信息，导致生成的电商商品图、广告素材等难以达到商用设计标准。

### 方法关键点
- 第一阶段采用Caption-Based Reverse Distillation（CRD）做SFT：选取设计优质的图像生成密集字幕作为增强提示的监督目标，补充CoT设计 rationale 让模型学习设计逻辑，同时拉近增强prompt与T2I底座训练语料的分布差距
- 第二阶段采用Groupwise Design Reward（GDR）做RL优化：同请求下生成多组增强提示对应的图像，将所有候选图拼成网格用多模态裁判做联合打分，多次打乱顺序消除排序偏差，结合设计维度奖励与语义对齐奖励，用GRPO更新增强器

### 关键实验结果
在Qwen-Image-Bench上测试，底座为Qwen-Image-2.1时，Qwen-Image-PE-397B较原始请求总体得分提升7.81分，9B版本超越所有公开PE基线；在4个第三方T2I底座上均获得2.53分以上的总体提升，甚至超越HunyuanImage-2.1、FLUX 3 Image Klein的原生提示增强器3.07、2.74分；人类评估净胜率较原始请求达35.48%。

### 核心结论
提示增强性能沿训练数据量、模型尺寸、信息密度三个维度缩放，其中足够的信息密度是增强生效的前置条件。
