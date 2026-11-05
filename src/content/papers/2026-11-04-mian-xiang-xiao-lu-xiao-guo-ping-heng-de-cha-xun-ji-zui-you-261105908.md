---
title: Optimal Re-Ranking Depth
title_zh: 面向效率效果平衡的查询级最优重排序深度研究
authors:
- Siqing Huo
- Andrew Parry
- Debasis Ganguly
- Charles L. A. Clarke
affiliations:
- University of Waterloo
- University of Glasgow
arxiv_id: '2611.05908'
url: https://arxiv.org/abs/2611.05908
pdf_url: https://arxiv.org/pdf/2611.05908
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 搜索重排序 · 效率效果平衡优化
tags:
- Re-ranking
- Efficiency Optimization
- LLM Judge
- Query Performance Prediction
- DCG
one_liner: 基于LLM相关性标注提出IR-DCG@10指标，实现查询级动态重排序深度选择降本提效
practical_value: '- 架构层面可复用动态重排序深度思路，替代全局固定重排深度：对初排质量高的头部查询用浅深度、质量低的长尾查询用深深度，可大幅降低算力成本

  - 特征层面可借鉴IR-DCG@10设计：用轻量LLM judge对初排top10打相关性分作为深度选择特征，效果远优于传统QPP指标

  - 工程层面可复用百分位校准方法：将预测值映射到重排深度，可通过阈值灵活调整效率效果平衡，无需重新训练模型适配不同业务场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界重排序普遍采用固定全局深度，默认深度越深效果越好，但实际大量查询达到特定深度后效果不再增长甚至下降，造成算力浪费；此前人工标注成本过高，无法支撑大规模查询级深度分析，LLM自动标注的出现让该研究具备可行性，同时Agentic IR流程也需要判断是否继续重排、还是触发query改写/用户澄清的信号。

### 方法关键点
- 定义查询级最优重排序深度：达到该查询最大DCG@10的最浅深度，最小化不必要的重排计算
- 对比11种传统QPP预测指标，提出IR-DCG@10预测因子：用LLM judge对初排top10打相关性分计算DCG@10，直接衡量初排质量
- 采用百分位校准方法将预测值映射到重排序深度，支持通过阈值灵活调整效率与效果的平衡关系

### 关键实验
实验基于MSMARCO v1 DEV、TREC DL 2019数据集，初排器覆盖BM25、SPLADE，重排器覆盖MonoT5、MonoELECTRA，对比11种传统QPP方法。核心结果：IR-DCG@10在保持与全深度（1000）重排效果持平的前提下，平均重排深度降低3倍；Oracle最优选择下，检索效果提升7%以上，平均重排深度降低5倍；SPLADE这类高质量初排器的最优平均重排深度仅为20，固定深度20即可满足需求。

### 核心结论
重排序效果不会随深度单调上升，针对查询特性动态选择深度，是兼顾检索效率和效果的低成本优化方向。
