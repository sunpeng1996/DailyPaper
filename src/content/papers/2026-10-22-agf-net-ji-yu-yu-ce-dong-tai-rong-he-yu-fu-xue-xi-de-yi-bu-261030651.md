---
title: 'AGF-Net: A Robust Multimodal Emotion Recognition Model for Asynchronous Audio-Visual
  Signals Based on Predictive Dynamic Fusion with Negative Learning'
title_zh: AGF-Net：基于预测动态融合与负学习的异步音视频鲁棒情绪识别模型
authors:
- Chuan Han Li
- Yun Chien Cheng
affiliations:
- National Yang Ming Chiao Tung University
- National Taiwan University
arxiv_id: '2610.30651'
url: https://arxiv.org/abs/2610.30651
pdf_url: https://arxiv.org/pdf/2610.30651
published: '2026-10-22'
collected: '2026-10-24'
category: Multimodal
direction: 多模态情绪识别 · 跨模态融合优化
tags:
- Multimodal Fusion
- Emotion Recognition
- Negative Learning
- Dynamic Fusion
- Audio-Visual Processing
one_liner: 提出无需人工标注话语边界的音视频多模态情绪识别框架，噪声场景下性能优于现有方法
practical_value: '- 电商直播/智能客服的用户情绪识别可复用自动话语分段+Audio-Guided Fusion框架，降低对人工标注对话边界的依赖

  - 多模态特征融合场景可借鉴Predictive Dynamic Fusion+Multimodal Negative Learning策略，提升低质/噪声输入下的模型鲁棒性

  - 模态质量不稳定的业务场景（如用户上传音视频内容审核）可复用负学习约束平衡不同模态的贡献权重'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态情绪识别依赖人工标注的话语边界，真实场景下自动分段的片段存在边界偏移、模态质量不稳定等问题，易导致特征不一致、识别精度下降。
### 方法关键点
AGF-Net框架集成三大核心策略：1）Audio-Guided Fusion实现跨模态对齐融合；2）Predictive Dynamic Fusion动态适配不同模态的质量波动；3）Multimodal Negative Learning约束模态间平衡，降低低质特征干扰；无需依赖人工标注话语边界，可直接从连续对话中自动生成候选分段并提取特征。
### 关键结果数字
干净条件下准确率64.92%、F1-score 65.47%；中等噪声下准确率62.13%、F1-score 63.08%；高噪声下准确率58.19%、F1-score 59.41%，各场景性能均优于现有同类方法。
