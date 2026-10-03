---
title: 'A Shared Taste for Model-Written Text: The Generator-by-Selector Matrices
  of "AI-AI Bias" Show No Detectable Own-Model Premium'
title_zh: AI生成文本的通用偏好：LLM不存在可检测的自有生成文本溢价
authors:
- Dmitrij Żatuchin
affiliations:
- Estonian Entrepreneurship University of Applied Sciences
- Rankfor.AI
arxiv_id: '2610.00369'
url: https://arxiv.org/abs/2610.00369
pdf_url: https://arxiv.org/pdf/2610.00369
published: '2026-09-30'
collected: '2026-10-03'
category: LLM
direction: LLM行为研究 · LLM-as-Judge 评估
tags:
- LLM-as-a-Judge
- AI-AI-Bias
- Self-Preference
- Permutation-Test
- Model-Evaluation
one_liner: 重分析AI-AI偏好实验数据，证实LLM普遍偏好AI文本但无显著自有模型偏好
practical_value: '- 用LLM-as-Judge做电商商品描述、广告文案排序评估时，无需考虑Judge模型与生成模型的同源偏差，可直接选用通用能力强的大模型作为评估器

  - 电商场景商品描述生成可优先选用GPT-4作为基线，其生成的内容被所有LLM选择器的接纳率可达77%~95%，优于其他模型生成结果

  - 做LLM偏好类A/B测试或评估实验时，必须严格控制内容排序的位置偏差，本研究显示位置偏差最高可导致0.42的选择占比偏移'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
PNAS 2025研究证实LLM作为选择器时，相比人类撰写的文本更偏好AI生成文本，但未验证LLM是否会额外偏好自身生成的文本，可能导致LLM-as-Judge评估存在同源偏差隐患。

### 方法关键点
基于原研究公开的21828条有效trial数据重构5x5生成-选择矩阵，拟合带自有模型偏好项的双向固定效应模型，采用严格排列检验做显著性验证，同时控制位置偏差等干扰因素。

### 关键结果数字
1. 各场景下自有模型偏好溢价均不显著：商品场景+0.013（p=0.24）、论文摘要场景-0.010（p=0.74）、电影场景+0.054（p=0.07），合并样本+0.019（p=0.14），95%置信区间[-0.008, 0.046]
2. 原研究核心结论成立：所有LLM选择器对GPT-4生成的商品描述选择率达77%~95%
3. 位置偏差最高可影响0.42的选择占比，排除顺序干扰后自有偏好结果无变化
