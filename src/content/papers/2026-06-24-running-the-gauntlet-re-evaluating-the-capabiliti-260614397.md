---
title: 'Running the Gauntlet: Re-evaluating the Capabilities of Agents Beyond Familiar
  Environments'
title_zh: 'Running the Gauntlet: Re-evaluating the Capabiliti'
authors:
- Mykola Vysotskyi
- Runqi Lin
- Grzegorz Biziel
- Michal Zakrzewski
- Sebastian Montagna
- Damian Rynczak
- Shreyansh Padarha
- Kumail Alhamoud
- Zihao Fu
- William Lugoloobi
arxiv_id: '2606.14397'
url: https://arxiv.org/abs/2606.14397
pdf_url: https://arxiv.org/pdf/2606.14397
published: '2026-06-24'
collected: '2026-06-27'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: As agentic systems continue to evolve and are widely deployed in real-world
  scenarios, there is...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: huggingface-daily
depth: abstract
---

### 摘要

As agentic systems continue to evolve and are widely deployed in real-world scenarios, there is a growing demand to faithfully evaluate their capabilities. However, current benchmarks are typically built on popular applications with relatively simple tasks and focus on a narrow set of capabilities while overlooking broader dimensions, resulting in saturated performance on modern agents and failing to probe their limitations. To this end, we introduce GauntletBench, a web-based benchmark for evaluating agent generalisation in challenging scenarios, focusing on three underexplored capabilities (temporal perception, graphical understanding, and 3D reasoning), across five less-covered professional applications (Video Editor, Workflow Builder, 3D Modeller, Flight Analyser, and Circuit Designer), each with 20 vision-intensive tasks (100 in total). Our benchmark provides a modular pipeline that comprises an environment compatible with both open- and closed-source agent frameworks, a controlled web-based application, a well-structured task suite, and an automated evaluation engine with diverse metrics. Contrary to widespread expectations, our empirical results reveal that frontier agentic systems remain far from achieving human-level performance. Even the state-of-the-art agent achieves only a 19.1% success rate on our GauntletBench, highlighting the limitations in these overlooked capabilities and generalisation. By comparison, non-expert human annotators achieve over 80% success on our challenging yet feasible tasks, revealing the substantial gap between current agent capabilities and those required for complex real-world scenarios.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
