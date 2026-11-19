---
title: 'Depth Before Breadth: Reverse-to-Forward Curriculum with Advantage Decomposition
  for LLM Agent'
title_zh: 先深后宽：面向LLM Agent的反向到正向课程与优势分解方法
authors:
- Siyuan Du
- Yuxin Liu
- Meng Tang
- Haoran Li
- Yechao Bai
- Feiyang Pan
- Jia He
affiliations:
- Nanjing University
- Peking University
- University of Wales, Aberystwyth
arxiv_id: '2611.24697'
url: https://arxiv.org/abs/2611.24697
pdf_url: https://arxiv.org/pdf/2611.24697
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: LLM Agent 长序列任务RL训练优化
tags:
- LLM Agent
- Reinforcement Learning
- Curriculum Learning
- Credit Assignment
- Long Horizon
- GRPO
one_liner: 提出配对优势分解与反向转正向训练课程，解决长序列LLM Agent稀疏奖励下的信用分配难题
practical_value: '- 电商导购Agent、多轮搜索交互Agent的RL训练可复用反向到正向课程框架：先从靠近转化目标的短路径（如加购→下单）学起，再逐步倒推到商品搜索、query理解等上游环节，降低长交互任务的学习门槛

  - 信用分配的配对优势分解trick可直接迁移：无需额外标注过程奖励，将交互轨迹拆为前缀（进入可解区域）和后缀（完成任务）分别计算优势，大幅提升稀疏奖励下的信号利用率

  - 工程上可复用端点去重+多后缀采样设计：相同交互端点复用后缀采样结果，减少不必要的环境交互次数，相比传统GRPO降低训练成本

  - 针对现有GRPO训练容易陷入winner-takes-all、探索不足的问题，该方法可有效提升高价值交互端点的覆盖度，增强Agent在非参考路径下的泛化能力'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长 horizon LLM Agent 已广泛应用于多轮交互、工具调用场景，RL是主流训练范式，但稀疏终端奖励导致信用分配难、探索效率低。传统反向课程训练仅锚定参考轨迹，泛化性差，且长轨迹下奖励分配仍然粗糙，无法有效区分不同阶段动作的贡献。

### 方法关键点
- 定义policy-induced capability region：当前策略能以高于阈值概率完成任务的状态集合，将长序列任务拆为「进入可解区域」和「从可解区域完成任务」两个低难度子问题
- 提出Paired Advantage（PA）分解：将轨迹拆为前缀、后缀，前缀按交互端点分组，每个端点采样多个后缀，左优势评估前缀进入高价值端点的贡献，右优势评估后缀从端点完成任务的贡献
- 设计反向→正向两阶段课程：反向阶段沿成功参考轨迹从近目标点向后扩展可解区域，直到原始起点进入可解区域；正向阶段从原始起点采样前缀，扩展可解区域到参考轨迹外的探索状态

### 关键实验结果
在ALFWorld、WebShop两个长序列Agent基准上测试，base模型为Qwen2.5-1.5B/7B-Instruct，对比GRPO、GiGPO等SOTA RL方法：ALFWorld上1.5B/7B版本成功率分别达90.1%/96.1%，超GRPO 17.3/18.5个百分点；WebShop上1.5B/7B版本成功率分别达80.2%/82.6%，超之前SOTA CRPS 19.2/8.6个百分点，相同环境交互预算下成功率显著高于基线。

### 核心结论
仅用终端奖励训练长序列Agent时，先锚定近目标区域建立可靠能力边界，再逐步向外扩展，配合分层信用分配，效果远好于直接端到端训练
