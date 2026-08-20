---
title: 'MLREF: Efficient Module Reuse for Reward Design in Reinforcement Learning
  via Large Language Models'
title_zh: MLREF：基于大语言模型的强化学习奖励设计模块复用框架
authors:
- Chenglin Liu
- Xun Wang
- Ruishuo Chen
- Zhuoran Li
- Longbo Huang
affiliations:
- Institute for Interdisciplinary Information Sciences, Tsinghua University
arxiv_id: '2608.18827'
url: https://arxiv.org/abs/2608.18827
pdf_url: https://arxiv.org/pdf/2608.18827
published: '2026-08-19'
collected: '2026-08-20'
category: Agent
direction: Agent 强化学习奖励自动设计
tags:
- LLM
- Reinforcement Learning
- Reward Design
- Module Reuse
- Iterative Optimization
one_liner: 提出基于持久化模块池的LLM驱动RL奖励优化框架，提升性能同时大幅降低迭代波动
practical_value: '- 模块池架构可直接迁移到多目标推荐/广告排序优化：将CTR、CVR、客单价、复购等优化目标拆分为独立可复用模块，替代当前人工调参的权重分配方式，用历史效果+业务语义混合评分迭代权重，避免全量规则改写导致的效果跳水

  - 带回滚的迭代机制可复用在LLM驱动的业务策略迭代场景：比如搜索query改写规则、推荐个性化文案生成规则迭代时，为每个子规则单独计算贡献度，迭代效果不达阈值自动回滚到上一稳定版本，大幅降低线上实验风险

  - 分阶段Reflection的Prompt范式可直接套用：用LLM生成业务规则/代码时，先做任务目标分析、再做现有规则缺陷诊断、最后输出改进方案，拆分思考与执行步骤，减少LLM幻觉，提升输出准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM驱动的强化学习奖励设计方法均以整段奖励函数为优化单位，无法沉淀复用历史迭代中验证有效的组件，迭代过程性能波动大，容易出现效果倒退，亟需更稳定高效的自动化奖励优化方案。
### 方法关键点
- 核心抽象：持久化模块池，将奖励函数拆解为多个面向任务不同维度的独立可复用模块，每次生成的奖励为池内模块的线性加权组合，优化对象从单次奖励函数转为持续迭代的模块池
- 三大配套机制：① 双阶段反射：迭代前先做任务/环境语义分析、历史反馈归因，不直接生成代码，减少幻觉；② 混合信用分配：每个模块同时计算LLM语义评分、与训练效果的相关性评分，EMA平滑后融合，用UCB平衡探索与利用选择模块及权重；③ 带回滚的合并策略：并行迭代多个模块池版本，效果不达历史阈值则直接回滚到上一稳定版本，避免迭代波动
### 关键实验
在17个Isaac Gym、Bi-DexHands的运动与灵巧操作任务上，对比SOTA基线EUREKA、RF-Agent，locomotion任务平均性能提升25.2%，manipulation任务平均提升6.6%，迭代过程性能波动远低于基线。
### 核心结论
将优化对象从单次生成的完整策略，升级为可独立评估、可沉淀复用的组件库，是提升LLM驱动策略迭代效率与稳定性的核心路径
