---
title: 'Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security
  Agents'
title_zh: 超越成功率：攻防安全Agent的成本感知评估
authors:
- Paul Kassianik
- Blaine Nelson
- Yaron Singer
arxiv_id: '2607.15263'
url: https://arxiv.org/abs/2607.15263
pdf_url: https://arxiv.org/pdf/2607.15263
published: '2026-07-16'
collected: '2026-07-19'
category: Agent
direction: 安全Agent 成本感知评估体系
tags:
- Agent Evaluation
- Cost-Aware
- LLM Agent
- Benchmark
- Security Agent
one_liner: 提出成本感知的安全Agent评估框架，明确红蓝队任务不同的成本-性能缩放规律
practical_value: '- 业务Agent选型/评估可复用成本感知思路，不要只看峰值效果，新增推理、工具调用等成本维度计算ROI，适配电商推荐Agent、客服Agent等落地场景

  - 不同任务的缩放策略可直接复用：对依赖复杂推理的任务（如大促场景多条件商品导购）可提升推理预算提效；对依赖工具调用的任务（如订单查询、库存校验）优先优化工具调用策略，无需盲目堆大模型参数

  - 可复用固定成本下的性能对比方法，搭建业务场景专属Agent性价比Benchmark，快速筛选适配自身成本要求的模型/架构'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有安全Agent评估仅关注最优任务成功率，默认给足推理预算，未考虑实际落地中推理、工具调用、遥测查询等步骤的资源消耗，评估结果和真实运营场景脱节。
### 方法关键点
从成本-收益双视角评估LLM安全Agent，覆盖进攻类Cybench CTF任务、防御类Splunk BOTS v1 SOC调查任务；放弃仅上报最优效果的传统模式，在固定成本阈值下对比不同模型性能，拆分推理支出、工具支出两个维度拆解性能构成。
### 关键结果
1. 红队CTF任务效果随测试时计算预算提升正向缩放，优化后的开源模型可接近闭源前沿系统效果，同时成本竞争力更高；
2. 蓝队SOC调查任务无相同缩放效应，效果更依赖规范的工具使用、遥测导航、选择性信息增强，单纯提升推理预算对效果提升无显著作用；
3. 成本感知评估可更精准判断模型的落地实用性，明确防御Agent的优化方向。
