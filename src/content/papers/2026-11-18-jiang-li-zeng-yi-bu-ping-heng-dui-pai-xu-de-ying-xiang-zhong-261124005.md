---
title: 'How Reward Gain Imbalance Shapes Ranking: Rethinking Rubric-Based Reward Aggregation'
title_zh: 奖励增益不平衡对排序的影响：重思基于评分规则的奖励聚合
authors:
- Zhengyuan Fan
- Zhonghua Wu
- Tianyu Cheng
- Qun Chen
affiliations:
- School of Computer Science, Northwestern Polytechnical University
arxiv_id: '2611.24005'
url: https://arxiv.org/abs/2611.24005
pdf_url: https://arxiv.org/pdf/2611.24005
published: '2026-11-18'
collected: '2026-11-19'
category: Training
direction: 多准则奖励聚合 · GRPO训练优化
tags:
- RLHF
- Reward Aggregation
- GRPO
- Rubric
- Ranking
one_liner: 提出自适应双中心裁剪聚合DCC，提升多准则rubric奖励的排序准确性与GRPO训练效果
practical_value: '- 电商/广告多维度评分排序（如商品多指标排序、A/B测试多指标聚合）可直接复用DCC，无需标注数据，在线计算每组裁剪区间，抑制极端分的过度影响，比直接加权平均更稳定

  - 做基于rubric的LLM Agent对齐训练（如电商导购Agent回复的相关性、专业性、转化导向多维度评价）时，用DCC做奖励聚合，无需额外训练权重，比原始加权、sigmoid归一化的GRPO训练效果更优

  - 多目标排序场景不要盲目做维度归一化消除增益差，实证显示该操作会放大残差噪声降低排序准确率，约束单维度贡献上限的思路效果更好'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
基于rubric的多准则奖励聚合是RLHF的核心环节，传统等权聚合默认各维度贡献一致，但实际不同准则的评分尺度、判别力差异大（即奖励增益不平衡），会导致候选排序失真。现有方案多聚焦优化评分器、学习准则权重，未明确增益不平衡与排序的内在关联，且盲目归一化消除增益差反而会降低排序准确率，亟需更合理的聚合策略。

### 方法关键点
- 提出奖励差三分解：将任意两个候选的奖励差拆分为基础满意信号（由满足的准则数决定）、奖励增益不平衡项、残差噪声项，实证显示错排主要集中在增益不平衡项为负、削弱基础信号的配对
- 设计自适应双中心裁剪（DCC）：对每个候选组的所有评分做二分聚类，取两类的中位数作为裁剪上下界，将所有评分裁剪到该区间内再加权平均，仅依赖当前组评分数据无需标注，时间复杂度O(NK log(NK))，适配GRPO每轮rollout的在线计算需求
- 核心逻辑是限制单个准则的评分差对总奖励差的贡献上限，既保留连续评分的有效信息，又抑制极端分的过度影响，不需要完全消除增益不平衡

### 关键结果
在PointRubric、RubricHub-6两个基准上对比原始加权、二值化、sigmoid归一化、RLVR2等方案，DCC在所有排序指标上最优：Mistral-7B下Exact指标分别提升1.92、1.24个百分点，Qwen3.6-27B下分别提升0.24、3.36个百分点。作为GRPO的奖励函数训练Mistral-7B，WritingBench总分比原始奖励高6.41分，比基线模型高8.92分。

### 最值得记住的一句话
多准则聚合不要盲目消除维度增益差异，约束单维度贡献上限比完全归一化更能提升排序稳定性与训练效果
