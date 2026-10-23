---
title: Data-Void Exploits in Web-Searching LLMs
title_zh: 联网搜索类大模型的数据空白漏洞利用研究
authors:
- Michele Guerra
- Wuyeh Jobe
- Sanjana Nambiar
- Christina Pöpper
- Azza Abouzied
affiliations:
- New York University Abu Dhabi
arxiv_id: '2610.30365'
url: https://arxiv.org/abs/2610.30365
pdf_url: https://arxiv.org/pdf/2610.30365
published: '2026-10-21'
collected: '2026-10-23'
category: LLM
direction: 联网大模型 · 漏洞攻防研究
tags:
- Data Void
- LLM Security
- Web-Searching LLM
- GEO
- Adversarial Attack
one_liner: 首次系统验证联网大模型的数据空白漏洞，单页恶意内容即可31%概率被引用或使用
practical_value: '- 电商导购类Agent/联网LLM应用需新增数据源可信度校验规则，对小众新品牌、突发热点相关query，优先采信权威域名内容，阻断低可信度新域名的恶意内容植入

  - 做品牌内容GEO优化以提升在联网LLM回复中的露出概率，可复用验证有效的5项因子：准确专业术语、统计数据、inline引用、安全提示、开篇摘要，效果远优于流畅文案或权威语气

  - 内容安全防控模块可重点监控突发热点类query，该场景数据空白漏洞利用成功率是普通场景的3.58倍，需提前核验相关内容可信度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
联网搜索类LLM已成为用户信息查询的主流入口，其合成回复会掩盖传统搜索的来源可信度、结果排序等风险提示。恶意攻击者可在搜索结果稀缺的「数据空白」场景植入虚假内容诱导LLM引用，该漏洞此前缺乏系统性量化研究，极易被用于虚假商品营销、舆论操纵等场景，对电商、内容平台的用户信任威胁极大。
### 方法关键点
- 覆盖5类数据空白构造策略（突发新闻、新造术语、过时术语、概念拆分、敏感设问）、5个领域，构建56个可控数据空白场景，每个场景仅植入1页攻击者控制的网页
- 设置3级网页可见度变量：高可见度为6年以上老域名自动收录，中可见度为新域名手动提交收录，低可见度为新域名不主动提交，对比有无5项经验证的有效GEO因子的差异
- 测试3款主流联网LLM（ChatGPT、Gemini、Sonar Pro），覆盖中性、好奇、怀疑3种用户提问语气，统计恶意内容被使用、引用、列入来源列表的概率
### 关键结果
- 全场景下恶意内容植入成功率达31%，中高可见度场景下成功率升至42.3%，低可见度页面从未成功植入
- 突发新闻类数据空白的植入成功率是其他策略的3.58倍，敏感设问类成功率仅为其他策略的29%
- 用户提问语气、LLM型号选择对植入成功率无显著影响，仅26.8%的被引用恶意内容会被LLM标注风险警告
### 核心结论
联网LLM的数据源优先级远高于内容本身质量，仅靠内容层面的GEO优化或用户侧谨慎提问无法抵御数据空白漏洞攻击，必须从域名可信度、来源多样性维度做前置防控
