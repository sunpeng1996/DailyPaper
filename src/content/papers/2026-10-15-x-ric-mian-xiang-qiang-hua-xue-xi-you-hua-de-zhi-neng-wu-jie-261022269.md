---
title: 'X-RIC: An Agentic RAN-Intelligent Controller Benchmark for Enhancing Reinforcement
  Learning'
title_zh: X-RIC：面向强化学习优化的智能无线接入网控制器Agent基准
authors:
- Adhwaa Al-Chaab
- Ayman Younis
- Dario Pompili
affiliations:
- Department of Electrical and Computer Engineering, Rutgers University–New Brunswick
arxiv_id: '2610.22269'
url: https://arxiv.org/abs/2610.22269
pdf_url: https://arxiv.org/pdf/2610.22269
published: '2026-10-15'
collected: '2026-10-19'
category: Agent
direction: Agent 通信域强化学习控制优化
tags:
- Agentic AI
- Reinforcement Learning
- Behavior Cloning
- O-RAN
- Benchmark
one_liner: 将Agentic AI与RL结合，推出可解释RAN智能控制器X-RIC框架及配套域专用评测基准BARX
practical_value: '- RL训练可先结合领域启发式规则做Behavioral Cloning预训练，大幅提升收敛速度、降低样本消耗，可迁移到推荐动态定价、流量调度、广告出价等RL优化场景

  - 领域专用轻量化Transformer模块与传统RL结合的架构，兼顾决策可解释性与输出稳定性，可复用在多目标推荐排序RL调优场景，降低策略方差

  - 生产级Agent上线前需配套域专属评测指标（延迟、合规性、确定性），该评测框架设计思路可直接复用在电商Agent的上线校验流程，减少线上风险'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
O-RAN架构下的RAN智能控制器（RIC）现有AI方案缺乏推理能力与可解释性，无法满足动态场景下低延迟、高合规的闭环控制需求。
### 方法关键点
1. 融合Agentic AI与RL，采用领域启发式规则做自动化Behavioral Cloning预训练，降低RL采样成本
2. 引入电信域专用Transformer模块TLM，提供上下文抽象与决策可解释性
3. 在近实时RIC控制闭环内实现协同适配，支持策略持续迭代优化
4. 配套域专用评测基准BARX，从延迟、合规性、确定性三个维度评估Agent控制效果
### 关键结果
在SLA感知网络切片场景下，实现89%运营成本降低且维持SLA合规；收敛速度提升75%，训练步数减少50%，输出方差降低46%
