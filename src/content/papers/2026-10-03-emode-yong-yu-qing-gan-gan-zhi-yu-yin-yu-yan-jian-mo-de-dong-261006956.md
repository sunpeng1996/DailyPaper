---
title: 'EMODE: Dynamic Para-Semantic Experts for Emotion-Aware Speech Language Modeling'
title_zh: EMODE：用于情感感知语音语言建模的动态副语义专家
authors:
- Jianan Pan
- Yiwen Gu
- Xinze Li
- Rui Wang
- Kejie Huang
affiliations:
- Zhejiang University
arxiv_id: '2610.06956'
url: https://arxiv.org/abs/2610.06956
pdf_url: https://arxiv.org/pdf/2610.06956
published: '2026-10-03'
collected: '2026-10-10'
category: LLM
direction: 语音大语言模型 · 情感感知 动态专家路由
tags:
- Speech LLM
- Emotion Awareness
- Dynamic Expert Routing
- Paralinguistic Feature
- Empathetic Generation
one_liner: 提出基于动态副语义专家的情感感知语音大模型，兼顾词汇保真与情感敏感性，优化共情响应生成
practical_value: '- 搭建语音交互类电商Agent（智能客服、直播数字人）时，可复用DPSE的语义/副语义双通路拆分融合架构，同时保留用户语音的语义内容与情绪信息，避免仅识别文本忽略用户情绪导致的体验下降

  - 多模态特征解耦训练可借鉴三阶段课程学习策略+正交约束正则，确保不同特征通路的功能专属，减少不同维度特征的互相干扰

  - 做用户情感导向的个性化推荐/营销文案生成时，可复用语义-声学对齐方法，将语音情感信号映射为可匹配推荐标签的结构化特征维度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有语音大模型的声学表征存在特征纠缠问题，模型过度依赖语音转写的文本内容，忽略韵律中承载的情感等副语义信息，难以实现高情感感知能力的交互生成。
### 方法关键点
1. 核心模块Dynamic Para-Semantic Experts（DPSE）将连续语音特征拆分为语义、副语义两条独立通路，动态路由后融合输入大语言模型
2. 采用三阶段课程训练范式：语义预热、副语义激活、联合优化，搭配Orthogonal Expert Guidance、Semantic-to-Acoustic Alignment、Gating Diversity Regularization三类正则约束，保证双通路功能独立不混淆
### 关键结果
在SER测试、共情响应评估、新构建的双语MEPA基准上，实现词汇保真度与情感敏感性的平衡提升，跨语料情感理解鲁棒性、共情响应生成效果均显著优于现有基线
