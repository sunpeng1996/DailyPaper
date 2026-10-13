---
title: Fast Gradient-Based Approximation of Continuous Dynamic Time Warping
title_zh: 连续动态时间规整的快速梯度驱动近似算法
authors:
- Pierre Houedry
- Romain Tavenard
- Nicolas Courty
- Romaric Gaudel
affiliations:
- INRIA Rennes
- IRISA, UMR 6074, CNRS, Université de Rennes
- IRISA, UMR 6074, CNRS, Université de Bretagne Sud
arxiv_id: '2610.13129'
url: https://arxiv.org/abs/2610.13129
pdf_url: https://arxiv.org/pdf/2610.13129
published: '2026-10-09'
collected: '2026-10-13'
category: Other
direction: 时间序列相似度度量 · 可微DTW优化
tags:
- DTW
- Time Series Similarity
- Differentiable Metric
- GPU Acceleration
- Monte Carlo Estimator
one_liner: 提出GPU友好的FastCDTW算法，两种求解策略大幅降低CDTW计算成本且支持梯度回传
practical_value: '- 电商用户行为序列相似度计算场景（如相似用户召回、冷启动用户群匹配）可替换现有DTW/欧氏距离，兼顾计算效率与可微性，支持端到端训练

  - 会话推荐、时序用户建模等场景中，可直接将FastCDTW嵌入深度学习 pipeline，无需额外做时序对齐预处理

  - GPU友好的实现可直接适配现有推荐系统大规模并行训练框架，几乎无额外工程改造成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
DTW是时序相似度度量的主流方案，但原生实现依赖动态规划，速度慢且不可微；现有Soft-DTW、CDTW等改进方案计算成本仍过高，无法适配大规模机器学习流水线。
### 方法关键点
1. 首先证明CDTW在宽松约束下具备可微性
2. 提出FastCDTW两类高效近似求解策略：针对分段线性规整函数的精确闭式求解方案、针对光滑规整函数（如隐式神经网络）的无偏蒙特卡洛估计器
3. 两类策略均支持对规整函数、输入时序的梯度计算，天然适配GPU并行架构
### 关键结果
在时序平均、时序分类、深度域适配三类任务上验证算法有效性，相比现有CDTW实现计算效率提升1个数量级以上，可直接嵌入大规模端到端训练流程。
