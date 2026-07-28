---
title: A corrective agentic hybrid RAG and an operations-grounded evaluation for a
  scientific facility
title_zh: 面向科研设施运营的纠错式智能混合RAG系统及落地评估
authors:
- Rajat Sainju
- Dariusz Jarosz
- Hairong Shang
- Michael Prince
- Ryan M. Aydelott
- Mathew J. Cherukara
- Yine Sun
- Michael D. Borland
affiliations:
- Argonne National Laboratory, USA
arxiv_id: '2607.24663'
url: https://arxiv.org/abs/2607.24663
pdf_url: https://arxiv.org/pdf/2607.24663
published: '2026-07-27'
collected: '2026-07-28'
category: RAG
direction: Agent混合RAG · 运营场景落地优化
tags:
- Hybrid_RAG
- Agentic_RAG
- GraphRAG
- RAG_Evaluation
- Knowledge_Graph
one_liner: 提出融合多通道检索的纠错式智能混合RAG，配套运营场景评估基准，较BM25基线严格关键信息召回提升6.4pp
practical_value: '- 多通道检索融合可复用：按查询意图动态分配稠密向量/BM25/知识图谱的RRF权重，比如电商搜索中商品ID、型号查询调高BM25权重，售后故障排查类query调高知识图谱权重，比固定权重效果更优

  - 低本高效的保真度优化：新增轻量自评审门控（用小模型判断答案是否有依据、是否切题），无需增加太多算力就能降低幻觉率，适合推荐系统的问答导购、售后智能助手场景控错

  - 组件优化优先级可参考：RAG系统迭代优先投入跨编码器重排模块，实验显示移除重排后严格关键信息召回直接下降32.8pp，收益远高于Agent纠错循环、知识图谱等模块，适合工程资源倾斜

  - 运营场景评估方法可复用：采用nugget级别的召回率+幻觉率评估，替代传统BLEU/ROUGE等表面相似度指标，更贴合业务场景对答案准确性的要求，适合电商客服、商品问答等场景的RAG效果评估'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大型机构的运营知识分散在日志、技术文档、聊天记录、实时控制系统等异构数据源，无统一检索入口，问题排查效率低，经验易随人员流动流失；普通RAG单通道检索准确率不足，生成内容幻觉率高，无法支撑高可靠性的运营决策需求。

### 方法关键点
- 检索层融合稠密向量（Qdrant + e5-large-v2）、稀疏关键词（Elasticsearch + BM25）、知识图谱三个通道，根据查询意图（事实类、多跳推理类、故障排查类等）动态调整三个通道的RRF融合权重
- 基于LangGraph搭建纠错Agent循环，自定义评分规则评估答案的相关性、证据支撑度、完整度，得分低于阈值时自动扩召回、重写查询，最多重试2轮；前置轻量自评审门控用小模型快速过滤不合格草稿，降低算力开销
- 知识图谱专门面向故障排查场景，抽取故障、组件、系统、日志等实体及因果关系，支持多跳路径查询还原故障-原因-解决链路
- 搭建运营场景评估基准APS-Bench，包含50道来自真实运营数据的QA对，采用严格关键信息召回率、幻觉率作为核心评估指标，替代传统表面相似度指标

### 关键结果数字
- 所有RAG变体的严格关键信息召回率均优于纯BM25基线（63.8%→65.5%~70.3%），完整的纠错式Agent GraphRAG达到最高的70.3%
- 跨编码器重排是影响最大的组件，移除后严格关键信息召回率大幅下降32.8%（p<1e-4）
- Agent纠错循环可降低幻觉率1.5pp，知识图谱对多跳、故障排查类query有正向收益，但整体提升幅度未达统计显著性

最值得记住的一句话：RAG系统工程迭代优先级中，跨编码器重排的收益远高于Agent循环、知识图谱等模块，低算力消耗的自评审门控是控制幻觉的高性价比方案
