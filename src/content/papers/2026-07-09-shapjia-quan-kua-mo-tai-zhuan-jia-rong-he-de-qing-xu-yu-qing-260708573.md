---
title: 'SHAP-Weighted Cross-Modal Expert Fusion for Emotion and Sentiment Recognition:
  Evidence and Limits'
title_zh: SHAP加权跨模态专家融合的情绪与情感识别方法及效果边界
authors:
- Adis Alihodzic
- Selma Skopljakovic Hubljar
affiliations:
- University of Sarajevo
arxiv_id: '2607.08573'
url: https://arxiv.org/abs/2607.08573
pdf_url: https://arxiv.org/pdf/2607.08573
published: '2026-07-09'
collected: '2026-07-11'
category: Multimodal
direction: 多模态融合 · SHAP可解释性
tags:
- SHAP
- Multimodal Fusion
- Emotion Recognition
- Sentiment Analysis
- TreeSHAP
- Mixture of Experts
one_liner: 验证sum-abs TreeSHAP加权跨模态专家融合可追平早融合精度且保留模块化特性
practical_value: '- 电商多模态召回/排序场景（融合商品图文、视频、用户评论、行为信号）可采用sum-abs SHAP加权的多专家融合方案，既保留各模态专家独立迭代的模块化优势，又能追平早融合的精度表现

  - 多模态特征维度差异较大时，避免使用mean-abs/median-abs做SHAP归因降维，会压制高维特征的贡献权重，优先选择sum-abs降维保留总归因质量

  - 多模态专家池设计优先投入资源增加跨模态（尤其是全模态）专家，收益远高于优化复杂的单样本路由逻辑，可在降低工程复杂度的同时拿到核心效果收益'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
多模态融合常用早融合（精度高但耦合性强难迭代）、晚融合（模块化但易丢失跨模态交互）两种范式，现有XAI引导的自适应融合（XGAF）方法在专家特征维度不均时，会出现高维跨模态专家被压制的问题。
### 方法关键点
基于TreeSHAP构建单模态、跨模态专家组成的树状混合融合架构，对比mean-abs、median-abs、sum-abs三种SHAP归因降维逻辑，样本级融合权重由SHAP归因幅度生成。
### 关键结果
MELD 7类情绪识别任务上，sum-abs XGAF的Transformer变体加权F1达0.5983，仅比早融合低0.0035，比概率平均晚融合高0.1385，McNemar检验显示与早融合无显著差异（p=1.0）；CMU-MOSEI 3类情感识别任务上加权F1达0.6519，超过早融合的0.6485和晚融合的0.5696，提升统计显著（p=0.0452）；消融验证收益主要来自跨模态（尤其是三模态）专家，而非复杂的单样本路由逻辑，sum-abs权重会向全模态专家集中。
