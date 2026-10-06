---
title: 'Beyond States: Investigating the Effects of Context on User Modeling with
  Feature-Conditioned Markov Models'
title_zh: 基于特征条件马尔可夫模型的上下文感知用户建模研究
authors:
- Jana Isabelle Friese
- Andreas Konstantin Kruff
- Timo Breuer
- Philipp Schaer
- Norbert Fuhr
affiliations:
- University of Duisburg-Essen
- TH Köln - University of Applied Sciences
arxiv_id: '2610.06060'
url: https://arxiv.org/abs/2610.06060
pdf_url: https://arxiv.org/pdf/2610.06060
published: '2026-10-05'
collected: '2026-10-06'
category: RecSys
direction: 上下文感知用户行为建模
tags:
- UserModeling
- MarkovModel
- ContextAware
- UserSimulation
- InteractiveIR
one_liner: 为传统马尔可夫用户模型引入多维度上下文特征，兼顾效率与可解释性，提升行为模拟保真度
practical_value: '- 搜索/推荐场景的用户行为仿真可直接复用特征条件马尔可夫架构，相比LLM仿真大幅降低计算成本，同时保留可解释性，适合A/B测试的用户模拟基底

  - 特征选择可参考场景适配经验：常规排序场景优先加位置特征，非排序曝光场景（如专题页、随机feed）优先加内容匹配特征，时序行为模拟优先加历史交互计数特征

  - 用户模拟评估可复用文中6层级评估框架，避免单指标拟合导致的仿真失真，覆盖从点到面的行为对齐需求

  - 会话用户建模无需盲目堆叠特征，需根据建模目标（如模拟点击/停留/会话终止）选择对应特征子集，冗余特征反而会降低部分维度的模拟效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统基于马尔可夫的用户行为模拟模型仅依赖固定状态转移概率，无法引入上下文信息，模拟真实度低；而LLM类用户模拟方案计算成本高、可解释性差、行为可控性弱，缺乏兼顾效率、可解释性与上下文感知能力的折中方案，同时不同上下文特征对不同场景、不同建模目标的增益也缺乏系统性验证。
### 方法关键点
- 提出特征条件马尔可夫用户模型，将转移概率建模为当前状态+上下文特征的分类输出，在增强状态空间保留马尔可夫属性，无需显式枚举超大状态矩阵，计算效率与基础马尔可夫模型相当
- 上下文特征划分为4类：位置特征（文档排名、query序号）、时序特征（会话累计时长）、知识特征（历史点击/标记数）、内容特征（检索得分、query-文档相似度）
- 设计6层级评估框架，覆盖预测拟合、聚合行为对齐、文档级交互重叠、时序动态对齐、检索结果质量、会话轨迹相似度，全面衡量模拟保真度
### 关键实验结果
在3个公开搜索会话数据集（TREC 2014、LISP、TIPPS）上与无上下文的基础马尔可夫模型对比：全特征版本模型的平均per-action NLL相对下降22%~32%，文档级点击召回相对提升13%~26%，会话轨迹Fréchet距离相对下降23%~42%；排序搜索场景下位置特征增益最大，随机排序无相关性信号的场景下内容特征增益最大。
### 核心结论
用户行为模拟不存在通用最优特征集，需根据场景和建模目标选择对应上下文特征，盲目堆叠特征反而可能降低特定维度的模拟效果。
