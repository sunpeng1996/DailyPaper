---
title: Minimax PAC Bounds for Learning in Exogenous Contextual MDPs
title_zh: Minimax PAC Bounds for Learning in Exogenous Conte
authors:
- Corentin Pla
- Hugo Richard
- Marc Abeille
- Vianney Perchet
arxiv_id: '2606.25170'
url: https://arxiv.org/abs/2606.25170
pdf_url: https://arxiv.org/pdf/2606.25170
published: '2026-06-23'
collected: '2026-06-27'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: We study PAC learning in tabular discounted Markov decision processes with
  exogenous i.i.d. con...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 摘要

We study PAC learning in tabular discounted Markov decision processes with exogenous i.i.d. contexts, with discount factor $γ$, finite state space $\mathcal X$, action space $\mathcal A$, and context space $\mathcal Z$. At each time step, a context is drawn independently from an unknown distribution $μ$ and revealed before the agent acts. This context may affect both rewards and transitions, while remaining uncontrolled by the agent. Depending on the regime, the learner has access either to a sampling oracle for $μ$, to a sampling oracle for the transition kernel conditioned on state-context-action tuples, or to both. Oracles can be accessed before and during policy execution. The sample complexity is measured by a couple $(n,m)$, where $n$ is the number of calls to the sampling oracles before execution and $m$ is the number of calls to the sampling oracles during execution. When rewards and transitions are known and only the context distribution $μ$ is sampled, we give a variance-reduced algorithm that solves policy evaluation (PE), best-value estimation (BVE), and best-policy extraction (BPE) with $\left(\widetilde O\left(1/((1-γ)^3\varepsilon^2)\right), 0 \right) $ sample complexity. The rate is independent of $|\mathcal Z|$ and minimax optimal up to logarithmic factors. As a corollary, we also obtain tight rates in the case of one-step perfect look-ahead, improving upon the existing guarantees. In the fully unknown regime, where both $μ$ and P must be learned, we show that PE remains $|\mathcal Z|$-free, with matching upper and lower bounds $\bigl(\widetilde O(|\mathcal X|/((1-γ)^3\varepsilon^2)),\, \widetilde O(1/((1-γ)^2\varepsilon^2))\bigr)$.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
