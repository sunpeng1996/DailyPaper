---
title: A Self-Triggered Agentic Push Recommendation System
title_zh: 自触发式Agent推送推荐系统STEPS
authors:
- Zhao-Yu Zhang
- Qingying Chen
- Chunyuan Zheng
- Jing Zhou
- Jian Sun
- Siqi Chen
- Leiying Chen
- Chuan Zhou
- Huiyou Jiang
- Xin Tao
affiliations:
- ByteDance
- Peking University
arxiv_id: '2608.01949'
url: https://arxiv.org/abs/2608.01949
pdf_url: https://arxiv.org/pdf/2608.01949
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent 推送推荐场景决策优化
tags:
- Agentic RecSys
- Push Notification
- Decision Transformer
- Ordinal Regression
- Resource Efficiency
one_liner: 将推送推荐重构为自触发智能体流程，在抖音10亿用户规模落地提活跃降干扰省算力
practical_value: '- 推送、消息触达类场景可复用「规划Agent+执行Agent+轻量过滤Agent」三段式架构，联合优化发送时机和发送决策，避免分阶段优化的局部最优问题

  - 高噪声工业场景下用Gated-RTG机制替换传统RTG特征拼接，通过元素乘法注入目标回报信号，解决条件信号被高维状态特征淹没的问题

  - 连续值预测任务（如时间间隔、价格）可转化为等频分桶的有序回归任务，兼顾训练稳定性和预测精度，还可灵活适配不同业务的误差容忍需求

  - 算力敏感的推荐链路可引入轻量过滤层，将下游重模型知识蒸馏到无Item特征的小MLP，提前拦截低价值请求，在指标损失极小的前提下大幅降低算力开销'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Push推送是平台主动唤醒用户、提升长期留存的核心渠道，现有方案分为两类：离线预分配推送时间的方法缺乏实时适配性，固定间隔轮询的方法则面临算力开销过高和最优推送时机漏抓的两难，多阶段框架还普遍存在局部最优问题，亟需在严格的系统资源约束下解决「要不要发、什么时候发」的联合优化难题。
### 方法关键点
- 将推送推荐重构为自触发智能体闭环，系统不仅决策当前是否发Push，还自主生成下一次唤醒时间，完全脱离人工预定义调度规则
- 规划Agent采用Gated-RTG机制注入目标回报信号，避免低维RTG被高维状态特征淹没；将连续时间间隔预测转化为100个等频分桶的有序回归任务，大幅提升训练稳定性
- 执行Agent基于Bellman方程构建回报，用价值引导学习修正离线日志的次优行为，支持在线动态调整正负收益权重无需重训
- 新增轻量过滤Agent，蒸馏执行Agent知识到3层无Item特征的MLP，提前拦截低价值请求，同时搭配系统/用户侧硬规则做边界防护
### 关键实验
在抖音10亿用户规模生产环境开展14天A/B测试，对比现有生产基线（离线预分配方案），STEPS提升用户活跃天数0.2843%，降低Push权限关闭率1.9089%，过滤Agent额外降低79.42%的算力开销；对比相同算力预算下的固定间隔触发方案，STEPS核心指标优势显著。
### 核心结论
工业级时序决策场景下，把「什么时候执行决策」也作为模型输出的自触发Agent架构，可同时实现业务指标提升和算力成本下降
