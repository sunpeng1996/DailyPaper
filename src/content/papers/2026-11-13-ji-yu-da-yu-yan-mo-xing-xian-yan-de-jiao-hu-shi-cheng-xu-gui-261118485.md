---
title: Interactive Program Induction with Language Model Priors
title_zh: 基于大语言模型先验的交互式程序归纳
authors:
- Robin Shing Moon Chan
- Ryan Cotterell
affiliations:
- ETH Zürich
arxiv_id: '2611.18485'
url: https://arxiv.org/abs/2611.18485
pdf_url: https://arxiv.org/pdf/2611.18485
published: '2026-11-13'
collected: '2026-11-16'
category: Reasoning
direction: 大语言模型 · 程序归纳推理
tags:
- Program Induction
- Interactive Learning
- LLM Prior
- Importance Sampling
- Bayesian Inference
one_liner: 提出基于LM先验的贪心查询选择算法，降低交互式程序归纳的查询量同时大幅提升准确率
practical_value: '- Agent工具生成/规则生成场景可复用LM先验+贝叶斯后验更新框架，减少用户标注量，降低交互成本

  - 交互式任务的查询选择可借鉴贪心策略+重要性采样估算目标的方法，以最少交互获取最高信息增益

  - 电商低代码规则工具（如商品属性批量规整、商家批量改价）可复用该程序归纳框架降低用户使用门槛'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
程序归纳（从少量输入输出样例还原目标程序）存在固有歧义：有限样例理论上可匹配无穷多泛化结果不一致的程序，纯LM生成的程序准确率低、所需样例数多。
### 方法关键点
1. 贝叶斯视角建模，以LM输出作为程序先验分布$p^0$，通过新增观测样例将后验概率收敛到目标程序；
2. 设计贪心查询选择算法，主动选择信息增益最大的输入向用户索要输出，采用重要性采样估算查询选择目标，引入PAC式程序等价松弛降低匹配约束。
### 关键结果
在CodeARC基准上，相比纯LM基线，准确率最高提升22个百分点，所需输入输出样例最多减少10.5个，算法查询次数上界为$❌(rac{1}γ𝑒ογ 1/p^0(f^⭐))$。
