---
title: 'BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation Paradigms'
title_zh: 大规模场景下BM25胜出：四类RAG范式的可扩展性对比研究
authors:
- Pengyu Wang
- Benfeng Xu
- Shaohan Wang
- Xin Zeng
- Huarui Wu
- Lei Zhang
- Licheng Zhang
affiliations:
- University of Science and Technology of China
- Metastone Technology
- Beijing Academy of Agriculture and Forestry Sciences
arxiv_id: '2607.26497'
url: https://arxiv.org/abs/2607.26497
pdf_url: https://arxiv.org/pdf/2607.26497
published: '2026-07-29'
collected: '2026-07-31'
category: RAG
direction: RAG范式 大规模选型与性能对比
tags:
- RAG
- BM25
- Dense Retrieval
- GraphRAG
- Agentic Retrieval
- Scaling Law
one_liner: 基于450倍语料规模的受控实验，揭示RAG范式的规模依赖效应，10M token后BM25显著领先
practical_value: '- 电商/企业知识库RAG选型：语料规模超过10M token时直接选BM25作为默认检索底座，无需盲目上GraphRAG或纯Agent遍历，成本更低效果更优

  - Agent+RAG架构优化：不要让Agent直接遍历原始语料，先通过BM25做全局召回缩小候选集，再用Agent做精细化推理，可将query token消耗降至1/9，效果提升14个点以上

  - GraphRAG落地约束：除非业务70%以上查询为强关系类问题，否则十万/百万级语料场景下GraphRAG构建成本极高，性价比远低于BM25

  - RAG选型验证规范：做跨范式对比时必须测试多规模嵌套语料，单语料规模下的结论存在严重误导性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有RAG范式（词法、稠密、图、Agent检索）的评估均在单一语料规模下开展，不同范式的精度-成本随规模的变化规律完全不清晰，而企业级知识库动辄数十万文档且持续增长，选型缺乏可落地的规模依赖参考依据。

### 方法关键点
- 设计28层严格嵌套的语料梯队，覆盖1.7M~601M token（约450倍规模差），固定所有问题、相关文档、对抗负样，仅新增无关背景语料实现严格控制变量
- 统一使用Qwen3.6-27B作为reader和Agent策略模型，Qwen3-Embedding-0.6B作为共享embedding模型，统一token计量和评判协议，对比4类共7种RAG pipeline的精度、构建/查询token消耗、延迟
- 开展控制变量实验拆分Agent策略和检索底座的效果贡献，定位不同范式的缩放瓶颈

### 关键实验结果
基于EnterpriseRAG-Bench的51万+文档、500个企业级问题，对比BM25、DenseRAG、4种GraphRAG、文件系统Agent的表现：
1. 规模交叉效应：10M corpus token以下Agent检索效果最优，超过该阈值BM25反超，全规模（601M token）下BM25得分50.5，比Agent高19.8分，比DenseRAG高20.6分
2. 成本对比：Agent单query token消耗是BM25的39~60倍，GraphRAG构建成本极高，LightRAG全规模构建预估需要4实例年，远高于BM25的零LLM构建成本
3. 优化组合效果：Agent+BM25架构全规模下得分69.4，比纯Agent高32.5分，token消耗仅为纯Agent的1/9

**最值得记住的结论**：全局词法排序是大规模企业语料下的最优RAG默认选项，Agent推理应该放在召回缩圈之后，而不是替代全局检索
