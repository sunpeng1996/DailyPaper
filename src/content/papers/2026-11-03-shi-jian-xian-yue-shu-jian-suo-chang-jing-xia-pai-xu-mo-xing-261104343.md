---
title: Do Retrieval Ranking Models Capture Event Order? A Study of Timeline-Constrained
  Retrieval
title_zh: 时间线约束检索场景下排序模型的事件顺序感知能力研究
authors:
- Alon Eirew
- Lidan Avisar
- Kfir Bar
- Ido Dagan
affiliations:
- Bar-Ilan University
- Reichman University
arxiv_id: '2611.04343'
url: https://arxiv.org/abs/2611.04343
pdf_url: https://arxiv.org/pdf/2611.04343
published: '2026-11-03'
collected: '2026-11-04'
category: RecSys
direction: 检索排序 · 时序约束感知优化
tags:
- Temporal Retrieval
- Reranking
- Evaluation
- Event Order
- Semantic Matching
one_liner: 构建时间线约束检索评测数据集，验证现有检索模型时序感知缺陷，提出保序对齐方法大幅提升效果
practical_value: '- 电商场景下处理用户时序诉求检索（如「下单后退款再换货流程」「种草后下单发货收货全链路攻略」）时，可复用本文保序对齐思路：先拆分query为时序事件节点，对候选文档做事件时序预排序，用动态规划做保序匹配，大幅提升时序相关检索准确率

  - 现有语义检索、重排模型对时序约束的感知能力极弱，不要仅靠加「then」类连接词、时序prompt优化时序检索效果，单独抽取时序特征做外挂模块成本低收益高

  - 构建时序相关检索评测集时，可复用本文标注协议：先验证单个query事件的语义支持，再验证时序一致性，用LLM标注加人工抽检的方式大幅降低标注成本

  - 处理用户时序诉求的Agent（如电商客服Agent匹配历史案例、售后政策），可复用本文离线文档事件时序预排序方法，将非结构化的会话、政策、订单记录按事件时间重排，提升匹配效率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有语义检索模型仅关注语义匹配，无法捕捉query中事件的时序约束，比如用户搜索「灾害发生后先救援再重建」的相关报告，即使文档包含所有事件但顺序颠倒也会被误判为相关。这类时序约束检索需求在医疗、公共事务、电商等场景广泛存在，但现有模型的时序感知能力尚无系统评估，也缺乏可落地的优化方案。
### 方法关键点
- 构建时间线约束检索评测数据集：从6000+救灾报告中生成66个时序query，标注时先验证每个query事件是否在文档中存在语义支持，再验证事件时序是否与query一致，最终得到234个正样本，标注准确率经人工验证Cohen's κ达0.8
- 提出保序对齐（OP）重排方法：离线阶段先将每个文档的句子按事件发生的时序重新排序，在线阶段先计算query事件与文档句子的语义相似度矩阵，再用动态规划做保序序列匹配，加入query覆盖率正则项，仅对BM25召回的Top250候选重排，耗时1-5秒/query可落地
- 控制变量对比保序对齐与无顺序约束的匹配（OA），以及现有主流语义检索、重排模型的效果
### 关键结果
对比基线包括BM25、BGE-M3、E5-Large、Qwen3-Embedding、BGE-Reranker、MiniLM-L12等。实验显示：现有主流语义检索模型效果甚至低于BM25，加时序prompt或连接词无明显提升；保序对齐方法相比原生MiniLM-L12重排，MRR@10从0.57提升到0.70，mAP@10从0.32提升到0.50，相比无顺序的OA匹配，MRR@10提升27%以上，所有提升均在p<0.005水平显著。
### 核心结论
现有语义检索/重排模型的时序约束感知能力几乎为零，外挂轻量的保序对齐模块即可获得大幅收益，远好于靠大模型语义能力硬解时序问题。
