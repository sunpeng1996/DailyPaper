---
title: Instruction-Tuned Models Locally Reuse Human Syntax More Than Humans Do
title_zh: 指令微调大模型对人类对话语法的复用程度高于人类自身
authors:
- Zandi Eberstadt
affiliations:
- Department of Computer Science, University of Oxford
arxiv_id: '2607.26015'
url: https://arxiv.org/abs/2607.26015
pdf_url: https://arxiv.org/pdf/2607.26015
published: '2026-07-28'
collected: '2026-07-30'
category: LLM
direction: 大模型对话语法收敛特性量化分析
tags:
- Instruction Tuning
- Syntactic Convergence
- LLM Evaluation
- Dialogue Generation
- CFG Rule
one_liner: 对比16款Llama与Gemma模型，量化验证指令微调模型的人类对话语法复用度高于人类基准
practical_value: '- 对话式导购/智能客服场景可利用指令微调模型高语法复用特性，优化回复的用户适配性，降低对话违和感

  - 生成式推荐话术（商品评价、push文案、客服回复）可引入CFG规则复用度指标，提升生成内容的语境匹配度

  - 强上下文一致性需求的对话场景（如售后跟进）可针对性调整模型微调策略，降低无关上下文的语法复用干扰'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
人机对话中人类存在无意识复用对方语法的语法收敛特性，但大模型是否存在同类特性、不同训练范式下的表现差异尚未被系统量化。
### 方法关键点
采用对话替换范式：用模型生成内容替换已有人类对话中的某一方发言，在1901个匹配对话位置上，测量16款参数覆盖1B-70B的Llama、Gemma模型对前序人类发言的CFG规则复用率，对比人类基准、预训练与指令微调模型的表现差异。
### 关键结果
所有模型对前序人类发言的CFG规则重合度均高于无关人类发言，低频规则的复用差异更显著；8组同架构配对中，指令微调后对实际前序发言的语法重合度均高于预训练版本，且高于被替换的人类回复；相比预训练版本，指令微调模型对无关上下文的语法重合度更高、实际-随机重合度增量更低，控制规则集大小后条件复用概率更低；所有模型的词汇、语义相似度均高于人类回复，指令微调模型的语义相似度更高。
