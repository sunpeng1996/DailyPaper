---
title: Decision-Aware Training for Sample-Based Generative Models
title_zh: 面向采样式生成模型的决策感知训练方法
authors:
- Kornelius Raeth
- Nicole Ludwig
affiliations:
- University of Tübingen
- University of Augsburg
arxiv_id: '2607.01171'
url: https://arxiv.org/abs/2607.01171
pdf_url: https://arxiv.org/pdf/2607.01171
published: '2026-07-01'
collected: '2026-07-02'
category: Training
direction: 生成模型训练 · 决策感知优化
tags:
- Generative Model
- Decision-Aware Training
- Probabilistic Forecasting
- Proper Scoring Rule
- Loss Function
one_liner: 为采样式生成模型设计融合可微决策损失的训练目标，兼顾概率预测精度与下游决策成本优化
practical_value: '- 电商大促库存/流量预测场景可复用该思路，在原有预测损失基础上叠加缺货/超卖对应决策损失，优先保障高风险区域预测精度

  - LLM驱动的Agent行动决策模块训练时，可将下游业务成本构造为可微损失加入训练目标，避免高代价决策错误

  - 生成式推荐模型训练时，可引入用户决策成本（如退款、投诉损失）作为正则项，提升高价值用户的推荐效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
采样式生成模型广泛应用于高风险决策场景的概率预测，但传统训练采用严格proper scoring rule（如能量分数），仅按数据密度分配训练信号，完全不感知下游决策的成本结构，有限模型容量无法向高错误代价区域倾斜，导致关键场景决策损失过高。
### 方法关键点
提出决策感知训练框架，在原有能量分数损失基础上叠加可微的决策损失项，直接惩罚基于模型预测产生的决策成本；该决策损失本身是proper scoring rule，整体训练目标有理论支撑，不会破坏模型原有的概率预测能力。
### 关键结果
在1个合成任务、2个真实世界任务上验证，成本敏感区域的决策损失得到针对性优化，同时完整保留模型的全概率预测能力。
