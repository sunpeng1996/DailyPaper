---
title: Kernel weighted importance sampling for off-policy evaluation in contextual
  bandits
title_zh: 上下文老虎机离线策略评估的核加权重要性采样方法
authors:
- Joshua Spear
- Matthieu Komorowski
- Rebecca Pope
- Neil J Sebire
- Erica E. M. Moodie
affiliations:
- University College London
- Strive Health Ltd
- National Institute for Health Research
- Great Ormond Street Hospital
- McGill University
arxiv_id: '2607.15067'
url: https://arxiv.org/abs/2607.15067
pdf_url: https://arxiv.org/pdf/2607.15067
published: '2026-07-16'
collected: '2026-07-17'
category: Eval
direction: 上下文老虎机 · 离线策略评估
tags:
- Off-policy Evaluation
- Contextual Bandit
- Importance Sampling
- Kernel Method
- Causal Inference
one_liner: 提出Kernel-WIS estimator，统一IS与WIS优势，行为策略misspecification下OPE精度显著提升
practical_value: '- 推荐/广告/Agent决策的离线评估场景中，若日志策略和待评估策略偏差大、行为策略拟合不准，可替换传统WIS为Kernel-WIS，实测可降低14%-21%的评估误差，适合策略迭代频繁的业务

  - 核带宽选择可复用论文中的K折交叉验证方案，以权重预测MSE为目标、配合L-BFGS-B优化器自动调优，避免人工调参的低效问题

  - 遇到IS权重方差爆炸问题时，除传统权重截断方案外，可尝试Kernel-WIS的核平滑思路，在保持估计值有界性的同时降低偏差，尤其适配样本量中等的业务数据集'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
上下文老虎机的离线策略评估（OPE）是推荐、广告等在线决策系统迭代的核心基础，传统重要性采样（IS）方差大无界，加权IS（WIS）虽然降方差但存在样本依赖导致偏差难控，尤其是行为策略拟合不准（misspecification）的工业常见场景下现有方法评估误差极高，亟需更鲁棒的IS类OPE estimator。

### 方法关键点
- State-WIS作为Kernel-WIS的极限形式，对相同context的权重做归一化，保证样本独立性但偏差高
- Kernel-WIS采用RBF核计算context相似度，对相似context的权重做加权归一化，同时保留IS的独立性和WIS的有界性
- 理论上在温和假设下Kernel-WIS具有渐近一致性
- 配套K折交叉验证流程优化核带宽，以权重预测MSE为目标用L-BFGS-B求解最优带宽

### 关键结果
基于10个公开分类数据集改造的contextual bandit场景，对比VIS、WIS、CLPD VIS等baseline，非Oracle行为策略下（工业界常态），Kernel-WIS的MSE比WIS低14%-21%，75分位和99分位的估计值偏差比WIS低10%-15%；Oracle场景下和WIS效果相当，仅连续奖励场景下略逊于WIS。

最值得记住的一句话：工业OPE场景下行为策略几乎不可能完全拟合，核平滑加权的思路可以大幅提升策略评估的鲁棒性。
