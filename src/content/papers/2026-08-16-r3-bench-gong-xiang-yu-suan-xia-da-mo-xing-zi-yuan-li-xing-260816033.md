---
title: 'R^3-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets'
title_zh: R³-Bench：共享预算下大模型资源理性推理能力基准
authors:
- Peisong Wang
- Zhiwei Ma
- Bowen Liu
- Feixue Liu
- Aochuan Chen
- Chenyi Zi
- Hongchuan Zeng
- Yuhan Li
- Jia Li
affiliations:
- 香港科技大学（广州）
- 香港大学
- 腾讯混元团队
arxiv_id: '2608.16033'
url: https://arxiv.org/abs/2608.16033
pdf_url: https://arxiv.org/pdf/2608.16033
published: '2026-08-16'
collected: '2026-08-18'
category: Eval
direction: LLM推理评测 · 共享预算资源分配
tags:
- Benchmark
- Resource-Rationality
- LLM Reasoning
- Agent Evaluation
- Budget Allocation
one_liner: 提出首个覆盖工具-free与Agent场景的共享预算资源理性推理基准，暴露LLM跨任务资源分配短板
practical_value: '- 多Agent并发调度可借鉴其预算校准方法，按模型原生资源消耗设置相对压力阈值，避免绝对配额对不同能力模型的公平性偏差

  - 电商大促/峰值场景下的多任务（召回、排序、文案生成）资源分配，可参考其基于响应曲线的离线最优分配oracle做离线压测上限推演

  - Agent调度器优化可复用其轻量调度策略结论：有明确runtime反馈的任务（如权益校验、数据查询）优先用「先全量覆盖再深度投入」的策略，弱反馈任务（如创意文案、语义匹配）用固定调度易出现负向效果

  - LLM/Agent能力评估可新增资源分配维度，现有单任务准确率无法代表多任务共享配额下的实际表现，可引入类似Gap Ratio指标衡量资源利用效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM推理、Agent基准均采用单任务独立配额，无法评估多任务共享有限资源时的跨任务分配能力——而真实业务中多Agent并发、多任务共享API/算力配额是常态，现有能力评估存在核心维度缺失。

### 方法关键点
- 覆盖数学、竞赛编程、抽象推理3个领域，每个领域构造50组6题竞赛套件（3易2中1难），难度按参考模型平均输出长度分层，避免事后准确率偏差
- 支持工具-free（按输出token算预算）、Agent（按工具调用动作算预算）两种场景，预算按每个模型无约束下的原生资源消耗校准为相对压力（ρ=0.2强压力/0.8中压力）
- 设计单任务响应曲线oracle（离线最优分配基准）、均等分配回放两个基线，用Oracle与实际得分的Gap、Gap Ratio衡量资源分配效率

### 关键结果
评测8个SOTA LLM，72组模型-场景-压力-领域实验中，oracle得分全部≥实际得分，71组严格更高，最大Gap Ratio达82.47%；强压力下42%~95%的失败源于预算被其他任务占用，中压力下38%~67%的失败源于中途放弃可解任务；轻量在线调度可在6/9的模型-领域组合中提升表现，但无跨领域通用调度策略，代码等有明确运行时反馈的任务调度收益显著，数学、抽象推理等弱反馈领域调度易负向。

**最值得记住的结论**：单任务能力强的LLM/Agent，在多任务共享资源场景下的实际表现可能远低于预期，资源分配能力是现有评估体系完全遗漏的独立维度。
