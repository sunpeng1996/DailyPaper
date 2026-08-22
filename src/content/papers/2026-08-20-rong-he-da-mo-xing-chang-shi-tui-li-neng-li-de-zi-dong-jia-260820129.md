---
title: Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs
  for Autonomous Driving
title_zh: 融合大模型常识推理能力的自动驾驶多智能体编排框架
authors:
- Mehdi Azarafza
- Faezeh Pasandideh
- Ali Ehteshami Bejnordi
- Stefan Henkler
- Achim Rettberg
affiliations:
- Hamm-Lippstadt University of Applied Sciences, Germany
arxiv_id: '2608.20129'
url: https://arxiv.org/abs/2608.20129
pdf_url: https://arxiv.org/pdf/2608.20129
published: '2026-08-20'
collected: '2026-08-22'
category: MultiAgent
direction: 多智能体编排 · LLM常识推理融合
tags:
- Multi-Agent
- LLM Reasoning
- Orchestration
- Reinforcement Learning
- Hybrid Architecture
one_liner: 提出融合LLM常识推理、协调RL与传统控制的自动驾驶混合决策框架
practical_value: '- 多系统协作的编排器设计思路可复用：LLM做决策层调度规则引擎+传统算法做执行层，兼顾推理灵活性与性能稳定性，适合推荐/广告系统冷热流量混合调度场景

  - LLM迭代优化RL奖励函数的思路可迁移：针对推荐系统冷启、稀疏反馈场景，用LLM常识先验动态调整RL排序/召回模型的奖励权重，降低手动调参成本

  - 混合架构规避LLM hallucination的思路可借鉴：将LLM限制在推理调度环节，不直接输出最终执行指令，适合Agent驱动的导购、营销文案生成等强容错要求的业务场景'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
自动驾驶场景中，传统RL、规则控制方法在需上下文推理的未知场景性能明显下降，直接用LLM输出车辆控制指令又存在高延迟、幻觉风险，现有方案无法同时兼顾安全性、泛化性与上下文推理能力。

### 方法关键点
1. 设计混合决策框架，引入编排器统一调度PPO训练的RL模型与PID传统控制模块，全链路嵌入LLM常识推理能力；
2. 用LLM常识先验迭代优化RL奖励函数，动态适配多变的驾驶环境；
3. 限制LLM仅负责推理调度环节，不直接输出最终控制指令，从架构层面规避幻觉与延迟问题。

### 关键结果
在高度随机化的CARLA仿真平台多环境、多交通场景下完成测试，未披露具体量化提升指标，验证了LLM推理能力与传统自动驾驶方案融合的可行性，可完整保留原有结构化控制、安全机制。
