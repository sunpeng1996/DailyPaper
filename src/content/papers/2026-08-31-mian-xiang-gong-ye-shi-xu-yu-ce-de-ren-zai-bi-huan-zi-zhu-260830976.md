---
title: A Human-in-the-Loop Autonomous Agent for Industry Time Series Forecasting
title_zh: 面向工业时序预测的人在闭环自主Agent系统
authors:
- Xiaoyu Tao
- Mingyue Cheng
- Ze Guo
- Bokai Pan
- Qi Liu
- Shijin Wang
- Enhong Chen
affiliations:
- State Key Laboratory of Cognitive Intelligence, University of Science and Technology
  of China
arxiv_id: '2608.30976'
url: https://arxiv.org/abs/2608.30976
pdf_url: https://arxiv.org/pdf/2608.30976
published: '2026-08-31'
collected: '2026-09-02'
category: Agent
direction: 人在闭环Agent · 工业时序预测
tags:
- Time-Series Forecasting
- Human-in-the-Loop
- LLM Agent
- Tool Use
- Forecasting System
one_liner: 提出人在闭环时序预测Agent CastClaw，融合多源能力，精度优于16类基线方法
practical_value: '- 人在闭环的Agent编排框架可直接迁移到电商销量预测、库存周转预估场景，把专用时序模型、运营规则、人工干预输入统一纳管，替代原有固定预测pipeline

  - 预测结果校验→缺失信息补全（调用工具/询问人）→按终止条件输出的流程设计，可复用在大促流量预估、广告投放效果预判等高可靠性要求场景，降低预测误差

  - 版本化全链路执行记录+可解释报告的设计，可复用在推荐/广告系统的效果归因、迭代审计环节，降低业务排查与对齐成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
工业时序预测落地需串联任务定义、数据模型调度、领域知识融合、合理性校验全流程，现有专用预测模型pipeline固定灵活性差，通用LLM Agent缺乏预测场景专属校验约束与终止规则，无法适配复杂业务需求。
### 方法关键点
1. 构建CastClaw人在闭环预测Agent，统一纳管时序数据、专用预测模型、分析工具、用户输入与版本化执行记录；
2. 支持用户用自然语言定义预测目标、周期、约束与假设，自动校验时序模式与用户约束，缺信息时自动召回上下文、调用工具/模型或询问用户，按显式终止条件决定保留/修正/升级结果；
3. 输出最终预测结果+全链路执行审计报告，全程可追溯。
### 关键结果
在5个电价预测数据集上，点估计MSE、MAE均为16个基线中最低；已在华北2026年1-6月省级电力负荷数据完成离线验证
