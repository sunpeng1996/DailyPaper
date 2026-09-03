---
title: 'Bilevel Coordinated Reflection: A Game-Theoretic Approach to Multi-Agent LLM
  Systems'
title_zh: 双层协调反思：博弈论驱动的多智能体LLM系统优化方法
authors:
- Yihang Chen
- Yuxiang Chen
- Yuxuan Huang
- Meng Fang
- Weilin Luo
- Jun Wang
affiliations:
- UCL Centre for Artificial Intelligence
- University of Liverpool
- Huawei
arxiv_id: '2609.02750'
url: https://arxiv.org/abs/2609.02750
pdf_url: https://arxiv.org/pdf/2609.02750
published: '2026-09-02'
collected: '2026-09-03'
category: MultiAgent
direction: 多智体协调·收敛性优化
tags:
- MultiAgent
- GameTheory
- Reflection
- Grounding
- Convergence
- LLM
one_liner: 基于双层协调博弈建模多智能体交互，提出接地验证的SRMA算法，保障反思机制收敛性
practical_value: '- 搭建电商多Agent运营/客诉系统时，放弃纯文本自评估反思逻辑，必须加入业务接地验证（如订单状态校验、用户反馈埋点），避免幻觉累积

  - 任务分解可复用弱耦合量化指标，控制子任务关联度κ和最大关联子任务数dmax，降低多智能体协作误差

  - 动态业务场景（如大促规则变更）可复用SRMA重锚定机制，每次更新记忆前重新评估当前风险，快速适配新环境

  - 记忆更新不要无条件提交，新增置信门控逻辑，仅候选记忆严格降低业务风险时才留存，避免性能震荡'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多智能体LLM系统的反思机制多为纯文本自反馈，缺乏协调逻辑的理论支撑，存在幻觉累积、收敛性无保障、纯文本自评估无法适配环境变化三大问题，任务分解质量、外部验证的作用长期没有可落地的量化解释。

### 方法关键点
- 将编排器-工作者交互建模为双层协调博弈，下层工作者子博弈为近似势博弈，均衡误差由任务分解的耦合度κ和最大关联子任务数dmax共同决定
- 证明纯文本自门控的信息论不可能性：仅观测生成文本的门控无法在文本规则相同但语义相反的环境下同时优化，必须引入环境接地信号
- 提出SRMA（Stochastic Reflective Memory Ascent）算法，仅当候选记忆严格降低接地评估风险时才提交，支持置信门控适配随机评估场景、重锚定适配非平稳环境，理论上可实现几何或多项式阶收敛

### 关键结果
- SWE-bench 500个实例上，基于Kimi的双层SRMA系统解决率达72.2%，优于公开mini-SWE-agent v2基线的70.8%
- Overcooked多智能体协作任务上，接地SRMA比纯文本自门控得分提升14.3%~30%
- 资源分配任务上，SRMA达到98.5%~99.5%的Oracle奖励，相比无记忆配置regret降低60.8%

最值得记住的结论：多智能体系统的反思机制不能仅依赖文本自评估，grounding验证是保障收敛、避免幻觉累积的必要条件
