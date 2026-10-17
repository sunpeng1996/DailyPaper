---
title: 'PremiseSQL: Evaluating Premise Critique and Abstention in Text-to-SQL Systems'
title_zh: PremiseSQL：Text-to-SQL系统前提校验与拒答能力评测基准
authors:
- Shuo Lin
- Jinzhe Li
- Chenlu Guo
- Yanhan Li
- Yuan Wu
- Yi Chang
affiliations:
- School of Artificial Intelligence, Jilin University
- Engineering Research Center of Knowledge-Driven Human-Machine Intelligence, MOE,
  China
- International Center of Future Science, Jilin University
- Bilibili Inc.
- Xingchen AGI Lab, China Telecom Artificial Intelligence Technology (Beijing) Co.,
  Ltd
arxiv_id: '2610.22158'
url: https://arxiv.org/abs/2610.22158
pdf_url: https://arxiv.org/pdf/2610.22158
published: '2026-10-15'
collected: '2026-10-17'
category: Eval
direction: Text-to-SQL · LLM行为评测
tags:
- Text-to-SQL
- NL2SQL
- LLM Evaluation
- Benchmark
- Prompt Engineering
one_liner: 推出含1800条缺陷查询的PremiseSQL基准，评测Text-to-SQL系统的前提校验与拒答能力
practical_value: '- 电商/广告搜索场景的NL2SQL检索模块可新增前置前提校验逻辑，先识别用户查询的前提缺陷（如商品属性不存在、筛选条件歧义等），避免返回错误结果误导用户，降低客诉率

  - 搭建面向运营/商家的数据分析Agent时，可复用prompt诱导前提校验的思路，通过小样本prompt调优平衡缺陷召回率与正常查询误判率，减少无效SQL生成

  - 业务侧构建自定义NL2SQL能力验收数据集时，可参考PremiseSQL的4类前提故障分类框架，覆盖自身业务常见的查询缺陷场景，提前做能力摸底'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有LLM驱动的NL2SQL系统默认假设用户查询合法可答，对存在前提缺陷（如数据不存在、字段歧义等）的查询仍会生成可执行但逻辑错误的SQL，误导下游数据分析、检索类应用。
**方法关键点**：推出PremiseSQL评测基准，覆盖4类典型前提故障，包含1800条标注的缺陷NL查询+对应1800条正常原始查询；设计三类prompt设置下的统一评测框架，分别衡量模型固有前提感知能力、prompt诱导的前提校验与拒答能力。
**关键结果**：当前主流前沿LLM默认高度信任查询前提，缺陷主动检测率不足10%；面向校验优化的prompt可将缺陷查询拒答率提升42%，但同时会带来18%的正常查询误判率，显著抑制合法SQL的生成效率。
