---
title: 'DGC-Net: Cross-Modal Dynamic Routing with Global-Guided Compensation in Multimodal
  Sentiment Analysis'
title_zh: DGC-Net：多模态情感分析中带全局引导补偿的跨模态动态路由
authors:
- Linan Zhu
- Huaijing Wu
- Xiao Han
- Yuhao Wang
affiliations:
- Zhejiang University of Technology
- Alibaba Group AIDC
- City University of Hong Kong Department of Data Science
arxiv_id: '2611.04841'
url: https://arxiv.org/abs/2611.04841
pdf_url: https://arxiv.org/pdf/2611.04841
published: '2026-11-03'
collected: '2026-11-07'
category: Multimodal
direction: 多模态情感分析 · 跨模态特征融合
tags:
- Multimodal Sentiment Analysis
- Dynamic Routing
- Cross-Modal Fusion
- Gating Mechanism
- Multimodal Representation
one_liner: 提出融合跨模态动态路由与全局引导补偿的DGC-Net，解决多模态情感分析的模态不一致与贡献失衡问题
practical_value: '- 短视频商品评价、直播用户反馈等电商多模态UGC情感分析场景，可复用跨模态动态路由机制，用全局上下文引导局部模态专家选择，降低单模态噪声干扰

  - 多模态特征融合模块可借鉴全局引导动态补偿思路，固定全局语义为主锚点，自适应调整局部特征权重，避免不可靠局部特征的过度干扰

  - 电商用户偏好挖掘、商品口碑自动化打标场景可直接适配该模型架构，提升情感分类准确率，无需针对不同模态分布做大量定制化调整'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态情感分析（MSA）需融合文本、语音、视觉三类模态判断用户对商品/服务的态度，现有方法存在两个核心痛点：一是单模态局部情感cue建模忽略跨模态全局上下文，导致模态间情感cue不一致；二是全局-局部融合的贡献权重无自适应能力，要么浪费有效局部信息，要么被不可靠局部信息干扰，难以适配不同样本的局部cue可靠性差异。
### 方法关键点
1. 设计跨模态贡献感知的动态专家路由，用全局上下文引导局部专家选择，缓解跨模态情感cue不一致问题
2. 设计全局引导的动态补偿融合机制，以全局语义为主锚点，自适应融入专家优化后的局部cue，解决全局-局部贡献失衡问题
### 关键结果
在5个多模态基准数据集上效果优于现有SOTA，ablation study验证两个核心模块均带来明确性能增益
