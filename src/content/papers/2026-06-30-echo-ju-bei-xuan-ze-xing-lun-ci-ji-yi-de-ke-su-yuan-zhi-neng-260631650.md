---
title: 'ECHO: Prune to act, trace to learn with selective turn memory in agentic RL'
title_zh: ECHO：具备选择性轮次记忆的可溯源智能体强化学习框架
authors:
- Zijun Xie
- Binbin Zheng
- Enlei Gong
- Jihua Liu
- Yuyang You
- Lingfeng Liu
- Jiayao Tang
- Guanqun Zhao
- Aoqi Hu
- Zeyu Chen
affiliations:
- Peking University
- Baidu Inc.
- University of Science and Technology of China
arxiv_id: '2606.31650'
url: https://arxiv.org/abs/2606.31650
pdf_url: https://arxiv.org/pdf/2606.31650
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: Agent长轮次记忆与信用分配优化
tags:
- LLM Agent
- Reinforcement Learning
- Context Management
- Credit Assignment
- Long-Horizon
one_liner: 提出源索引选择性轮次记忆框架，同时解决长轮次智能体上下文压缩与RL信用分配问题
practical_value: '- 电商导购/搜索任务型Agent可复用「单轮生成带源索引紧凑记忆+策略驱动记忆选择」设计，替代滚动摘要/硬截断，既节省context窗口，又保留关键证据可溯源性，减少冗余交互

  - 多轮交互Agent RL优化可借鉴溯源导向信用分配：仅给最终回答、被选中的历史证据轮次、记忆选择动作分配正奖励，避免冗余轮次被误强化，降低推理成本

  - 跨任务泛化要求高的Agent场景（多品类咨询、多目标搜索）可复用ECHO的记忆-学习对齐设计，训练得到的上下文管理能力无需微调即可迁移，适配稠密和MoE backbone'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长轮次语言智能体的上下文管理通常采用截断、滚动摘要等方法，存在两个核心问题：一是历史信息被压缩/丢弃后，细粒度证据难以复用；二是原始轮次失去源地址性后，基于结果的RL无法把策略更新和支撑成功回答的证据对齐，会导致无效交互轮次暴增、训练效率低、收敛效果差。

### 方法关键点
- 每轮工具交互完成后，生成带源轮次索引的紧凑记忆记录，包含轮次动作、局部结论，所有记忆独立保留源索引，不做全局折叠
- 当上下文超出预算时，由策略从记忆库中选择有用的记忆记录，结合最近交互重构符合窗口限制的上下文，替代全局摘要压缩
- 信用分配时复用选择的源索引，仅给最终回答段、选中的历史源轮次对应token、记忆生成token、记忆选择动作分配正奖励，负向奖励轮次不做溯源分配，避免噪声

### 关键实验
主实验在长轮次工具QA基准BrowseComp-Plus上，基于Qwen3-32B-Instruct backbone，对比GRPO、SUPO基线：ECHO的held-out准确率达43.4%，比GRPO（28.9%）高14.5pct，比SUPO（36.1%）高7.3pct；同时平均轮次比SUPO低27.5%，轨迹量低25.1%。零样本泛化跨多目标QA、代码生成、深度信息检索三类任务，平均准确率达40.2%，优于基线，且增益在稠密和MoE backbone上均一致。

最值得记住的一句话：上下文管理不能只服务于推理时的窗口压缩，还要同时保留源溯源性，为RL训练的信用分配提供路径，才能在提升长轮次性能的同时避免无效交互膨胀。
