---
title: Studying Image Tokenizers as Visual Languages in Unified Multimodal Models
title_zh: 统一多模态模型中作为视觉语言的图像分词器研究
authors:
- Siting Li
- Zhengyang Wang
- Simon Shaolei Du
- Xi Chen
- Yang Liu
affiliations:
- University of Washington
- Amazon FAR
arxiv_id: '2609.09143'
url: https://arxiv.org/abs/2609.09143
pdf_url: https://arxiv.org/pdf/2609.09143
published: '2026-09-07'
collected: '2026-09-12'
category: Multimodal
direction: 多模态统一模型 · 图像分词器优化
tags:
- Multimodal Model
- Image Tokenizer
- Autoregressive Training
- Text-to-Image
- Image-to-Text
- Tokenizer Evaluation
one_liner: 搭建可控纯自回归测试床，揭示图文联合训练下图像分词器的表现规律与设计参考
practical_value: '- 电商多模态业务（商品图生成、图文检索、商品配文）选型图像分词器时，优先参考I2T损失作为跨方案的统一评估指标，稳定性远高于T2I损失

  - 图像分词器选型不要仅看重建精度指标，需额外验证其对下游目标任务的实际效果，以及联合训练时对文本建模能力的副作用

  - 多模态预训练调优时按任务拆分损失监控，不同任务的损失缩放规律差异大，避免用单一损失评判整体模型训练效果'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有图像分词器多采用孤立指标或单模态任务评估，无法准确反映图文联合训练时的实际表现，缺乏适配多模态场景的统一评估框架。
### 方法关键点
搭建可控纯自回归测试床，在多模态持续预训练过程中跟踪文本、图像、T2I、I2T四类任务的验证损失，分析损失缩放规律与下游性能的关联，验证判别器、语义监督、词表大小三大分词器设计维度的影响。
### 关键结果
1. 不同任务损失缩放规律差异显著，对分词器的排序结果不一致；
2. 跨分词器评估时I2T损失一致性远高于T2I损失，且与微调后的生成、视觉理解性能均相关；
3. 分词器重建效果优不代表下游任务表现好，且分词器选型会显著影响联合训练中的文本建模效果。
