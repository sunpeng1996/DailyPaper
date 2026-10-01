---
title: 'Decision-Oriented Recommendation Reranking: An Empirical Study of Jev'
title_zh: 面向决策的推荐重排模型Jev的实证研究
authors:
- Hanjia Lyu
- Yinglong Xia
affiliations:
- Singapore Management University
- Meta AI
arxiv_id: '2609.40241'
url: https://arxiv.org/abs/2609.40241
pdf_url: https://arxiv.org/pdf/2609.40241
published: '2026-09-29'
collected: '2026-10-01'
category: RecSys
direction: 推荐重排 · 质量延迟权衡分析
tags:
- Reranking
- Recommendation System
- LLM
- Decision Model
- Latency Optimization
one_liner: 实证对比决策导向模型Jev与传统/LLM重排器的效果与延迟特性，给出不同候选集规模下的选型参考
practical_value: '- 重排策略选型可直接参考结论：候选集规模>50的电商/内容推荐场景，决策导向模型对比pointwise LLM重排的延迟优势显著，且效果损失可控，适合对延迟敏感但需要语义理解能力的重排阶段

  - LLM重排范式选择可落地：小候选集（K<20）场景可选listwise LLM降本，中大规模候选集优先选pointwise LLM保证效果，避免listwise随K增大的效果陡降问题

  - 线下重排实验可复用其hard负例构造方法：用召回模型的topK结果作为负例，避免随机负例导致的效果虚高，评测结果更贴近线上真实重排难度

  - 结构化决策类任务（重排、多选项分类）可优先尝试决策导向模型，无需走通用LLM的文本生成路径，可大幅优化推理延迟'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM 用于推荐重排存在明显的效果-延迟权衡：pointwise 范式延迟随候选集规模线性增长，listwise 范式效果随候选集增大陡降，传统 ID 类推荐模型延迟低但语义理解能力不足，决策导向模型的重排表现尚未被系统验证，亟需明确不同重排范式的适用场景边界。
### 方法关键点
- 实验设计隔离重排与召回效果：仅选用 SASRec 召回 top200 中包含正例的样本，构造 1 正例 + K-1 个召回 top 硬负例的候选集，所有模型在完全一致的候选集上测试
- 对比三类重排范式：传统推荐模型（SASRec、DCNv2）、通用 LLM 重排器（Qwen2.5 7B 的 pointwise、listwise 版本）、决策导向模型 Jev
- 统一评测维度：覆盖效果（NDCG@10、HR@10、MRR）与观测延迟，候选集规模 K 取 20/50/100/200 四个梯度，跨影视、游戏、图书三个领域验证
### 关键实验结果
数据集采用 Amazon Reviews 2023 的三个领域，所有本地模型在单张 A800 上测试。核心数字：K=200 时，Jev 的 NDCG@10 比 pointwise Qwen 平均高 21%，观测延迟仅为后者的 1/10；比 listwise Qwen 平均效果高 37%，延迟仅高 2~3 倍；传统推荐模型延迟<2ms 但效果比 Jev 低 40% 以上。
### 核心结论
候选集规模是重排范式选型的核心变量，决策导向模型在中大规模候选集重排场景下，能提供比通用 LLM 重排器更优的质量-延迟权衡
