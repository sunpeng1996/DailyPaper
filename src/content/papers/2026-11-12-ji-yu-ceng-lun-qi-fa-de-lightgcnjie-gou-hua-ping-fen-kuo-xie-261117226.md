---
title: Sheaf-Inspired Structured Scoring Extensions of LightGCN for Collaborative
  Filtering
title_zh: 基于层论启发的LightGCN结构化评分扩展协同过滤方法
authors:
- Ksenia Belkovskaya
- Timur Lidzhiev
- Maria Stebliy
- Alexander Tarakanov
arxiv_id: '2611.17226'
url: https://arxiv.org/abs/2611.17226
pdf_url: https://arxiv.org/pdf/2611.17226
published: '2026-11-12'
collected: '2026-11-13'
category: RecSys
direction: 协同过滤 · LightGCN 评分模块优化
tags:
- Collaborative-Filtering
- LightGCN
- Graph-RecSys
- Scoring-Function
- Recommendation
one_liner: 在3层LightGCN上新增层论启发的模块化结构化评分头，对比不同打分器的排序与覆盖效果
practical_value: '- 可直接将现有LightGCN的内积打分替换为结构化打分头，无需修改backbone传播逻辑，兼容现有部署链路，AB实验迁移成本极低

  - 可根据业务对排序精度/长尾曝光的优先级，选择参数量匹配的对角矩阵/低秩矩阵/全矩阵变体，权衡效果与算力开销

  - 若业务核心诉求是提升catalog覆盖度、增加长尾商品曝光，可优先尝试结构化打分头，其覆盖度提升幅度远高于精度变化'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有LightGCN依赖用户与item embedding内积计算匹配度，默认二者共享同一embedding坐标空间，无法显式建模用户与item表征之间的异构转换关系，打分灵活性不足，也难以兼顾覆盖度需求。
### 方法
不对图传播逻辑做修改，仅在3层LightGCN backbone之上新增层论启发的模块化结构化打分扩展，引入pair-dependent的embedding转换，对比5种参数量匹配的打分方案：原生内积、对角矩阵、秩1低秩矩阵、全矩阵残差打分、残差MLP基线，在4个公开推荐数据集上验证top10/top20的排序质量与catalog覆盖度。
### 结果
结构化打分变体的排序质量提升幅度较小且强依赖数据集，无普适性精度收益；部分场景下可带来显著的覆盖度提升；实验未证明层论几何本身的因果增益，仅结构化打分设计有效。
