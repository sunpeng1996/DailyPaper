---
title: 'DeFT-RAG: Incrementally Decomposing Multi-Hop Questions into Self-Contained
  Sub-Questions with Reusable Answers'
title_zh: DeFT-RAG：将多跳问题增量分解为可复用答案的自包含子问题的RAG框架
authors:
- Dingyi Kang
- Bingzhe Li
affiliations:
- University of Texas at Dallas
arxiv_id: '2610.37826'
url: https://arxiv.org/abs/2610.37826
pdf_url: https://arxiv.org/pdf/2610.37826
published: '2026-10-27'
collected: '2026-10-30'
category: RAG
direction: RAG · 多跳问答优化
tags:
- RAG
- Multi-hop QA
- Question Decomposition
- LoRA
- Cache
one_liner: 提出面向多跳问答的DeFT-RAG框架，精度超13个基线同时降低LLM调用开销
practical_value: '- 电商导购Agent、多轮搜索query理解场景可复用增量子问题拆解思路：每次仅生成1个明确包含所有实体的自包含子问题，无需提前规划全链路，避免规划/依赖/改写错误，适配用户模糊需求的逐步拆解。

  - 高频子问题QA缓存设计可直接落地：通过语义匹配+轻量判定模型判断子问题是否可复用，实测可降低12.9%的LLM调用，适合电商客服、搜索导购等子问题重复率高的场景降本提效。

  - 大小模型分工思路可复用：将检索片段相关性判断、是否足够回答等yes/no任务交给LoRA微调的小模型完成，减少大模型上下文压力，避免长上下文跟踪错误，可直接优化搜索推荐场景的RAG链路。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG在多跳问答场景缺陷明显：图RAG仅从原问题提及的实体出发检索，很难覆盖未出现的桥接实体；迭代RAG要求大模型同时完成子问题规划、依赖判断、改写、状态跟踪等多任务，易产生四类错误，且中间结果无法复用，推理成本高。

### 方法关键点
- 增量问题分解：每次仅生成1个自包含子问题，子问题明确标注所有涉及实体，无需提前规划、判断依赖或改写，大模型仅需完成生成子问题、回答子问题、最终总结三个细粒度生成任务
- 任务外迁：用规则维护QA表跟踪已获取的QA对，避免大模型长上下文跟踪错误；用LoRA微调的4B轻量决策模型完成三类yes/no判断：是否可直接回答、现有QA是否足够、检索片段是否相关，降低大模型负载
- QA缓存：跨问题存储自包含子问题的QA对，通过语义匹配+决策模型判断是否可复用，无需重复检索和调用大模型

### 关键结果
在MuSiQue、2WikiMultiHopQA、HotpotQA三个多跳QA基准上，对比13个基线（含图RAG、迭代RAG），用gpt-4o-mini和Qwen3.6双骨干，DeFT-RAG均取得最优精度，在MuSiQue上比次优基线精度高5.2+个点，输入token量低于所有迭代方法；开启QA缓存后，MuSiQue 1000个测试问题中23.1%的子问题可复用，LLM调用降低12.9%且精度无下降。

> 最值得记住的话：多跳RAG优化的核心是让大模型只做擅长的细粒度生成任务，把规则可处理、小模型可判定的任务尽可能外迁，同时通过中间结果复用降低开销。
