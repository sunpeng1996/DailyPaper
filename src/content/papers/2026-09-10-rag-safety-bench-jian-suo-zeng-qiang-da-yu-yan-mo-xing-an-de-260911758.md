---
title: 'RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety'
title_zh: RAG-Safety-Bench：检索增强大语言模型安全性的可靠评估
authors:
- Adithiyan Rajan Indira Saravanan
- Kathleen C. Fraser
affiliations:
- University of Ottawa
arxiv_id: '2609.11758'
url: https://arxiv.org/abs/2609.11758
pdf_url: https://arxiv.org/pdf/2609.11758
published: '2026-09-10'
collected: '2026-09-11'
category: Eval
direction: RAG安全性评测基准构建
tags:
- RAG
- LLM Safety
- Evaluation Benchmark
- Safety Guardrail
- Open-source LLM
one_liner: 推出隔离检索器干扰的RAG安全性评测基准，量化不同召回场景下大模型的安全降级风险
practical_value: '- 业务RAG系统安全评测可复用其四场景拆分方法，排除检索器质量干扰，单独定位安全风险来源

  - 业务RAG上线前需做专项安全校验，不可依赖原生LLM的安全护栏，避免恶意prompt结合召回内容生成违规输出

  - 召回阶段需增加风险类query的拦截逻辑，即使无直接有害答案的相关文档也可能触发不安全生成'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
RAG广泛用于降低LLM幻觉、提升输出可信度，但现有研究发现用户输入有害prompt时，RAG可能触发意外的安全降级，业界缺乏可隔离干扰因素的标准化RAG安全评测工具，无法明确不同因素对安全的影响权重。
### 方法关键点
推出RAG-Safety-Bench，排除检索器质量的混淆影响，拆分四类受控评测场景：无RAG、RAG召回含有害请求答案的oracle文档、RAG召回相关但无直接有害答案的文档、RAG召回随机安全文档，精准隔离不同因素对安全降级的影响。
### 关键结果
在5款开源LLM上测试得到：1）模型良性性能和不安全响应能力呈负相关；2）原生LLM的安全护栏完全无法保障RAG场景下的输出安全；3）部分模型即使召回无风险的相关文档，也可能生成不安全内容。
