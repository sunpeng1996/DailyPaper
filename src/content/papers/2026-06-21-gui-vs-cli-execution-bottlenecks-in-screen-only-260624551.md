---
title: 'GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use
  Agents'
title_zh: 'GUI vs. CLI: Execution Bottlenecks in Screen-Only'
authors:
- Xiao Zhou
- Siyue Zhang
- Yilun Zhao
- Jinbiao Wei
- Tingyu Song
- Arman Cohan
- Chen Zhao
arxiv_id: '2606.24551'
url: https://arxiv.org/abs/2606.24551
pdf_url: https://arxiv.org/pdf/2606.24551
published: '2026-06-21'
collected: '2026-06-26'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Computer-use agents can execute software tasks through either graphical
  interfaces or programma...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: huggingface-daily
depth: abstract
---

### 摘要

Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. We introduce a matched execution-layer benchmark of 440 desktop tasks across 18 applications and 12 workflow categories, where screen-only GUI agents and skill-mediated CLI agents receive identical goals, states, and final-state verifiers while being restricted to modality-native actions. In this controlled setting, the strongest GUI agent reaches a 59.1% full pass rate, outperforming the strongest original-skill CLI agent at 48.2%; however, verifier-guided skill augmentation raises CLI success to 69.3%, showing that much of the CLI deficit comes from incomplete skill coverage rather than model capability alone. These results suggest that GUI and CLI expose different execution bottlenecks: GUI agents are limited by reliable grounded interaction over long-horizon workflows, whereas CLI agents are limited by the coverage and scalability of their skill interfaces.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
