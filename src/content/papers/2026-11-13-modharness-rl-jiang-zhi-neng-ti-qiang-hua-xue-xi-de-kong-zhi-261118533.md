---
title: 'ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for
  Agentic RL'
title_zh: ModHarness-RL：将智能体强化学习的控制层转化为可学习演进的程序
authors:
- Zelin He
- Siyu Zhu
- Jacob Helwig
- Yujian Liu
- Li An
- Rohit Jain
- Shiyu Chang
- Alborz Geramifard
affiliations:
- The Pennsylvania State University
- LinkedIn
- University of California, Santa Barbara
arxiv_id: '2611.18533'
url: https://arxiv.org/abs/2611.18533
pdf_url: https://arxiv.org/pdf/2611.18533
published: '2026-11-13'
collected: '2026-11-16'
category: Agent
direction: Agent 强化学习 · 可演进控制层优化
tags:
- Agentic_RL
- Harness_Optimization
- Context_Compression
- GRPO
- Program_Synthesis
one_liner: 提出将Agent RL的harness拆分为可学习的压缩与引导程序，随训练动态演进提效
practical_value: '- 电商导购/搜索多轮Agent可复用Compression思路：将用户交互、召回结果拆解为typed block，用离线生成的确定性规则压缩上下文，比实时LLM摘要省100x+调用成本，还能保留KV
  cache复用率，降低推理时延

  - Agent训练引导策略可复用Steering的Replay机制：对历史轨迹跑规则检测，仅对持续存在的失败模式加引导，避免过度干预模型学习，适合电商场景用户行为变化时的动态规则迭代

  - 做Agent RL训练时可直接复用控制层与模型交替更新的架构：先固定压缩规则保证训练上下文稳定，再随训练迭代引导规则，效果优于固定手写harness或同时调整所有组件'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Agentic RL的harness（负责上下文拼接、行为引导的控制层）均为手写固定配置，既需针对任务、模型、上下文预算人工调优，无法规模化落地；也无法适配模型训练过程中行为变化、失败模式动态迭代的特性，成为性能瓶颈。

### 方法关键点
- 将Agent交互记录拆分为带类型的STATE块（推理内容、工具调用参数、工具返回结果等），把harness拆解为两个无LLM调用的可执行程序：Compression（压缩历史保留关键信息，适配上下文预算）、Steering（检测异常行为，追加针对性引导）
- Compression仅在训练前离线拟合1次：从初始策略的rollout轨迹中由LLM生成候选程序，经执行校验、held-out集筛选后固定，保证训练上下文稳定
- Steering随训练动态演进：每轮训练后从新轨迹生成候选引导规则，回放到全量历史轨迹判断失败模式是否持续存在，仅对稳定未解决的失败加引导，经held-out集验证后更新
- 训练流程交替执行策略权重更新和Steering规则更新，保证harness始终匹配当前模型能力

### 关键结果
在CodeSearch、ALFWorld、BIRD SQL三个任务，1.5B~8B模型上验证：
- CodeSearch任务较固定harness baseline提升14~24%，比记忆、技能、prompt演进等最强基线高5~12%
- Compression比实时LLM上下文压缩少100x+模型调用，单步时延从百ms级降至0.3ms以内，上下文充足场景下降低74% prefill token
- 8个测试场景中有7个单独添加Compression或Steering就优于固定harness

### 核心结论
Agent RL的性能瓶颈很大程度上不在模型本身，而在适配模型能力动态变化的控制层设计，用可执行程序替代手写固定规则是低成本提效的有效路径
