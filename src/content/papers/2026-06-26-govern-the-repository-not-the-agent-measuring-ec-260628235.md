---
title: 'Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native
  Software'
title_zh: 'Govern the Repository, Not the Agent: Measuring Ec'
authors:
- Daniel Russo
arxiv_id: '2606.28235'
url: https://arxiv.org/abs/2606.28235
pdf_url: https://arxiv.org/pdf/2606.28235
published: '2026-06-26'
collected: '2026-06-29'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Autonomous coding agents now open and merge pull requests in shared repositories
  at scale, and...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 摘要

Autonomous coding agents now open and merge pull requests in shared repositories at scale, and the field evaluates them the way it has always evaluated components, one agent at a time, on isolated benchmark tasks. Yet agents that each pass their own tests still leave repositories that accumulate problems no single contribution accounts for. We ask whether this problem belongs to the individual agent or to the repository where it accumulates. We study integration friction, the cost of integrating a contribution into a codebase that other contributors are concurrently changing. Across more than 930,000 agent-authored pull requests, we measure how much of the variation in friction stays with the repository after the contribution, its author, its size, and its agent are accounted for. About half does, and it survives full controls. In the same repositories, agent-authored contributions concentrate this repository-level friction roughly twice as much as human ones (intraclass correlation 0.30 versus 0.16), a gap that holds after controlling for codebase size, age, task shape, process maturity, and merge path. The risk is a property of the ecosystem, not the agent. AI-native software is therefore better measured and governed at the ecosystem level than one agent at a time.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
