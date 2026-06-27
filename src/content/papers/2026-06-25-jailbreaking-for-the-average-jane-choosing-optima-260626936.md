---
title: 'Jailbreaking for the Average Jane: Choosing Optimal Jailbreaks via Bandit
  Algorithms for Automatically Enhanced Queries'
title_zh: 'Jailbreaking for the Average Jane: Choosing Optima'
authors:
- Prarabdh Shukla
- Ritik
- Suhas Rao
- Arpit Agarwal
- Arjun Bhagoji
arxiv_id: '2606.26936'
url: https://arxiv.org/abs/2606.26936
pdf_url: https://arxiv.org/pdf/2606.26936
published: '2026-06-25'
collected: '2026-06-27'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
one_liner: With a profusion of jailbreaks for LLMs now widely known, a growing concern
  is that non-expert...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 摘要

With a profusion of jailbreaks for LLMs now widely known, a growing concern is that non-expert malicious actors ("the average Jane") could elicit actionable responses to malicious requests. In this work, we examine whether this concern is justified. A non-expert malicious actor requires two ingredients for a successful attack: a powerful jailbreak for their target model, acting on an effective malicious query. For the former, we propose a novel attack strategy based on the multi-armed bandit framework. This allows efficient online learning of the optimal jailbreak from a large choice set via noisy exploration on a small number of queries, with subsequent application of the learnt policy on an exploitation set. For the latter, we curate $\mathrm{FrankensteinBench}$, a safety benchmark of $11,279$ malicious queries drawn from manual curation over $7$ existing benchmarks, along with automated enhancement and generation. Each query is categorized as simple or complex by the technical expertise required to craft it. Our findings confirm the concern. Our bandit-based attack achieves success rates as high as $97\%$ on average over $15$ SoTA open-weight LLMs. Moreover, adding complexity to queries raises the attack success rate by up to $26\%$ on average across models -- making it an effective, automatable prompting strategy.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
