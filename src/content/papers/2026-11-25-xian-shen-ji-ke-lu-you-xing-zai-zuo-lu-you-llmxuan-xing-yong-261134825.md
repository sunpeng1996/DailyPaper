---
title: 'Routeability Before Routing: Routeability Audit Protocol (RAP) and RouteabilityBench
  for Audited LLM Model Selection'
title_zh: 先审计可路由性再做路由：LLM选型用RAP协议与RouteabilityBench基准
authors:
- Yihang Lu
- Denica Kjorvezir
- Ana Gjorgjevikj
- Carola Doerr
- Tome Eftimov
affiliations:
- Sorbonne Université
- CNRS
- Jožef Stefan Institute
- INRAE
- LIP6
arxiv_id: '2611.34825'
url: https://arxiv.org/abs/2611.34825
pdf_url: https://arxiv.org/pdf/2611.34825
published: '2026-11-25'
collected: '2026-11-26'
category: Eval
direction: LLM路由评估 · 可路由性审计
tags:
- LLM Routing
- Evaluation Protocol
- Benchmark
- Model Selection
- Routeability
one_liner: 提出可路由性前置审计框架RAP与配套基准，验证多数场景下LLM路由增益不如单最优模型
practical_value: '- 落地多LLM路由（如电商多场景Agent、多模型文案生成/query改写）前，先跑可路由性诊断，计算SBS/VBS头room、平局模型占比，避免在头room不足/平局过多的场景浪费资源开发复杂路由

  - 路由效果评估复用tie-aware的regret、gap closure指标，替代传统单winner准确率，避免大量平局导致的评估结果失真，更贴合业务真实收益

  - 优先在多粒度评分、平局少的场景落地路由（如复杂商品属性问答、数学类工具调用），这类场景比二分类简单任务更容易拿到稳定路由增益

  - 构建LLM模型池时不要仅选平均得分最高的模型，按prompt维度的性能分布聚类选差异大的模型，保证路由有足够的优化空间'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM路由研究默认只要搭建模型池就能通过路由获得比单最优模型（SBS）更好的效果，但多数基准数据集存在大量模型得分平局，单最优模型本身已接近性能上限，复杂路由很难拿到实际收益，缺乏前置的可路由性校验机制，导致很多路由效果结论泛化性极差。
### 方法关键点
- 提出可路由性审计协议RAP，为后置审计流程，在拿到模型池-基准的得分矩阵后、解读路由对比结论前运行，包含5项核心诊断：SBS/VBS头room、平局模型分布、嵌入-性能相关性、强制路由regret、选择性路由校准性
- 配套开源RouteabilityBench工具包，内置30个固定种子的数据集划分、prompt ID对齐校验、家族校正统计检验、一键验真脚本，覆盖4个主流LLM基准、66个不同权限的LLM模型得分矩阵
- 采用tie-aware评估体系，不使用严格单winner准确率，以regret、gap closure为核心指标，避免大量平局导致的评估不稳定
### 关键实验结果
在Omni-MATH、GPQA、MMLU-Pro、IFEval 4个基准、66个LLM模型上测试，对比多种路由优化手段：
1. 仅Omni-MATH场景路由能拿到正收益，gap closure为8.1%，其余3个场景路由gap closure均为负，效果不如直接用单最优模型
2. 所有通用路由优化手段（多嵌入视图、PCA降维、选择性弃权、聚类、更强回归器）都无法在全数据集上稳定超过单最优模型，仅IFEval场景用ExtraTrees回归器能比Ridge降低1.64%的regret，但仍未超过单最优模型
3. 模型池规模≥33时Omni-MATH场景路由收益才稳定为正，小模型池场景路由很难优于单最优模型

可路由性头room是LLM路由有效的必要非充分条件，所有路由增益结论都需要和可路由性诊断、平局分析、模型池构建细节、校正后的统计检验一起发布，不能脱离场景谈路由效果
