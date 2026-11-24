---
title: Self-Upgrading Embodied Agents
title_zh: 自升级具身Agent：无需梯度无需外部模型的在役权重自更新
authors:
- Jiajun Fan
- Neil He
- Qinglong Zheng
- Changyi Yang
- Tong Wei
- Andy Mao
- Zetian Li
- Chaoran Cheng
- Hui Ren
- Ruihan Guo
affiliations:
- UIUC
- CMU
- Brown
- Stanford
- Northeastern
arxiv_id: '2611.31117'
url: https://arxiv.org/abs/2611.31117
pdf_url: https://arxiv.org/pdf/2611.31117
published: '2026-11-23'
collected: '2026-11-24'
category: Agent
direction: 具身Agent · 终身持续自学习
tags:
- EmbodiedAgent
- SelfImprovement
- WeightEditing
- ContinualLearning
- NoGradient
one_liner: 首个仅用前向传播在任务间隙自更新权重的27B具身Agent，实现稳定持续自我提升
practical_value: '- 可复用自升级安全校验框架：先在内部小流量任务上做新旧版本paired测试，仅当预定义核心指标达标、且预留验证集泛化性达标才上线变更，避免新版本回滚风险，适配推荐/广告系统的模型迭代场景

  - 故障根因定位思路可迁移：从业务badcase日志中定位核心问题（比如大模型推荐生成的文案冗余导致token溢出），通过隐空间方向识别+单张量秩1更新修复，比全量SFT成本低90%以上

  - 低overhead持续优化范式：将模型优化与在线推理解耦，闲时（比如电商低峰期）用日志做模型修复，无需额外推理阶段外挂prompt/RAG，不影响线上响应延迟与资源消耗'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前基于LLM的具身Agent/业务大模型权重部署后即冻结，要提升效果要么依赖额外训练（需要梯度、奖励模型、人工标注），要么依赖推理阶段外挂prompt/reflection/RAG，每步都有额外开销，任务切换后优化失效，无法实现低成本终身持续学习。

### 方法关键点
- 设计昼夜双阶段自升级循环：白天用当前权重执行任务，夜间基于当日执行日志做自诊断，定位核心故障模式
- 无梯度权重编辑：通过前向传播读取隐层状态，定位故障对应的隐空间方向，对单张量做秩1更新，无需梯度、无需外部模型、无需标注数据
- 多重安全校验：编辑后先做新旧版本同任务同种子paired测试，再在完全未见过的预留任务集上做验证，仅当核心故障指标显著下降、任务完成率不下降才保留更新，否则回滚，避免模型退化

### 关键实验
用Qwen3.5-27B在ALFWorld household任务上测试，baseline为原权重版本；升级后任务完成率从41.6%提升到45.2%，无动作浪费步骤占比从45.9%降到39.5%，单轮episode token消耗从15.1k降到13.9k，优化效果多轮稳定不退化；仅27B规模模型可完成自升级，更小模型（2B/4B/9B）均无法找到有效更新。

### 最值得记住的一句话
自升级系统的核心不是怎么改权重，而是怎么保证改了之后只会变好不会变坏，安全校验比编辑能力更重要
