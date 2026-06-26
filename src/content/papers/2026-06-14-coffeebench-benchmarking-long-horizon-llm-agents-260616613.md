---
title: 'CoffeeBench: Benchmarking Long-Horizon LLM Agents in Heterogeneous Multi-Agent
  Economies'
title_zh: 'CoffeeBench: Benchmarking Long-Horizon LLM Agents'
authors:
- Issa Sugiura
- Daichi Hattori
- Kazuo Araragi
- Keita Ogawa
- Shota Onose
- Taro Makino
- Teppei Usuki
- Takashi Ishida
arxiv_id: '2606.16613'
url: https://arxiv.org/abs/2606.16613
pdf_url: https://arxiv.org/pdf/2606.16613
published: '2026-06-14'
collected: '2026-06-26'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: As LLM agents become capable of increasingly long-horizon tasks, evaluating
  their performance i...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: huggingface-daily
depth: abstract
---

### 摘要

As LLM agents become capable of increasingly long-horizon tasks, evaluating their performance in economic systems is becoming increasingly important. Unlike existing benchmarks that primarily evaluate a single agent interacting with a passive environment, economic systems are inherently multi-agent, requiring autonomous agents to communicate, negotiate, and transact while pursuing their own objectives over extended periods. We introduce CoffeeBench, a benchmark for evaluating LLM agents in a long-horizon multi-agent economy composed of heterogeneous firms. In CoffeeBench, two farmers, two roasters, and two retailers autonomously operate their businesses over a 90-day simulation, each seeking to maximize cumulative net income through communication and transactions while managing cash, inventory, and pricing. The evaluated model controls one coffee roaster, while the remaining firms are controlled by fixed reference agents. Across several recent open-weight and proprietary LLMs, all models outperform a passive baseline that takes no actions, with most achieving positive net income. Analysis of agent behavior reveals substantial differences in long-horizon economic interaction: higher-performing models communicate more actively with other firms, whereas Claude~Haiku~4.5 exhibits an idle-drift failure mode, repeatedly choosing inaction despite producing coherent assessments and plans. We release our code and agent trajectories to support future research.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
