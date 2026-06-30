---
title: Uncertainty-Aware Generation and Decision-Making Under Ambiguity
title_zh: 模糊场景下的不确定性感知LLM生成与决策方法
authors:
- Nico Daheim
- Iryna Gurevych
affiliations:
- Technical University of Darmstadt UKP Lab
- National Research Center for Applied Cybersecurity ATHENE
arxiv_id: '2606.30578'
url: https://arxiv.org/abs/2606.30578
pdf_url: https://arxiv.org/pdf/2606.30578
published: '2026-06-29'
collected: '2026-06-30'
category: LLM
direction: LLM决策优化 · 不确定性感知
tags:
- Uncertainty Estimation
- Conformal Prediction
- Bayesian Decision Theory
- LLM Generation
- Risk-Averse Decision
one_liner: 结合贝叶斯决策与共形预测，提升高模糊场景下LLM生成的效用与可信度
practical_value: '- 电商客服Agent、商品种草文案生成等场景可复用贝叶斯决策框架：先定义业务自定义utility函数（如转化率、用户满意度），对中间决策变量（如回复策略、卖点选择）的分布加权选最优生成结果，避免硬选单一决策带来的误差传播

  - 需要输出置信区间的业务场景（如广告预估得分区间、推荐理由可信度范围），可适配带模糊标签的共形预测，输出有统计保证的决策集，同时最多可降低50%的效用计算成本

  - 高合规要求的生成场景（如售后回复、广告合规文案）慎用minmax风险规避策略，决策集过宽时易生成通用无效内容，优先选择鲁棒性更好的贝叶斯方案'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM被广泛应用于高模糊、高风险的复杂场景（如智能辅导、内容评审），现有多步生成方法通常硬选单一中间决策变量（如辅导策略、评审分数），既不考虑决策的不确定性，也没有统计可信度保证，容易传播误差，大幅降低生成结果的实际效用，用户信任度不足。

### 方法关键点
- 基于贝叶斯决策理论设计生成策略：对中间离散决策变量Ω的分布p(ω|x)加权，选择期望效用最高的生成结果，避免硬选单一决策的误差传播；
- 引入适配模糊标签的共形预测，生成有1-α统计覆盖保证的决策集C(x)，既可以给用户提供决策的置信范围，也能剪枝Ω的计算范围，降低效用计算成本；
- 补充风险规避的minmax决策规则，针对高风险场景优化最坏决策下的效用。

### 关键结果
在Review-5K、NLPEER论文评审数据集和MathDial辅导对话数据集上测试，对比普通ancestral采样基线：贝叶斯决策规则在评审任务的 actionable 指标最高提升0.34，辅导任务奖励提升4%，相对采样的win率达54.3%；共形预测最多可降低50%的效用计算量，性能损失可忽略；minmax规则仅在部分场景有效，决策集过宽时会导致生成过于通用的内容，性能反而下降。

最值得记住的一句话：高模糊场景下，不对中间决策做硬截断、而是对决策分布做边际化的贝叶斯方法，鲁棒性和效用普遍优于硬选单一最优决策的方案。
