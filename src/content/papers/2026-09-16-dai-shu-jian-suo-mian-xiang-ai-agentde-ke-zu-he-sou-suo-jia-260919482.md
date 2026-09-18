---
title: 'Algebraic Retrieval: Composable Search for Agents'
title_zh: 代数检索：面向AI Agent的可组合搜索框架
authors:
- Damian Delmas
affiliations:
- Independent Researcher, Vancouver, BC
arxiv_id: '2609.19482'
url: https://arxiv.org/abs/2609.19482
pdf_url: https://arxiv.org/pdf/2609.19482
published: '2026-09-16'
collected: '2026-09-18'
category: Agent
direction: Agent 可组合检索能力增强
tags:
- Agent
- Composable Search
- Programmatic Embedding
- Vector Retrieval
- Query Optimization
one_liner: 提出面向AI Agent的代数检索范式，支持查询时动态组合检索规则，执行分数误差低于1e-6
practical_value: '- 电商/广告多目标检索可复用该代数范式：把语义相关、时效权重、负向偏好、准入约束（如排除已购/临期商品）组合为单条查询表达式，减少多阶段
  pipeline 冗余，提升链路可解释性

  - 工程上可借鉴向量运算合并优化：将多语义偏好的多次相似度计算合并为单次矩阵乘（如直接用q1-0.5*q2作为查询向量），降低检索耗时，保证分数逻辑等价

  - Agent 调用检索工具可引入orient接口机制：先查询当前可用的候选池、权重、向量等资源列表，自主生成合法检索表达式，无需硬编码工具参数'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent检索接口仅支持单查询加少量参数，无法灵活组合多维度相关度规则、准入约束、排序偏好，需要多次调用检索+后处理才能实现复杂策略，链路冗长且可解释性差。
### 方法关键点
- 基于PEM暴露检索过程中的向量、分数计算能力，设计代数查询语法，支持相似度加减/缩放、候选池mask过滤、单样本权重加权、top-k截断等操作的自由组合
- 内置查询优化：将多组相似度计算合并为单次矩阵乘（如(E@q1)-0.5*(E@q2)等价为E@(q1-0.5q2)），减少计算量，保证分数数学等价
- 提供orient元数据查询接口，Agent可先获取当前可用的候选池、权重、查询向量等资源，再生成合法检索表达式，也可基于返回结果动态修改规则迭代检索
### 关键实验
在11429篇文档的公开Vaswani数据集上，对比代数检索实现、SQL、PyTerrier三种方案的执行一致性：
1. 三组不同复杂度的检索程序返回的文档集完全一致，分数差异均低于1e-6
2. 仅1组因float32浮点精度差异导致1对分数完全相同的文档排序不同，其余排序完全一致
### 核心结论
数值一致性不等于排序一致性，小于两倍浮点误差的分数差可能出现排序反转，复杂检索链路的一致性验证需要同时校验文档集、分数、排序三个维度
