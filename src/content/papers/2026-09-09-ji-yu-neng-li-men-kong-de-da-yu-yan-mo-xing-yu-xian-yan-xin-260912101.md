---
title: Competence-Gated Pooling of Language Models and Priors for Event Forecasting
title_zh: 基于能力门控的大语言模型与先验信号混合事件预测方法
authors:
- Aditi Tiwari
- Aashrith Bandaru
- Heng Ji
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2609.12101'
url: https://arxiv.org/abs/2609.12101
pdf_url: https://arxiv.org/pdf/2609.12101
published: '2026-09-09'
collected: '2026-09-15'
category: LLM
direction: LLM 混合预测信号融合优化
tags:
- LLM
- Hybrid Forecasting
- Gating Mechanism
- Probability Calibration
- Forecast Fusion
one_liner: 能力门控机制基于边际价值选择性融合大模型与外部先验，提升混合预测性能
practical_value: '- 推荐/广告多模型融合场景可复用能力门控逻辑，不单独评估单模型准确率，而是基于其相对于已有基线的边际价值分配权重，避免冗余信号引入噪声

  - 小样本域的多信号融合可借鉴「域级权重估计+向全局权重收缩」的校准方法，解决小样本下权重估计不稳定的问题

  - Agent调用LLM做决策的场景，不要依赖LLM输出的口头置信度，用历史落地结果反推的领域能力值做是否调用LLM的决策更可靠'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
混合预测场景下已存在市场、统计、人群预测等成熟先验信号，直接引入LLM预测不一定带来增量收益，单模型独立准确率无法代表其在现有系统中的边际价值，缺乏可解释的LLM信号价值判断方案。

### 方法关键点
基于Brier损失推导域级权重相比全局融合权重的增益边界，能力门控核心逻辑：1）用历史已解算结果估计不同域下各信号的权重；2）将不确定的域权重向全局权重收缩，避免小样本域过拟合；3）重校准融合后的预测结果。

### 关键结果
- 2357个二元预测问题、5个LLM测试下，主外部基线Brier得分从0.0771降至0.0732，显著优于全局融合方法
- 门控会自动向更强的外部信号妥协，在ForecastBench市场子集无显著增益
- LLM口头置信度无法有效判断模型是否优于外部基线，基于历史结果估计的能力值可支撑更优的弃权决策
