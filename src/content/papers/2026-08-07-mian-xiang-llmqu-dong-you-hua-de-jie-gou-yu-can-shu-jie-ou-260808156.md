---
title: A Hybrid Nested Harness for Decoupling Structure and Parameters in LLM-Driven
  Optimization
title_zh: 面向LLM驱动优化的结构与参数解耦混合嵌套框架
authors:
- Víctor Gallego
affiliations:
- Komorebi AI Technologies
arxiv_id: '2608.08156'
url: https://arxiv.org/abs/2608.08156
pdf_url: https://arxiv.org/pdf/2608.08156
published: '2026-08-07'
collected: '2026-08-11'
category: LLM
direction: LLM驱动优化 · 结构参数解耦
tags:
- LLM-driven Optimization
- Hybrid Nested Search
- Evolutionary Algorithm
- Numerical Optimization
- Pluggable Framework
one_liner: 提出结构与参数解耦的混合嵌套搜索框架，性能超越纯LLM及纯数值优化基线
practical_value: '- 推荐系统超参/策略迭代场景可复用该嵌套架构：LLM生成召回规则分支、排序逻辑等结构，内层用CMA-ES/梯度法调阈值、权重等数值参数，降低LLM
  token消耗的同时提升优化效率

  - Agent控制流/工具调用优化时，可解耦结构（调用流程、工具组合逻辑）与参数（调用阈值、超时时间），分别用LLM和数值优化器迭代，大幅降低纯LLM试错成本

  - 生成式推荐prompt优化场景可将prompt拆解为结构模板与可调参数（温度系数、召回topK阈值），分别迭代提升优化效果'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LLM驱动的进化算法中，LLM需同时更新结构（如控制流、逻辑分支）和连续数值参数，但其在连续参数优化上效率极低，会消耗大量token反复试错，效果远弱于传统数值优化器。

### 方法关键点
1. 解耦优化任务为结构层、参数层两类子任务，提出混合嵌套搜索框架；
2. 外层循环由LLM生成带数值空位的结构草图（如代码逻辑、控制流框架），发挥LLM常识与结构设计能力；
3. 内层循环接入可插拔的数值优化器（支持零阶CMA-ES、梯度法、MCMC采样器等），对结构中的数值参数做高效调优；
4. 内外层求解器完全可插拔，支持任意文本优化器与数值优化器自由组合。

### 关键结果
在闭式测试函数元优化、系统研究/社会困境代码策略、近似贝叶斯推理三类任务上，混合框架效果全面优于纯LLM驱动搜索、纯数值优化两类基线。
