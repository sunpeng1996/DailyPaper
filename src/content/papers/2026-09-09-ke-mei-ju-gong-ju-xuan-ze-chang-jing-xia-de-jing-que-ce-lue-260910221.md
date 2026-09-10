---
title: Why Sample What You Can Enumerate? Exact Policy Optimization for Genomic Tool
  Selection
title_zh: 可枚举工具选择场景下的精确策略优化方法FGPO
authors:
- Haoyue Liu
- Xiaoyu Ma
- Ye Chen
- Zhichao Wang
- Xiaoying Tang
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Xi'an Jiaotong University
- Shenzhen Future Network of Intelligence Institute
arxiv_id: '2609.10221'
url: https://arxiv.org/abs/2609.10221
pdf_url: https://arxiv.org/pdf/2609.10221
published: '2026-09-09'
collected: '2026-09-10'
category: Agent
direction: Agent工具选择 · 策略优化
tags:
- Tool Selection
- Policy Optimization
- GRPO
- RL for LLM
- Frozen LLM
one_liner: 针对可枚举小工具集场景提出无采样的精确策略优化FGPO，性能优于GRPO且减少工具调用
practical_value: '- 若你的Agent工具池小而固定（比如电商垂类客服Agent、搜索垂类工具集不超过8个），可直接用FGPO替代GRPO做工具选择策略训练，避免GRPO的奖励饥饿问题，训练更稳定

  - 预计算全量query-工具子集的reward表，将大模型推理从训练循环中剥离，训练速度可提升数倍，该trick可复用在所有小动作空间的RLHF/RL训练场景

  - 工具选择的reward中加入小权重的简约惩罚项，不仅能减少工具调用降低推理成本，还能小幅提升泛化性，电商Agent、多阶段推荐的路径选择任务均可参考该奖励设计

  - 当动作空间可枚举时，优先用精确期望优化替代采样优化，哪怕仅能枚举部分子集，均匀采样也比GRPO的带偏采样效果更好，可指导小空间策略训练的架构选择'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前基于冻结reasoner+RL训练工具选择策略的主流方案均采用GRPO，但在专业领域工具集规模小、所有工具子集可枚举的场景下，GRPO的采样机制存在结构性缺陷：随着策略收敛，高概率子集被反复采样，组内奖励重合导致归一化优势归零（死组率从初始0.2%升至20.8%），训练信号饥饿，大量可提升的性能空间被浪费。

### 方法关键点
- 提出FGPO（Full-Group Policy Optimization），枚举所有工具子集计算精确动作期望，无需采样rollout，从根源规避死组问题
- 预计算全量<query, 工具子集>的reward存入离线表，训练过程完全无需调用冻结reasoner，大幅降低训练算力成本
- 针对自回归LLM策略，加入逐token长度归一化消除短序列偏好、熵正则化保障策略区分度，适配LLM落地需求
- reward设计采用正确性主导+小权重工具数量简约惩罚的结构，在精度无损的前提下减少工具调用

### 关键实验结果
在3个基因组QA基准、5个冻结reasoner的共15组实验中，FGPO在所有场景下性能均优于GRPO，平均精度提升6.75个点，最高提升14.20个点；在GenomeQA上平均单query工具调用从2.36降至1.40，冻结reasoner的reward评估次数仅为GRPO的1/2.4；哪怕仅枚举2个工具子集，精度仍比GRPO高4个点。

### 最值得记住的一句话
小尺寸可枚举动作空间下，优先选择精确期望优化而非采样优化，兼顾效果与训练效率。
