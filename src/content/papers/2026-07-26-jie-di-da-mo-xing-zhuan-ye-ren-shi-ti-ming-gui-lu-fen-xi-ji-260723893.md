---
title: 'Who Gets Named: Citation Type Predicts Individual Naming by Grounded Language
  Models, and a Roster Instrument Captures 0.5% of It'
title_zh: 接地大模型专业人士提名规律分析及名册测量工具覆盖度验证
authors:
- Dmitrij Żatuchin
affiliations:
- Estonian Entrepreneurship University of Applied Sciences (EUAS)
- Rankfor.AI
arxiv_id: '2607.23893'
url: https://arxiv.org/abs/2607.23893
pdf_url: https://arxiv.org/pdf/2607.23893
published: '2026-07-26'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · LLM推荐行为分析
tags:
- LLM4Rec
- Grounded LLM
- Visibility Measurement
- Citation Analysis
- Recommendation Evaluation
one_liner: 通过2400次Grounded LLM调用实验揭示专业人士提名规律，证实现有名册测量工具覆盖率仅0.5%
practical_value: '- 做本地生活/服务类生成式推荐时，可优先抓取个人站点、垂类门户的内容作为RAG数据源，能提升目标服务人员的曝光概率

  - 多语言市场的生成式推荐策略需区分语种，英语query的个性化推荐粒度可细化到具体个人，小语种本地query可优先推荐机构

  - 评估LLM推荐的品牌/个人曝光效果时，不要依赖固定名册作为唯一真值，固定名册覆盖率不足0.5%会导致评估结果严重偏差'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有AI品牌曝光研究仅聚焦企业主体，缺少服务类场景下LLM提名具体专业人士的行为规律分析，且基于固定名册的曝光测量方案有效性未得到验证。
### 方法关键点
2小时内针对4款主流Grounded LLM发起2400次调用，覆盖120条购买意图Prompt、4个欧洲市场、5种查询语言，采用无名册规则级联标注响应，标注精度96.9%、召回61.7%，统计时修正Prompt内聚类偏差。
### 关键结果
LLM整体提名个人比例为25.8%，类目差异显著（房产35.4%、汽车经销商32.9%、保险仅9.1%）；不同模型提名率差4倍（Grok 38.0% vs Gemini 9.3%）；提名行为仅与引用来源类型相关（个人站点、垂类门户引用分别高2.6、4.3个百分点），与引用量无关；英语Prompt提名率是本地语言的2.3倍；基于LinkedIn的939人名册仅覆盖0.47%的提名提及，代表性极差
