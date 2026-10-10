---
title: Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station
title_zh: 基于多Agent环境Station的开放式科学发现能力验证与优化
authors:
- Wenyu Du
- Stephen Chung
affiliations:
- DualverseAI
- University of Hong Kong
- University of Cambridge
arxiv_id: '2610.08927'
url: https://arxiv.org/abs/2610.08927
pdf_url: https://arxiv.org/pdf/2610.08927
published: '2026-10-05'
collected: '2026-10-10'
category: Agent
direction: 多智能体 · 开放式任务探索机制优化
tags:
- MultiAgent
- OpenEndedExploration
- LLMAgent
- ExplorationMechanism
- ScientificDiscovery
one_liner: 给去中心化多Agent科研环境增加Supervisor与Meta Reflection机制，开放式任务发现率较基线提升超2倍
practical_value: '- 业务开放式探索场景（如新垂类用户兴趣挖掘、广告创意生成、冷启动策略探索）可引入Supervisor机制，要求每个探索方向锁定N轮迭代，禁止中途随意切换，缓解优先做容易任务的街灯效应，提升深度发现概率

  - 定期增加Meta Reflection环节，用统一的强LLM评估当前探索方向是否匹配业务核心目标，淘汰无价值的边缘探索，将资源集中到高价值方向，降低无效探索成本

  - 无明确优化指标的探索任务优先选用去中心化多Agent架构，相比中央控制器分配任务的架构，能覆盖更多探索路径，更容易找到超出预期的高价值策略'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有AI Agent在有明确评价指标的任务上进展快速，但开放式任务（无明确进度反馈、无法直接量化打分）下容易出现判断偏离人类预期、优先选择易解决子问题的「街灯效应」，难以完成高价值的深度探索，这类场景广泛存在于科研、新业务场景探索等领域。

### 方法关键点
- 基于去中心化多Agent环境Station扩展，多个异构Agent独立选择探索方向、开展实验、共享知识，无需中央控制器分配任务
- 新增Supervisor机制：要求Agent提交探索方案后，必须锁定方向至少60个时间步，仅特殊情况允许中途切换，保障探索持续性
- 新增Meta Reflection机制：每50个时间步用通用强LLM引导Agent自我评估方向是否符合人类价值，判断是否要继续深入，对齐探索目标
- 新增Consolidation Agent，最终整合所有Agent的发现输出完整报告

### 关键实验
选取3篇ICLR oral论文的科研问题作为重发现任务，对比Codex Multiagent-v2、AI Scientist-v2等基线，Station平均重发现率达62.7%，较基线最高20.6%提升超2倍；消融实验显示去掉两个机制后，重发现率从75.8%降至57.9%，71.7%的Meta Reflection后Agent会选择深入当前方向；无预设结论的2个探索任务中，Agent的发现与人类后续发表的科研成果高度重合，还提出了新的优化方法。

开放式探索任务中，比起给Agent更强的单模型能力，通过环境机制设计保障探索的持续性、对齐人类价值判断，往往能带来更显著的效果提升。
