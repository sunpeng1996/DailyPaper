---
title: Social Laws for Multi-agent Coordination in Stochastic Environments
title_zh: 随机环境下多智能体协调的社会法则研究
authors:
- Rolando Fernandez
- Caleb Probine
- Tyler Lee
- Jeffrey Chen
- Erez Karpas
- Muhammad Arrasy Rahman
- Peter Stone
- Ufuk Topcu
affiliations:
- The University of Texas at Austin
- Technion Israel Institute of Technology
arxiv_id: '2609.18929'
url: https://arxiv.org/abs/2609.18929
pdf_url: https://arxiv.org/pdf/2609.18929
published: '2026-09-16'
collected: '2026-09-17'
category: MultiAgent
direction: 多智能体协作 · 非合作场景协调规则设计
tags:
- MultiAgent
- Social Law
- Robustness
- MDP
- Stochastic Environment
- Coordination
one_liner: 将多智能体社会法则扩展至随机奖励场景，提出α-鲁棒性度量与基于MDP的鲁棒性验证框架
practical_value: '- 电商多业务线Agent（广告投放/个性化推荐/用户触达）协同场景可引入社会法则作为全局动作约束，避免不同Agent的动作冲突（如同时间段重复推送打扰用户）

  - 评估多Agent协同规则的合理性时，可复用α-鲁棒性指标，量化单Agent在全局约束下保留的最优效用占比，平衡全局协调效果与单业务目标达成率

  - 验证多Agent约束规则的可行性时，可参考将问题规约为多个独立MDP求解的思路，避免指数级复杂度的多Agent联合规划'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有多智能体社会法则研究仅适配确定性、目标导向场景，无法满足随机奖励驱动场景下的多Agent协调需求，无法有效规避Agent间动作干扰、保障个体性能。

### 方法关键点
1. 扩展社会法则至随机奖励环境，定义α-鲁棒性：所有Agent遵守规则时，单Agent执行最优个体策略可获得的最低效用占无约束最优效用的比例，量化规则的鲁棒性；
2. 提出鲁棒性验证方案，将问题规约为求解一系列MDP，大幅降低多Agent联合规划的复杂度。

### 关键结果
在多个toy环境的实验验证了框架的可行性，可准确量化不同社会法则的α-鲁棒性指标，具备实际落地潜力。
