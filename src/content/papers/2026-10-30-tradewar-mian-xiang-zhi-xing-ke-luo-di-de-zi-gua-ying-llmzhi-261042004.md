---
title: 'TradeWar: A Benchmark for Execution-Grounded Trade Negotiation with Adaptive
  LLM Agents'
title_zh: TradeWar：面向执行可落地的自适应LLM智能体贸易谈判基准
authors:
- Xiangyu Kong
- Ruirui Yang
- Xia Hou
affiliations:
- 北京信息科技大学计算机学院
arxiv_id: '2610.42004'
url: https://arxiv.org/abs/2610.42004
pdf_url: https://arxiv.org/pdf/2610.42004
published: '2026-10-30'
collected: '2026-11-02'
category: MultiAgent
direction: 多智能体 · LLM谈判基准与自适应策略
tags:
- LLM Agent
- Multi-Agent Negotiation
- Benchmark
- Self-Adaptation
- Execution Grounded
one_liner: 提出覆盖谈判-执行-反馈全链路的贸易谈判基准TradeWar，及无需微调的自适应谈判Agent TACTIC
practical_value: '- 电商供需撮合、广告资源谈判、商家议价类Agent任务，不要仅把对话达成率作为核心指标，需将条款落地后的真实业务收益作为评估标准，规避表面达成但实际无价值的陷阱

  - 多轮交互类Agent无需反复微调基座LLM，可通过外挂执行落地后的经验记忆、对手画像、结构化反思模块实现跨轮次策略迭代，既降低迭代成本也避免通用能力遗忘

  - 带业务约束的动态决策任务（如大促资源分配、供应链动态调度），可在LLM生成决策后加一层规则校验模块，提前拦截不符合约束、无法落地的策略，提升执行效率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM谈判类基准大多仅评估协议达成率，忽略了自然语言承诺落地为可执行策略后的实际价值，也未考虑执行环节的约束、网络耦合效应和延迟反馈，导致高达成率的谈判可能最终无实际收益甚至带来负向效果，无法支撑高 stakes 场景下的谈判Agent研发。

### 方法关键点
- 提出TradeWar基准：模拟多国贸易谈判场景，将自然语言谈判内容映射为关税、贸易份额等可执行政策，引入产能、贸易网络约束的结算环节，最终用经济健康指数（EHI）评估谈判的真实价值，覆盖「谈判→执行→反馈」全链路
- 提出TACTIC智能体：无需微调基座LLM，通过四大模块实现跨轮次迭代：①经验记忆存储谈判条款与落地后的真实收益；②对手建模维护对手信任度、履约能力画像；③结构化反思从延迟反馈中提炼策略优化点；④边界规划生成符合约束的谈判策略

### 关键实验
基座采用GPT-4o-mini，对比零-shot CoT的PromptLLM、仅保留单轮内记忆的MemoryLLM等基线：
1. PromptLLM达成率达75%但最终EHI仅57.1，TACTIC达成率85%，EHI达68.8
2. 20轮连续交互后，TACTIC EHI从58.2提升至73.2，比无跨轮次更新的 ablation 高8分
3. 技术管制、能源危机冲击场景下，TACTIC性能降幅比PromptLLM低15-17个百分点

**最值得记住的一句话**：谈判类任务中，协议达成率是非常差的最终价值代理指标，必须打通从自然语言交互到执行落地、价值反馈的全链路才能评估真实效果。
