---
title: Fast and Efficient Approximate Nearest Neighbor Search for High-Dimensional
  LLM Embeddings
title_zh: 面向高维LLM嵌入的快速高效近似最近邻搜索
authors:
- Nico Hezel
- Kai Uwe Barthel
- Bruno Schilling
- Konstantin Schall
- Andre Moelle
- Klaus Jung
affiliations:
- HTW Berlin, Germany
- vviinn, Berlin, Germany
arxiv_id: '2607.20957'
url: https://arxiv.org/abs/2607.20957
pdf_url: https://arxiv.org/pdf/2607.20957
published: '2026-07-23'
collected: '2026-07-24'
category: RecSys
direction: 向量检索 · LLM高维嵌入ANNS优化
tags:
- ANNS
- DEG
- EVP
- MIPS
- LLM_Embedding
one_liner: 优化动态探索图DEG，结合EVP量化、维度增强、缓存布局，大幅提升LLM嵌入ANNS性能
practical_value: '- 电商推荐召回/RAG场景下，可复用EVP+FP16重排的混合精度pipeline：用EVP快速建图+粗筛，再用原始FP16特征重排，兼顾百万级以上高维嵌入的索引构建速度与召回率

  - 处理非归一化LLM嵌入的MIPS（最大内积搜索）任务时，可直接套用维度增强方法，把向量升到d+1维转化为欧氏距离搜索，兼容现有近邻图检索框架，避免精度损失

  - 静态数据集（如商品库、内容库）的检索索引优化，可加入FLAS预排序步骤，无需修改检索逻辑即可提升CPU缓存命中率，降低20%左右查询延迟，性价比极高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
高维LLM嵌入的近似最近邻搜索（ANNS）是搜索推荐、RAG、多模态检索的核心基础组件，现有方案在千万级1024维以上嵌入场景下，存在建图速度慢、非归一化向量MIPS精度低、查询延迟高等痛点，无法满足大流量业务的性能要求，SISAP 2026挑战提出的更大规模、分布偏移的LLM嵌入检索任务进一步放大了上述问题。

### 方法关键点
- 归一化高维嵌入kNNG构建：将无训练的EVP量化集成到DEG框架加速建图，用EVP做粗检索召回超量候选，再用原始FP16特征重排，平衡速度与精度
- 非归一化嵌入MIPS检索：采用维度增强升维方法，将向量映射到d+1维超球面，把非对称内积最大化转化为对称欧氏距离最小化，兼容标准图检索框架
- 全局缓存优化：建图前用FLAS算法对向量做一维预排序，让相似向量存储在连续内存地址，提升CPU缓存命中率，降低遍历延迟

### 关键实验结果
- Task1数据集：640万1024维BGE-M3归一化嵌入，对比纯FP16 DEG基线，混合精度方案总耗时降低39%，维持0.8以上召回
- Task2数据集：25.6万128维Llama-3.2-8B非归一化嵌入，对比原生MIPS基线，维度增强方案将查询latency从100ms降至33ms，叠加FLAS预排序后进一步降至29ms，共降低71%延迟，满足0.8召回要求

### 核心结论
ANNS优化可通过几何变换、内存布局优化与检索框架解耦的方式实现，无需改动核心图结构即可获得显著性能收益
