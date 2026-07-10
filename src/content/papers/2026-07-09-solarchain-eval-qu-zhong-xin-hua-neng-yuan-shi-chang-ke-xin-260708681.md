---
title: 'SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic
  Agents in Decentralized Energy Markets'
title_zh: SolarChain-Eval：去中心化能源市场可信经济Agent的物理约束评估基准
authors:
- Shilin Ou
- Yifan Xu
- Luyao Zhang
affiliations:
- Duke Kunshan University
arxiv_id: '2607.08681'
url: https://arxiv.org/abs/2607.08681
pdf_url: https://arxiv.org/pdf/2607.08681
published: '2026-07-09'
collected: '2026-07-10'
category: Agent
direction: 可信经济Agent 物理约束评估基准
tags:
- Agent
- Benchmark
- Trustworthy AI
- LLM Auditor
- MDP
- Evaluation
one_liner: 提出融合物理约束与LLM规划审计层的去中心化能源市场可信经济Agent多维度评估基准
practical_value: '- 高风险决策Agent落地可复用「先验规则+LLM审计」双校验架构，降低违规动作占比

  - 多维度Agent评估框架可迁移至电商营销、广告出价等资源分配场景，补充公平性、稳定性、可审计性评估维度

  - 可借鉴物理约束嵌入MDP环境的思路，在电商流量分配、库存调度场景将业务硬约束作为前置拦截器，规避奖励误设导致的违规'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
Agent在信息物理系统落地时缺乏同时覆盖效果与可信性的评估框架，去中心化能源市场中Agent易利用无效物理数据、制造虚假流动性、生成不稳定决策，现有基准未纳入物理约束与可审计性要求。
### 方法关键点
1. 构建Gymnasium兼容的MDP环境，将市场治理决策抽象为小时级动作空间
2. 覆盖6维度评估指标：市场效用、物理安全、滑点、动作平滑性、空间公平性、可审计性
3. 新增LLM Planner/Auditor层：Planner定义回合级动作边界与审计规则，Auditor审核修正高风险动作，全链路留痕干预过程
### 关键结果
实验覆盖5类策略，验证存在明确的效用-安全权衡；纯RL策略可提升市场效用但仍会产生不安全行为；移除物理惩罚后，奖励最大化策略会利用无效发电数据将虚假流动性提升超40%；LLM规划审计层可缓解约65%的选定高风险行为，提升全链路可审计性，但无法完全补偿奖励函数误设带来的问题。
