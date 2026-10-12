---
title: Inducing Process Supervision from Outcome-Only Reinforcement Learning
title_zh: 基于仅结果强化学习的过程监督诱导框架TIPS
authors:
- Shengda Fan
- Xin Cong
- Zhong Zhang
- Haotian Chen
- Yankai Lin
affiliations:
- Renmin University of China
- Tsinghua University
- University of Electronic Science and Technology of China
- Shanghai Jiao Tong University
arxiv_id: '2609.36641'
url: https://arxiv.org/abs/2609.36641
pdf_url: https://arxiv.org/pdf/2609.36641
published: '2026-09-28'
collected: '2026-10-12'
category: Training
direction: LLM训练 · 过程奖励模型低监督优化
tags:
- PRM
- Reinforcement Learning
- GRPO
- Chain-of-Thought
- Process Supervision
one_liner: 仅用结果标签RL训练生成式PRM，3.2K样本实现超GPT-5.4的过程奖励效果
practical_value: '- 电商Agent/推荐路径审核场景可复用TIPS框架：用最终交易/转化结果标签反哺步骤级错误检测，无需人工标注每一步操作的对错，大幅降低标注成本

  - 训练推荐场景的生成式reward model时，强制模型先输出CoT再给出最终排序/判定结果，用GRPO基于最终业务指标优化，可同时提升结果准确率和中间步骤可解释性，适配归因分析需求

  - 选择PRM训练基座时优先选带Thinking/CoT预训练先验的模型，训练过程中可通过ORM准确率plateau提前停止，避免过程检测能力退化，降低工程试错成本

  - 搜索推荐的query改写、用户路径优化场景可复用outcome-process耦合思路：用最终点击/转化信号反推路径中各节点的有效性，无需人工标注路径节点质量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Process Reward Model (PRM) 是LLM推理、Agent优化的核心组件，可提供细粒度步骤级反馈，但传统训练依赖昂贵的人工步骤标注或高算力成本的Monte Carlo估计，且后者易偏离步骤本身的内在正确性，低代价获取高性能PRM是行业核心痛点。

### 方法关键点
- 提出TIPS框架，基于仅结果RL训练生成式PRM：输入任务和候选轨迹，模型先生成Chain-of-Thought (CoT) 检查中间步骤，再输出各步骤正确性标签和最终结果标签，仅用最终结果是否匹配ground truth作为奖励信号
- 采用GRPO优化，同一条输入的多轮采样结果的组相对优势会作用于生成的所有token（包括CoT、步骤标签、结果标签），无需显式过程标注即可强化步骤级验证能力
- 信息论层面证明：当步骤正确性决定最终结果、且结果判断需要推理时，仅优化结果判断会迫使模型的CoT编码步骤正确性信息

### 关键实验
- 数学推理基准ProcessBench上，仅用3.2K结果标注样本训练的TIPS-Qwen3-4B-Thinking达到85.2 F1，超过72B参数的Qwen2.5-Math-PRM、GPT-5.4-Instruct（79.4 F1）、Claude-4.7-Opus，仅落后o1-mini 2.7个点
- Agent基准AgentProcessBench上，TIPS可将4B Thinking模型的FirstErrAcc平均提升5.4个点，适配Qwen、DeepSeek、Llama等多类基座
- 对比同量级仅结果监督的PRM方法，TIPS效果提升超过30个F1点，数据效率提升超60倍

### 核心结论
当任务的最终结果与中间步骤强耦合时，仅优化最终结果的RL可自动诱导出可靠的步骤级验证能力，无需显式过程标注
