---
title: 'HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific
  Visualization'
title_zh: 'HiLSVA: Design and Evaluation of a Human-in-the-Lo'
authors:
- Kuangshi Ai
- Patrick Phuoc Do
- Chaoli Wang
arxiv_id: '2606.26614'
url: https://arxiv.org/abs/2606.26614
pdf_url: https://arxiv.org/pdf/2606.26614
published: '2026-06-25'
collected: '2026-06-26'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Large language model (LLM) agents enable natural language interaction for
  scientific visualizat...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.HC
depth: abstract
---

### 摘要

Large language model (LLM) agents enable natural language interaction for scientific visualization (SciVis). Still, prior systems have essentially prioritized autonomy over human analytical control, thereby limiting transparency and human oversight. We present HiLSVA, a human-in-the-loop agentic system that supports mixed-initiative SciVis workflows. HiLSVA integrates a plan-first multi-agent architecture with explicit human oversight, stepwise provenance tracking, and learn-at-test-time adaptation from user feedback. The system supports fluid handoff between humans and agents through both natural language and direct manipulation of visualizations, while sandboxed execution ensures safe, reproducible workflows. In doing so, HiLSVA reframes agentic SciVis as a collaborative process that augments, rather than replaces, human analytical reasoning. We evaluate HiLSVA through representative case studies and a controlled user study with twelve participants of varying expertise across multiple autonomy settings. Results show that mixed-initiative interaction improves task completion, user control, and workflow transparency across different levels of user expertise, while revealing a tradeoff between execution efficiency and human oversight. These findings highlight the importance of human-centered design in agentic SciVis and guide the development of future collaborative visualization systems. We encourage readers to explore our demo video, case studies, and source code at https://hilsva.github.io/.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
