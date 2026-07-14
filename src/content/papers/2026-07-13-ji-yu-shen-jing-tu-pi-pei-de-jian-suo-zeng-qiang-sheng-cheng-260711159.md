---
title: 'NGM-RAG: Neural Graph Matching based Retrieval-Augmented Generation'
title_zh: 基于神经图匹配的检索增强生成框架NGM-RAG
authors:
- Guo Chen
- Ziwen Li
- Maolin Zheng
- Hao Gao
- Junjie Huang
- Tao Jia
affiliations:
- Southwest University
- Beijing Institute of Control Engineering
arxiv_id: '2607.11159'
url: https://arxiv.org/abs/2607.11159
pdf_url: https://arxiv.org/pdf/2607.11159
published: '2026-07-13'
collected: '2026-07-14'
category: RAG
direction: 检索增强生成 · 图匹配性能优化
tags:
- RAG
- Neural Graph Matching
- GNN
- Multi-hop Reasoning
- Long Context Summarization
one_liner: 融合文本匹配与GNN图匹配的RAG框架，提升多跳推理性能同时大幅降低token成本
practical_value: '- 电商商品/客服问答场景可直接复用三阶匹配策略：先通过编辑距离匹配实体名召回高相关节点，再用BM25匹配节点文本语义，最后叠加GNN捕捉商品-属性-品牌等关联关系，显著提升「XX品牌防水千元机有哪些」这类多跳query的回答准确率

  - 工程落地可直接采用默认权重λ1=λ2=1融合多匹配信号，无需复杂超参数调优即可达到最优效果，大幅降低上线成本

  - 垂直领域RAG场景可复用其成本优化思路，通过图匹配过滤冗余上下文，Token成本较普通RAG降低90%以上，延迟低于LightRAG等现有GraphRAG方案，适配高并发搜索推荐场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统RAG依赖纯文本语义检索，无法有效捕捉实体间的关联关系，在需要多跳推理的复杂问题上容易召回无关上下文，导致回答错误；现有GraphRAG方案普遍存在检索精度不足、推理成本高、延迟大的问题，难以落地到高并发工业场景。
### 方法关键点
- 统一框架包含三个核心模块：先用LLM从语料和用户query中分别提取知识图谱，节点附带名称、类型、描述属性，边附带关系描述；再通过图匹配召回高相关节点；最后输入LLM生成答案。
- 图匹配融合三类互补信号：基于Levenshtein距离的实体名直接匹配、基于BM25的节点文本语义匹配、基于GNN的结构匹配（支持无参数LightGCN或带参数GINE，GINE用对比损失训练优化）。
- 三类匹配得分通过自适应加权融合，取Top-k关联节点的上下文作为生成输入，默认权重λ1=λ2=1即可达到最优效果。
### 关键实验
在HotpotQA、MultiHop-RAG两个多跳QA数据集，以及UltraDomain长摘要数据集上测试，对比NaiveRAG、GraphRAG、LightRAG等主流基线。以DeepSeek-R1 API为底座时，HotpotQA上EM达0.506、F1达0.654，较LightRAG分别提升17%、18.7%；平均单query Token成本仅808，较NaiveRAG降低90%以上，推理延迟也低于其他GraphRAG方案。
### 核心结论
文本语义匹配与图结构匹配的多信号融合，是同时提升RAG效果、降低推理成本的核心可行路径
