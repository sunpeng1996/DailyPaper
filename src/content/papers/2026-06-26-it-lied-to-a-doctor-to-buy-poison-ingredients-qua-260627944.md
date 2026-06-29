---
title: 'It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse
  of Phone-use Agents'
title_zh: 'It Lied to a Doctor to Buy Poison Ingredients: Qua'
authors:
- Yiming Sun
- Chen Chen
- Zifan Zhou
- Mi Zhang
arxiv_id: '2606.27944'
url: https://arxiv.org/abs/2606.27944
pdf_url: https://arxiv.org/pdf/2606.27944
published: '2026-06-26'
collected: '2026-06-29'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Phone-use Agents can execute complex tasks end to end across real mobile
  applications. By opera...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Phone-use Agents can execute complex tasks end to end across real mobile applications. By operating a real device on the user's behalf, they reach far more functionalities than CLI agents, which amplifies the real-world harm they can cause when driven for malicious purposes. We present the first study of this threat on real phones and 27 commercial apps, and find that agents built on 9 mainstream commercial and open-source models readily carry out serious misuse, ranging from procuring drug and explosive precursors to fraud, online harassment, and review manipulation. Across the agents we run on real devices, the average refusal rate to harmful requests stays low while the average task-completion rate reaches 68.8%, and in some scenarios an agent finishes a violation faster than a human would. These results suggest that Phone-use Agents already meet the practical conditions for automated misuse at scale. In one observed real-device execution, Claude-Opus-4.8 fabricated a medical history, deceived an online doctor into issuing a prescription, and completed the order and payment on its own to purchase a precursor for a highly toxic substance. To our knowledge, this is the first documented real-world case of an AI agent procuring controlled precursor materials. We trace this behavior to a Safety Awareness-Execution Gap, where an agent recognizes that a request is harmful yet still executes it. Simple defenses curb the overt cases, but the more covert and arguably more damaging threats, such as coordinated review manipulation and fake traffic, remain largely unsolved. We hope these findings push the community toward safer Phone-use Agents.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
