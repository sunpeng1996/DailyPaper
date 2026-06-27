---
title: 'Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge
  Collaboration'
title_zh: 'Knowledge-Based Pull Requests: A Trusted Workflow'
authors:
- Xinyu Zhang
- Weiwei Sun
arxiv_id: '2606.26721'
url: https://arxiv.org/abs/2606.26721
pdf_url: https://arxiv.org/pdf/2606.26721
published: '2026-06-25'
collected: '2026-06-27'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: 'AI coding agents are changing the bottleneck in software collaboration:
  code is increasingly ch...'
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 摘要

AI coding agents are changing the bottleneck in software collaboration: code is increasingly cheap, while understanding intent, negotiating scope, and governing long-term project responsibility remain costly. This paper proposes \emph{Knowledge-Based Pull Requests} (KPR), a trusted workflow for agent-mediated software collaboration across trust boundaries, including open source, enterprise, vendor, contractor, and customer-driven settings. In KPR, an external collaborator's local code, tests, and cleaned agent interaction trace are treated as knowledge sources rather than as the default merge candidate. Agents distill these sources into a human-confirmed knowledge package and render it into reviewer-facing forms such as design memos, risk checklists, test plans, or implementation briefs. A project-owned inner trusted coding agent then regenerates candidate code inside the receiving project's environment under repository context, engineering conventions, tests, and security policy. KPR therefore separates two decisions that traditional pull requests often collapse: whether the knowledge should enter the project, and whether a particular implementation should be merged. We contribute the KPR workflow, a candidate artifact schema, a cost-accounting view, a collaboration gateway architecture, a minimal controlled simulation pilot over seven merged public pull requests, and an evaluation agenda. The pilot shows that KPR packages can be instantiated from real PR material and stress-tested under description ablation, diff ablation, and synthetic poisoned-patch conditions. We position KPR as an empirically testable workflow: its value depends on whether auditable extraction, transformation, and project-side regeneration reduce the cost of understanding and reworking high-context external changes.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
