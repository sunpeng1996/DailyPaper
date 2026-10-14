---
title: 'TPPO: Tracking-Value PPO For Language Model Reasoning'
title_zh: TPPO：面向大语言模型推理的轨迹价值跟踪PPO算法
authors:
- Futing Wang
- Chenxi Li
- Jianhao Yan
- Yun Luo
- Zhi Wang
- Yizhuo Li
- Runzhe Zhan
- Yu Cheng
- Tao Lin
affiliations:
- Zhejiang University
- Westlake University
- Shanghai AI Laboratory
- The Hong Kong University of Science and Technology
- Nanjing University
arxiv_id: '2610.16794'
url: https://arxiv.org/abs/2610.16794
pdf_url: https://arxiv.org/pdf/2610.16794
published: '2026-10-11'
collected: '2026-10-14'
category: Training
direction: 大模型RL训练 · PPO信用分配优化
tags:
- PPO
- Reinforcement Learning
- Credit Assignment
- LLM Reasoning
- RLVR
one_liner: 通过log-odds空间累积的critic参数化优化PPO信用分配，提升稀疏奖励下LLM推理性能
practical_value: '- 做基于LLM的Agent决策/多轮推理RL训练时，可替换原有PPO的critic为TPPO的累积log-odds参数化结构，仅用终端稀疏奖励就能提升中间步骤信用分配精度，无需额外过程标注

  - 电商场景下用RL优化商品文案生成、搜索query改写的长序列生成任务时，可复用TPPO的BCE损失+累积价值估计方案，缓解长序列下PPO价值估计不准的问题，提升生成效果

  - 工程上TPPO无需额外采样、无额外推理 overhead，仅修改critic的输出头和损失即可落地，可直接适配现有PPO训练框架，迁移成本极低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
标准PPO在LLM长链推理的稀疏终端奖励场景下，critic独立预测每个前缀的价值，无法跟踪推理轨迹上的价值演变，导致token级信用分配错误，价值变化符号预测准确率接近随机，训练中甚至降至45.91%，严重影响RL优化效果。
### 方法关键点
- 推导二进制终端奖励下，连续前缀价值的贝叶斯更新在log-odds空间满足可加性，相邻状态的价值log-odds差值等于token的成败似然比
- 设计TPPO critic结构：每个位置输出一个标量增量，累积求和后过sigmoid得到该前缀的价值估计，而非独立预测每个前缀价值
- 仅用终端二元结果的BCE损失训练，无需额外过程标注、额外采样，生成的价值可直接接入GAE和标准PPO目标函数
### 关键实验结果
- 在数学推理、Countdown、科学编码任务上验证，对比标准PPO：Qwen3-4B-Base数学推理平均准确率提升7.0个点，Qwen3-8B-Base提升8.4个点，Qwen3-4B提升10.1个点；科学编码任务平均提升7.0个点，LiveCodeBench任务提升15.5个点
- 价值演变方向预测准确率比标准PPO高2-7.4个点，优势估计符号准确率提升15.3-19.9个点，训练更稳定，梯度范数更小，熵衰减更慢
### 核心结论
仅通过修改critic的参数化方式为累积log-odds结构，就能在不增加额外成本的前提下大幅提升PPO在稀疏终端奖励长序列任务上的性能
