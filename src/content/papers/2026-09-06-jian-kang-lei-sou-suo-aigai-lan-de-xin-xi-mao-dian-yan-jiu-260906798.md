---
title: Who Anchors AI Overviews in Health? Baidu, Google, and the Geography of Authority
title_zh: 健康类搜索AI概览的信息锚点研究：百度、谷歌与地域权威性
authors:
- Mingyue Zha
- Ho-Chun Herbert Chang
affiliations:
- Dartmouth College
arxiv_id: '2609.06798'
url: https://arxiv.org/abs/2609.06798
pdf_url: https://arxiv.org/pdf/2609.06798
published: '2026-09-06'
collected: '2026-09-10'
category: Eval
direction: 生成式搜索算法审计 · 健康信息公平
tags:
- generative_search
- algorithmic_auditing
- health_information
- information_equity
- AI_overview
one_liner: 跨12国4语种审计百度谷歌健康类AI概览，揭示信息来源的平台地域语言差异
practical_value: '- 做健康、美妆等合规要求高的垂类生成式搜索/Agent问答时，需避免过度导流自有平台，优先接入合规多元的本地数据源，降低合规风险

  - 做多语言/多地域的搜索推荐服务时，使用当地官方语言召回内容，可大幅提升本地来源占比，优化本地化用户体验

  - 垂类内容的免责声明需适配当地语言、文化与监管要求，不可直接套用通用模板，降低内容争议风险

  - 跨地域搜索服务的算法审计可参考本文的跨地域、跨语言、跨主题对照实验设计，高效定位信息差问题'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
生成式AI快速落地搜索场景，但跨平台、地域、语言的搜索信息差异缺乏系统性审计，健康等高利害垂类的信息公平问题无实证支撑。
### 方法关键点
覆盖12个国家、4种语言的1920条健康查询，对百度、谷歌的AI Overview系统做对照审计，测量信息锚点分布，涵盖不同严重度、争议性的健康主题（含中医）。
### 关键结果数字
1. 两家平台均存在垂直整合倾向，AI概览优先导流自有平台而非多元原始来源；
2. 本地化程度低的小型国家，健康查询的本地来源引用占比更低；
3. 使用一国官方语言而非英语查询，本地来源引用占比提升3.5~13.5倍；
4. 健康免责声明随语言、文化呈现多维度差异。
