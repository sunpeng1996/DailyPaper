---
title: 'CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level
  Policy Grafting'
title_zh: CO-GRAFT：基于角色级策略嫁接的搜索Agent强化学习增益归因框架
authors:
- Ramraj Chandradevan
- Sayontan Ghosh
- Vinoth Selvendran
arxiv_id: '2611.31185'
url: https://arxiv.org/abs/2611.31185
pdf_url: https://arxiv.org/pdf/2611.31185
published: '2026-11-23'
collected: '2026-11-24'
category: Agent
direction: 搜索Agent · RL增益归因
tags:
- Search Agent
- Reinforcement Learning
- Attribution
- Shapley Value
- Policy Grafting
one_liner: 提出无权重修改的策略嫁接框架，将搜索Agent的RL增益精确归因到不同功能角色
practical_value: '- 做搜索/推荐Agent RL优化时，无需盲目投入资源优化Query生成，实验显示其增益占比最高不超15%，可优先将算力、奖励设计倾斜到推理、答案提取、搜索决策模块

  - 可复用CO-GRAFT的角色拆分+策略嫁接方法，诊断业务训练的Agent性能增益来源，无需修改权重、无需获取训练reward即可快速定位瓶颈模块，减少无效迭代

  - 中小模型底座的Agent RL训练重点优化推理与决策的耦合增益，大模型/指令微调底座优先优化答案格式合规性与提取准确率，适配不同模型规模的优化优先级

  - 搜索Agent的决策模块经RL训练后大多学到固定任务级搜索次数而非自适应停止逻辑，业务落地时可直接硬编码最优搜索次数，无需浪费算力让RL学习决策逻辑'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RL训练可将搜索Agent的Exact Match（EM）指标最高提升32个点，但传统端到端评估无法定位增益具体来自哪个功能模块，也无法识别多模块耦合效应，导致RL优化方向盲目，缺乏轻量化的归因工具。

### 方法关键点
- 把搜索Agent的轨迹拆分为4个互斥功能角色：中间推理（R）、搜/答决策（D）、搜索Query生成（Q）、最终答案提取（A）
- 实现CO-GRAFT框架，让RL训练后模型与预训练基线分别控制不同角色组合，在带实时检索的闭环环境下生成轨迹，无需修改模型权重、无需重新训练
- 遍历所有16种角色分配组合，用Shapley值将总增益拆分到单个角色，用Möbius交互项识别多角色的耦合增益

### 关键结果
在NQ、HotpotQA数据集上测试Qwen2.5、Llama-3.2系列共8组模型，覆盖GRPO、PPO两种优化器，base/指令微调两种底座：
1. Query生成的增益占比始终≤15%，不是RL增益的核心来源
2. 大模型/指令微调底座的增益更多来自答案提取（A），占比最高可达46%，小base模型的增益主要来自R与D的耦合效应
3. 决策模块的增益几乎都来自学到固定任务级搜索次数，而非自适应停止逻辑

**最值得记住的一句话**：搜索Agent RL训练的核心增益几乎不来自Query生成，优先优化推理、答案提取和固定搜索预算，投入产出比更高
