---
title: Agentic Hardware Design as Repository-Level Code Evolution
title_zh: Agentic Hardware Design as Repository-Level Code E
authors:
- Cunxi Yu
- Chenhui Deng
- Nathaniel Pinckney
- Brucek Khailany
arxiv_id: '2606.28279'
url: https://arxiv.org/abs/2606.28279
pdf_url: https://arxiv.org/pdf/2606.28279
published: '2026-06-26'
collected: '2026-06-29'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: We present HORIZON, a self-evolving agent framework that treats hardware
  design as repository-l...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 摘要

We present HORIZON, a self-evolving agent framework that treats hardware design as repository-level code evolution. A Markdown harness is compiled into a project pack containing domain knowledge, an executable evaluator, an acceptance predicate, and a git/runtime policy; a hands-free agent loop then evolves an isolated git worktree, using repository operations for state management, tracing, and replay. This extends prior works of repository-scale self-evolution from EDA software systems, to hardware-design artifacts themselves. We evaluate our approach on ChipBench, RTLLM, Verilog-Eval, and nine CVDP categories, achieving 100\% benchmark completion across all suites with a fully hands-free agentic loop. However, we do not claim that agentic AI for hardware design is solved: these benchmarks are controlled proxies for a much broader engineering problem in chip design. Section~\ref{sec:discuss} examines the limitations of the current study and highlights open research challenges.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
