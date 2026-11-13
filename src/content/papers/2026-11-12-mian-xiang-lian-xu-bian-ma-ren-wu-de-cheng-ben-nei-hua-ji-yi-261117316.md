---
title: 'CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective
  Valuation'
title_zh: 面向连续编码任务的成本内化记忆框架CoReMem：前瞻估值方法
authors:
- Peiwen Li
- Harshit Verma
- Sophia Zhou
- Haiwen Wang
- Ngoc Bui
- Heng Chang
- Fei Fei
- David van Dijk
- Rex Ying
affiliations:
- Yale University
- Tsinghua University
- Goodvision AI
arxiv_id: '2611.17316'
url: https://arxiv.org/abs/2611.17316
pdf_url: https://arxiv.org/pdf/2611.17316
published: '2026-11-12'
collected: '2026-11-13'
category: Agent
direction: Agent 长时记忆优化 · 连续任务
tags:
- AgentMemory
- ReinforcementLearning
- LongHorizonTask
- LLMAgent
- SuccessiveTask
one_liner: 提出带前瞻估值的成本内化记忆框架CoReMem，降低连续编码Agent处理未来未知任务的开销
practical_value: '- 记忆设计可复用前瞻估值方案：无需存储全量历史，通过对比「有无该记忆段的未来任务表现」筛选高价值锚点，可直接迁移到电商用户跨会话记忆构建场景，仅保留能降低下次召回/排序成本的用户行为锚点（如明确点击的品类、评价过的商品属性），大幅降低记忆存储和读取开销

  - Agent RL训练可复用溯源门控价值分配逻辑：仅给明确用到记忆的步骤分配记忆带来的价值增益，其他步骤仅分配任务本身的结果奖励，可解决推荐/导购Agent盲目依赖历史记忆、忽略当前实时需求的问题，提升记忆有效使用率

  - 奖励设计可复用成本内化思路：优先保证任务成功率，仅在成功完成的任务中惩罚步骤数/Token开销，避免为了降低成本损害核心业务指标，可直接用到电商导购Agent、文案生成Agent的优化中'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有编码Agent记忆方案未适配「同一共享状态下连续未知任务、状态随任务演进继承」的场景：要么仅服务单任务、要么跨独立任务迁移通用经验，无法平衡记忆的存储读取成本和未来任务收益，甚至会增加总Token消耗；同时现有方案仅优化记忆存储/检索逻辑，不调整Agent的记忆使用策略，无法在任务执行过程中动态高效利用记忆。

### 方法关键点
- **前瞻段估值**：对比同一历史状态下，有无某段轨迹记忆的未来任务表现，计算每段轨迹的价值，仅保留能降低未来任务步骤的高价值片段作为锚点（仓库位置、可执行检查命令），最终记忆仅占全量轨迹的6%字节，可保留全部步骤收益
- **成本内化On-Policy估值**：训练时每组rollout混合带对应记忆、无记忆、带错位记忆三种会话，奖励优先保证任务解决率，仅在成功任务中扣减步骤数成本，自动计算记忆的实际价值
- **溯源门控价值分配**：仅给明确用到记忆锚点的步骤分配记忆带来的价值增益，其他步骤仅分配任务本身的结果奖励，避免Agent盲目依赖无关记忆

### 关键实验结果
在ChainSWE连续编码任务基准上：CoReMem将27B base模型的任务解决率从21.0%提升到25.7%，步骤减少17%，总cache感知Token减少11%；跨3种不同规模开源Actor模型，平均每千Token解决率提升41%。

### 最值得记住的一句话
跨连续任务的记忆价值只能通过未来未知任务的实际收益衡量，而非生成记忆的当前任务效果。
