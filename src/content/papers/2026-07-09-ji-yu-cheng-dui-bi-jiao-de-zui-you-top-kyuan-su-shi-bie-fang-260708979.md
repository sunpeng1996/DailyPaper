---
title: Optimal Top-$k$ Identification from Pairwise Comparisons
title_zh: 基于成对比较的最优Top-k元素识别方法
authors:
- Motti Goldberger
- Nils Rudi
affiliations:
- Yale University
arxiv_id: '2607.08979'
url: https://arxiv.org/abs/2607.08979
pdf_url: https://arxiv.org/pdf/2607.08979
published: '2026-07-09'
collected: '2026-07-13'
category: RecSys
direction: 推荐排序 · 成对比较Top-k识别
tags:
- Pairwise Comparison
- Top-k Identification
- Bandit
- Active Learning
- Sample Complexity
one_liner: 提出首个基于潜在效用模型成对比较的渐近最优固定置信度Top-k识别算法
practical_value: '- 电商爆款选品、广告素材A/B测试场景可复用该成对比较采样策略，大幅降低达到固定置信度所需的对比样本量，减少测试成本

  - LLM评测、多模型效果比对场景可直接套用该渐近最优分配算法，快速筛选出Top-k符合要求的候选模型，缩短评测周期

  - 推荐系统冷启动时的小众新item排序场景，可结合用户隐式反馈（点击/加购的成对偏好）实现低样本量下的精准Top-k召回，减少冷启动损耗'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
固定置信度下基于噪声成对比较的Top-k识别是LLM评测、内容选优、爆款筛选的核心问题，现有方案均无法达到渐近最优，采样量远高于信息论下界，导致对比成本过高，此前该场景下无被证明的渐近最优算法。

### 方法关键点
1. 推导了潜在效用模型下成对比较Top-k识别的信息论下界结构，将其形式化为鞍点问题；
2. 设计计算高效的原对偶在线流程，在线学习得到渐近最优的比对样本分配策略；
3. 构造自适应比对分配跟踪算法，实时匹配原对偶模块输出的最优分配规则，保证采样效率。

### 关键结果
算法被严格证明为该场景下首个渐近最优方案，期望样本复杂度随置信度阈值δ趋近于0时完全匹配信息论下界，无冗余采样开销。
