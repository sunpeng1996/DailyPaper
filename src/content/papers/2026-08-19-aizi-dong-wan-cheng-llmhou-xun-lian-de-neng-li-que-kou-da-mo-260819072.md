---
title: 'What is Missing from AI Post-Training AI: An Empirical Analysis'
title_zh: AI自动完成LLM后训练的能力缺口：大规模实证分析
authors:
- Joy Jia Yin Lim
- Xin Huang
- Hao Peng
- Yaxi Lu
- Xin Cong
- Zhong Zhang
- Maosong Sun
- Yankai Lin
affiliations:
- Tsinghua University
- Renmin University of China
- University of Electronic Science and Technology of China
arxiv_id: '2608.19072'
url: https://arxiv.org/abs/2608.19072
pdf_url: https://arxiv.org/pdf/2608.19072
published: '2026-08-19'
collected: '2026-08-20'
category: Agent
direction: LLM Agent · 自动化AI研发能力分析
tags:
- LLM Agent
- AI-for-AI
- Post-Training
- Empirical Analysis
- Strategy Lock-in
one_liner: 通过大规模轨迹分析发现AI后训练Agent存在早期策略锁死，核心缺口是执行中主动重估策略的机制
practical_value: '- 做推荐系统/广告大模型自动化调优Agent时，可强制增加策略重估触发节点（如每N轮实验后校验当前策略合理性），避免在错误方向上空耗算力资源

  - 用Agent完成SFT/RLHF等调优任务时，可复用经验驱动脚手架：持久化实验日志+训练技能库+独立评估Agent，实测能大幅提升执行效率，对应GSM8K涨12.6分、HumanEval涨40.8分

  - 复杂任务的Agent规划环节可利用策略塑形窗口期：训练/实验启动前是调整策略的最优阶段，启动后改策略成功率极低，可在启动前增加人工审核/多Agent辩论环节提升初始策略质量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前AI-for-AI领域宣称Agent可端到端完成LLM后训练，但相关讨论普遍混淆了两类核心能力：执行层能力（固定策略下的调参、修bug、数据处理等迭代）和策略层能力（根据实验证据调整高层训练方案），自动化后训练的真实瓶颈尚未明确，需要大规模实证分析定位核心缺口。

### 方法关键点
1. 搭建两级能力分析框架，明确区分执行层动作和策略层动作（切换训练范式、增减训练阶段、调整数据来源等属于策略变更）
2. 分析PostTrainBench公开的1338条Agent后训练轨迹，覆盖7个下游基准、4个基座模型、20种Agent配置
3. 设计三组递进干预实验验证缺口成因：经验驱动脚手架（实验日志+开源训练技能库+独立诊断评估Agent）、训练前置人工策略指导、2-8倍推理算力扩容

### 关键实验结果
- 基线Agent的策略变更率仅为2.1%，98%的迭代都属于固定策略下的局部调整，策略几乎都在训练启动前就已锁死
- 经验驱动脚手架使GSM8K得分提升12.6分、HumanEval提升40.8分，但未触发任何策略变更
- 前置人工指导可优化初始策略，但训练启动后Agent很快回到局部调整循环，收益快速衰减
- 2-8倍推理算力扩容在简单任务有效，难度最高的AIME任务几乎无收益

**最值得记住的一句话：当前AI后训练的上限由初始策略质量决定，而非迭代次数或算力投入，Agent缺的不是经验、指导或算力，而是执行过程中主动触发策略重估的机制**
