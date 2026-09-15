---
title: 'Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe
  Control'
title_zh: 向非对齐Agent授权：联盟对齐与安全控制
authors:
- Natalie Collina
- Surbhi Goel
- Aaron Roth
- Sikata Bela Sengupta
arxiv_id: '2609.15803'
url: https://arxiv.org/abs/2609.15803
pdf_url: https://arxiv.org/pdf/2609.15803
published: '2026-09-14'
collected: '2026-09-15'
category: Agent
direction: Agent 多智体授权安全对齐
tags:
- MultiAgent
- AgentAlignment
- AgentSafety
- AuthorizationControl
- GameTheory
one_liner: 提出k-鲁棒联盟对齐条件，无需单个Agent对齐即可保障多Agent授权流程安全
practical_value: '- 电商/广告推荐的多Agent审核场景可直接复用k-鲁棒联盟对齐思路，无需强求单个审核Agent完全对齐平台目标，构造满足条件的审核面板即可容忍最多k个Agent失效，降低对齐成本同时拦截所有有害内容/动作

  - 自动化交易、客诉处理等多Agent执行流程可采用「基线策略+单步动作审核」架构，每个动作仅需审核单步加后续走基线的期望收益，无需预判全轨迹，大幅降低审核计算量的同时保障全局收益不低于基线

  - 若审核Agent可能存在策略性投票行为，优先采用全票通过规则，可保障所有纳什均衡下的流程安全；若需要更高通过率，可采用k容忍阈值规则，但需配套审核Agent的k+1联盟稳定性校验'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长生命周期Agent执行自动化任务时逐动作申请人类授权会成为效率瓶颈，直接委托其他AI Agent审核又面临审核Agent自身非对齐的安全风险，现有方案要求单个审核Agent完全对齐，实现成本极高，亟需更宽松的安全约束条件。
### 方法关键点
- 定义k-鲁棒联盟对齐条件：移除任意k个审核Agent后，剩余Agent的效用非负组合加可行域非负项可表示委托人效用，无需单个Agent对齐
- 阈值规则安全充要条件：容忍最多k个反对票的审核规则安全当且仅当审核面板满足k-鲁棒联盟对齐
- 序列决策场景下，仅需每个状态的本地动作审核满足安全条件，即可保障全局期望收益不低于基线策略，无需预判后续动作轨迹
- 策略性投票场景下，全票通过规则只要面板满足全联盟覆盖，所有纳什均衡均安全；k容忍阈值规则需配套k+1联盟稳定性校验
### 关键实验
基于现有奖励模型和安全评估器组成审核面板测试：答案选择任务中，全票审核可100%拦截所有低于基线正确率的候选答案，即使单个审核Agent会漏过部分有害答案；容忍1个反对票时，仍可100%拦截所有有害响应，同时放行更多可接受响应；使用数值评分替代二元投票可在同等安全水平下放行更多有效提案。
### 核心结论
多Agent审核的安全保障无需依赖单个Agent的完美对齐，合理的联盟结构与规则设计可大幅降低对齐成本，同时兼顾流程效率与安全。
