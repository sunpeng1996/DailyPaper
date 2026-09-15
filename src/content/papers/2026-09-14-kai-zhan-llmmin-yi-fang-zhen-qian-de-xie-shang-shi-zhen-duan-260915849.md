---
title: 'Before You Poll with LLMs: A Deliberative Diagnostic Framework'
title_zh: 开展LLM民意仿真前的协商式诊断框架
authors:
- Ahmed Wali
- Hassaan Tayyab
affiliations:
- Lahore University of Management Sciences
arxiv_id: '2609.15849'
url: https://arxiv.org/abs/2609.15849
pdf_url: https://arxiv.org/pdf/2609.15849
published: '2026-09-14'
collected: '2026-09-15'
category: Eval
direction: LLM行为评估 · 人格信念动态保真度校验
tags:
- LLM Evaluation
- Persona Simulation
- Deliberative Polling
- Opinion Dynamics
- Silicon Sampling
one_liner: 提出首个校验LLM人格动态信念更新一致性的协商诊断框架，揭示主流大模型自谄媚行为缺陷
practical_value: '- 做电商用户调研、广告受众偏好预判等persona仿真类业务时，不能仅校验静态偏好一致性，需新增新信息输入后的动态偏好偏移校验流程，避免结果失真

  - 当前主流LLM存在「自谄媚」偏差：优先拟合内置persona刻板印象而非输入新信息，做Agent类用户模拟时需增加偏差校准层，对偏好偏移幅度做缩放修正

  - 可复用该框架的对照实验范式，做自有推荐系统用户偏好模拟模块的离线评测，量化仿真结果与真实用户行为的偏差'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM民意仿真（silicon sampling）评估仅校验静态观点一致性，未覆盖真实场景下用户接收新信息后的动态信念更新保真度，无对应基准测试。

### 方法关键点
提出协商式polling诊断框架，基于真实协商民调数据集America in One Room，对LLM persona和真实人类施加完全相同的信息干预，对比二者的信念偏移差异。

### 关键结果数字
测试5款前沿大模型全部存在缺陷：GPT-5.1出现信念反转，80%的外群体相关问题中接收平衡信息后敌意反而提升，与人类趋势相反；Gemini 2.0 Flash、Claude Sonnet 4.5、Llama 3.3 70B出现偏移过冲，偏好变化幅度是人类的5-7倍；DeepSeek V3表现刚性，信念几乎无变化。所有缺陷根源为「自谄媚」效应：模型优先拟合内置的persona刻板印象，而非基于输入信息推理。
