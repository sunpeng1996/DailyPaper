---
title: 'DS@GT ARC at ImageCLEFmedical 2026: Architectural Diversity for Concept Detection
  and Foundation-Model Scaling for Caption Prediction in Medical Image Analysis'
title_zh: 2026 ImageCLEF医疗图像挑战赛DS@GT方案：多架构概念检测与大模型字幕预测
authors:
- Bowen Wang
- Youwen Zhang
- Ritesh Mehta
affiliations:
- Georgia Institute of Technology
arxiv_id: '2607.27763'
url: https://arxiv.org/abs/2607.27763
pdf_url: https://arxiv.org/pdf/2607.27763
published: '2026-07-30'
collected: '2026-08-02'
category: Multimodal
direction: 多模态医疗图像分析 · 多方案梯度选型
tags:
- Multimodal
- Model Ensemble
- KNN Retrieval
- VLM
- Zero-shot Learning
one_liner: 面向医疗图像概念检测与字幕预测提出多架构方案，在ImageCLEFmedical 2026挑战赛获两项任务Top3
practical_value: '- 多模型晚融合搭配正则化阈值调优的方法，可迁移到电商商品图标注、广告素材打标签等多模态分类场景，解决长尾类目验证集过拟合问题

  - 冻结预训练CLIP类模型embedding做无训练KNN检索的方案，可在成本敏感的多模态分类场景替代微调方案，效果接近微调集成但算力成本大幅降低

  - 覆盖零样本/微调、小/大参数模型的梯度选型思路，可参考用于推荐系统多模态生成类任务的成本-效果权衡评估'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
医疗图像分析存在概念分布极度长尾、多模态大模型输出的事实性与流畅性难以平衡的痛点，针对ImageCLEFmedical 2026挑战赛的概念检测、字幕预测两个赛道优化方案。
### 方法关键点
1. 概念检测赛道：主方案采用ConvNeXt-V2、BiomedCLIP ViT-B/16、DenseNet-169三模型晚融合集成，搭配正则化「Honest Threshold Tuning」流程避免罕见概念过拟合；同时提供训练成本为0的冻结BiomedCLIP embedding KNN检索基线。
2. 字幕预测赛道：覆盖不同成本梯度的方案选型，包括微调Gemma-3 27B、全微调BLIP带自定义Vizwins合并、零样本MedGemma-4B搭配PubMed风格prompt。
### 关键结果
概念检测赛道主方案F1=0.5790排名第一，无训练KNN方案F1=0.5780效果几乎持平；字幕预测赛道微调Gemma-3 27B得分0.3571排名第三，零样本方案得分0.3186。
