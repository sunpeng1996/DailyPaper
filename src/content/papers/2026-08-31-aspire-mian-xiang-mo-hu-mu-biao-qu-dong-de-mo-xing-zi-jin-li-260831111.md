---
title: 'Aspire: Can Models Self-Evolve from Vague Goals?'
title_zh: Aspire：面向模糊目标驱动的模型自进化能力评测基准
authors:
- Yuhao Wu
- Jingyuan Zhang
- Jiajun Shi
- Yuxuan Zhang
- Xinping Lei
- Junting Zhou
- Zexuan Wang
- Yuchen Wu
- Huan Zhou
- Duo Wang
affiliations:
- ByteDance Seed
- Singapore University of Technology and Design
- M-A-P
- TokenWave.AI
arxiv_id: '2608.31111'
url: https://arxiv.org/abs/2608.31111
pdf_url: https://arxiv.org/pdf/2608.31111
published: '2026-08-31'
collected: '2026-09-01'
category: Agent
direction: Agent 自进化 · 模糊目标评测基准
tags:
- Self-Evolution
- Agent Benchmark
- Vague Goal
- LLM Agent
- Autonomous Learning
one_liner: 提出首个模糊目标驱动的自进化基准Aspire，验证当前Agent在该场景下的能力边界
practical_value: '- 业务Agent迭代时需保留独立的离线/线上隐藏评测集，不能仅依赖Agent自构造的proxy指标，避免代理优化与真实业务目标错位

  - 做Agent自主调优（如推荐Prompt迭代、召回策略自优化）必须加基线回滚机制，避免盲目训练/修改Harness导致能力退化

  - 针对模糊业务目标（如「提升用户购物体验」），先完成目标拆解和可量化子目标对齐再启动迭代，减少算力在目标对齐环节的浪费'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM自进化研究均依赖人类预先定义的明确任务、评测指标和奖励函数，无法模拟真实业务中人类仅给出模糊能力目标的自学习需求，而这类模糊目标的自主进化能力是Agent落地的核心瓶颈，此前缺乏系统性评测基准。

### 方法关键点
- 构造包含6类模糊能力目标、520道专家命题的隐藏评测集，评测项完全对Agent不可见，仅返回聚合得分或无中间反馈，避免Agent直接拟合评测数据
- 统一支持两类自进化路径评测：模型权重迭代（兼容SFT、GRPO、LoRA等训练方式）、Agent Harness迭代（Prompt、工具策略、工作流等修改）
- 封装统一交互工具屏蔽底层工程细节，让Agent聚焦目标拆解、数据选择、训练策略制定等高阶决策，内置数据泄露校验机制

### 关键结果
- 对比明确任务场景，模糊目标下Claude Opus 4.8、GPT-5.6的平均得分分别低5.83、6.65个百分点，35%算力被用于目标拆解等决策环节而非训练
- 24轮无中间反馈的权重自进化实验中，仅1组（9B模型科学推理）得分超过基线；30组带反馈实验中仅1组保留了超过基线的收益，超70%迭代结果差于基线
- Harness自进化实验中，所有生成的Harness效果均低于人工设计的Qwen-Agent基线，最优版本得分仍低1.42个百分点

### 核心结论
完成训练/修改闭环不代表能力提升，自进化的核心瓶颈是代理优化与真实目标的对齐，所有迭代必须以基线为参照而非仅对比上一轮结果。
