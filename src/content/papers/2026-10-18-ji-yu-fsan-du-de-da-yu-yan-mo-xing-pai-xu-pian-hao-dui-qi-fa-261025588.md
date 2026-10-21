---
title: Divergence based Ranked Preference Alignment for LLMs
title_zh: 基于f散度的大语言模型排序偏好对齐方法f-RPO
authors:
- Rajdeep Haldar
- Yue Xing
- Qifan Song
affiliations:
- Purdue University
- Michigan State University
arxiv_id: '2610.25588'
url: https://arxiv.org/abs/2610.25588
pdf_url: https://arxiv.org/pdf/2610.25588
published: '2026-10-18'
collected: '2026-10-21'
category: Training
direction: LLM偏好对齐 · 排序反馈优化
tags:
- Preference Alignment
- f-divergence
- Rank Optimization
- LLM Training
- Direct Preference Optimization
one_liner: 提出基于f散度的排序偏好对齐框架f-RPO，兼容pairwise场景，多尺度模型上性能优于现有基线
practical_value: '- 电商LLM导购、生成式推荐场景中若有多候选回复/商品的排序标注，可直接用f-RPO替代将排序拆为pairwise的DPO训练，避免丢弃结构化信息，提升标注利用效率

  - 落地时优先选择f-RPO的Total Variation或Reverse KL变种，实验验证二者在排序准确性、生成质量上均优于PL-DPO、Mallows-RCPO等基线，可减少调参成本

  - 可复用论文的权重设计规则：给排名更高的样本、排名差距更大的对比对分配更高训练权重，能进一步提升排序对齐的效果

  - 做推荐结果、候选query排序的LLM对齐时，可复用长度归一化log-likelihood作为排序得分的评估方法，和业务的Spearman相关、Top-1准确率等指标直接对齐，降低离线线上gap'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前LLM偏好对齐大多依赖pairwise二元标注，但单个多候选排序标注包含的信息量远高于二元对比，直接拆解为二元对比会丢弃排序结构化信息、降低训练效率；现有排序偏好对齐方法缺乏统一理论框架，效果仍有提升空间，而此前基于散度的对齐框架仅支持二元偏好场景，无法利用排序标注。

### 方法关键点
- 提出f-RPO框架，将排序偏好对齐建模为高排名响应分布D+和低排名响应分布D-之间的f散度估计问题，可兼容任意f散度，且k=2时直接退化为二元偏好对齐方法，和现有DPO等流程完全兼容
- 设计秩偏好权重规则：ρ(i)∝k-i（高排名样本权重更高）、q(j|i)∝j-i（排名差距越大的对比对权重更高），理论证明满足该规则时，模型最优解可严格保持原始偏好排序一致性
- 给出Total Variation、Reverse KL等常用散度对应的f-RPO具体损失函数形式，无需额外训练奖励模型，属于直接偏好优化类方法，可直接落地

### 关键实验
在UltraFeedback构建的5元排序数据集上，对齐Qwen、Llama、Gemma系列0.5B~9B参数量的基础模型，对比PL-DPO、Mallows-RCPO等基线：
- 排序指标上，f-RPO的TV、Reverse KL变种在Spearman相关系数上平均比基线高0.03~0.11，Top-1准确率最高提升3.23pp
- 生成质量上，AlpacaEval 2.0相对基础模型的胜率最高达94.84%，比基线最高提升11.68pp
- 直接用排序标注训练比拆解为pairwise训练的Spearman相关系数最高提升0.11，标注利用效率显著更高

### 核心结论
多候选排序标注的信息密度远高于二元标注，基于散度的f-RPO框架可高效利用排序标注实现更优的LLM偏好对齐，无需额外改造成本即可兼容现有二元对齐流程
