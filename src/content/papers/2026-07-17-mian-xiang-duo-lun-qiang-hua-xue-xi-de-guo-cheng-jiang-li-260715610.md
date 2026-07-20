---
title: Process Reward Informed Tree Rollout for Effective Multi-Turn RL
title_zh: 面向多轮强化学习的过程奖励引导树扩展框架
authors:
- Xintong Li
- Sha Li
- Yuwei Zhang
- Changlong Yu
- Rongmei Lin
- Hongye Jin
- Shuyi Guan
- Xin Liu
- Linwei Li
- Qingyu Yin
affiliations:
- UC San Diego
- Amazon
- MIT Alumni
arxiv_id: '2607.15610'
url: https://arxiv.org/abs/2607.15610
pdf_url: https://arxiv.org/pdf/2607.15610
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: 多轮Agent · RL训练采样优化
tags:
- Multi-turn Agent
- RL
- GRPO
- Tree Rollout
- Process Reward Model
one_liner: 提出过程评分引导的自适应树扩展框架，提升多轮LLM Agent RL训练采样效率
practical_value: '- 电商多轮导购Agent、搜索意图纠错Agent的RL训练可复用这套树扩展+提前剪枝逻辑，将采样预算倾斜给有潜力的轨迹，减少无效采样成本

  - 过程评分的三种实现（启发式规则/预训练PRM/分阶段LLM-as-judge）可按需复用，电商场景可基于业务中间指标（如是否命中用户意图、是否触发加购）搭建轻量启发式评分器，无需复杂建模

  - 剪枝后的无效轨迹不要丢弃，全部保留到GRPO训练组作为负样本，可显著提升奖励对比的区分度，该trick可直接落地

  - PATR与标准GRPO完全兼容，无需修改RL优化目标，可无缝接入现有LLM Agent训练管线，改造门槛极低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前GRPO等主流多轮LLM Agent RL方法采用独立完整轨迹采样策略，预算平均分配到所有轨迹，长周期任务下大量算力浪费在无意义的死路轨迹，有潜力的中间状态探索不足，导致优势估计噪声大、训练效率低。
### 方法关键点
- 提出PATR框架，将轨迹组组织为树结构，每K轮用过程评分器评估所有活跃分支：高分分支扩展采样M条子路径，中分分支保留进入下一轮迭代，低分/重复动作分支提前剪枝，子路径共享父前缀算力
- 过程评分器支持三种可灵活切换的实现：任务适配的启发式规则、预训练PRM、分阶段LLM-as-judge，适配不同复杂度的业务场景
- 剪枝轨迹全部保留到训练组，与完成轨迹一起输入标准GRPO进行优化，过程评分仅用于采样资源分配，不修改任务奖励与优化目标，完全兼容现有RL管线
### 关键实验
在FrozenLake导航任务、SWE-Bench编码Agent任务上对比GRPO、ARPO、DAPO等基线，相同训练预算下，FrozenLake任务成功率最高提升+9.3个百分点，SWE-Bench任务解决率最高提升+5.0个百分点，训练收敛速度也显著优于基线。
### 核心结论
过程反馈仅用于采样资源分配、不干预RL优化目标的设计，既大幅提升训练效率又避免引入额外偏置，是该方法可快速落地工业场景的核心优势。
