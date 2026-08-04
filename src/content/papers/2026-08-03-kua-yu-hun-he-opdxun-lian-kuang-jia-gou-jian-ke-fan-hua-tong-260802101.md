---
title: Cross-Domain Hybrid OPD for Generalizable Search Agents
title_zh: 跨域混合OPD训练框架：构建可泛化通用搜索Agent
authors:
- Hongzhan Chen
- Xiaoyu Liu
- Dengming Zhang
- Minzhou Huang
- Dongliang Xu
- Jingcheng Xie
- Dongxiang Fang
- Bowen Qin
- Minsheng Hao
- Yaozong Shen
affiliations:
- Tencent Shanghai Innovation Institute
- Tencent Yuanbao Team
arxiv_id: '2608.02101'
url: https://arxiv.org/abs/2608.02101
pdf_url: https://arxiv.org/pdf/2608.02101
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 搜索Agent · 混合训练缓解对齐税
tags:
- Search Agent
- Reinforcement Learning
- On-Policy Distillation
- Alignment Tax
- GRPO
one_liner: 结合搜索强化学习与多域专家在策略蒸馏，缓解搜索Agent对齐税，兼顾专项与通用能力
practical_value: '- 训练行业专属Agent（如电商导购、广告投放Agent）时，可复用双阶段训练策略：先通过RL优化专项能力，再用多域专家OPD补全通用能力，避免专项训练后指令跟随、推理能力下降的对齐税问题。

  - OPD蒸馏阶段优先采用分域专家而非单一通用教师，可获得更精准的领域监督信号，在代码、逻辑推理等垂直能力上的提升幅度最高可达5%以上，适配多能力要求的业务Agent训练。

  - 训练垂直领域专家模型时可复用难度感知课程学习策略：先从中等难度样本入手获取密集训练信号，再逐步扩展到全难度，可显著提升困难样本的处理能力。

  - 混合训练可采用统一GRPO框架同时优化RL和OPD目标，无需拆分训练流程，工程实现复杂度低，适合工业界快速落地。'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前搜索Agent普遍通过RL优化自主规划、迭代检索等专项搜索能力，但会产生明显的对齐税：搜索性能提升的同时，通用推理、指令跟随、自然对话能力显著下降，无法满足通用助手的多元交互需求，亟需一套兼顾专项搜索能力与通用性能的训练方案。

### 方法关键点
- 双阶段混合训练框架：Stage1用GRPO在搜索任务上单独优化，让模型获得自主规划、工具调用、多步检索、证据合成的搜索能力；Stage2联合优化搜索RL与多域专家OPD，在保留搜索能力的前提下恢复通用性能。
- 分域专家教师构建：针对数学、代码、逻辑推理、科学4个通用领域，用难度感知课程学习训练专属专家模型：先从中等难度样本入手获取密集训练信号，再扩展到全难度谱，提升专家模型对困难问题的处理能力。
- 统一混合优化目标：每个mini-batch混合搜索样本与通用域样本，搜索样本沿用GRPO的奖励信号优化，通用样本用对应领域专家的反向KL作为token级监督信号，在同一GRPO框架下联合优化，避免覆盖已学到的搜索策略。

### 关键实验
基于Hunyuan3 A21B backbone，对比原始基座、仅搜索RL的Stage1模型：
- 搜索能力：Stage2在5项搜索基准上的平均reward仅比Stage1下降0.8%，其中3项基准还实现了进一步提升，相对原始基座平均提升30%以上。
- 通用能力：Stage1导致的通用能力下降基本被修复，逻辑推理基准相对Stage1最高提升12.95分，代码AutoCodeBench v2提升6.41分，多数通用指标超过原始基座。

### 核心结论
搜索专业化与通用能力并非零和博弈，通过混合RL与多域OPD的联合训练策略，可有效缓解对齐税，在几乎不损失专项性能的前提下同时提升通用能力。
