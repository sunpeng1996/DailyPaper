---
title: 'Decentralized Master-Mind: Joint Action Refinement through Iterative Intent
  Denoising in Multi-Agent Pathfinding'
title_zh: 去中心化Master-Mind：多智能体路径规划的迭代意图去噪联合动作优化
authors:
- Valeriy Vyaltsev
- Anton Andreychuk
- Taisia Zlotnikova
- Konstantin Yakovlev
- Aleksandr Panov
- Alexey Skrynnik
affiliations:
- CogAI Lab, Moscow, Russia
arxiv_id: '2609.32019'
url: https://arxiv.org/abs/2609.32019
pdf_url: https://arxiv.org/pdf/2609.32019
published: '2026-09-24'
collected: '2026-10-03'
category: MultiAgent
direction: 多智体协作 · 分布式路径规划
tags:
- MultiAgent
- PathFinding
- Decentralized
- ReinforcementLearning
- ImitationLearning
one_liner: 提出迭代意图去噪的去中心化多智能体路径规划方法，解决独立采样动作冲突，支持百万级智能体扩展
practical_value: '- 多Agent协同决策场景（如电商投放/选品/定价多Agent配合、广告系统多模块协同）可复用迭代意图细化思路：各Agent先输出初始决策意图，多轮通信对齐后再提交最终动作，避免独立决策产生的全局冲突

  - 无critic的MICPO强化学习方法可直接迁移到分布式多Agent系统微调：通过同初始条件下的多轨迹对比计算优势，无需处理组合爆炸的全局状态，大幅降低多Agent
  RL的落地成本

  - 多轮通信迭代的多Agent系统训练可复用带退火的teacher forcing trick：初期强制对齐专家意图降低训练难度，逐步减少引导提升模型泛化性

  - 在线多Agent服务可复用推理裁剪trick：跳过已完成目标/无决策需求的Agent的计算，在高并发场景下大幅降低算力开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
去中心化多智能体路径规划（MAPF）是仓储物流、自动驾驶等场景的核心问题，现有学习式方案即使引入通信机制，最终独立采样动作的步骤仍会将局部有效选择重组为冲突的联合动作，导致调度成功率低；中心化求解器则存在算力瓶颈，无法扩展到十万级以上智能体规模。

### 方法关键点
- DMM框架将单次动作采样替换为多轮迭代意图细化：智能体初始化随机动作意图，每轮通信交换携带当前意图的消息，逐步协同对齐意图后再提交最终动作，设计思路来自扩散模型的迭代去噪
- 两阶段训练范式：先通过模仿学习预训练拟合专家路径数据，再用无critic的MICPO强化学习方法微调，通过匹配初始意图的同组轨迹对比计算优势，规避中心化critic需处理组合爆炸联合状态的问题
- 训练阶段引入带退火策略的teacher forcing，降低初期意图噪声过大导致的训练不稳定问题
- 推理阶段支持跳过已抵达目标智能体的计算，大幅降低高智能体密度场景的算力开销

### 关键结果
- POGEMA基准测试中，192智能体的仓库场景下DMM-MICPO成功率达100%，优于基线LC-MAPF的93.8%
- 1600个MovingAI任务集上，DMM-MICPO-3M成功求解1598个任务，为所有参评方法最高，求解成本仅比全局虚拟最优解高1.8%
- 可支持104万同时运行的智能体调度，障碍密集场景下目标完成率100%，大幅优于传统PIBT方法

### 核心结论
多智能体协同的核心瓶颈往往不是单智能体的决策精度，而是独立采样带来的联合动作隐式冲突，通过多轮迭代传递未成熟的决策意图实现协同，可在保持去中心化执行的同时大幅提升全局效率
