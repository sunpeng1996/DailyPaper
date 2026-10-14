---
title: 'SkillScaffold: Scaffolding Agentic Reinforcement Learning with Policy-Adaptive
  Skill Credit Assignment and Selective Injection'
title_zh: SkillScaffold：面向Agent强化学习的策略自适应技能训练框架
authors:
- Wenlin Zhong
- Hao Wang
- Kun Yuan
- Fan Yang
- Jinluan Yang
- Dian Jin
- Xu Tan
- Yiquan Wu
- Kun Kuang
affiliations:
- Zhejiang University
- University of the Chinese Academy of Sciences
- Kuaishou Technology
- Zhejiang University of Science and Technology
arxiv_id: '2610.18807'
url: https://arxiv.org/abs/2610.18807
pdf_url: https://arxiv.org/pdf/2610.18807
published: '2026-10-13'
collected: '2026-10-14'
category: Agent
direction: Agent强化学习 · 技能辅助训练
tags:
- AgenticRL
- SkillInjection
- CreditAssignment
- GRPO
- LLM4Agent
one_liner: 复用已验证训练轨迹做低开销技能效用评估，训练时选择性注入技能实现无技能推理性能提升
practical_value: '- 训练阶段注入技能、推理阶段剥离技能的架构可直接复用在电商导购Agent、搜索推荐多轮交互Agent的RL训练中，既能提升训练效率，又不增加推理开销

  - 无需额外环境rollout的技能效用评估方法，通过对比已有成功/失败轨迹在有技能/无技能下的似然差计算效用，适合电商/广告这类真实环境交互成本高的场景降低采样开销

  - 技能注入的正效用门控机制可直接复用在现有RAG、技能库调用的决策逻辑中，仅当估计效用为正时才调用技能，避免错误召回的内容对业务效果产生负向影响'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于技能的Agentic RL方法要么默认所有生成技能均有益，要么依赖额外环境rollout评估技能效用，采样成本高、评估结果不稳定，且技能收益随当前策略能力、query特性动态变化，无法自适应决策是否注入、注入哪类技能，多数方法推理时还依赖技能通路，增加部署开销。

### 方法关键点
- 单共享模型同时承担Executor和Generator角色：Executor先采样无技能的Scout轨迹，标注成功/失败结果；Generator基于已标注轨迹生成候选技能
- 低开销技能效用计算：无需额外环境rollout，通过对比Scout轨迹在有技能/无技能上下文下的似然差，结合轨迹结果加权得到效用值，适配全成功/全失败/混合三类轨迹组
- 正效用门控的选择性注入：仅当最高效用技能的估计值为正时才注入Executor后续rollout，否则保持无技能执行
- 双GRPO目标联合优化：Executor用环境奖励监督，Generator用技能效用监督，推理时完全剥离技能通路，无额外推理开销

### 关键结果
在ALFWorld、WebShop电商购物模拟、ScienceWorld、τ2-Bench四个基准测试，对比GRPO、SkillRL等强基线：WebShop平均成功率46.6%，超最强基线3.3pp；ALFWorld平均成功率94.8%，超最强基线3.0pp；τ2-Bench平均Pass@1 63.4%，超最强基线3.4pp；训练时仅12%~39%的query需要注入技能，无技能推理效果优于带技能的基线。

最值得记住的结论：技能是训练阶段的脚手架而非推理时的必需品，自适应选择性注入既能提升训练效率，又能让模型将技能内化到参数中，实现低开销高性能推理。
