---
title: 'WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment
  Evolution'
title_zh: WorkRover：基于递归环境演化的长序列协作Agent训练框架
authors:
- Hang He
- Linting Wang
- Guanming Liu
- Bo Mao
- Jinxiu Liu
- Yiran Suo
- Maosen Zhou
- Zhiheng Xi
- Guanting Dong
- Zhou Shao
affiliations:
- Fudan University
- East China Normal University
- Renmin University of China
- Shanghai Qiji Zhifeng Co., Ltd.
- Shanghai Innovation Institute
arxiv_id: '2610.18067'
url: https://arxiv.org/abs/2610.18067
pdf_url: https://arxiv.org/pdf/2610.18067
published: '2026-10-12'
collected: '2026-10-14'
category: Agent
direction: 长序列协作Agent训练框架优化
tags:
- Long-Horizon Agent
- Reinforcement Learning
- Credit Assignment
- Environment Synthesis
- GRPO
one_liner: 提出递归环境演化框架WorkRover，大幅提升长序列协作Agent训练效率与性能
practical_value: '- 训练电商导购、运营自动化等长路径工具调用Agent时，可复用VTCA细粒度信用分配思路：基于业务状态变化、工具调用依赖给每步动作分配正向奖励，无需中间人工标注，解决长序列任务奖励稀疏问题

  - 构建Agent训练仿真环境/任务数据集时，可借鉴FCR最小修复方案：针对上下文、任务、验证器的不匹配问题，做组合级验证选最小改动的修复方案，避免破坏原有任务意图，提升环境复用率

  - 落地行业Agent训练流程时，可复用Harness驱动的对齐机制：同步构建「工作上下文-任务-验证器」并跟踪三者依赖，减少环境组件不一致问题，提升训练奖励信号的可靠性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长horizon协作Agent的RL训练存在两大核心痛点：一是合成训练环境的工作上下文、任务、验证器容易出现语义不匹配，迭代修复时难以保持组件对齐，导致奖励信号不可靠；二是长轨迹奖励稀疏，仅靠终端奖励无法有效区分有用动作与冗余动作，信用分配难度大。
### 方法关键点
- 采用Harness驱动的环境合成框架，联合构建语义对齐的工作上下文、可执行任务、基于证据的验证器，显式跟踪三者依赖，提前校验任务可行性和验证器一致性
- 设计Factorial Compatibility Replay（FCR）算法，针对环境缺陷的修复提案做组合级依赖闭包回放验证，选择满足约束的最小修复方案，避免改动破坏原有任务意图和评价规则
- 提出Verifier-to-Turn Credit Assignment（VTCA）算法，基于工作区状态变化的确定性检查，结合工具输出、工件依赖给前置步骤分配bounded正向奖励，在无需中间Judge的情况下补充细粒度训练信号，优化GRPO更新效果
### 关键结果
基于Qwen3.5-35B-A3B训练的WorkRover-35B-A3B在5个Agent基准集上全面超过基线：JobBench提升26.27pp，OfficeQA Pro提升29.32pp，GDPval v2提升413.25 Elo；FCR相比全量重建将自然缺陷的安全修复率从60.7%提升至70.3%，任务意图改动率从14.3%降至1.3%；VTCA相比仅用终端奖励的GRPO，在所有基准上均有提升，最高增益达5.7pp。
### 核心结论
长horizon Agent训练的性能提升，不仅要优化策略本身，更要同步提升训练环境的可靠性和奖励信号的细粒度程度
