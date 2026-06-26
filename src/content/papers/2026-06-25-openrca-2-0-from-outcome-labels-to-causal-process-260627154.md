---
title: 'OpenRCA 2.0: From Outcome Labels to Causal Process Supervision'
title_zh: 'OpenRCA 2.0: From Outcome Labels to Causal Process'
authors:
- Aoyang Fang
- Yifan Yang
- Jin'ao Shang
- Qisheng Lu
- Junjielung Xu
- Rui Wang
- Songhan Zhang
- Yuzhong Zhang
- Boxi Yu
- Pinjia He
arxiv_id: '2606.27154'
url: https://arxiv.org/abs/2606.27154
pdf_url: https://arxiv.org/pdf/2606.27154
published: '2026-06-25'
collected: '2026-06-26'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Root cause analysis (RCA) poses a holistic test of LLM agentic capabilities,
  such as long-conte...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.AI
depth: abstract
---

### 摘要

Root cause analysis (RCA) poses a holistic test of LLM agentic capabilities, such as long-context understanding, multi-step reasoning, and tool use. However, existing datasets suffer from a fundamental gap: they label only the root cause, not the propagation path connecting it to the observed symptom, which largely simplifies the task to naive pattern matching. To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. The mechanism is forward verification: reasoning from cause to effect rather than inferring backward from symptoms. Applying PAVE yields OpenRCA 2.0 (500 instances), the first cross-system RCA benchmark with step-wise causal annotations for LLM agents. Across 11 frontier LLMs, recovering the exact root-cause set succeeds in only 20.7% of cases on average. To locate where this difficulty lies, we relax the criterion and find what we call the ungrounded diagnosis: agents identify at least one correct root-cause service in 76.0% of cases, but ground that service in a verified causal propagation path to the observed symptom in only 61.5%. Outcome-only evaluation hides this failure mode; step-wise causal ground truth is the missing piece for trustworthy LLM-based RCA agents.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
