---
title: Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation
  on Live IOS Apps
title_zh: 面向实时iOS应用UI导航的规划-接地Agent在线稠密强化学习框架
authors:
- Peitong Duan
- Khashayar Gatmiry
- Jeffrey Nichols
- Samy Bengio
- Emmanuel Abbe
affiliations:
- Apple
arxiv_id: '2610.39264'
url: https://arxiv.org/abs/2610.39264
pdf_url: https://arxiv.org/pdf/2610.39264
published: '2026-10-28'
collected: '2026-10-30'
category: Agent
direction: UI导航Agent · 在线RL训练
tags:
- UI-Navigation
- Reinforcement-Learning
- LLM-as-Judge
- PPO
- Online-Training
one_liner: 拆分规划与接地模块，结合LLM-as-Judge稠密奖励与GiGPPO训练8B UI导航Agent性能追平Gemini-3.1-Pro
practical_value: '- 架构拆分trick：将序列决策Agent的低阶确定性能力（如UI坐标匹配、指令转操作）与高阶推理能力（如路径规划、错误恢复）拆分，仅对推理模块做RL训练，可大幅降低训练成本，可直接迁移到电商导购Agent、自动化操作类Agent开发。

  - RL奖励设计复用：采用LLM-as-Judge输出步级稠密过程奖励+终端任务奖励的不对称折扣策略，避免奖励hacking，适合所有长序列决策Agent的训练，比如电商多轮转化优化、长会话追投的RL建模。

  - 算法优化迁移：GiGPPO引入同任务相似状态的邻居奖励信号优化critic稳定性、加速收敛，可直接复用到推荐系统的多步奖励建模、用户长周期价值预估场景。

  - 工程架构复用：基于虚拟机快照快速重置环境的大规模并发交互方案，可支撑需要和真实业务环境交互的Agent规模化在线训练，比如电商平台自动化A/B测试Agent的训练。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有UI导航Agent存在两类落地瓶颈：前沿VLM推理成本高达单任务数美元，无法规模化落地；小模型通过SFT/离线RL训练时容易记忆静态轨迹，泛化性差、错误恢复能力弱，仅用终端奖励的RL又存在训练信号稀疏、收敛速度慢的问题。

### 方法关键点
- 架构解耦：将Agent拆分为规划模块和接地模块，规划模块基于8B VLM，输入任务、截图、历史动作，输出CoT推理+当前步骤+剩余计划；接地模块用SFT训练后冻结，负责将规划指令转为具体屏幕操作坐标，RL仅优化规划模块，大幅降低训练开销。
- 双路奖励设计：用LLM-as-Judge提供两类奖励，步级稠密奖励用Gemini-3.5-Flash评估每步任务进度，惩罚无效循环、幻觉推理、任务完成后的多余操作；终端奖励用Gemini-3.1-Pro评估整体任务完成度，支持验证码、付费墙等不可抗障碍下的部分奖励。
- 训练优化：采用不对称折扣策略，稠密奖励γ=0.5避免Agent刻意拉长轨迹骗取奖励，终端奖励无折扣保证最终目标权重；提出GiGPPO，引入同任务下视觉相似状态的邻居奖励信号优化critic，提升训练稳定性。
- 工程支撑：搭建512并发的iOS虚拟设备集群，通过快照10秒重置环境，支撑大规模在线RL实时交互训练。

### 关键实验结果
在UINavBench、iOSWorld、AndroidWorld三个基准上测试，核心结果：8B PPO模型在真实iOS应用基准UINavBench上成功率32.4%，追平Gemini-3.1-Pro，超越Gemini-3.5-Flash（28.4%）、Qwen3.8-27B（19.6%）；在跨分布Android环境下成功率32.8%，是SFT基线（4.7%）的近7倍；稠密奖励+GiGPPO相比仅终端奖励的PPO收敛速度提升1倍。

### 核心结论
将序列决策任务中的低阶确定性能力与高阶探索性推理能力拆分训练，结合稠密过程奖励的在线RL，是小模型超越大模型零-shot能力、实现低成本落地的可行路径。
