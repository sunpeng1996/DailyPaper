---
title: 'EmoEUS: Uncertainty Supervision for Multimodal Emotion Recognition in Conversation'
title_zh: EmoEUS：面向对话多模态情感识别的不确定性监督框架
authors:
- Zilong Huang
- Kong Aik Lee
- Junjie Li
- Zhe Li
- Man-Wai Mak
affiliations:
- 香港理工大学电子及电机工程系
- 香港大学语音语言与认知实验室
arxiv_id: '2607.18336'
url: https://arxiv.org/abs/2607.18336
pdf_url: https://arxiv.org/pdf/2607.18336
published: '2026-07-19'
collected: '2026-07-24'
category: Multimodal
direction: 多模态对话情感识别 · 不确定性监督
tags:
- Multimodal Fusion
- Emotion Recognition
- Uncertainty Estimation
- MERC
- Supervised Loss
one_liner: 提出显式不确定性监督的对话多模态情感识别框架，通过动态模态加权提升识别性能
practical_value: '- 多模态融合场景（如商品评论、直播内容情感分析）可借鉴不确定性动态加权方案，解决不同模态噪声差异大的问题

  - 显式监督损失设计可复用：将预测方差与特征到聚类中心的距离对齐，降低噪声样本对模型的干扰

  - 可迁移到电商客服对话情感识别、直播观众情绪感知等业务场景，提升情感分类准确率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有对话多模态情感识别（MERC）融合方案普遍忽略不同utterance间的模态特定不确定性，该不确定性来源于线索冲突、噪声波动、模态信号缺失等问题，导致融合效果不稳定。
### 方法关键点
1. 基于学习得到的方差估计动态分配各模态权重，实现不确定性感知的多模态融合；
2. 设计显式监督损失，将每个utterance的预测方差与该utterance分布表征到对应情感、模态专属聚类中心的距离对齐，约束不确定性估计的合理性。
### 关键结果
在IEMOCAP和MELD两个公开MERC数据集上，效果持续超越现有SOTA方法。
