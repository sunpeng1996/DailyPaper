---
title: Does Listening Matter? Backchanneling and Nodding in AI Clone
title_zh: AI克隆中倾听反馈与点头行为对交互真实感的影响研究
authors:
- Koji Inoue
- Kazushi Kato
- Tatsuya Kawahara
- Shunichi Kasahara
affiliations:
- Kyoto University
- Sony Computer Science Laboratories
arxiv_id: '2608.19527'
url: https://arxiv.org/abs/2608.19527
pdf_url: https://arxiv.org/pdf/2608.19527
published: '2026-08-20'
collected: '2026-08-23'
category: Agent
direction: 交互Agent · 多模态行为优化
tags:
- AI Clone
- Multimodal Interaction
- Backchannel
- Nodding
- Co-presence
one_liner: 为AI克隆加入实时驱动的口头反馈、点头倾听行为，显著提升交互真实感与共处感
practical_value: '- 电商数字人客服/导购Agent可新增实时检测用户输入停顿触发的简短口头反馈（如“嗯”“对的”）和点头动效，提升用户感知的服务友好度与停留时长

  - 虚拟数字人直播、AI Clone类个人陪伴Agent的研发团队，可将倾听行为纳入数字人真实度评估体系，而非仅优化话术与音色

  - 多模态交互Agent工程实现中，可采用轻量级实时预测模型驱动反馈行为，无需LLM生成，低延迟下即可获得体验增益'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有AI克隆仅复刻目标人物的说话内容、音色风格，完全忽略倾听阶段的行为表现；而人际交互中倾听反馈是传递注意力、提升共处感的核心要素，相关优化路径此前未被验证。
### 方法关键点
在已集成voice cloning、LLM应答能力的AI克隆系统中，额外加入由实时预测模型驱动的两类倾听行为：口头短反馈（backchannel）、头部点头动作，与用户语音输入做时序对齐。
### 关键结果
35人组内对照实验显示，加入两类倾听行为后，用户对Avatar的感知注意力评分、“与真实人物对话”体感评分、共处感评分均实现统计显著提升，验证了倾听行为对AI克隆真实度的核心增益。
