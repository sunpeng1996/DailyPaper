---
title: An Empirical Study of Counterfactual Self-Explanations in LLMs
title_zh: 大语言模型反事实自解释能力的实证研究
authors:
- Giannis Kalyvas
- Giorgos Filandrianos
- Orfeas Menis Mastromichalakis
- Vassilis Lyberatos
- Giorgos Stamou
affiliations:
- National Technical University of Athens
- Instituto de Telecomunicações
arxiv_id: '2609.17119'
url: https://arxiv.org/abs/2609.17119
pdf_url: https://arxiv.org/pdf/2609.17119
published: '2026-09-15'
collected: '2026-09-16'
category: LLM
direction: 大语言模型可解释性 · 反事实自解释
tags:
- LLM
- Counterfactual Explanation
- Faithfulness
- Instruction Tuning
- Empirical Study
one_liner: 对LLaMA-3、Qwen-2.5系列10个指令微调模型的反事实自解释能力做系统评测，明确质量影响因素
practical_value: '- 做LLM驱动的推荐/Agent决策可解释性时，优先选用大参数量指令微调模型，其反事实自解释忠实度更高，可更准确地定位模型决策依据

  - 若需生成符合人类认知的最小改动反事实样本，可加入人工标注rationale引导生成，能显著提升人机对齐度，适合电商推荐理由、广告决策解释等面向用户的场景

  - 不可默认自解释的忠实度符合要求，相关功能上线前必须做离线实证验证，避免生成看似合理但不符合模型真实决策逻辑的解释导致用户信任受损'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM自解释生成门槛低、可读性强，但普遍存在忠实度不足的问题，无法反映模型真实决策逻辑，此前缺乏对反事实自解释能力的系统性实证评测。
### 方法关键点
选取LLaMA-3、Qwen-2.5两个系列共10个指令微调模型，在情感分析、自然语言推理两个任务上，从忠实度、最小改动性、人工标注rationale对齐度三个维度，对比模型规模、是否引入rationale引导对解释质量的影响。
### 关键结果
模型规模是解释质量的核心决定因素，大模型生成可翻转自身预测、对准决策相关证据的反事实样本的概率远高于小模型；加入rationale引导生成的反事实样本改动量更小，和人类认知对齐度更高，但忠实度无稳定提升；反事实自解释可靠性高度依赖模型容量，不可默认有效，必须经过实证验证。
