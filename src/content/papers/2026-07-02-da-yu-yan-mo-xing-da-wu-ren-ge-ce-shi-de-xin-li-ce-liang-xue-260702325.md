---
title: Personality Without Persons? A Psychometric Critique of Big Five Testing in
  Large Language Models
title_zh: 大语言模型大五人格测试的心理测量学批判
authors:
- Kim Zierahn
- Cristina Cachero
- Anna Korhonen
- Nuria Oliver
affiliations:
- ELLIS Alicante, Spain
- University of Alicante, Spain
- University of Cambridge, United Kingdom
arxiv_id: '2607.02325'
url: https://arxiv.org/abs/2607.02325
pdf_url: https://arxiv.org/pdf/2607.02325
published: '2026-07-02'
collected: '2026-07-04'
category: Eval
direction: LLM 人格测评有效性验证
tags:
- LLM
- Big Five Personality
- Psychometric Evaluation
- Model Alignment
- Evaluation Framework
one_liner: 基于244款LLM的大规模测评验证人类大五人格量表不适用于LLM，会产生误导性结论
practical_value: '- 电商导购/客服Agent做个性化人设标定时，不要直接套用人类大五人格量表，需基于LLM特性自定义人设测评指标，避免标定人设与实际输出不符

  - 做Agent对齐训练时可参考结论：对齐训练会系统性让LLM输出向社会期许特质偏移，可利用该规律定向调整导购/客服Agent的回复风格

  - 跨LLM选型做推荐系统/Agent基座时，不要将人格类指标作为模型差异对比维度，该类指标仅能解释3%的模型差异，无实际参考价值'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前行业普遍直接套用人类大五人格量表标定LLM人格、对比模型甚至指导治理，但这类量表专为人类设计，未经过LLM场景的有效性验证，可能产生误导性结论。
### 方法关键点
对5种常用大五人格量表做内容效度验证，筛选出适配LLM的版本后，对覆盖49个模型家族的244款不同LLM开展大规模测评，从内容适配性、模型区分度、因子结构一致性三个维度验证量表有效性。
### 关键结果数字
1. 仅适配LLM的大五题项能达到足够内容效度，原生人类题项完全无效；
2. 大五量表几乎无法区分不同LLM，模型间得分差异仅占总方差的3%；
3. LLM的得分无法还原大五的五因子结构，4个维度相关度≥0.92完全坍缩；
4. 对齐训练会系统性让大五得分向社会期许特质偏移，量表测得的并非等价于人类的人格特质。
