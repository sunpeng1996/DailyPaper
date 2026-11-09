---
title: Adaptive Scheduling Pipeline for Multi-Instance Asynchronous Reinforcement
  Learning
title_zh: 多实例异步大模型强化学习的自适应调度流水线ASP
authors:
- Salah Chikhi
- Luis Zuin
- Entong Li
- Zeng Li
affiliations:
- École polytechnique
- Huawei Technologies
- Shenzhen Research Institute of Big Data
arxiv_id: '2611.08864'
url: https://arxiv.org/abs/2611.08864
pdf_url: https://arxiv.org/pdf/2611.08864
published: '2026-11-06'
collected: '2026-11-09'
category: Training
direction: 大模型RL训练 · 多实例异步调度优化
tags:
- ReinforcementLearning
- LLMTraining
- Scheduling
- AsynchronousPipeline
- RolloutOptimization
one_liner: 通过离线预调度同时解决三类rollout空泡问题，大模型RL训练端到端吞吐量最高提3.22倍
practical_value: '- 做LLM批量推理（如推荐批量文案生成、Agent批量工具调用）时，可复用ASP的长度同构minibatch构造方法：先预测输出长度，动态组装长度接近的prompt到同一batch，实测padding率可从0.32降至0.22，推理吞吐量提升约20%

  - 多实例异步生成+训练pipeline（如RL优化推荐排序策略、Agent对齐训练），可增加batch-group重排序步骤：用模拟退火打散长短minibatch为负载均衡的分组，避免队列波动导致的训练端空等，实测能将batch组负载变异系数从0.4降至0.07，迭代时间再降5%以上

  - 用GRPO做RLHF/RL对齐时，只要控制策略滞后在3个训练步以内，收敛效果与同步训练无明显差异，无需额外复杂的离策略修正，可大幅降低工程复杂度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大模型RL后训练（RLHF、GRPO等）中，rollout生成阶段通常是核心瓶颈，现有多实例异步RL架构存在三类资源浪费：单batch内输出长度差异导致的padding空泡、长尾输出导致的skewness空泡、按长度排序调度导致样本到达速率波动的sorting空泡，共同导致资源利用率低、训练迭代慢，甚至出现扩展瓶颈。

### 方法关键点
- 三步离线预调度：1）用小样本微调小模型预测每个prompt的输出长度，仅需粗粒度排序准确即可；2）用动态规划构造长度同构的minibatch，允许batch size在小范围内浮动，最小化padding率；3）用模拟退火将minibatch重排序为负载均衡的batch组，平滑训练队列的样本到达速率
- 配套异步架构：解耦生成单元(GU)和训练单元(TU)，通过控制队列深度+每训练步刷新权重，把策略滞后控制在可观测范围内，适配GRPO等对离策略容忍度较高的算法

### 关键实验
在DEEPSCALER数学推理、MAZE迷宫推理数据集上，对比MindSpeed-RL、verl两个主流RL框架，在Qwen3 MoE/稠密模型上测试：1）端到端吞吐量相对MindSpeed-RL最高提3.22倍，迭代时间降76.8%；相对verl迭代时间降62.5%；2）仅调度模块就能让同架构下迭代时间降10.9%，batch组负载变异系数降82.5%；3）策略滞后控制在3.3训练步时，收敛效果与同步训练无明显差异。

最值得记住的结论：多实例异步生成的调度不能只优化单batch利用率，还要同时平衡全局样本到达的稳定性，离线预调度可在几乎无在线开销的前提下同时解决三类空泡问题。
