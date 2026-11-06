---
title: 'Scientist World: Grow a Research World for AI-Scientists'
title_zh: Scientist World：面向AI科学家的可执行科研环境平台
authors:
- Taiming Lu
- Sachin Konan
- Zhuang Liu
affiliations:
- Princeton University
arxiv_id: '2611.08478'
url: https://arxiv.org/abs/2611.08478
pdf_url: https://arxiv.org/pdf/2611.08478
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 科研智能体训练评估
tags:
- AI-Scientist
- Agent Evaluation
- Training Environment
- Auto-Reproduction
- GRPO
one_liner: 将学术论文自动转化为可执行科研环境，用于AI科学家的能力评估与迭代训练
practical_value: '- 可复用多角色Agent流水线（Reproducer/Designer/Packager/Verifier）的分工模式，搭建业务侧算法自动迭代/AB实验自动复现工具链，降低算法创新的工程门槛

  - 借鉴Frontier-Normalized Improvement（FNI）的归一化思路，解决不同业务场景下算法优化效果的横向可比问题，避免局部指标优化偏差

  - SFT+GRPO两步走小模型训练方案可迁移到垂类Agent（如电商选品Agent、广告策略优化Agent）训练，用真实业务反馈作为奖励信号提升小模型垂直能力

  - 环境构建时的可见/隐藏数据集拆分思路可用于推荐/广告算法离线评估，避免算法过拟合离线可见数据集，提升优化效果的线上泛化性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前AI科学家Agent缺乏可规模化、可演进、可执行的评估与训练环境，现有基准多为人工构建、固定不变，无法匹配真实科研的开放迭代属性，也难以区分Agent的真实科研能力和记忆、话术能力，同时AI科研能力的训练缺乏真实实验反馈的闭环数据。

### 方法关键点
- 设计无人工参与的多角色Agent流水线，通过Reproducer复现论文方法、Designer定义科研任务规则、Packager打包可执行环境、Verifier交叉验证，将论文转化为标准化可执行科研环境
- 提出Frontier-Normalized Improvement（FNI）指标，以论文复现的基线结果为基准，归一化不同任务的优化效果，客观衡量AI科学家的能力
- 支持两种评估模式：Improve模式（给定论文基线方法要求优化）、Innovate模式（仅给定问题要求从0设计方法），区分不同维度的科研能力
- 环境同时作为benchmark、数据集、训练gym，基于生成的科研轨迹数据，用SFT+GRPO的方式训练小模型科研Agent

### 关键结果
从12万篇arXiv AI领域论文中筛选出1000篇构建首批环境，测试10余款前沿大模型：前沿AI科学家在Improve模式下84%的尝试超过人类论文基线，Innovate模式下74%的尝试超过人类基线；基于该环境训练的8B小模型，经过SFT+GRPO后，科研创意能力的FNI从基线41提升到106，达到前沿大模型的平均水平。

### 核心结论
衡量智能体的创新能力核心看真实执行后的结果，而非话术或记忆，可执行、可演进的环境是智能体自主迭代的核心基础。
