---
title: 'Triadic Werewolf: A Jester Role for Multi-Hop Theory of Mind in LLMs'
title_zh: 'Triadic Werewolf: A Jester Role for Multi-Hop Theo'
authors:
- Avni Mittal
arxiv_id: '2606.27909'
url: https://arxiv.org/abs/2606.27909
pdf_url: https://arxiv.org/pdf/2606.27909
published: '2026-06-26'
collected: '2026-06-29'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Theory-of-mind evaluations of large language models typically use dyadic
  social-deduction games...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Theory-of-mind evaluations of large language models typically use dyadic social-deduction games, where every observable cue points to a single hidden side, so a model with strong language priors can score well without ever simulating opponents' incentives. We extend the Werewolf game with a Jester, a third faction whose utility on peer suspicion is inverted because it wins by being voted out, so optimal play requires reasoning across three opposing utility functions. Across 60 games on GPT-4.1, DeepSeek-V3.1, and Llama-3.3-70B with Jester self-learning on and off, the Jester wins 60-70% of games while Werewolves never exceed 20%, and GPT-4.1 wolves vote the Jester out on day 1 in 60-70% of games, a strictly self-defeating action. Self-learning helps DeepSeek and Llama but hurts GPT-4.1, with the cost landing on Villagers rather than Werewolves. Only DeepSeek learns the subtle strategy of looking suspicious without looking intentionally suspicious, and it gains the most from the loop. Triadic incentive structure exposes a layer of multi-agent reasoning that dyadic deduction games leave invisible.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
