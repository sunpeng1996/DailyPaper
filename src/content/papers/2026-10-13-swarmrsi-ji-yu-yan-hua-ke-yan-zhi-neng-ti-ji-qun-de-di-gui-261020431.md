---
title: 'SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm'
title_zh: SwarmRSI：基于演化科研智能体集群的递归自我改进框架
authors:
- Qianru Meng
- Xi Zhang
- Konstantinos Papakostas
- Congfeng Cao
- Wenxiang Hu
- Tianyi Lu
- Xiao Zhang
- Lun Zhou
- Zaiqiao Meng
- Zhaochun Ren
affiliations:
- Huawei Technologies Co., Ltd.
- Leiden University
- University of Groningen
arxiv_id: '2610.20431'
url: https://arxiv.org/abs/2610.20431
pdf_url: https://arxiv.org/pdf/2610.20431
published: '2026-10-13'
collected: '2026-10-15'
category: MultiAgent
direction: 多智体协作 · 递归自我改进
tags:
- MultiAgent
- RecursiveSelfImprovement
- AgentSwarm
- EvolutionaryComputation
- LLMAgent
one_liner: 提出融合三类演化机制的科研Agent集群递归自改进框架，在多基准达SOTA
practical_value: '- 可复用反馈引导的H/P突变机制：在推荐多Agent迭代优化（如召回/排序策略迭代）中，区分假设（如「用户长兴趣权重更高」）和实现（如特征工程、模型结构）的失败归因，避免错杀有效假设

  - 互补重组的rebase/crossover操作：在多版本推荐策略迭代中，跨策略复用有效组件（如A策略的召回规则+B策略的排序Loss），哪怕原策略整体效果未提升

  - 共享状态图+UCB自适应调度机制：多Agent协作场景下，用共享图存储所有迭代历史（含失败尝试），用UCB动态分配「探索新假设/优化现有实现」的算力，提升迭代效率

  - 继承态迁移思路：同领域多任务下，预积累的迭代历史可冷启动新任务，比如电商多品类推荐的策略经验可直接迁移到新品类，提升冷启动效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有科研Agent集群的递归自改进面临两个核心痛点：1）实验失败无法区分是假设错误还是实现缺陷，导致有效假设被废弃；2）整体效果未提升的程序中隐藏的有效组件被忽略，无法跨Agent复用，限制了集群的迭代效率。

### 方法关键点
- Feedback-Guided Swarm Mutation：基于跨Agent的实验反馈，区分H-mutation（修改研究假设）和P-mutation（仅修复代码实现），避免错杀有效假设
- Complementary Swarm Recombination：通过rebase（保留假设复用其他Agent的有效实现）、crossover（跨程序融合互补优势组件）两种操作复用局部有效结果，哪怕原程序整体无增益
- Recursive Swarm Evolution：所有实验结果（含失败、无增益结果）存入共享研究状态图，用带需求压力的折扣UCB动态调度「假设探索/实现优化」的资源，迭代更新后续Agent的初始状态

### 关键实验结果
在OpenProblems（6个单细胞分析任务）、NatureBench（90个跨领域科研编码任务）、MLE-Bench Lite（22个机器学习竞赛任务）上测试，对比AIDE、Arbor、TusoAI等基线：
1. 用Gemini 3.1 Pro Preview时，OpenProblems平均得分76.2，达到SOTA
2. NatureBench上Match-SOTA率达44.4%，为所有对比方法最高；77%的最优程序来自rebase、crossover或反馈驱动的更新
3. MLE-Bench Lite上Any-Medal率达81.8%，优于同backbone的单假设/单程序演化Agent

### 核心结论
多Agent协作迭代的核心价值不是并行加速，而是通过跨个体的失败归因、局部组件复用，把所有尝试（哪怕是失败的）都变成后续迭代的有效资产
