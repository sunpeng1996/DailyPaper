---
title: 'Interpretable Humans, Alien LLMs: Expert Analysis of Latent Structures in
  Assessment Responses'
title_zh: 人类可解释 vs LLM黑盒：答题潜在结构的专家分析
authors:
- Alona Strugatski
- Licol Zeinfeld
- Jason Cooper
- Shelley Rap
- Gil Schwarts
- Giora Alexandron
affiliations:
- Weizmann Institute of Science
arxiv_id: '2608.17810'
url: https://arxiv.org/abs/2608.17810
pdf_url: https://arxiv.org/pdf/2608.17810
published: '2026-08-18'
collected: '2026-08-20'
category: Eval
direction: LLM评估 · 认知结构对齐验证
tags:
- LLM Evaluation
- Exploratory Factor Analysis
- Cognitive Alignment
- Interpretability
- Assessment
one_liner: 通过EFA和专家盲评证实LLM答题的潜在因子与人类可解释认知结构存在显著差异
practical_value: '- 设计LLM能力评估方案时，避免直接将人类标准化测试得分等价于LLM对应技能，需补充认知对齐校验环节

  - 电商/推荐场景下的LLM应用（如导购Agent、商品文案生成）能力评估，可复用EFA+盲评框架校验LLM逻辑与人类认知的匹配度

  - 做LLM可解释性优化时，可参考该框架定位人类无法理解的潜在因子，针对性开展对齐微调'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有LLM评估普遍复用面向人类设计的标准化测试，隐含假设LLM与人类采用相同认知结构解题，该假设从未得到系统验证。
### 方法关键点
1. 采集人类与6款LLM在定量推理、化学两类学科测试的答题数据，分群体独立做Exploratory Factor Analysis (EFA) 提取潜在因子
2. 邀请领域专家采用盲评方式，对两类群体的因子结构做认知含义标注
### 关键结果数字
专家可解释绝大多数人类来源的潜在因子；定量推理场景下所有LLM来源的因子均无法被解释，化学场景下仅50%的LLM因子可被赋予认知含义，证实LLM底层运作机制与人类推理存在本质差异。
