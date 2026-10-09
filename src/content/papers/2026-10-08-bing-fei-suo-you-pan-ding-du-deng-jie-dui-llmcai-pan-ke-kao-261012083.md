---
title: 'All Verdicts are Not Equal: Rethinking LLM Judge Reliability'
title_zh: 并非所有判定都等价：对LLM裁判可靠性的重新思考
authors:
- Vineet Kumar
- Darshita Rathore
- Anindya Moitra
affiliations:
- PayPal Artificial Intelligence
arxiv_id: '2610.12083'
url: https://arxiv.org/abs/2610.12083
pdf_url: https://arxiv.org/pdf/2610.12083
published: '2026-10-08'
collected: '2026-10-09'
category: Eval
direction: LLM评测 · 裁判可靠性优化
tags:
- LLM-Judge
- Evaluation
- Position Bias
- Reproducibility
- Robustness
one_liner: 对LLM裁判开展多维度压力测试，揭示其系统性缺陷，提出可信判定率指标与鲁棒评测方案
practical_value: '- 做GenRec、Agent效果评估时，不要完全依赖pairwise LLM裁判的结果，需交叉验证避免位置偏置、重复判定不一致的问题

  - 可复用本文提出的可信判定率(T)指标，从可复现、顺序无关、准确性三个维度量化自家LLM评测流程的可靠性

  - 优先采用整体rubric评分替代pairwise胜率统计，比单纯调prompt更能提升LLM评测可信度，减少A/B测试结论偏差'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM-as-a-Judge已是NLP领域通用评测范式，长期被当作确定性真值使用，但其系统可靠性缺乏系统性验证。
### 方法关键点
对6个前沿大模型开展多维度压力测试，覆盖4个基准、5种prompt格式、2种内容呈现顺序、3种采样温度，单条件重复10次；提出统一度量可信判定率(T)，量化评测的可复现性、顺序无关性、准确性的联合概率。
### 关键结果
零温下相同输入也会出现判定波动，困难任务中内容顺序调换会翻转多数判定，确定性最高的裁判虽一致性拉满但准确率仅51%；改用整体rubric评分比任何单prompt优化的可信性提升幅度都更高
