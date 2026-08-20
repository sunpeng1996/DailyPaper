---
title: Redakto - The Incognito Tab for LLMs
title_zh: Redakto：面向大语言模型的文本隐私匿名工具
authors:
- Saurav Kumar Saha
- Tom Röhr
- Felix Bießmann
affiliations:
- Berlin University of Applied Sciences
- Einstein Center Digital Future
arxiv_id: '2608.18260'
url: https://arxiv.org/abs/2608.18260
pdf_url: https://arxiv.org/pdf/2608.18260
published: '2026-08-18'
collected: '2026-08-20'
category: LLM
direction: LLM隐私合规 · PII匿名工具
tags:
- Privacy-Preserving NLP
- PII Detection
- Text Anonymization
- GDPR Compliance
- Privacy-Utility Tradeoff
one_liner: 开源轻量LLM前置PII匿名工具Redakto，支持多端调用，匿名后文本效用与原文持平
practical_value: '- 业务接入第三方通用LLM/大模型服务前，可集成Redakto作为前置PII清洗节点，避免电商用户地址、手机号、身份标识等隐私信息泄露，满足国内外数据合规要求

  - 可复用其「PII精准识别+匿名/伪匿名双策略」框架，对用户评论、客服咨询对话、搜索Query等文本脱敏后再送入RAG/Agent/生成式推荐链路，在降低隐私风险的同时保障语义完整性

  - 其「轻量本地部署+标准化API接口」的架构设计可直接复用，快速嵌入现有推荐/搜索/Agent业务的文本预处理流程，无需大幅改造现有链路'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
欧盟GDPR等隐私法规落地后，LLM应用输入文本的PII（个人可识别信息）泄露风险成为业务落地的核心阻碍，现有匿名方案普遍存在语义效用损失大、部署成本高、难以快速集成到业务链路的问题。
### 方法关键点
1. 开源轻量PII匿名工具Redakto，支持PII擦除、伪匿名两类核心能力，同时提供面向终端用户的Web应用、面向开发者的REST API/MCP接口两种接入方式，可直接本地部署，对算力要求低；
2. 针对法律、医疗等强隐私要求领域的文本做了策略优化，重点平衡匿名程度与文本语义完整性。
### 关键结果
在法律、医疗域公开数据集测试中，经Redakto不同匿名策略处理后的文本，下游任务效用得分与原文本持平，无显著性能损失，可直接接入各类LLM任务链路。
