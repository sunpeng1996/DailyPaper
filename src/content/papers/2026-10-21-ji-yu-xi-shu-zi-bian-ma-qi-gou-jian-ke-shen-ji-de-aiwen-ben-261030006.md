---
title: Building Auditable AI Text Detectors with Sparse Autoencoders
title_zh: 基于稀疏自编码器构建可审计的AI文本检测器
authors:
- Liam Dugan
- Callum McDougall
- Matthew Denton
- Philip Pham
- Christine Kaeser-Chen
- Chris Callison-Burch
affiliations:
- University of Pennsylvania
- Google DeepMind
arxiv_id: '2610.30006'
url: https://arxiv.org/abs/2610.30006
pdf_url: https://arxiv.org/pdf/2610.30006
published: '2026-10-21'
collected: '2026-10-23'
category: LLM
direction: 大模型生成文本检测 · 可解释性
tags:
- Sparse Autoencoder
- AI Text Detector
- Interpretability
- Out-of-Distribution
- Auditable AI
one_liner: 用稀疏自编码器提取黑盒文本检测器可解释特征，构建兼顾准确率、可解释性与OOD性能的可审计检测器
practical_value: '- 电商内容审核、虚假评价检测场景可复用SAE提取黑盒分类器可解释特征的思路，解决AI生成内容审核结果无法解释、用户申诉无依据的问题

  - 可迁移「特征保真度筛选+轻量分类器」架构，优化异常用户识别、广告合规审核等OOD场景分类任务的泛化性能

  - 对需要满足监管审计要求的推荐/广告算法场景，可参考这套从黑盒模型中提取可审计特征的流程，降低合规风险'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有高性能AI生成文本检测器多为黑盒微调神经分类器，决策过程完全不透明，无法满足教育、内容审核、合规审计等高利害场景的可解释要求；而基于文体、语言特征的透明检测器性能与黑盒模型差距极大，无法落地。
### 方法关键点
1. 直接在黑盒检测器的残差流上训练Sparse Autoencoder（SAE），为每个SAE学习到的隐特征分配自动解释标签
2. 仅保留特征描述满足全局保真度阈值的可解释特征，基于筛选后的特征训练轻量级分类器
### 关键结果
提取的SAE隐特征可对应AI生成文本的高特异性、高预测性语言标识；基于可解释特征构建的分类器不仅可审计，在分布外（OOD）文本上的检测性能优于原黑盒神经分类器和传统文体特征分类器两类基线。
