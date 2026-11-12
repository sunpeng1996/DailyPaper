---
title: Differentially Private Statistical Inference for Rankings from Pairwise Comparisons
title_zh: 面向成对比较排序任务的差分隐私统计推断方法
authors:
- Xintao Xia
- Jia Gu
affiliations:
- Center for Data Science, Zhejiang University
arxiv_id: '2611.13485'
url: https://arxiv.org/abs/2611.13485
pdf_url: https://arxiv.org/pdf/2611.13485
published: '2026-11-10'
collected: '2026-11-12'
category: RecSys
direction: 差分隐私 · 成对比较排序优化
tags:
- Differential Privacy
- Bradley-Terry Model
- Pairwise Comparison
- Ranking
- Top-K Inference
one_liner: 提出边差分隐私约束下的Bradley-Terry模型排序推断方法，支持置信区间计算与top-K成员检验
practical_value: '- 电商用户偏好成对比较类排序任务（如商品A/B打标、榜单生成）可直接复用该差分隐私框架，避免用户偏好数据泄露

  - 公开可获得比较概率的场景（如固定曝光的候选集对比）可直接复用其无额外隐私开销的置信区间、top-K检验流程

  - 小样本成对比较场景可借鉴其岭偏差校正+高斯-拉普拉斯校准的trick，提升排序结果稳定性'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
基于人类/用户成对比较的排序任务（如LLM评测、电商商品偏好打标、榜单生成）需严格保护单条偏好记录的隐私，现有方法缺少差分隐私约束下可解释的统计推断能力，难以量化排序结果可信度。
### 方法关键点
1. 基于边差分隐私约束的Bradley-Terry模型，提出目标扰动估计器，通过留一法分析得到欧氏、逐元素估计误差的有限样本边界，支持低隐私预算的稠密比较图场景；
2. 引入岭偏差校正+高斯-拉普拉斯校准优化小样本表现，结合bootstrap流程实现同步排序推断，支持单样本得分、成对得分差的置信区间计算，以及top-K成员资格检验。
### 关键结果
当比较概率公开已知时，所有推断流程无需额外隐私预算；仿真验证了有限样本表现，已落地应用于创意写作类LLM的排名任务
