---
title: 'PresenceBench: An Exploratory Evaluation of Large Language Model Adaptation
  to User State'
title_zh: PresenceBench：大语言模型用户状态适配能力探索性评估
authors:
- Peña Arroyo Gallego
- Mauro Ruiz Moreno
- Alejandro Acien
- Sergio Romero-Tapiador
- Teresa Arroyo-Gallego
affiliations:
- Area 2 AI Corporation
arxiv_id: '2610.23625'
url: https://arxiv.org/abs/2610.23625
pdf_url: https://arxiv.org/pdf/2610.23625
published: '2026-10-16'
collected: '2026-10-20'
category: Eval
direction: LLM评测 · 用户状态适配能力
tags:
- LLM Evaluation
- User State Adaptation
- Benchmark
- Human Preference
- Context-Aware AI
one_liner: 推出评测LLM适配用户功能状态能力的基准PresenceBench，完成4款主流模型探索性测评
practical_value: '- 做用户状态感知Agent时可复用五臂因果评测设计，区分信号增益vs通用上下文增益，避免伪效果

  - 可将用户状态（如购物决策阶段、浏览沉浸度）转化为响应策略而非直接传原始状态，降低LLM调用token成本

  - 评估状态适配效果时优先采用正确性过滤后的人类成对比较，避免响应正确性干扰适配性判断'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM评估体系缺少对用户功能状态（就绪度、心流、稳定性）适配能力的专项评测框架，无法量化模型是否能有效利用用户状态信号，在保障任务质量与安全的前提下优化响应。
### 方法关键点
推出PresenceBench基准，将适配能力拆解为接收性、特异性两个可测维度，采用五臂因果实验设计，以正确性门控的人类成对比较作为评分标准，覆盖18个单轮、6个固定三轮、6个自然对话场景。
### 关键结果数字
4款主流LLM传入用户状态后人类偏好点估计均>0.5，其中3组95%置信区间排除随机概率；传递策略化状态可降低输出token与调用成本，安全故障占比仅3.6%（13/360）；当前实验未验证特异性，无法区分正确状态增益与通用适配指令增益。
