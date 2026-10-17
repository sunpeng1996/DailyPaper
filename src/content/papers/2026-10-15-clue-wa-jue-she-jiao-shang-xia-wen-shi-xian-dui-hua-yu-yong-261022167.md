---
title: 'CLUE: Uncovering Social Context for Pragmatic Understanding'
title_zh: CLUE：挖掘社交上下文实现对话语用理解
authors:
- Chengfei Wu
- Zhaoqing Wu
- Dan Goldwasser
affiliations:
- Purdue University
arxiv_id: '2610.22167'
url: https://arxiv.org/abs/2610.22167
pdf_url: https://arxiv.org/pdf/2610.22167
published: '2026-10-15'
collected: '2026-10-17'
category: Training
direction: 大模型训练 · 对话语用理解优化
tags:
- GRPO
- LoRA
- Reinforcement Learning
- Conversational Understanding
- Pragmatic Reasoning
one_liner: 提出两阶段训练框架CLUE，结合证据监督与IUG奖励优化GRPO，提升对话语用理解效果与推理效率
practical_value: '- 电商客服Agent、用户评论情感分析、社交内容审核场景可复用两阶段训练思路：先SFT让模型学会引用原始文本作为证据，再通过GRPO加自定义奖励优化判断准确率，不需要大量标注数据

  - IUG奖励设计可直接迁移到RAG问答、Agent推理的事实性优化：奖励新增的、有证据支撑的有效推论，同时惩罚冗余推理token，同时提升输出可信度和推理速度，降低部署成本

  - 低资源跨场景适配可参考其泛化思路：仅用单语言少量对话数据训练，即可实现跨语言、跨任务的效果提升，适合小语种市场、新兴业务场景的模型快速微调'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有对话理解模型难以定位长交互中的有效上下文线索，依赖额外注入的社交/文化知识才能提升语用判断效果，且推理过程冗余、跨场景泛化能力弱，需要让模型自主从对话中挖掘支撑判断的有效上下文，同时兼顾效果和推理效率。

### 方法关键点
- 两阶段训练：第一阶段用带证据标注的推理轨迹做SFT，新增`<evidence>`特殊标记引用对话原文，仅用LoRA微调，冻结其他参数；第二阶段用GRPO做RL优化，结合任务正确率、IUG奖励、证据格式三个奖励项
- 提出Grounded Information Utilization（IUG）奖励：用大模型作为裁判，判断推理块是否输出了新增的、有证据支撑的有效推论，同时核算推理成本，对超过预算的冗余token做惩罚，鼓励简洁的有依据推理
- 奖励权重设计保证正确答案优先级始终高于部分正确的答案，避免模型为了拿推理奖励牺牲正确率

### 关键结果
基于Qwen3.5-9B训练，仅用CCU中文2568条对话微调，测试覆盖情感识别、对话行为识别等8个任务，对比base Qwen：域内平均加权F1相对提升17.3%，域外提升9.3%，平均推理token减少80%以上，5个域外任务中4个F1更高，同时MMLU得分不降反升，无灾难性遗忘。

### 核心结论
让模型学会主动定位并引用上下文证据，再通过可验证的奖励强化这种能力，能同时提升效果、泛化性和推理效率，远好于仅优化最终预测正确率的训练方式。
