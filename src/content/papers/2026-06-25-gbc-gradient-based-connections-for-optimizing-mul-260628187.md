---
title: 'GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems'
title_zh: 'GBC: Gradient-Based Connections for Optimizing Mul'
authors:
- Xiaocheng Yang
- Abdulrahman Alrabah
- Dilek Hakkani-Tür
- Gokhan Tur
arxiv_id: '2606.28187'
url: https://arxiv.org/abs/2606.28187
pdf_url: https://arxiv.org/pdf/2606.28187
published: '2026-06-25'
collected: '2026-06-29'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Multi-agent systems (MAS) built on large language models (LLMs) provide
  a promising framework f...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: huggingface-daily
depth: abstract
---

### 摘要

Multi-agent systems (MAS) built on large language models (LLMs) provide a promising framework for solving complex tasks through role specialization and structured interaction. However, their performance is often limited by miscoordination and, more fundamentally, the lack of fine-grained credit assignment across agents. Existing approaches typically rely on coarse-grained feedback, making it difficult to identify which agents or interaction steps are responsible for errors. We propose Gradient-Based Connections (GBC), an approach for fine-grained attribution and optimization of multi-agent systems. GBC models a MAS as a computational graph and introduces gradient-based connection weights to quantify the influence of each agent's output on downstream agents at the token level. By constructing an attribution graph and propagating task-specific loss signals backward, our method enables precise identification of error sources and targeted prompt optimization. We further develop AgentChord, an efficient implementation that leverages prefix-based gradient computation. Experiments on MultiWOZ and τ-bench show that GBC improves multi-agent performance and outperforms strong single-agent and multi-agent baselines, and higher attribution quality is associated with greater optimization effectiveness. Code is available at: https://github.com/yxc-cyber/AgentChord.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
