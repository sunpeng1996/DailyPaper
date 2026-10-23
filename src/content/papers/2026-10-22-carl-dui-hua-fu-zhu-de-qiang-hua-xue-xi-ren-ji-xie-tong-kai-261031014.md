---
title: 'CARL: Chat Assisted Reinforcement Learning'
title_zh: CARL：对话辅助的强化学习人机协同开发框架
authors:
- Sanjiv Das
- Harshad Khadilkar
- Sukrit Mittal
- Daniel Ostrov
- Jacob Sisk
affiliations:
- Santa Clara University
- Franklin Templeton
arxiv_id: '2610.31014'
url: https://arxiv.org/abs/2610.31014
pdf_url: https://arxiv.org/pdf/2610.31014
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent 人机协同强化学习开发
tags:
- Reinforcement Learning
- Human-in-the-loop
- LLM Agent
- Specification Engineering
- Code Generation
one_liner: 提出结构化10步人机协同RL开发流程，弥合RL落地的规格定义与性能优化缺口
practical_value: '- 可复用「先交互式规格对齐，后自动化执行」的Agent架构，搭建电商/广告场景的RL策略开发工具：在动态出价、个性化推荐等场景的RL落地流程中，先通过结构化问询对齐业务约束、reward定义、状态空间，再生成训练代码，大幅降低业务人员使用RL的门槛

  - 可复用「单步skill文件+决策摘要记忆」的上下文管理机制：适配电商场景下多轮需求确认的Agent开发，比如运营活动选品、push文案生成的需求对齐流程，每步仅输出紧凑摘要供后续步骤消费，既降低token开销，又避免长会话上下文混乱

  - Trillian预填回复的设计可复用在人机协作工具中：提前生成符合业务惯例的默认选项，减少用户输入成本，比如RL调参时自动推荐适合广告出价、商品推荐场景的默认超参数，用户仅需调整差异项即可'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有RL落地失败大多源于两类缺口：一是规格缺口，业务专家的领域意图无法精准转化为正式的MDP定义、reward函数、约束条件；二是性能缺口，业务专家无法验证RL方案有效性，超参数或reward权重配置不当。通用代码生成Agent直接生成RL代码时，常出现reward hacking、状态混叠、偏离业务需求等问题，即使代码无bug也无法产出可行策略，RL落地周期通常长达数月。
### 方法关键点
- 拆分10步结构化工作流：前7步为交互式规格对齐阶段，按顺序完成问题定义、参考文献收集、参数探索、状态/动作/reward定义、超参数确认，每步绑定专属skill文件约束对话边界，避免跨阶段逻辑混淆；后3步为自动化执行阶段，自动生成代码、测试、训练，最终支持迭代优化的重访步骤。
- 引入Trillian辅助persona，基于领域知识预填每步的默认回复选项，用户可接受/编辑/拒绝，降低非RL专业的业务专家交互成本；每步完成后仅输出紧凑决策摘要作为后续步骤的上下文，避免全量会话导致的上下文过载。
- 明确权责边界：规格对齐阶段由业务专家掌握决策权，MDP定义完全确认后再进入自动化代码生成与训练阶段，避免出现「正确实现错误MDP」的无效工作。
### 关键结果
跨两个差异极大的路径依赖优化领域验证：金融目标导向财富管理、航空航天动压约束火箭控制，通用全自主代码生成方案全部失败，CARL可稳定产出可行策略；在最优停止基准任务上，生成的RL策略达到99.93%的理论最优性能。
### 核心结论
RL落地的核心瓶颈不是算法能力，而是模糊业务意图到形式化RL定义的转化效率，人机协同的结构化规格工程是破解该瓶颈的核心路径。
