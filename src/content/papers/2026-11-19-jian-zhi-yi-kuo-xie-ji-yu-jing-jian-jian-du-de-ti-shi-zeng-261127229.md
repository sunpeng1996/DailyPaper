---
title: 'Prune to Expand: Training Prompt Enhancers with Less to Imitate'
title_zh: 剪枝以扩写：基于精简监督的提示增强模型训练方法
authors:
- Tianhe Wu
- Qilin Sun
- Kede Ma
affiliations:
- City University of Hong Kong
- The Chinese University of Hong Kong (Shenzhen)
arxiv_id: '2611.27229'
url: https://arxiv.org/abs/2611.27229
pdf_url: https://arxiv.org/pdf/2611.27229
published: '2026-11-19'
collected: '2026-11-23'
category: LLM
direction: 大模型提示增强 · 监督数据优化
tags:
- Prompt Enhancement
- Supervised Fine-Tuning
- Data Pruning
- Intent Alignment
- Text Generation
one_liner: 提出纯文本监督剪枝方法P2E，以更少冗余标注提升提示增强模型的效果与意图对齐性
practical_value: '- 电商素材生成场景可复用P2E思路剪枝SFT标注对的冗余信息，在不降低文案/图像生成质量的前提下减少标注与训练成本

  - Agent的用户意图理解模块可借鉴P2E的过滤规则，保留核心需求的同时补充合理结构化背景信息，提升交互匹配度

  - 生成式推荐的prompt增强环节可复用单样本删除阈值约束的剪枝策略，提升生成内容与用户偏好的对齐度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有提示增强（PE）模型的SFT训练普遍通过密集图像描述生成用户风格短提示构造训练对，默认生成效果越好的描述对监督价值越高，但反直觉发现，生成增益差异极大的标注对训练出的PE模型效果几乎无差，核心是密集描述中大量与用户意图弱相关的图像专属细节带来冗余监督，额外增加训练成本还降低意图对齐性。
### 方法关键点
提出纯文本驱动的Prune to Expand（P2E）方法，无需额外标注，在单样本删除边界约束下，选择性剔除密集描述中的冗余句子，仅保留明确用户需求和高信息量视觉结构的内容作为监督信号。
### 关键结果
相同训练配置下，P2E训练的PE模型跨多类图像场景、多款主流视觉生成器，相较传统密集描述SFT方案，人类偏好对齐度与生成视觉质量均实现统计显著提升。
