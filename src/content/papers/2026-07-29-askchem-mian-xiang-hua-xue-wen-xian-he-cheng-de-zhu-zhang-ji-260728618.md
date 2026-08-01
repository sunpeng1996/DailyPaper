---
title: 'AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis'
title_zh: AskChem：面向化学文献合成的主张中心化检索基础设施
authors:
- Bing Yan
- Gregory Wolfe
- Stefano Martiniani
- Kyunghyun Cho
affiliations:
- New York University
- Matterstack, Inc.
arxiv_id: '2607.28618'
url: https://arxiv.org/abs/2607.28618
pdf_url: https://arxiv.org/pdf/2607.28618
published: '2026-07-29'
collected: '2026-08-01'
category: RAG
direction: RAG细粒度检索架构优化
tags:
- Claim-Level-Retrieval
- RAG
- Provenance-Grounding
- Agent-Tool
- Information-Extraction
one_liner: 将化学文献检索粒度下沉为带溯源原子主张，配套多结构检索与Agent访问接口
practical_value: '- 做垂类RAG/Agent工具（如电商客服Agent、商品知识库检索）时，可将检索粒度从完整文档/段落下沉到带溯源的原子信息单元，大幅降低LLM信息抽取与校验成本，减少幻觉

  - 垂类检索系统可配套多结构检索能力：分层分类树满足精准检索需求、关联证据图满足拓展检索需求、动态分类体系满足探索性检索需求，覆盖不同用户场景

  - 对外提供Agent访问接口时，除常规REST/SDK外可新增MCP协议支持，适配多Agent协作场景的工具调用需求，降低Agent集成成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有文献检索系统仅返回排序文档列表，科研人员与AI Agent需手动跨文档定位信息、校验溯源、拼接答案，效率极低。
### 方法关键点
将检索粒度从整文档改为带溯源的原子claim，每条claim绑定源DOI、原文引用或明确证据定位符；在共享claim库之上搭建三层互补检索结构：稳定分面分类树支持分层检索浏览、证据图关联相关claim、动态活分类体系将论文归入科学原理分类；同时提供网页端、REST/SDK/MCP接口供用户与AI Agent调用。
### 关键结果
当前已索引14.7万篇论文的240万条claim；在AskChem-Bench测试中，基于AskChem的GPT-5.5阅读器DOI可解析率达100%，较无检索场景高11.7pct，为5个测试系统中引用密度最高。
