---
title: 'AgentOPSD: Turn-Level Credit Assignment via Recursive Belief Revision'
title_zh: AgentOPSD：基于递归信念修正的多轮Agent轮次级信用分配
authors:
- Yizhuo Li
affiliations:
- Beijing Institute of Technology
arxiv_id: '2611.12587'
url: https://arxiv.org/abs/2611.12587
pdf_url: https://arxiv.org/pdf/2611.12587
published: '2026-11-09'
collected: '2026-11-10'
category: Agent
direction: Agent强化学习 · 轮次信用分配
tags:
- AgentRL
- CreditAssignment
- GRPO
- SelfDistillation
- BayesianUpdate
one_liner: 无critic的递归信念修正框架实现多轮Agent细粒度信用分配，效果优于GRPO等基线
practical_value: '- 电商导购Agent、多轮对话式推荐场景可直接复用该轮次信用分配方案，替代GRPO的全轨迹统一优势分配，解决长交互序列的关键决策识别问题

  - 自蒸馏设计可迁移到推荐系统RL训练：仅训练时加入特权信息（业务先验、优质动作规则），推理无额外开销，平衡训练效果与线上性能

  - 利用轨迹组成功率作为信念初始化先验、log-odds空间做递归更新的技巧，可直接复用在其他稀疏奖励RL场景，无需额外训练critic，大幅降低训练成本

  - bounded multiplier设计保证优化方向始终和终端奖励一致，避免自蒸馏信号偏离业务目标，适合对指标稳定性要求高的电商场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多轮Agent的RL训练普遍采用GRPO等方法，将轨迹级稀疏奖励的优势均匀分配到所有轮次，粒度过粗无法区分长交互中的关键决策与冗余操作；现有自蒸馏方法仅输出局部token/单轮信号，未结合历史信息，无法作为可靠的序列信用信号。

### 方法关键点
- 轮次证据聚合：将单轮内所有token的技能条件自教师与学生策略的log概率差求和，作为该轮的证据值
- 递归信念更新：以轨迹组的平均成功率为初始先验，在log-odds空间递归更新轨迹成功概率的信念，每轮的信用等于该轮带来的信念变化量
-  bounded优势重塑：将信念变化量与轨迹级优势结合，输出轮次级的重塑优势，保证优化方向与终端奖励一致，无需额外训练critic或增加推理开销

### 关键实验
在ALFWorld多轮embodied任务上，采用Qwen2.5-3B/7B作为backbone，对比GRPO、GRPO+OPSD、StepOPSD等基线；7B规模下成功率达89.1%，比GRPO高7.9个百分点，每新增交互轮次仅损失0.54个百分点成功率，远优于GRPO的2.91个百分点损失；消融实验验证轮次聚合、递归信念更新、结果符号对齐三个核心组件均带来稳定收益。

**最值得记住的一句话**：轮次的信用不应仅取决于其局部信号，而应取决于该信号对轨迹最终成功概率信念的修正程度。
