---
title: Claim-Gated Source-Risk Auditing for Generative Search
title_zh: 面向生成式搜索的断言门控源风险审计机制
authors:
- Kainan Zhou
- Chuhong Xu
- Gangzhen Qian
- Zhaoyi Li
affiliations:
- Google LLC
- Sony Corporate of America
- Intuit Inc
arxiv_id: '2609.29145'
url: https://arxiv.org/abs/2609.29145
pdf_url: https://arxiv.org/pdf/2609.29145
published: '2026-09-24'
collected: '2026-09-27'
category: Eval
direction: 生成式搜索 · 内容合规审计
tags:
- generative_search
- source_audit
- citation_verification
- compliance_testing
- risk_control
one_liner: 针对生成式搜索源关联遗漏风险，提出断言门控审计框架实现可执行溯源合规校验
practical_value: '- 生成式电商搜索/导购场景可复用四要素校验逻辑：关系证据、回答采纳、重要性、披露要求，全满足才判定合规，可有效识别付费测评未披露、商家自宣未标注等风险

  - 可直接复用「不把证据缺失等同于无关联」的判定规则，减少合规审计误判率，避免漏过未公开的商业关联内容

  - 溯源审计可绑定版本化证据片段，解决大模型生成内容的溯源存证需求，适配监管要求的内容可追溯规则'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有生成式搜索的引用校验仅验证生成内容与引用段落的一致性，未覆盖源与查询目标的关联关系遗漏风险（如付费测评未披露、商家自宣未标注），易误导用户决策。

### 方法关键点
1. 对`query-源-回答`三元组实现断言门控审计，仅当同时满足**关联关系证据存在、回答采纳关联内容、内容具备重要性、关联关系已披露**四个条件时，才判定遗漏问题已解决；证据不全时标记为未解决，不直接判定为无关联。
2. 审计逻辑与引用支持、审核优先级解耦，判定结果绑定版本化证据片段，配套引用检查器实现可执行的溯源合约。

### 关键结果
在全量合成测试集上，可复现全部81种三态谓词组合，正确拒绝192个刻意构造的异常记录；消融实验验证了端点逻辑与缺证处理、引用支持逻辑的解耦有效性。
