---
title: Automating Potential-based Reward Shaping with Vision Language Model Guidance
title_zh: Automating Potential-based Reward Shaping with Vis
authors:
- Henrik Müller
- Daniel Kudenko
arxiv_id: '2606.27180'
url: https://arxiv.org/abs/2606.27180
pdf_url: https://arxiv.org/pdf/2606.27180
published: '2026-06-25'
collected: '2026-06-27'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
- Agent
one_liner: Sparse rewards are inherently challenging for reinforcement learning agents
  as they lack interm...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Sparse rewards are inherently challenging for reinforcement learning agents as they lack intermediate feedback to guide exploration and to correctly attribute the sparse success rewards to relevant parts of the trajectory. Naive reward shaping can induce reward hacking, yielding policies that exploit auxiliary signals instead of solving the intended task. Potential-based reward shaping (PBRS) guarantees preservation of the optimal policy set, but requires the definition of a heuristic potential function over the state space. In this work, we introduce the VLM-guided PBRS framework VLM-PBRS that learns the potential function directly from vision language model (VLM) feedback. We query a lightweight VLM to obtain preferences over image pairs and train a model of the potential function using these preferences. As this approach is based on potential-based reward shaping, it preserves the original optimal policies, and removes the need for expert-designed reward shaping terms. Because large VLMs are prohibitively expensive to invoke repeatedly during policy learning, we employ smaller, more computationally efficient VLMs. Although the resulting preference labels are less accurate, empirical evidence shows that the preference labels can still be used to accelerate learning. We validate our method empirically in the Meta-World and Franka Kitchen environments and highlight the connection between VLM preference label accuracy and sample efficiency improvements. Our contributions are threefold: (1) the first application of VLM preference-based learning to synthesize a potential function for PBRS, (2) a principled, low-cost solution that leverages small VLMs, and (3) extensive empirical demonstration of improved sample efficiency and robustness to reward hacking.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
