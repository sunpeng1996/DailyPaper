---
title: 'InductWave: Inductive Multi-Hop Logical Query Answering on Knowledge Graphs'
title_zh: InductWave：知识图谱上的归纳式多跳逻辑查询回答
authors:
- Mayank Kharbanda
- Michael Cochez
- Rajiv Ratn Shah
- Raghava Mutharaju
arxiv_id: '2607.07422'
url: https://arxiv.org/abs/2607.07422
pdf_url: https://arxiv.org/pdf/2607.07422
published: '2026-07-08'
collected: '2026-07-09'
category: Reasoning
direction: 知识图谱归纳式多跳查询推理
tags:
- Knowledge Graph
- Inductive Reasoning
- Multi-hop Query
- Graph Wavelet
- Query Answering
one_liner: 提出基于图小波的归纳式KG嵌入方法，用更少消息传递层实现SOTA多跳逻辑查询，支持训练未见实体推理
practical_value: '- 电商商品/用户知识图谱场景可复用该归纳式推理框架，无需全量实体训练即可支持新商品/新用户的多跳查询，降低训练资源开销

  - 搜索推荐的query理解链路可引入小波基消息传递机制，减少图神经网络层数同时保持推理精度，提升在线推理速度

  - Agent的知识库查询模块可集成该方法，解决训练阶段未见过的实体/关系的多跳逻辑问答问题，降低KG迭代后的重训成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有知识图谱（KG）多跳逻辑查询方法多为直推式推理，无法处理训练阶段未见过的实体，而大规模KG无法覆盖全量节点训练，资源开销过高，无法适配真实场景中实体持续新增的需求。

### 方法关键点
提出基于图小波的归纳式嵌入方法InductWave，仅用包含更少节点的训练集完成训练，即可在包含大量新实体的测试集上完成含与、或、非算子的多跳一阶逻辑查询，大幅精简消息传递层数量。

### 关键结果
- 仅用基线一半的消息传递层时，效果与基线持平
- 仅用基线75%的层数时，多数场景下效果超过所有SOTA模型
- 资源占用更低，可支持Wiki-KG这类超大规模图推理，在FB15k-237数据集的多组训练/测试图占比实验中均优于现有方法
