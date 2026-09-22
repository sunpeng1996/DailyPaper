---
title: 'Beyond Raw Engagement: A Counterfactual Observability Framework for Recommender
  Systems at Netflix'
title_zh: Netflix 推荐系统反事实可观测性框架：超越原始用户参与度
authors:
- Chaoran Guo
- Ding Tong
- Ting-Po Lee
- Scarlet Chen
affiliations:
- Netflix
arxiv_id: '2609.22747'
url: https://arxiv.org/abs/2609.22747
pdf_url: https://arxiv.org/pdf/2609.22747
published: '2026-09-19'
collected: '2026-09-22'
category: RecSys
direction: 推荐系统可观测性 · 因果反事实评估
tags:
- recommender_system
- observability
- counterfactual
- causal_inference
- offline_evaluation
one_liner: 提出基于反事实的推荐系统可观测性框架，拆分内容质量与模型行为，已在Netflix大规模落地
practical_value: '- 可直接复用基于IPS、Leave-One-Out的增量性度量方案，替代纯A/B测试做内容价值离线评估，大幅降低实验成本

  - 级联推荐场景下可将内容价值拆分为Irreplaceability（不可替代性）和Universality（覆盖度）两个可解释维度，分别服务内容创作者和模型开发者

  - 可在推荐链路加入Exploration & Exploitation模块记录选择概率，为后续反事实度量提供基础数据支撑，修正曝光、位置偏差'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前推荐系统的原始参与度指标（点击、观看、转化）混杂了内容质量、模型行为、曝光偏差、受众覆盖等多重因素，既会误导内容创作者误判内容价值，也会让模型开发者难以定位系统问题，最终损害平台长期健康，同时大量效果评估依赖在线A/B测试，迭代效率极低。

### 方法关键点
- 核心思路将可观测性转化为反事实度量问题：估算移除某特定内容或模型决策后，推荐系统的行为变化和对应的用户参与度变化
- 三大度量维度：1）偏差修正：用SNIPS等IPS类方法修正曝光、位置偏差；2）相对性：对比不同策略、不同内容的归一化表现，拆分模型和内容贡献；3）增量性：针对单阶段推荐用Leave-One-Out模拟移除内容后的效果差，针对级联推荐将内容增量价值拆分为不可替代性（内容本身质量）和覆盖度（系统曝光机会）的乘积
- 同一套度量框架同时适配两类受众：内容创作者获取无偏的内容价值信号，模型开发者获取系统链路的诊断信号

### 关键结果
- 仿真实验中，Leave-One-Out度量的内容增量价值与真实值高度对齐，低噪声场景下误差极小
- 11组Netflix在线A/B测试验证，提出的行级增量性度量与A/B测试真实结果的$R^2$达0.8212，可替代部分在线实验
- 生产监控中，基于增量性的指标成功发现了推荐模型的标签归因错误问题，大幅缩短异常定位时间

### 最值得记住的一句话
把可观测性作为推荐系统飞轮的核心环节，而非下游附属报表，可同时提升内容质量和模型效果，形成正向循环
