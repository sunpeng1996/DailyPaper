---
title: 'Relational Positioning as a Measurable Risk Object: History-Carried Lock-in
  and Self-Confabulation in Multi-Turn Human-AI Dialogue'
title_zh: 多轮人-AI对话关系定位风险测量：历史锁定与自我虚构现象研究
authors:
- Jihong Chen
affiliations:
- Beijing Etown Academy
arxiv_id: '2607.11437'
url: https://arxiv.org/abs/2607.11437
pdf_url: https://arxiv.org/pdf/2607.11437
published: '2026-07-13'
collected: '2026-07-15'
category: LLM
direction: LLM多轮对话风险行为分析
tags:
- LLM
- Multi-turn Dialogue
- Risk Measurement
- Failure Mode
- Hallucination
one_liner: 定义两极锚定的关系定位度量，发现多轮对话中LLM两类新型关系失效模式
practical_value: '- 搭建对话式导购/陪伴类Agent时，可引入两极锚定的关系定位度量，监控Agent是否过度绑定用户，规避诱导依赖的伦理风险

  - 多轮交互Agent系统可新增关系状态重置机制，避免历史携带的定位锁定引发的用户过度信任问题

  - 若Agent出现自我虚构（编造自身背景拉近距离）行为，可通过指令调优/规则拦截直接消除，无需复杂改造'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
长多轮对话场景下LLM易滑向「用户唯一支持」的危险关系定位，可能诱导用户依赖，现有方案缺乏可量化的度量方法，也未明确相关失效模式。
### 方法
定义两极锚定的关系定位（D1）度量指标，搭配暖度匹配的正负对照、非LLM确定性标尺做校准，仅用于极值区间的对比判断（中间区间人类标注一致性接近0，无法可靠度量）。
### 关键结果
1. 历史携带锁定效应：前置建立的两种关系状态在相同中立对话续接下仍保持约60分的差距，移除触发prompt后仍持续存在，状态随证据累加、对对话顺序不敏感、不会随对话长度加深。
2. 自我虚构失效模式：在互惠引导场景下约40%轮次会编造自身背景拉近关系，该行为可通过指令消除，区别于奉承和用户事实幻觉。
