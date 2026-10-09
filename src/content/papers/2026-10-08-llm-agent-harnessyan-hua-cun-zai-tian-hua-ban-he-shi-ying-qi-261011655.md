---
title: 'Harness Evolution Hits a Ceiling: When Weight Training Should Begin'
title_zh: LLM Agent Harness演化存在天花板：何时应启动权重训练
authors:
- Yuan Tian
- Bing Hu
- Hao Wang
- Binghang Lu
- Fang Wu
affiliations:
- Independent Researcher
- University of California, Berkeley
- Purdue University
- Stanford University
arxiv_id: '2610.11655'
url: https://arxiv.org/abs/2610.11655
pdf_url: https://arxiv.org/pdf/2610.11655
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: LLM Agent优化 · 失败驱动分阶段干预
tags:
- LLM Agent
- Harness Evolution
- LoRA
- Failure Analysis
- Trajectory Fine-tuning
one_liner: 提出基于Agent失败类型的诊断干预规则，明确Harness演化与权重训练的适用边界
practical_value: '- 做Agent优化前先做失败归因：将失败分为流程类（循环、调用阻塞、步数耗尽）和内容类（输出质量差），流程类优先迭代Harness（提示、工具、记忆逻辑），内容类再做权重微调，避免上来就微调浪费成本

  - Harness迭代优先投入能力型组件（状态账本、经验库、自定义工具），比合规型组件（退出门、检查点、硬拦截）增益大得多，无需过度投入强制校验逻辑

  - 判断Harness增益是否可沉淀到权重：看修改的是模型输出行为（如输出格式、工具调用逻辑）还是输入（如扩容上下文页数），改输出行为的可以用LoRA训到权重里，改输入的无法迁移，不用白费功夫训练

  - 评估前先校准噪声阈值：比如4次rollout下差异超过0.035才是真实增益，避免把噪声当成优化效果做无效迭代'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长周期LLM Agent优化通常有Harness（环绕模型的提示、工具、记忆、工作流等）迭代和权重微调两个方向，但两者适用边界模糊，迭代效果容易被噪声干扰，无法判断增益来源和可迁移性，导致优化成本高、效率低。

### 方法关键点
- 自动失败归因分类：将轨迹失败分为4类，F1证据不足、F2Harness本身阻塞、F3执行控制问题（循环、步数耗尽）为流程类失败，F4内容质量差为内容类失败
- 分阶段干预流程：先运行Harness自演化循环（LLM提案Harness修改、校验器验证效果）解决流程类失败，再基于演化后高质量轨迹做LoRA/全参数微调解决内容类失败
- 噪声校准测量协议：先确定单轮rollout噪声标准差，4次rollout下差异≥0.035才判定为有效增益，每次迭代后重测基准锚点消除选择偏差

### 关键结果
- 在DeepPlanning规划基准上，Harness自演化将Qwen3.5-4B held-out得分从0.16提升到0.30，Qwen3.5-9B从0.32提升到0.44，流程类失败占比下降30%-50%
- 基于演化轨迹训练的LoRA适配器在seed Harness下额外提分+0.13，4B模型两者叠加得分翻倍，9B模型单独LoRA即可匹配Harness演化最优效果，内容类失败从25%降至5%
- 在WebArena-Lite导航基准上Harness演化提分+0.09，因增益来自输入上下文扩容，无法迁移到模型权重

### 核心结论
流程类失败靠Harness演化解决，内容类失败靠权重训练解决；Harness增益如果来自修改模型输出行为可通过LoRA内化到权重，来自修改模型输入的则只能保留在Harness中
