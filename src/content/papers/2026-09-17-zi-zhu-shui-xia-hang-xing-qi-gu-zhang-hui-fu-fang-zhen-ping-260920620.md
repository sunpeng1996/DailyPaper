---
title: 'A Simulation Platform for AUV Fault Recovery: Exploring LLM-Based Diagnostic
  Strategies'
title_zh: 自主水下航行器故障恢复仿真平台：探索基于大模型的诊断策略
authors:
- Khalid Halba
- Kylie Cooper
- James G. Bellingham
affiliations:
- Exploration Robotics Laboratory, Johns Hopkins University
- Johns Hopkins Institute for Assured Autonomy
arxiv_id: '2609.20620'
url: https://arxiv.org/abs/2609.20620
pdf_url: https://arxiv.org/pdf/2609.20620
published: '2026-09-17'
collected: '2026-09-19'
category: Agent
direction: Agent 自主故障诊断与评估框架
tags:
- LLM
- Agent
- Fault Diagnosis
- Simulation Platform
- Ensemble Evaluation
one_liner: 提出AUV故障恢复闭环仿真平台SPAR，建立LLM辅助自主任务管理的集束评估方法
practical_value: '- 可复用「常规任务走确定性规则、异常场景调用LLM做诊断决策」的分层架构，适配电商推荐/广告投放的异常流量、链路故障自动排查场景

  - LLM驱动的业务模块评估可借鉴ensemble测试思路，针对同一场景做多轮抽样测试，避免单case结果的偶然性导致的评估偏差

  - 可复用「故障注入+LLM judge自动打分」的闭环仿真评估框架，降低Agent类业务模块上线前的测试成本，减少线上试错风险'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
长时作业的自主水下航行器（AUV）通信链路不可靠，需实现无人工干预的故障自主恢复；现有LLM辅助故障决策的评估多为单case演示，缺乏批量严谨的验证方案。
### 方法关键点
提出SPAR闭环仿真平台，耦合实时航行器控制软件与上层编排层，支持物理故障注入、结构化prompt、LLM交互、任务生成执行、LLM judge自动评分；采用ensemble测试范式，对比前沿闭源模型与3款本地可部署LLM在质量偏移故障下的诊断性能。
### 关键结果
480组试验显示，前沿模型将重心偏移故障机制排在前3假设的占比达85~90%，最优本地模型仅为60~78%；本地模型性能与是否严格遵循完整诊断流程正相关，弱模型易过早误判为升降舵故障；诊断性能与操作决策性能无明显关联。
