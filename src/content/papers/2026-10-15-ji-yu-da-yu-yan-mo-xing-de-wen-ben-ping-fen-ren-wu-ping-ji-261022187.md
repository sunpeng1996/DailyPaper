---
title: 'Change the Number, Change the Answer: Assessing Rating Scale Sensitivity in
  LLM-Based Text Scoring'
title_zh: 基于大语言模型的文本评分任务评级量表敏感度评估
authors:
- Wonjeong Jo
- Gyuwan Kim
- Ming Shan Hee
affiliations:
- UC Davis
- UC Santa Barbara
- MBZUAI
arxiv_id: '2610.22187'
url: https://arxiv.org/abs/2610.22187
pdf_url: https://arxiv.org/pdf/2610.22187
published: '2026-10-15'
collected: '2026-10-17'
category: Eval
direction: LLM 文本评分鲁棒性评估
tags:
- LLM
- Text Scoring
- Rating Scale
- Sensitivity Analysis
- Prompt Engineering
- Robustness
one_liner: 系统分析LLM文本评分的数值与语义量表敏感度，给出可靠评分的设计指引
practical_value: '- 用LLM做商品评论情感打分、UGC内容毒性检测、用户消费倾向判定等文本评分任务时，固定量表的格式、范围、符号，避免跨量表得分不可比

  - rubric-based prompt不会降低量表敏感度，无需为提升评分稳定性额外添加复杂评分规则prompt，可降低推理成本

  - 单极性评分任务（如内容毒性、商品好评度）对量表变动最敏感，上线前需做跨量表鲁棒性校验，避免结果漂移'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM被广泛用于各类文本标量评分任务，但不同场景下选用的评级量表设计差异大，量表设计对得分稳定性、可比性的影响缺乏系统性验证。
### 方法关键点
将量表敏感度拆分为数值敏感度（归一化得分波动）、语义敏感度（得分对应分类变化）两类；实验交叉验证2种量表格式（连续/序数）、4种分档范围（3/5/11/21档）、2种符号类型（有符号/无符号），覆盖政治倾向、情感、毒性3类任务，零样本、规则引导2种prompt策略，5款主流LLM。
### 关键结果数字
单量表设计元素变动平均导致归一化得分偏移0.10，约20%的文本分类结果发生变化；单极性的毒性评分任务敏感度最高；rubric-based prompt相比零样本prompt未降低量表敏感度。
