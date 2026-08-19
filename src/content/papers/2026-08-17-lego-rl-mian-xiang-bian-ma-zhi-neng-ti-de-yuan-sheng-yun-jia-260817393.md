---
title: 'LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents'
title_zh: LEGO-RL：面向编码智能体的原生运行框架强化学习方案
authors:
- Yiming Du
- Yuxin Jiang
- Tao Yuan
- Jianbo Dai
- Shaowei Wang
- Jierun Chen
- Chaofan Tao
- Xianzhi Yu
- Lifeng Shang
- Kam-Fai Wong
affiliations:
- Huawei Technologies Co., Ltd
- The Chinese University of Hong Kong
arxiv_id: '2608.17393'
url: https://arxiv.org/abs/2608.17393
pdf_url: https://arxiv.org/pdf/2608.17393
published: '2026-08-17'
collected: '2026-08-19'
category: Agent
direction: Agent强化学习 · 训练基建优化
tags:
- Agent
- Reinforcement_Learning
- MoE
- Training_Infrastructure
- Reward_Engineering
one_liner: 无需修改编码Agent原生控制流，即可对接可扩展策略梯度优化的RL训练框架
practical_value: '- 做多轮交互Agent（如电商导购、客服、推荐解释Agent）的RL训练时，可复用进程内代理方案，在服务侧直接捕获原始生成序列与路由元数据，避免上层框架改写上下文导致的训练推理不一致

  - 有明确业务验证规则的Agent RL训练可借鉴阶段式沙箱编排+镜像缓存方案，降低环境启动开销，同时加入网络限制、历史隐藏等防御措施防止Reward Hacking，保证奖励信号可信

  - 长周期多轮交互的RL训练可复用异步调度+终止感知过滤的流水线设计，避免长尾任务拖慢训练效率，同时过滤环境失败的无效轨迹，避免污染训练信号'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前编码Agent的RL训练依赖原生执行框架管理工具、上下文和执行反馈，但这类框架的原生环境和策略梯度训练存在天然错位：环境崩溃、Reward Hacking会破坏奖励信号，训练推理不一致导致采样行为和策略更新脱节，现有RL框架要么要求修改Agent原有控制流，要么缺乏可扩展执行、奖励完整性保护和轨迹级诊断能力。

### 方法关键点
- 可信优化：通过进程内LLM代理捕获原始生成流和生成元数据，训练侧重算对数概率，支持MoE模型的采样时路由决策回放，即使上层框架做了上下文压缩、重序列化也能保证对齐
- 可靠执行：可扩展沙箱编排，基于Nydus懒加载镜像缓存、阶段式防御策略缓解Reward Hacking，异步调度避免长尾任务拖慢训练
- 可观测训练：集成自动验证、监控插件和Live UI，支持颗粒度到轨迹的故障诊断

### 关键结果
用GSPO训练Qwen3.5-35B-A3B稀疏MoE模型，在OpenHands SDK、Claude Code、OpenCode三个原生编码Agent框架上测试，SWE-bench Verified指标分别从64.0%提升到70.4%、62.4%提升到68.2%、57.2%提升到66.6%，采样与训练概率相关性保持在0.99以上，异步调度相比同步训练单步速度提升2.5倍。

**最值得记住的一句话**：Agent RL训练的瓶颈往往不在优化算法本身，而在执行环境可靠性、轨迹对齐保真度、反馈机制的适配性上。
