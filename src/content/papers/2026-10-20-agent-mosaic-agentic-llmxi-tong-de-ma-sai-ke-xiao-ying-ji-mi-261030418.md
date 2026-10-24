---
title: 'Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems'
title_zh: Agent Mosaic：Agentic LLM系统的马赛克效应机密泄露检测
authors:
- Daniel Ruiz
- Luca Luceri
- Emilio Ferrara
affiliations:
- University of Southern California
- Information Sciences Institute
arxiv_id: '2610.30418'
url: https://arxiv.org/abs/2610.30418
pdf_url: https://arxiv.org/pdf/2610.30418
published: '2026-10-20'
collected: '2026-10-24'
category: Agent
direction: Agent 机密性风险评估
tags:
- LLM Agent
- Confidentiality
- Mosaic Effect
- Security Evaluation
- Data Leakage
one_liner: 量化LLM Agent的马赛克效应泄露风险，验证简单防护措施无法完全规避该类泄露
practical_value: '- 企业内部RAG/Agent服务除文档级权限校验外，需新增跨文档敏感组合规则校验，避免单独授权的用户数据（如浏览记录+消费记录）拼接后泄露用户隐私

  - Agent输出合规校验需覆盖拒绝话术内容，避免类似Claude的「拒绝回答但解释原因时泄露敏感信息」的问题

  - 不同业务域（如电商用户隐私、交易数据、商家机密）的马赛克泄露风险差异大，需分域制定防护规则，不要复用统一的泄露率阈值

  - 可见分类标头+显式聚合规则可降低36个百分点的泄露率，可作为低成本的第一级防护方案，再搭配后置敏感校验进一步降风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent的权限管控仅覆盖单文档访问级别，忽略了多个低密级/用户可访问的独立信息拼接后，会生成用户无权获取的高敏感结论（即马赛克效应），该风险在医疗、军工、企业数据等敏感场景下尤为突出，但此前缺乏系统性量化评估。

### 方法关键点
- 构建30个合成基准示例，覆盖网络安全、医疗、军工3个域，每个示例包含2条SECRET级单文档、1条TOP_SECRET级禁止拼接的复合结论、3类查询（仅需单文档信息的良性查询、直接索要复合结论的显式查询、诱导绕过规则的adversarial查询）
- 实验分两组：受控模拟组固定提供所有相关文档，测试GPT-5.6-Sol、Claude Sonnet 5、Qwen3.5-27B三个模型；真实Agent组测试Pi、Hermes两个开源Agent框架的原生表现
- 采用经过人工标注对齐的LLM judge标注泄露事件，同时区分「仅泄露」「仅拒绝」「拒绝且泄露」「无问题」四类结果

### 关键结果数字
- 无防护时，3个模型的平均泄露率达68.63%；开启分类标头+聚合规则防护后，平均泄露率仍达32.37%
- 即使是仅要求单文档信息的良性查询，GPT-5.6-Sol的泄露率也达7.08%，Pi、Hermes真实Agent的泄露率分别达12.50%、8.75%
- Claude的拒绝回答中超过50%会在解释原因时泄露敏感复合结论，反而成为泄露渠道

### 核心结论
LLM Agent的权限管控不能止步于单文档访问控制，必须对跨文档的敏感组合推理和输出进行全链路校验，才能规避马赛克效应泄露。
