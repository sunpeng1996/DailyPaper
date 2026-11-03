---
title: 'SIDRec: End-to-End Semantic ID Representation and Modeling for Recommendation'
title_zh: SIDRec：面向推荐的端到端语义ID表示与建模框架
authors:
- Zhuohang Jiang
- Yongsen Pan
- Pangjing Wu
- Zihuai Zhao
- Zheng Hu
- Yuxin Chen
affiliations:
- The Hong Kong Polytechnic University
- University of Electronic Science and Technology of China
- Southwest Jiaotong University
- Kuaishou Technology
arxiv_id: '2611.01136'
url: https://arxiv.org/abs/2611.01136
pdf_url: https://arxiv.org/pdf/2611.01136
published: '2026-10-31'
collected: '2026-11-03'
category: GenRec
direction: 生成式推荐 · Semantic ID 端到端优化
tags:
- Semantic-ID
- CTR-Prediction
- MMoE
- End-to-End
- Recommendation-System
one_liner: 融合内容与协同信号的端到端语义ID推荐框架，较SOTA最高提升5.15% GAUC
practical_value: '- Semantic ID构造阶段可复用自更新融合机制，将预训练内容表征与预训练排序模型产出的协同Embedding通过可学习门控加权融合，解决语义与协同偏好
  mismatch 问题，提升冷启动/长尾物品推荐效果

  - 可借鉴MMoE驱动的端到端联合优化范式，让下游推荐任务梯度直接回传更新Semantic ID量化过程，避免两阶段训练中SID固定导致的目标不匹配问题，实测最高带来5.15%的GAUC提升

  - 工业落地可直接复用SID训练的超参配置：3层残差量化码本各256个码字，历史序列截断为最近50个，CTR任务和SID tokenizer的学习率分别设为1e-3和1e-5，降低调参成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Semantic ID（SID）推荐方法存在两个核心痛点：一是仅基于内容语义构造SID，未充分融合用户交互反映的协同偏好，易出现语义相似但用户偏好差异大的匹配错误；二是SID构造与下游推荐任务拆分的两阶段训练范式下，SID固定无法适配推荐目标，限制效果上限，冷启动、长尾物品表现差。
### 方法关键点
- 自更新协同-多模态融合：将预训练排序模型产出的协同Embedding表，与固定的多模态内容Embedding通过可学习sigmoid门控加权融合，协同Embedding表在训练中持续更新，兼顾内容语义与用户偏好
- 可微分SID适配：基于残差量化VAE构造SID，采用直通量化+Gumbel扰动实现CTR任务梯度直接回传更新tokenizer的编码器、码本，解决两阶段训练的目标不匹配问题
- MMoE联合优化：共享4个FFN专家，分别适配CTR预测、SID预测两个任务的专属门控，联合优化CTR损失、SID预测损失、量化重建损失，统一训练目标
### 关键结果
在3个公开数据集（Amazon Electronics/Beauty、MovieLens-20M）上对比15个SOTA CTR基线，GAUC较最强基线TransAct最高提升5.15%，AUC最高提升4.27%；快手工业场景两个域的曝光、点击、转化任务UAUC最高提升2.57pp，WUAUC最高提升2.48pp；移除两个核心模块后AUC相对下降7.19%。
### 核心结论
Semantic ID的核心价值不在于静态内容语义编码，而在于对齐下游推荐目标、同时融合内容与协同信号的端到端自适应学习
