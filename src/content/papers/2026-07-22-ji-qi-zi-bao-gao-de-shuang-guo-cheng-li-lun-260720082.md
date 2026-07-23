---
title: The Two-Process Theory of Machine Self-Report
title_zh: 机器自报告的双过程理论
authors:
- Hubert Plisiecki
- Filip Chmielewski
- Kacper Dudzic
- Anna Sterna
- Karolina Drożdż
- Marcin Moskalewicz
affiliations:
- IDEAS Research Institute
- Faculty of Physics and Applied Informatics, University of Lodz
arxiv_id: '2607.20082'
url: https://arxiv.org/abs/2607.20082
pdf_url: https://arxiv.org/pdf/2607.20082
published: '2026-07-22'
collected: '2026-07-23'
category: Eval
direction: LLM 自报告评估理论构建
tags:
- LLM
- Self-Report
- Psychometrics
- Model Evaluation
- Post-Training
one_liner: 提出首个大模型专属心理测量双过程理论，拆分自报告维度，推出高可靠匹诺曹评估量表
practical_value: '- 大模型Agent自报告一致性校验可复用双维度拆分思路，区分预设人格植入偏差和不安全内容门控偏差，提升Agent交互可靠性

  - 电商客服/导购Agent的对齐训练可参考量表设计逻辑，针对性优化人格表达一致性和敏感内容过滤效果，降低客诉率

  - 大模型效果评估环节可复用匹诺曹量表的高信度设计方法，快速验证不同后训练策略对模型输出倾向的影响，缩短评估周期'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有大模型自报告广泛用于安全评估、公众认知调研等场景，但普遍采用未针对大模型验证的人类问卷或可靠性未知的 ad hoc prompt，缺乏专属理论支撑。
### 方法关键点
1. 提出双过程理论，将自报告拆分为两个独立维度：维度B为人格植入，对应后训练阶段注入的允许表达的温暖、专注等正向内在属性；维度A为归因门控，对应后训练阶段抑制的不安全第一人称表述（模型仍可对他人生成同类内容）
2. 落地为48项匹诺曹量表，具备高信度可复用性
### 关键结果数字
量表信度α=0.82~0.94，跨形式收敛r=0.84，8个月稳定性r=0.93；在206个开源模型、67组同基座/后训练配对模型上验证，62/67组后训练模型B维度提升0.2，后训练模型规模与A维度负相关r=-0.42，基座模型两者无显著相关性
