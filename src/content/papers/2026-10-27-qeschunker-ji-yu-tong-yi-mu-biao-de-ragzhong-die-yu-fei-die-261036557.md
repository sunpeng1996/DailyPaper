---
title: 'QESChunker: A Single Objective Unifies Overlapping and Non-Overlapping Chunking
  for RAG'
title_zh: QESChunker：基于统一目标的RAG重叠与非重叠分块框架
authors:
- Yifan Zhao
- Qianyang Zhao
- Xinyu Guan
- kai wei
- Yuming Deng
affiliations:
- Alibaba Group
- Taobao (China) Software Co., Ltd.
arxiv_id: '2610.36557'
url: https://arxiv.org/abs/2610.36557
pdf_url: https://arxiv.org/pdf/2610.36557
published: '2026-10-27'
collected: '2026-10-28'
category: RAG
direction: RAG · 文档分块优化
tags:
- RAG
- Chunking
- Submodular Optimization
- Dynamic Programming
- Retrieval
one_liner: 通过问题-证据监督构造统一分块目标，支持非重叠DP最优解与重叠贪心近似解，提升RAG证据召回
practical_value: '- 电商FAQ、商品详情页、政策类高复用静态文档的RAG分块可直接复用这套框架：非重叠场景用DP求全局最优分块，重叠场景用成本效益贪心算法，相同检索预算下提升完整证据召回率，尤其适配客服问答、商品信息查询等低返回预算场景

  - 分块的分层结构先验可直接复用：段落>句子>分句>任意位置的权重设计，能在不损失召回的前提下让分块更符合语义边界，降低人工调整分块规则的成本

  - 冷启动无标注数据时，可先用LLM生成文档对应问题-证据对作为监督信号，不需要标注测试查询就能训练分块器，适合业务快速落地

  - 低返回预算场景下优先开启非重叠分块的整段例外规则，可额外提升1pp左右的完整证据召回'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG的分块是预处理核心步骤，但现有分块方法大多基于启发式规则，无法针对检索目标优化完整证据召回率，且重叠、非重叠分块场景缺乏统一优化框架，高召回要求、低返回预算的场景下效果瓶颈明显。

### 方法关键点
- 提出统一的hit-gated效用最大化目标，包含证据覆盖项和分层结构先验项，同时适配重叠、非重叠两种分块约束
- 非重叠场景下目标可分解为单块效用之和，通过动态规划算法在多项式时间内求得全局最优分块，额外支持整段例外规则适配长段落语义单元
- 重叠场景下目标为单调子模函数，NP-hard无法求精确解，提出带单例保护的懒加载成本效益贪心算法，可达到(1-1/√e)≈0.393的近似比

### 关键实验
在2个自建中文政策数据集+3个公开英文数据集上对比固定长度切分、语义聚类分块、LLM分块等10余种基线，相同检索和返回预算下：非重叠DP版本在9/10的测试组中排名第一，最大相对提升3.98pp完整证据召回；重叠贪心版本在10/10的测试组中排名第一，最大相对提升8.11pp，且在低返回预算下优势更明显。

### 核心结论
对于高复用、有充足历史查询的静态文档，将分块从启发式预处理转为有监督的预算感知优化问题，可在不增加检索成本的前提下显著提升RAG的证据召回效果。
