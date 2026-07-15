---
title: 'EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval'
title_zh: EvoGraph-R1：面向智能体检索的自进化多模态知识超图
authors:
- Jiashi Lin
- Changhong Jiang
- Xiangru Lin
- Ruifei Zhang
- Xinyi Zhu
- Jiyao Liu
- Cheng Tang
- Ye Du
- Shujian Gao
- Junzhi Ning
arxiv_id: '2607.12764'
url: https://arxiv.org/abs/2607.12764
pdf_url: https://arxiv.org/pdf/2607.12764
published: '2026-07-14'
collected: '2026-07-15'
category: RAG
direction: 多模态RAG · 自进化知识超图
tags:
- GraphRAG
- Multimodal RAG
- Knowledge Hypergraph
- Agentic Retrieval
- MDP
one_liner: 提出自进化多模态知识超图GraphRAG框架，将检索建模为MDP实现知识结构动态迭代优化
practical_value: '- 电商多模态商品知识库可借鉴自进化超图架构，支持用户交互过程中动态补全商品关联、修正错误知识，降低RAG幻觉

  - 可将Agent检索流程建模为MDP，在召回、网页补全、知识编辑、终止四类动作中自适应决策，大幅提升多跳检索准确率

  - 大促等知识快速更新场景可复用动态KG迭代逻辑，无需全量离线重建即可纳入新商品、新活动规则，降低运维成本'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有GraphRAG将知识图谱作为静态离线结构，与知识密集型推理的交互迭代特性错配，存在三大瓶颈：文本碎片化阻碍跨模态推理、结构固化无法纳入新证据修正错误、单遍检索无自适应优化。
### 方法关键点
提出EvoGraph-R1自进化GraphRAG框架，将知识超图重构为随Agent交互动态演化的环境，把检索流程建模为MDP，Agent可执行4类动作：知识检索（GraphRetrieve）、网页扩量（WebSearch）、图谱编辑（GraphEdit）、终止推理输出结果（Answer），动作执行过程同步重塑超图结构、生成反馈信号引导后续演化，形成闭环支持多跳推理。
### 关键结果
在多模态VQA、文本QA基准上，相比现有RAG基线在准确率、知识覆盖、可溯源性上均实现大幅提升。
