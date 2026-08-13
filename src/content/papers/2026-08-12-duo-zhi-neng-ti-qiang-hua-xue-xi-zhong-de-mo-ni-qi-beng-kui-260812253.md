---
title: 'One Frozen Simulator Is Not Enough: Simulator Collapse in Multi-Agent RL'
title_zh: 多智能体强化学习中的模拟器崩溃问题及两种互补解决方案
authors:
- Simon Yu
- Nicholas Tomlin
- Marwa Abdulhai
- Ximing Lu
- Derek Chong
- Abe Hou
- Dilara Soylu
- Sergey Levine
- Christopher D. Manning
- Weiyan Shi
affiliations:
- Northeastern University
- New York University
- UC Berkeley
- University of Washington
- Stanford University
arxiv_id: '2608.12253'
url: https://arxiv.org/abs/2608.12253
pdf_url: https://arxiv.org/pdf/2608.12253
published: '2026-08-12'
collected: '2026-08-13'
category: Agent
direction: 多智能体强化学习 · 模拟器泛化优化
tags:
- Multi-Agent RL
- Simulator Collapse
- Verbalized Sampling
- Co-Training
- LLM Simulation
one_liner: 发现单冻结LLM模拟器训练RL的崩溃问题，提出推理与训练端两种解法提升泛化性
practical_value: '- 训练电商客服、导购等多轮交互Agent时，避免只用单个冻结LLM做用户模拟器，否则策略易过拟合到单一回复模式，上线应对真实用户多样性表现极差

  - 推理端可快速接入Verbalized Sampling：让用户模拟器先输出多个带概率的候选回复再采样，无需重训即可提升策略多样性，成本低见效快，适合快速迭代场景

  - 训练端可采用Co-Training范式：同步更新用户模拟器与Agent策略，让训练环境动态演进，避免策略锁定到固定模拟器模式，大幅提升真实用户场景表现

  - 多轮交互Agent RL训练时，将策略熵作为核心监控指标，熵快速下跌大概率是出现模拟器崩溃，需及时调整训练方案'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前多轮交互Agent（客服、导购、协作Agent等）的RL训练普遍依赖单个冻结LLM模拟用户行为，但训练出的策略泛化性极差，上线真实场景后表现大幅跳水。核心原因是对齐后的LLM模拟器本身存在mode collapse，导致策略过拟合到模拟器的主流回复模式，即「模拟器崩溃」，该问题严重阻碍多轮交互Agent落地。

### 方法关键点
- 推理端方案Verbalized Sampling：每轮模拟器回复时，先让LLM输出多个带概率的合理候选回复，再从该分布中采样，无需重训即可拓宽模拟器行为多样性，缓解mode collapse
- 训练端方案Co-Training：将用户模拟器和Agent策略联合优化，模拟器随策略迭代动态更新行为模式，成为动态移动目标，避免策略过拟合到单一固定模式；进阶的Population Co-Training从历史模拟器checkpoint池中采样，进一步提升环境多样性

### 关键结果
在3个多轮交互基准（劝捐基准Persuasion for Good、客服基准τ2-bench、代码协作基准CooperBench）上验证：对比单模拟器RL基线，Verbalized Sampling提升OOD成功率最高9%，Co-Training进一步提升到14%；真实用户测试中，Co-Training的任务成功率比单模拟器RL高62.8%，两种方案的对话自然度均显著优于基线。

最值得记住的一句话：多智能体RL训练中，训练环境的多样性比策略本身的优化更能决定模型上线真实场景的泛化能力。
