---
title: 'EVIDENT: Evaluating Evidence Grounding in GUI Agents'
title_zh: EVIDENT：GUI智能体证据归因能力评估基准
authors:
- Yerin Nam
- Minkyung Cho
- MinKyu Kim
- SeungWoo Song
- Hangyeol Yoo
- Jihyo Kim
- KyungTae Lim
affiliations:
- Korea Advanced Institute of Science & Technology
arxiv_id: '2611.20488'
url: https://arxiv.org/abs/2611.20488
pdf_url: https://arxiv.org/pdf/2611.20488
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: GUI Agent 证据归因评估
tags:
- GUI Agent
- Evaluation Benchmark
- Evidence Grounding
- Hallucination
- Multimodal LLM
one_liner: 提出GUI智能体证据归因评估基准，通过三层指标区分表面成功与有真实证据支撑的可靠回答
practical_value: '- 电商导购/商品咨询Agent的评估可直接复用三层指标体系：将TSR替换为用户问题回答准确率，ESR对应是否采集到商品价格、库存、参数、活动规则等必要证据，GSR对应回答内容是否完全匹配采集到的证据，可有效识别「瞎编商品属性、报错价格」的幻觉问题

  - 多步交互Agent的自动评估pipeline可参考分阶段方案：先从交互轨迹中抽所有可见证据，再做声明-证据匹配，比直接将全轨迹扔给LLM判分的准确率提升17pct以上，同时降低判分成本

  - 对于高事实准确性要求的Agent场景，可添加强制校验规则：回答涉及实时/站点专属信息（价格、库存、活动、站点规则）时，必须引用轨迹中采集到的明文/视觉证据，禁止直接输出模型参数知识，从生成环节减少幻觉'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有GUI Agent评估仅考核任务最终完成状态，无法识别「回答看似合理、实则依赖模型参数知识而非导航过程中观察到的网页真实证据」的隐藏幻觉，这类失败在电商商品信息查询、政务办事、行程规划等高事实准确性要求的场景会直接造成用户损失，当前行业缺乏可量化这类风险的评估标准。
### 方法关键点
- 构建220个英韩双语真实Web任务，覆盖语义匹配、隐式约束推理、视觉证据归因三类核心用户意图与网页信息的gap，每个任务配人工标注的证据元数据，明确必须核实的核心信息点，不绑定固定导航路径，适配不同交互策略
- 提出三层递进评估指标：TSR（表面任务成功率）仅考核回答合理性，ESR（证据采集成功率）额外要求Agent观察到所有必要证据，GSR（归因成功率）进一步要求回答的所有核心声明均有观察到的证据支撑
- 设计分阶段证据感知评估pipeline：先从轨迹截图抽取所有可见文本/视觉证据，再做任务要求、回答声明与证据的映射匹配，最后完成判分，避免直接处理长轨迹的判分误差
### 关键实验结果
- 测试6个主流闭源/开源GUI Agent，闭源模型表现显著占优，最强Gemini CUA英文任务TSR达87.14%，但GSR仅55.71%，两者差距达31.43pct；开源模型最高英文GSR仅45.71%，韩文任务GSR普遍低于10%
- 上下文推理、视觉归因类任务的GSR比语义匹配类低20-40pct，是幻觉重灾区
- 证据抽取前置步骤可将LLM判分与人类标注的一致性从58%~72%提升至89%~97%
### 核心结论
GUI Agent的表面任务成功率是其可靠性能的上限，仅靠结果评估会严重高估实际可用性，必须增加证据采集和归因校验环节
