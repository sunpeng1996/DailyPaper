---
title: 'TRIAGE: Trustworthy Retrieval Instrumentation And Graph Evaluation'
title_zh: TRIAGE：面向Graph-RAG的分阶段可信赖评估框架
authors:
- Axel TahmasebiMoradi
- Lucas Schott
- Martin Royer
affiliations:
- IRT-SystemX
arxiv_id: '2607.03447'
url: https://arxiv.org/abs/2607.03447
pdf_url: https://arxiv.org/pdf/2607.03447
published: '2026-07-03'
collected: '2026-07-07'
category: Eval
direction: Graph-RAG 可信赖性评估框架
tags:
- Graph-RAG
- Knowledge Graph
- Trustworthiness
- Evaluation
- Retrieval
one_liner: 为Graph-RAG全链路提供分阶段无黄金标注的信任度度量与故障定位能力
practical_value: '- 拆分Graph-RAG全链路为知识构建、校验、推理三个阶段，每个阶段新增可观测指标，避免仅靠最终回答判断效果导致的故障漏检，电商商品/售后知识图谱构建场景可直接复用TCS指标过滤低质量LLM抽取结果

  - 落地无黄金标注的在线监控指标：QGR（查询实体匹配率）、ERC（检索实体覆盖率）、RRS（子图连通性），无需标注即可实时监控检索质量，可用于电商多跳咨询、Agent工具调用前的有效性校验

  - 复用预推理triage机制：生成回答前先判断检索子图有效性，低于阈值直接切换普通RAG或兜底话术，同时可结合RPC（检索路径成本）指标平衡效果与推理时延，降低大模型调用成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Graph-RAG依赖的知识图谱大多由LLM自动抽取构建，现有评估仅以最终回答正确性为标准，无法定位故障来自抽取、图谱构建还是检索阶段，也未纳入检索时延、算力成本维度；同时LLM可通过参数知识补全检索缺失的信息，输出看似正确的回答，导致大量检索隐形故障无法被发现，且多数评估指标依赖黄金标注无法在线部署。
### 方法关键点
- 全链路拆分为KG实现（抽取构建）、KG校验（专家审核）、KG使用（检索推理）三个独立阶段，每个阶段设计专属度量指标，80%以上指标无需黄金标注，仅离线校准指标需要标注数据
- KG实现阶段设计TCS（基于LLM token概率的三元组置信分）、SCR（源文本抽取覆盖率）等指标，量化抽取质量，可直接用于低质量三元组过滤
- KG校验阶段设计DNR（死节点率）、SRR（语义冗余率）等指标，衡量图谱整体结构质量，指导实体融合、schema优化
- KG使用阶段设计QGR（查询实体匹配率）、RRS（检索子图连通性）等预推理指标，在调用生成大模型前即可判断检索有效性，同时纳入RPC（检索路径成本）、RHD（推理跳数）等成本指标，平衡效果与时延
- 所有指标组成故障诊断链，首个失效指标直接定位故障阶段，对应给出抽取优化、图谱优化、检索策略优化的修复方向
### 关键结果
在多跳KGQA探针上验证，当检索缺失必要证据时，LLM仍有62%概率输出看似正确的回答，传统仅评估回答的方案漏检41%的检索故障，而TRIAGE的预推理指标可100%识别这类隐形检索故障。

最值得记住的一句话：Graph-RAG评估不能仅看最终回答，要在生成前度量检索子图的结构有效性，才能定位隐形故障
