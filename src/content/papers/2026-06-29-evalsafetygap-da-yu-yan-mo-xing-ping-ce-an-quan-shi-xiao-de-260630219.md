---
title: 'EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety
  Failures'
title_zh: EvalSafetyGap：大语言模型评测安全失效的混合调研与概念框架
authors:
- Buğra Alperen Uluırmak
- Rifat Kurban
affiliations:
- Erciyes University
- Abdullah Gül University
arxiv_id: '2606.30219'
url: https://arxiv.org/abs/2606.30219
pdf_url: https://arxiv.org/pdf/2606.30219
published: '2026-06-29'
collected: '2026-06-30'
category: Eval
direction: LLM安全评测 · 偏差分析框架
tags:
- LLM Evaluation
- AI Safety
- Goodhart's Law
- Benchmark Validity
- Jailbreak Robustness
one_liner: 提出EvalSafetyGap框架梳理LLM评测安全偏差，配套十模型审计方案与统一术语体系
practical_value: '- 落地LLM驱动的推荐/Agent服务时，安全评测需拆分能力、行为安全、治理三个独立维度，避免单一benchmark分数与实际安全表现存在偏差

  - 优化对齐奖励模型时，可参考Instability Decomposition方法拆解proxy失效原因，规避Goodhart效应引发的reward hacking问题

  - 内部LLM服务安全审计可复用多尝试、多协议交叉验证思路，避免单一评测协议导致的结论偏差'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM评测与AI安全存在共性测量问题：benchmark分数、奖励模型信号、公开安全指标提升的同时，其对应的真实潜在属性难以验证，优化压力下极易出现proxy失效。
### 方法关键点
结合混合调研（系统检索+叙事合成+灰色证据追踪）覆盖2018-2026年8个领域的评测安全相关工作，提出EvalSafetyGap假设，整合古德哈特定律、自研的Instability Decomposition、Alignment Trilemma工具分析评测侧与对齐侧的proxy失效，配套10个模型的结构化审计方案。
### 关键结果
10个模型样本中，能力与持续对抗鲁棒性的相关性无统计显著性（Pearson r=+0.232，p=0.520）；开源闭源模型的安全差距较小，主要来自治理披露差异而非行为鲁棒性，评测结论高度依赖协议设定。
