---
title: A Tree-based RAG Framework for Evidence-Intensive QA via Adaptive Planning
  and Topology-Aware Evidence Gathering
title_zh: 面向证据密集QA的自适应规划与拓扑感知树状RAG框架
authors:
- Songeun Lee
- Kyungjin Min
- Injae Na
- Suyeong Lee
- Chiyoung Kim
- Woohwan Jung
affiliations:
- Korea University
- Hanyang University
- Hyundai Motor Company
arxiv_id: '2609.04981'
url: https://arxiv.org/abs/2609.04981
pdf_url: https://arxiv.org/pdf/2609.04981
published: '2026-09-04'
collected: '2026-09-07'
category: RAG
direction: 检索增强生成 · 树状结构化RAG优化
tags:
- RAG
- Tree-Structured Reasoning
- Evidence-Intensive QA
- Adaptive Planning
- Batched Generation
one_liner: 提出APT-RAG树状RAG框架，显著提升证据密集QA效果同时降低推理延迟
practical_value: '- 电商场景下多文档聚合类需求（如全渠道商品参数整合、多来源售后问题解答、长周期用户行为分析）可复用拓扑感知证据收集策略，复用兄弟节点已生成的QA结果、子节点向上聚合结论，减少30%以上重复检索与LLM调用

  - 处理批量同属性查询（如多款商品的价格/库存/合规参数查询、多订单的物流状态汇总）时，可落地证据引导的批量回答生成方法，将共享同一证据源的查询聚类合并，最高降低40%长尾查询的推理延迟

  - 构建电商咨询Agent的RAG系统时，可替换固定推理路径为自适应规划逻辑，根据问题复杂度动态调整推理树深度，简单问题直接回答、复杂问题逐层分解，平衡回答准确率与响应速度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有结构化RAG在需要合成数十甚至上百份分散文档信息的证据密集QA场景下，存在两个核心瓶颈：一是结构僵化，预先构建的固定推理计划无法动态调整，单节点被迫处理过量证据易出现错误；二是忽略推理拓扑结构，仅在根节点聚合证据，无法复用子节点、兄弟节点的中间结果，证据覆盖率低且推理冗余度高。

### 方法关键点
- 自适应规划：以深度优先遍历递归构建推理树，每个节点先做可回答性检查，可复用兄弟节点结果则直接生成答案，否则判断是否需分解为子问题，动态调整推理树的深度与广度
- 拓扑感知证据收集：支持三类证据获取路径：横向复用前置兄弟节点已生成QA对、外部直接检索相关文档、纵向聚合子节点QA结果，避免重复检索与计算
- 证据引导批量回答生成：对共享高重叠证据的同类子查询做聚类，合并为单次LLM调用批量生成结果，大幅降低推理开销

### 关键结果
在证据密集QA基准MoNaCo（单问题平均需43.3份支撑文档）、QAMPARI（平均需13份支撑文档）上测试：使用Qwen3-30B作为基座时，APT-RAG在MoNaCo上较最优基线Plan*RAG的Answer F1提升8pp，检索召回提升11.5pp；批量生成模块平均降低41.4%推理延迟，95分位长尾查询延迟最高降低105.9s。

最值得记住的一句话：拓扑感知的动态推理树+多粒度证据复用策略，是解决大规模分散文档下复杂查询问题的核心可行路径。
