---
title: Addressing Exogenous Variability in Cooperative Multi-Agent Reinforcement Learning
title_zh: 面向合作多智能体强化学习外生变异问题的鲁棒性优化方法
authors:
- Seongmin Kim
- Woohyeon Byeon
- Jiwon Jeon
- Seungyul Han
- Youngchul Sung
affiliations:
- KAIST
- UNIST
arxiv_id: '2611.22067'
url: https://arxiv.org/abs/2611.22067
pdf_url: https://arxiv.org/pdf/2611.22067
published: '2026-11-17'
collected: '2026-11-18'
category: MultiAgent
direction: 多智能体协作 · 外生环境鲁棒性
tags:
- MARL
- CTDE
- Exogenous Variability
- Generalization
- Intrinsic Reward
one_liner: 提出CTDE兼容的LEICA算法，大幅提升外生变异下多智能体协作的训练性能与泛化能力
practical_value: '- 多智能体协同系统（如电商流量分配、多广告位联合调度）遇到外生变量波动（如竞品策略变化、平台规则调整）时，可借鉴状态拆分思路：将状态划分为智能体动作直接可控分量和外生因素主导分量，降低策略拟合难度

  - 做策略泛化优化时，可复用影响加权反事实内在奖励设计：通过计算可控分量变化对外生响应的延迟影响权重，给策略更新提供更明确的信号，减少对特定训练环境的过拟合

  - 无领域知识时可借鉴自动状态拆分方法：训练初期通过动作扰动测试各状态分量的敏感性自动划分可控/外生分量，无需人工标注特征属性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有合作MARL算法在对手策略、环境规则等不受智能体团队控制的外生变异场景下泛化性极差，仅靠多场景训练加上下文推断只能小幅提升性能，核心痛点是策略不知道哪些可控状态变化能真正影响外生因素的后续响应，导致训练过拟合、测试性能崩溃。

### 方法关键点
1. 提出ED-POMDP形式化框架，将全局状态拆分为直接动作响应分量Sd（智能体动作可直接改变）和非直接动作响应分量Sr（外生因素主导，仅受Sd延迟影响）
2. 设计CTDE兼容的LEICA算法，包含两个核心模块：一是上下文编码器，分别学习Sd和Sr的历史依赖表征；二是影响加权内在奖励，通过反事实计算每个智能体动作对Sd的改变量，乘以该Sd分量对后续Sr变化的影响权重和价值敏感性权重，作为附加奖励指导策略更新
3. 支持无领域知识的自动状态拆分：训练初期通过动作扰动测试状态分量的动作敏感性，自动划分Sd/Sr

### 关键实验
在SMAX星际多智能体对战基准上测试，设置对手策略、初始距离等外生变量的训练/测试分布偏移，对比MAPPO、QMIX、MAPPO+ctx等7个基线：LEICA在见过的场景胜率从61.0%提升到78.2%，在未见过的外生场景胜率从34.5%提升到59.5%，推理端开销仅增加不到5%。

**最值得记住的一句话**：外生波动场景下提升多智能体泛化性的核心不是仅识别当前环境类型，而是要找到哪些可控动作的变化能真正影响外生响应，给策略明确的优化信号。
