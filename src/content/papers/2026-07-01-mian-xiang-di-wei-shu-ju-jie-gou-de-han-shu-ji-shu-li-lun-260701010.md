---
title: Function-Counting Theory for Low-Dimensional Data Structures
title_zh: 面向低维数据结构的函数计数理论
authors:
- Konstantin Häberle
- Helmut Bölcskei
affiliations:
- ETH Zurich
arxiv_id: '2607.01010'
url: https://arxiv.org/abs/2607.01010
pdf_url: https://arxiv.org/pdf/2607.01010
published: '2026-07-01'
collected: '2026-07-06'
category: Other
direction: 机器学习理论 · 低维数据分类能力分析
tags:
- Learning Theory
- Binary Classification
- Low-dimensional Data
- Function Counting
one_liner: 优化Cover经典函数计数理论假设，构建适配低维数据的模型分类能力分析框架
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
真实数据普遍存在低维结构，传统Cover函数计数理论依赖通用位置假设，完全忽略数据本征结构，无法分析其对模型分类、泛化能力的影响，且该假设在低维场景下通常失效。
### 方法关键点
1. 优化通用位置假设，引入低维数据结构约束，推导可反映数据本征几何特征的二分计数结果；
2. 将Cover的分离容量、泛化问题分析框架扩展到低维数据场景，支持量化数据底层结构对两类指标的影响。
### 关键结果
纯理论推导类工作，无实证实验量化结果，填补了低维数据场景下函数计数分析框架的空白，为后续分析真实数据结构对模型能力的影响提供了数学基础。
