---
title: Requirement--Evidence Alignment for Compositional E-Commerce Queries
title_zh: 面向组合式电商查询的需求-证据对齐重排序框架
authors:
- Weihao Shen
- Wei Chen
- Fuwei Zhang
- Meng Yuan
- Yuqin Lan
- Guojun Liu
- Qingsong Hua
- Wei Lin
- Fuzhen Zhuang
affiliations:
- Beihang University
- Meituan
arxiv_id: '2608.02500'
url: https://arxiv.org/abs/2608.02500
pdf_url: https://arxiv.org/pdf/2608.02500
published: '2026-08-03'
collected: '2026-08-04'
category: RecSys
direction: 电商搜索重排序 · 需求-证据对齐
tags:
- E-commerce Search
- Reranking
- GRPO
- Intent Understanding
- Compositional Query
one_liner: 提出REAlign需求-证据对齐重排框架，优化组合式电商查询排序，降低顶部结果约束违反率
practical_value: '- 处理组合式搜索查询时，可直接复用需求-证据对齐思路：将用户query拆分为目标、预算、属性、排除项、履约要求等带强度、是否需显式证据的结构化原子，避免仅靠语义相似度排序导致的「近漏项」问题

  - 重排优化可复用R-GRPO的多维度奖励设计：在基础相关性奖励之外，叠加需求满足度、证据支持度、约束违反惩罚、输出有效性四个维度的加权奖励，优先降低Top结果的硬约束违反率，适配电商场景用户的刚性需求

  - 可复用需求导向的难负例构造方法：按不同需求的违反情况构造对比样本，而非仅用语义相似度筛选难负例，大幅提升模型对约束差异的感知能力，减少训练时的信号混淆'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有电商搜索重排器多以聚合语义相关性为核心优化目标，处理包含多约束（如预算、属性、排除项、配送要求）的组合式查询时，容易将语义相近但违反关键约束的「近漏项」排在前列，无法区分需求满足、违反、无证据三种状态，导致相关性监督信号和细粒度需求决策存在gap，用户拿到的结果看似相关但实际不可用。
### 方法关键点
- 需求-证据表示层：将组合式query解析为带类型、操作符、取值、强度、是否需显式证据的需求原子；对每个商品，用确定性验证器判断每个需求的状态（满足/违反/无证据），压缩为包含覆盖率、风险得分的紧凑候选状态。
- 需求导向对比样本构造：按需求违反类型划分候选角色（预算超标、属性不符、缺证据等），构造语义相近但需求满足度不同的对比训练组，弥补传统难负例仅靠语义相似度筛选的缺陷。
- R-GRPO优化：在GRPO的组相对策略优化基础上，设计分解式列表奖励：基础相关性奖励+需求满足奖励+证据支持奖励-约束违反惩罚-无效输出惩罚，仅对Top-K曝光的候选计算奖励，在保障相关性的前提下优先排序满足约束的商品。
### 关键实验
在两个电商固定候选池重排基准Shop-Need、KS-Need上测试，对比SFT、PPO、DPO、GRPO等基线，采用Qwen3.5-4B作为backbone：在Shop-Need上NDCG@10达0.9293，较最强基线GSPO高1.07pp，Top5约束违反率降低0.18pp；在KS-Need上NDCG@10达0.5173，较最强基线GRPO高1.24pp，Top5约束违反率降低1.54pp，且查询复杂度越高、约束越多，增益越显著。
### 核心结论
组合式电商查询的排序中，语义相关性是必要不充分条件，细粒度需求与商品可验证证据的对齐，比单纯提升相关性打分精度对用户体验的提升更大。
