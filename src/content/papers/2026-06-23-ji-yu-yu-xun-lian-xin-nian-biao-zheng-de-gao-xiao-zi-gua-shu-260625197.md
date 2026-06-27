---
title: Efficient Adaptive Data Acquisition via Pretrained Belief Representations
title_zh: 基于预训练信念表征的高效自适应数据采集方法
authors:
- Daolang Huang
- Zhuoyue Huang
- Conor Hassan
- Luigi Acerbi
- Samuel Kaski
- Tom Rainforth
affiliations:
- ELLIS Institute Finland
- Aalto University
- University of Helsinki
- University of Manchester
- University of Oxford
arxiv_id: '2606.25197'
url: https://arxiv.org/abs/2606.25197
pdf_url: https://arxiv.org/pdf/2606.25197
published: '2026-06-23'
collected: '2026-06-27'
category: Training
direction: 自适应数据采集 · 策略学习架构优化
tags:
- Active Learning
- Bayesian Optimization
- Policy Learning
- Representation Learning
- Pretrained Model
one_liner: 提出POLAR框架，解耦表征与策略学习，降低自适应数据采集训练样本需求并提升性能
practical_value: '- 主动学习（Active Learning）场景可复用「预训练模型做信念编码器+轻量策略头」的解耦架构，降低冷启动标注样本需求，适配电商少样本类目识别、用户意图建模任务

  - 贝叶斯优化（Bayesian Optimization）调参场景可复用POLAR统一训练框架，仅替换任务特定效用函数即可适配不同目标，可用于推荐排序模型超参调优、广告出价策略优化

  - 序列决策类Agent可借鉴信念状态蒸馏思路，用预训练大模型压缩历史观测为低维信念表征，降低决策链路计算开销，提升Agent实时响应速度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
自适应数据采集（覆盖Active Learning、Bayesian Optimization、贝叶斯实验设计等场景）现有两类方案均存在缺陷：基于后验的方法依赖代理模型与后验近似，易出现误配或偏差；直接策略学习方法直接映射历史观测，无法利用已有模型表征，训练难度高、样本需求大。
### 方法
提出POLAR框架，核心思路是最优数据采集仅需通过充分信念状态关联观测历史，无需直接处理全量历史数据。框架解耦表征学习与策略学习：直接复用预训练预测基座模型作为信念状态编码器，仅在其输出表征之上训练轻量策略头，不同任务仅需替换训练用的任务特定效用函数即可适配，形成统一的摊销策略学习框架。
### 结果
跨三类任务的实验显示，POLAR性能优于现有SOTA摊销方法，同时训练样本需求量降低超50%，大幅提升自适应数据采集的可扩展性与效率
