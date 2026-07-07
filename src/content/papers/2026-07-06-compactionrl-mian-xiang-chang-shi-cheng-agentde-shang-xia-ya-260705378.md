---
title: 'CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon
  Agents'
title_zh: CompactionRL：面向长时程Agent的上下文压缩强化学习框架
authors:
- Yujiang Li
- Zhenyu Hou
- Yi Jing
- Jie Tang
- Yuxiao Dong
affiliations:
- Tsinghua University
- Z.AI
arxiv_id: '2607.05378'
url: https://arxiv.org/abs/2607.05378
pdf_url: https://arxiv.org/pdf/2607.05378
published: '2026-07-06'
collected: '2026-07-07'
category: Agent
direction: 长时程Agent · 上下文压缩强化学习
tags:
- Reinforcement Learning
- Long-Horizon Agent
- Context Compaction
- PPO
- LLM Agent
one_liner: 提出联合优化任务执行与摘要生成的RL框架，在固定上下文预算下提升长时程Agent性能
practical_value: '- 长时程对话类Agent（如电商导购、售后多轮咨询Agent）可复用该框架的上下文压缩训练逻辑，在不扩容KV cache、不增加推理成本的前提下延长有效交互轮次，避免上下文溢出导致的对话失效。

  - 多轮推荐/搜索场景的用户意图跟踪模块，可借鉴联合优化摘要与执行的思路，将对话历史摘要生成纳入推荐目标的RL训练链路，无需单独设计摘要质量评估指标，直接用最终推荐/转化收益反馈优化摘要策略。

  - 长序列RL训练场景可直接复用token-level loss normalization、跨轨迹GAE两个工程trick，解决分块训练时的长度权重偏差、时序信用分配错误问题，适配变长分段的训练样本。'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长时程LLM Agent的交互轨迹容易超出有限上下文窗口，单纯扩容上下文长度成本高且长序列信息利用率低；现有上下文压缩多为推理端启发式策略，未纳入RL训练链路，无法适配压缩带来的可变分段样本，组式RL方法（如GRPO）也无法处理分块轨迹的优化需求。

### 方法关键点
- 训练时自动触发上下文压缩：当上下文剩余量低于阈值时，由同一策略生成交互历史摘要，重构上下文为「系统提示+摘要+最近k轮交互」后继续任务，完整轨迹拆分为执行段、摘要段两类分段，共享最终任务奖励
- 适配压缩轨迹的RL优化：放弃组式优势估计，改用PPO+价值函数架构；采用token-level loss归一化消除不同分段长度、分段数量带来的权重偏差；设计跨轨迹GAE，根据分段在原轨迹的时序位置对优势进行折扣修正，解决信用分配失真问题
- 无需单独设计摘要质量奖励，直接用最终任务收益反向优化摘要生成策略

### 关键实验
在SWE-bench Verified、Terminal-Bench 2.0两个长时程编码基准测试，对比无压缩RL、基线模型：基于GLM-4.5-Air（106B），SWE-bench Verified Pass@1提升7.0个点至66.8%，Terminal-Bench 2.0提升3.1个点至24.5%；基于GLM-4.7-Flash（30B），两个基准分别提升5.5、6.8个点至56.0%、20.2%。

### 核心结论
上下文压缩不是推理端的旁支优化，而是决定长时程Agent性能上限的核心模块，必须纳入RL训练链路联合优化。
