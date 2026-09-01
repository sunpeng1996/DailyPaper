---
title: 'Call Neighbours Yourself: Graph Walks with Destination-Conditioned On-Policy
  Self-Distillation'
title_zh: 主动调用邻居：基于目标条件同策略自蒸馏的图游走推理框架
authors:
- Yilun Liu
- Boyu Luo
- Yanran Tang
- Ruihong Qiu
- Zi Huang
affiliations:
- The University of Queensland
arxiv_id: '2608.29588'
url: https://arxiv.org/abs/2608.29588
pdf_url: https://arxiv.org/pdf/2608.29588
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: Agent 文本属性图推理优化
tags:
- Text-Attributed Graph
- Reinforcement Learning
- Self-Distillation
- LLM Agent
- Graph Reasoning
one_liner: 让LLM主动在文本属性图中游走选择证据邻居，无需标注生成动作级训练信号
practical_value: '- 电商商品同购网络、用户行为图均为典型TAG，可复用CNY主动游走逻辑替代固定k跳邻居聚合，在用户兴趣探索、商品关联召回场景下减少无效上下文占用，降低token成本同时提升关联准确率

  - OPSD无标注动作信用分配方法可直接迁移到电商导购Agent、检索Agent的RL训练，无需标注中间决策轨迹即可给检索、跳转等动作分配奖励，大幅降低训练标注成本

  - 分层奖励设计可复用：按「任务正确>动作格式合法>有效探索>完成回答」设置优先级，解决RL冷启动阶段无正样本导致的学习信号缺失问题，训练收敛更稳定

  - 动态上下文选择逻辑比固定RAG省6倍以上token，适合大促、流量高峰等算力受限场景，在不扩容算力的前提下提升推理效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM基于文本属性图（TAG）推理时，普遍预先生成固定邻居上下文，稠密图中邻居规模常超出上下文窗口，无关邻居容易淹没关键证据；且强化学习训练邻居选择策略时，仅能获得最终结果奖励，缺乏步级标注导致信用分配困难，策略泛化性差。

### 方法关键点
- 提出CNY框架，将邻居选择建模为LLM的主动<walk>动作：初始仅暴露邻居短预览（标题/文本前缀），LLM自主决定是否展开查看邻居全文，游走受拓扑约束只能访问相邻节点
- 设计分层奖励机制，优先级为「预测正确>动作格式合法>有效获取证据>完成回答」，冷启动阶段也能获得有效学习信号，避免策略崩溃
- 提出目标条件同策略自蒸馏（OPSD）：走完邻居后，同一LLM分别用无邻居结果的原始上下文、带邻居摘要的上下文对walk动作重打分，概率差作为动作级信用，无需外部标注或额外rollout
- 基于GRPO优化，OPSD信用仅作用于walk动作对应的token，不影响推理路径的训练效果

### 关键结果
在引文、电商同购、知识图谱等8个TAG数据集上训练，零样本迁移到5个未见过的数据集：14B版本CNY较之前最优基线Graph-R1在所有任务上准确率领先2~5pp，跨图级任务Expla-Graph准确率达92.6%，超基线2.9pp；WikiCS场景下较同参数RAG准确率更高，token消耗低6.3倍；零样本迁移到WebQSP多跳KGQA任务，Hits@1达58.4%，较使用全1跳上下文的方案高9.4pp。

### 核心结论
图推理的效果不止取决于对已有证据的解读，更取决于推理过程中自适应获取高价值证据的能力。
