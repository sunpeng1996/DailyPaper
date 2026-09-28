---
title: 'Compress What You See, Not What You Say: Anchored Context Distillation for
  Latent-Observation Software Engineering Agents'
title_zh: 面向隐观测软件工程Agent的锚定上下文蒸馏方法
authors:
- Zhensheng Zou
- Guoqing Wang
- Dan Hao
affiliations:
- Peking University
arxiv_id: '2609.31430'
url: https://arxiv.org/abs/2609.31430
pdf_url: https://arxiv.org/pdf/2609.31430
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: Agent上下文压缩 · 行为一致性保留
tags:
- Agent
- Context Compression
- Distillation
- LoRA
- Soft Token
- Behavior Alignment
one_liner: 提出LOHA上下文布局+ACD蒸馏方法，大幅压缩Agent上下文同时控制行为漂移
practical_value: '- Agent会话管理可复用LOHA分层存储思路：仅压缩工具/召回返回的观测类内容，保留Agent自身输出、用户指令、最近K条观测的原始文本，平衡压缩率和精确信息需求，适配电商导购Agent、搜索推荐Agent等场景的上下文优化。

  - 适配软token压缩表征时可复用ACD双目标蒸馏范式：跨视图蒸馏让模型读懂压缩表征，自锚定项约束原始文本输入下的行为与基座一致，避免微调后原有能力退化，比单纯LoRA微调更能保留基座效果。

  - 上下文受限/高并发服务场景可直接复用Hard-Last-K超参数策略：K=3时压缩率和性能平衡最优，K=8时优先保障性能，可根据业务 latency 要求灵活选择，不需要重新训练。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent交互过程中工具返回的观测内容（如搜索结果、召回列表、日志）平均占上下文的69%，现有压缩方案要么丢弃关键信息导致后续动作失败，要么适配软token后基座原有行为漂移；同时电商/代码等场景下的工具调用（如商品ID匹配、精确文本替换）需要原始文本支持，现有方案无法兼顾压缩率、信息保留、行为一致性三个核心需求。

### 方法关键点
- LOHA上下文布局：仅将早于最近K条的工具观测压缩为16倍压缩率的软token，系统prompt、用户输入、Agent所有输出、最近K条工具观测保留原始文本，满足精确工具调用的原文需求。
- ACD双目标蒸馏：仅训练Adapter、LoRA阅读补丁、层归一化增益三类参数，冻结基座主体；蒸馏项对齐压缩视图与全文字段的基座预测分布，锚定项约束全文字段下适配后模型与原基座的行为偏差，最小化漂移。
- 推理时K值可灵活调整无需重训，小于128字符的观测始终保留原文不压缩。

### 关键结果
实验在SWE-bench Verified数据集上开展，对比未压缩基座、观测掩码、多种剪枝压缩基线：K=3时Qwen3-4B上下文减少43%，任务解决率12.1% vs 原基座14.5%；SWE-Master-4B-RL上下文减少57%，解决率21.8% vs 原基座27.5%；32K上下文限制下Qwen3解决率21.1% vs 全文本适配版本的11.1%，单GPU并发吞吐量提升1.9倍。

**最值得记住的一句话**：压缩Agent上下文时优先压缩环境返回的观测内容，不要修改Agent自身的输出和最近交互内容，配合自锚定蒸馏避免适配后的行为漂移。
