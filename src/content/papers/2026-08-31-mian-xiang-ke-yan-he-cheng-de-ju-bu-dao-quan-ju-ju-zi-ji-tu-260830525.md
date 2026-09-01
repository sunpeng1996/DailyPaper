---
title: Local-to-Global Sentence-Level Graph Reranking for Scientific Synthesis
title_zh: 面向科研合成的局部到全局句子级图重排序框架LoG-Reranker
authors:
- Zheng Dou
- Zhao Zhang
- Hao Geng
- Ningjing Wang
- Deqing Wang
affiliations:
- Beihang University
- Zhongguancun Laboratory
arxiv_id: '2608.30525'
url: https://arxiv.org/abs/2608.30525
pdf_url: https://arxiv.org/pdf/2608.30525
published: '2026-08-31'
collected: '2026-09-01'
category: RAG
direction: RAG检索增强 · 细粒度重排序优化
tags:
- Reranking
- Fine-grained Retrieval
- Graph Neural Network
- Scientific Synthesis
- RAG
one_liner: 结合角色感知局部打分与全局图建模，提升RAG科学合成的可信度与信息覆盖度
practical_value: '- RAG重排序可从段落级下沉到句子级，结合query意图与内容角色（如电商的商品参数、卖点、评价标签）做匹配打分，大幅提升上下文精准度，减少无效内容占用LLM窗口

  - 跨召回结果的全局关系建模可复用：对同角色、高语义相似的内容节点建边做图传播重排，既能避免信息冗余，又能补全多来源互补信息，适合电商多商品对比、多评论聚合类Agent问答场景

  - 重排后的上下文无需使用扁平列表，可搭配相邻上下文+相似关联内容做结构化输出，相同上下文长度下可提升LLM生成的信息覆盖度与逻辑连贯性，适合商品评测、详情文案生成场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG重排序多为段落级独立打分，一方面粗粒度筛选易将关键细节埋在长上下文中，导致生成内容可信度不足；另一方面忽略候选间的互补、对比关系，生成内容信息覆盖度不全，无法满足需整合多来源信息的复杂生成场景需求。

### 方法关键点
- 局部打分阶段：将召回段落拆分为句子，联合编码query与段落所有句子，预测query意图与句子角色（背景/方法/结果三类），通过意图-角色匹配度+语义相似度计算句子局部relevance分数
- 全局图重排阶段：构建跨段落句子图，节点特征融合语义表示、角色分布、局部分数；边分为段落内连续句子的邻接边、跨段落同角色高相似句子的关联边两类，用关系感知图注意力编码器传播信息，输出全局重排分数
- 结构化上下文构造：选取TopK高打分句子，补充其段落内相邻句+跨段落相似关联句，按全局分数排序后作为生成输入，保留上下文关联

### 关键结果
在ScholarQABench 7个科研合成数据集上和9个SOTA基线对比，重排序阶段14/15项指标最优，MAP相对最优基线最高提升1.36个点；生成阶段所有指标最优，citation F1最高提升1.52个点，信息覆盖度、逻辑性、相关性均显著优于基线。

### 核心结论
RAG的重排序不只是做相关性排序，本质是面向下游生成任务的上下文提纯，细粒度语义匹配+全局关系建模+结构化输出的组合，能在不增加上下文长度的前提下大幅提升生成质量。
