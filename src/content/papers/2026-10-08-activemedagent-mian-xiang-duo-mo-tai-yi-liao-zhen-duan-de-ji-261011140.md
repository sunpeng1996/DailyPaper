---
title: 'ActiveMedAgent: Cost-Aware Trajectory Learning for Multimodal Medical Diagnosis'
title_zh: ActiveMedAgent：面向多模态医疗诊断的成本感知轨迹学习
authors:
- Weiwei Ma
- Xiaobing Yu
- Peijie Qiu
- Jin Yang
- Zhaoqi An
- Xuanzhao Dong
- Xiaoqi Zhao
- Xiaofeng Liu
affiliations:
- Washington University in St. Louis
- Icahn School of Medicine at Mount Sinai
- Arizona State University
- Yale University
arxiv_id: '2610.11140'
url: https://arxiv.org/abs/2610.11140
pdf_url: https://arxiv.org/pdf/2610.11140
published: '2026-10-08'
collected: '2026-10-11'
category: Agent
direction: 多模态Agent · 成本感知决策优化
tags:
- Agent
- Multimodal
- Cost-Aware Policy
- Trajectory Learning
- VLM
one_liner: 提出成本感知多模态医疗诊断Agent框架，用轻量MLP学习证据采集轨迹，效果优于全模态基线
practical_value: '- 多模态调用成本优化场景可复用「效用-成本打分+离线轨迹学习」逻辑，比如广告/推荐的多模态特征按需拉取，降低API调用与IO开销

  - 轻量MLP控制器适配冻结大模型的决策调度方案，可迁移到LLM4Rec、多模态导购Agent的特征/工具调用决策模块，无需微调基座

  - 信息过载效应可复用在推荐系统特征工程：无需引入全量特征，通过策略学习筛选核心特征子集，反而能避免噪声提升排序效果'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态医疗AI多采用全模态输入的静态推理范式，忽略真实诊断从低成本到高成本证据逐步采集的逻辑，还存在全模态输入带来的信息过载导致效果下降的问题。

### 方法关键点
1. 基于冻结API访问的VLM，跟踪候选诊断的概率分布，对每次证据采集按「单步诊断效用-采集成本」打分；
2. 训练轻量MLP控制器，在已打分的轨迹数据上离线学习，决策何时请求额外证据、何时输出最终诊断。

### 关键结果数字
在3个通用基准上，轨迹策略学习效果一致优于无引导采集和全模态基线；175个测试案例中，Agent用更少模态输入得到正确诊断，而全模态基线判断错误。
