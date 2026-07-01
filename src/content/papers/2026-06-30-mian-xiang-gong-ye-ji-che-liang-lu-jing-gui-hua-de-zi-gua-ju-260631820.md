---
title: Adaptive Cluster-First Route-Second Decomposition for Industrial-Scale Vehicle
  Routing
title_zh: 面向工业级车辆路径规划的自适应先聚类后路径分解方法
authors:
- Oguzhan Karaahmetoglu
- Hyong Kim
arxiv_id: '2606.31820'
url: https://arxiv.org/abs/2606.31820
pdf_url: https://arxiv.org/pdf/2606.31820
published: '2026-06-30'
collected: '2026-07-01'
category: Other
direction: LLM引导的大规模车辆路径规划优化
tags:
- LLM
- Vehicle Routing
- Cluster-First Route-Second
- Large-scale Optimization
- Decision Making
one_liner: 用LLM作为高层决策器实现自适应先聚类后路径分解，支撑50万客户级工业规模车辆路径规划
practical_value: '- 大规模分治类任务可借鉴LLM自适应选择算子的思路，替代固定分片规则，可落地到推荐大规模召回分块、广告人群定向分片等场景

  - 动态决策场景可复用「LLM监控任务状态+按需调用工具/算子」的架构，大幅降低多场景适配的开发成本

  - 超大规模优化任务可参考「先按容量约束联合聚类+再求解子问题」的分治思路，平衡算力开销与优化效果'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有带容量车辆路径规划（CVRP）的先聚类后路径（CFRS）方案依赖固定分片规则、预定义优化目标或学习策略，在空间、需求、运营特征不同的实例上表现不稳定，难以支撑工业级超大规模求解需求。
**方法关键点**：将分解过程建模为迭代决策流程，采用LLM作为高层决策者，动态分析当前分解状态，选择性调用聚类、均衡、精调算子；算法同步划分客户与车辆，实现容量感知的自适应聚类，适配每个问题的独有特征。
**关键结果**：在最多包含50万客户的合成与基准CVRP实例上验证，基准规模实例性能达到业界可比水平，超大规模问题上扩展性提升明显，路径质量稳定性更优。
