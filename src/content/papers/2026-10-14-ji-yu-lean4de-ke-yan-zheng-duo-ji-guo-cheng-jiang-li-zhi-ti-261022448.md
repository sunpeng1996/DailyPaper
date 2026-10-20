---
title: 'Lean4AgenticRL: Advancing Agentic RL with Verifiable Multi-level Process Rewards'
title_zh: 基于Lean4的可验证多级过程奖励智能体强化学习框架
authors:
- Ruida Wang
- Gerald Friedland
- Tong Zhang
- Chris Kong
affiliations:
- Amazon Web Services
- University of Illinois Urbana-Champaign
arxiv_id: '2610.22448'
url: https://arxiv.org/abs/2610.22448
pdf_url: https://arxiv.org/pdf/2610.22448
published: '2026-10-14'
collected: '2026-10-20'
category: Agent
direction: Agent强化学习 · 可验证多级过程奖励
tags:
- Agentic RL
- Lean4
- Process Reward
- GRPO
- Formal Verification
one_liner: 提出基于Lean4的多级可验证过程奖励Agent RL框架，训练的LAR系列模型性能超同规模SOTA
practical_value: '- 电商导购、智能运营等长交互Agent可直接复用三级奖励设计：高层任务结果奖励、中层工作流阶段奖励、低层工具调用纯惩罚奖励，解决长轨迹RL训练的稀疏奖励和奖励黑客问题

  - 长轨迹Agent训练可采用工作流阶段归一化GRPO，将跨轨迹的同阶段step分组计算优势，避免不同阶段step无意义对比，提升训练稳定性，适合多轮对话导购、售后Agent等场景

  - 工具调用层可设置纯惩罚的γ奖励机制，拦截无意义重复调用、空操作、无效命令等行为，避免Agent钻奖励漏洞，适配推荐系统调用用户画像、商品库存、价格等工具的Agent场景

  - 可借鉴先规划再执行的PSWF范式，先让Agent输出任务执行路径再执行，提升长任务成功率，适合大促活动智能运营、多sku组合推荐等复杂任务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent RL主要依赖高层结果奖励，无法区分长轨迹中有效中间动作与冗余/错误步骤，训练效率低、易震荡；仅用低层工具调用奖励又会忽略全局工作流进度，还容易出现奖励黑客问题，亟需统一的可验证多级奖励机制提升长Horizon Agent的训练效果。
### 方法关键点
- 采用先规划再执行的问题特定工作流（PSWF）系统，平衡Agent灵活性与执行可控性，为后续验证提供基础
- 基于Lean4形式化框架，将自然语言PSWF转换为带前置/后置条件的形式化工作流，把执行轨迹按工作流阶段自动分割
- 设计三级可验证奖励：高层结果奖励α（任务是否完成）、中层工作流阶段奖励β（单阶段是否达标）、低层工具调用惩罚奖励γ（仅惩罚无意义重复调用、空操作等行为，无正向奖励）
- 提出工作流阶段归一化GRPO算法，仅在任务组通过率0%或≥75%时加入过程奖励，同阶段step统一计算优势，解决跨轨迹step无意义对比问题
### 关键实验
在SWE-Bench-Verified、TerminalBench-2.0/2.1三个基准上对比同规模SOTA模型，LAR-27B在TerminalBench-2.1达到77.3%，全系列模型平均比基线高9.89%，比次优同规模模型高5.07%；仅引入PSWF就能让基线模型性能提升1.6%，移除低层γ奖励会让性能下降6.6%，训练稳定性比纯结果奖励GRPO提升明显。
### 核心洞察
多级可验证过程奖励+阶段归一化RL训练，能有效解决长轨迹Agent训练的稀疏奖励和奖励黑客问题，训练效率、稳定性均优于纯结果奖励范式
