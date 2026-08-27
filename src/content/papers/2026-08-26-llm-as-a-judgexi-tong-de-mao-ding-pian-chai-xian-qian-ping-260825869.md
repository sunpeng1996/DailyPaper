---
title: 'Anchoring Bias in LLM-as-a-Judge Systems: Prior Scores Compromise Evaluation
  Independence'
title_zh: LLM-as-a-Judge系统的锚定偏差：先前评分破坏评估独立性
authors:
- Ante Kapetanovic
- Kemal Altwlkany
- Andro Mercep
- Tomislav Duricic
- Emanuel Lacic
affiliations:
- Infobip
arxiv_id: '2608.25869'
url: https://arxiv.org/abs/2608.25869
pdf_url: https://arxiv.org/pdf/2608.25869
published: '2026-08-26'
collected: '2026-08-27'
category: Eval
direction: LLM评估 · 锚定偏差量化与验证
tags:
- LLM-as-a-Judge
- Anchoring Bias
- Evaluation Bias
- Prompt Engineering
- LLM Evaluation
one_liner: 实证LLM-as-a-Judge受上下文历史评分锚定影响，验证默认评估独立性假设不成立
practical_value: '- 用LLM-as-a-Judge做推荐文案/生成内容A/B测试评估、Agent回答质量打分时，禁止在prompt中带入历史评分、历史评估结果等元数据，避免锚定偏差导致结果失真

  - 若业务流程必须带历史评估信息，不要依赖CoT或「忽略元数据」类提示做缓解，需针对具体业务场景、使用的LLM单独验证缓解策略有效性

  - 电商场景下用LLM做用户评论情感分类、投诉工单定级时，历史工单/评论的标注结果不能作为上下文输入，否则会导致48%的错误无法被纠正，分类准确率下降约10%'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM-as-a-Judge范式广泛用于生成内容评分、迭代优化门控等生产流程，行业默认其评估结果与历史判断独立，该假设未经过系统验证。
### 方法关键点
设置三类prompt对照（无元数据、仅修订框架、带历史评分/尝试次数等锚定元数据），覆盖8款主流LLM、数值打分+带人工标注的行业分类两类任务，累计完成18.5万次有效评估。
### 关键结果
7/8测试模型存在显著锚定偏差，Cohen's d绝对值达0.71（中等偏强效应）；行业分类任务中，锚定元数据阻止48%的错误修正，将10.18%的正确判断导向错误标签；CoT、忽略元数据提示均无法降低整体偏差，仅后者小幅提升配对准确率。
