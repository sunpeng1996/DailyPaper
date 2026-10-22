---
title: 'Graph Topology Meets Energy-Driven Pathfinding: Preserving Contextual Consistency
  in Retrieval-Augmented Generation'
title_zh: 面向RAG上下文一致性保留的语义拓扑与能量驱动寻路框架
authors:
- Yufeng Li
- Zaijing Li
- Fuchen Zhang
- Zongzong Wu
- Ming Zhao
- Fengxiao Tang
affiliations:
- Central South University
- Harbin Institute of Technology, Shenzhen
arxiv_id: '2610.29933'
url: https://arxiv.org/abs/2610.29933
pdf_url: https://arxiv.org/pdf/2610.29933
published: '2026-10-21'
collected: '2026-10-22'
category: RAG
direction: 检索增强生成 · 多跳推理优化
tags:
- RAG
- Multi-hop QA
- Graph RAG
- Semantic Topology
- Energy Diffusion
one_liner: 提出ThreadRAG框架，通过语义拓扑图与能量驱动寻路解决Graph RAG的语义损失与模态 mismatch 问题
practical_value: '- 电商导购多轮问答RAG场景可复用Semantic Topology Graph（STG）的三元边构建逻辑：保留原文语义节点，用叙事/语义/lexical三类边建图，避免传统triplet抽取的语义损失

  - 多跳推理场景可直接复用Energy-Driven Pathfinding（EDP）的线性化方案：将离散子图按拓扑+叙事顺序拼接为连续文本，比LLM改写省token、无幻觉，总token成本可降至原方案23%

  - 商品/内容检索后的片段排序可借鉴EDP的能量扩散机制：以query匹配节点为锚点做PPR扩散选相关片段，再按文档+位置排序，提升上下文连贯性

  - 长文档知识结构化可复用论文中的轻量MLP语义分块方案：用蒸馏伪标签训练小模型分块，比固定长度chunk、LLM分块的latency更低、无生成噪声'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Graph RAG在多跳推理场景存在两大核心痛点：一是将文本转为离散三元组或固定长度chunk时损失大量上下文语义，破坏叙事连贯性；二是离散图结构与LLM预训练的连续文本模态不匹配，无论是直接输入图路径还是用LLM重写为文本，都会引入幻觉、信息遗漏或冗余，严重限制推理效果。

### 方法关键点
1. 核心框架ThreadRAG由Semantic Topology Mapper（STM）、Energy-Driven Pathfinding（EDP）、自适应推理Agent三部分组成
2. STM模块：先通过轻量RoBERTa+MLP分块得到保留完整上下文的Semantic Node，再构建三类边：叙事边（同文档相邻节点）、语义边（跨文档节点余弦相似度）、词汇边（实体共现Jaccard相似度），融合权重生成Semantic Topology Graph（STG）
3. EDP模块：以query匹配的高相关节点为锚点，通过PPR能量扩散得到query相关子图，剪枝后按文档+节点位置线性化为连续文本序列，直接作为LLM输入
4. 自适应Agent迭代判断上下文是否足够回答问题，不足则生成子query补充检索，更新STG后重新生成上下文

### 关键实验
在HotpotQA、2WikiMultihop、MuSiQue三个多跳QA基准上测试，对比IRCoT、HippoRAG、KnowTrace等14个SOTA基线：比文本基线IRCoT在HotpotQA上EM提升14.4%，比最优Graph RAG基线KnowTrace在2WikiMultihop上EM提升5.8%，总token成本仅为KnowTrace的23.3%。

### 最值得记住的一句话
Graph RAG的核心优化方向不是让LLM适配离散图结构，而是将图结构信息无损转化为LLM原生适配的连续文本序列，兼顾结构先验与语义完整性
