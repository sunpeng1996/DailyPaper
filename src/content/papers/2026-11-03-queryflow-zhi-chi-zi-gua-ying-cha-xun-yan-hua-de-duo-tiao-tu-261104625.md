---
title: 'QueryFlow: Multi-Hop Graph Retrieval with Adaptive Query Evolution'
title_zh: QueryFlow：支持自适应查询演化的多跳图检索框架
authors:
- Manzong Huang
- Chenyang Bu
- Yi He
- Jiapu Wang
- Xindong Wu
affiliations:
- Hefei University of Technology
- College of William and Mary
- Nanjing University of Science and Technology
arxiv_id: '2611.04625'
url: https://arxiv.org/abs/2611.04625
pdf_url: https://arxiv.org/pdf/2611.04625
published: '2026-11-03'
collected: '2026-11-04'
category: RAG
direction: 多跳RAG · 自适应查询演化
tags:
- GraphRAG
- Multi-hop Retrieval
- Query Evolution
- GNN
- Question Answering
one_liner: 耦合图证据传播与隐式查询演化，提升多跳RAG证据召回率与下游问答准确率
practical_value: '- 电商商品多跳关联检索、售后多轮问题求解场景可复用查询演化逻辑：不用显式改写文本query，仅通过隐式query状态迭代控制图传播的边界与关系权重，降低token开销

  - GraphRAG落地可借鉴双路反馈设计：边界反馈将迭代后的query状态重新注入问题关联实体，关系反馈按当前检索目标动态调制不同关系的特征权重，提升长链路证据召回率

  - 多目标检索损失可以复用：将listwise损失与加权二分类交叉熵结合，兼顾整体证据集的完整性和单个实体的区分度，适合需要召回全量关联证据的业务场景

  - 最终打分锚定初始query的设计可借鉴：避免演化后的query偏离用户原始意图，平衡上下文感知的检索拓展和初始需求的对齐度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多跳RAG的图检索方案大多采用固定原始查询条件，仅更新实体节点表征，无法根据已召回的中间证据动态调整检索目标，容易遗漏仅在推理链路中才体现相关性的补全证据，导致支持证据集召回不全，下游多跳问答准确率低，且显式改写查询的方案会带来额外的token开销与延迟。
### 方法关键点
- 框架将多跳检索建模为证据表征与查询条件的耦合演化过程，迭代交替执行图消息传播和隐式查询状态更新，无需生成显式改写文本
- 设计双路反馈机制控制图传播：边界反馈将更新后的查询状态重新注入问题关联实体，关系反馈用当前查询状态生成门控调制不同关系的特征权重，动态调整下一轮传播的范围与路径
- 每轮传播后用前序查询状态作为注意力query聚合全图实体表征，通过GRU更新共享隐式查询状态，无额外LLM调用开销
- 最终实体打分锚定初始原始query，避免演化后的查询偏离用户原始意图，实体得分通过逆文档频率加权聚合为文档排序结果
### 关键结果
在2WikiMultiHopQA、HotpotQA、MuSiQue、ConcurrentQA 4个多跳QA数据集上，对比GFM-RAG、LinearRAG、HippoRAG2等主流基线，宏观R@10、FR@10、LLM-Acc分别提升4.98、8.40、8.0个百分点；在线推理时间较GFM-RAG降低90.3%，token消耗降低34.1%，仅用5个召回文档即可达到GFM-RAG召回10个文档的全量证据召回率。
### 核心结论
多跳检索的核心是完整召回整个证据链而非单个高相关文档，隐式查询演化比显式query改写的成本更低、效率更高，更适合业务落地
