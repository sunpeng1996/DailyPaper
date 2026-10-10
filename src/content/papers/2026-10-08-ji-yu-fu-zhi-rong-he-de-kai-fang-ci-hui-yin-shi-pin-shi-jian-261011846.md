---
title: Open-Vocabulary Audio-Visual Event Localization via Complex-Valued Fusion
title_zh: 基于复值融合的开放词汇音视频事件定位
authors:
- Anirudh Praveen
- Koteswar Rao Jerripothula
- Pratik Joshi
- Aveen Dayal
- Neela Sawant
affiliations:
- IIT Kanpur
- Dolby Laboratories
arxiv_id: '2610.11846'
url: https://arxiv.org/abs/2610.11846
pdf_url: https://arxiv.org/pdf/2610.11846
published: '2026-10-08'
collected: '2026-10-10'
category: Multimodal
direction: 多模态音视频理解 · 开放词汇识别
tags:
- Multimodal-Fusion
- Open-Vocabulary
- Complex-Valued-NN
- Audio-Visual-Understanding
- OV-AVEL
one_liner: 用复值神经网络融合音视觉多流特征，刷新开放词汇音视频事件定位两项基准SOTA
practical_value: '- 多模态相似度融合场景（如短视频/商品多模态召回匹配）可替换固定加权/几何平均规则，采用复值神经网络做自适应融合，提升匹配精度

  - 多模态任务微调可复用「冻结预训练主干、仅训练融合层+注意力模块」的策略，大幅降低算力成本，适配业务快速迭代需求

  - 可尝试将单模态特征拆分为「标准预训练特征（实部）+ 模态专属补充特征（虚部）」的组合，在不改动预训练模型的前提下提升表征丰富度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有开放词汇音视频事件定位（OV-AVEL）方案依赖固定规则（几何平均、加权平均）融合音-文、视-文两路相似度，无法自适应学习模态贡献，也未充分挖掘模态补充特征的价值。
### 方法关键点
1. 采用复值表征架构：将预训练多模态模型输出的标准音视觉特征作为实部，新增补充特征流（视觉取iHSV虚部、音频取CycleGAN转换的相位谱）作为虚部
2. 用复值神经网络（CVNN）自适应融合两路复值相似度，仅训练时序注意力块与融合CVNN，音视觉编码器全程冻结，大幅降低训练成本
3. 同时提供四流高精度、轻量化双流两种架构可选，适配不同性能需求
### 关键结果
在OV-AVEBench unseen类拆分上Acc/Seg-F1/Event-F1达66.5%/59.1%/54.1%，较微调基线分别提升1.6/4.1/6.6个百分点；在改造后的AVE数据集上同样达SOTA，Acc/Seg-F1/Event-F1为60.7%/51.9%/50.4%
