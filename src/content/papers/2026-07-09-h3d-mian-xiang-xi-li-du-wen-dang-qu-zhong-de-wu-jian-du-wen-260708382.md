---
title: 'H3D: Benchmarking Unsupervised Text Hashing for Fine-Grained Document Deduplication'
title_zh: H3D：面向细粒度文档去重的无监督文本哈希基准
authors:
- Qianren Mao
- Jiaxun Lyu
- Junnan Liu
- Zhijun Chen
- Jingzheng Li
- Hanwen Hao
- Bo Li
affiliations:
- Zhongguancun Laboratory
- Beihang University
- Monash University Australia
- Hong Kong Polytechnic University
arxiv_id: '2607.08382'
url: https://arxiv.org/abs/2607.08382
pdf_url: https://arxiv.org/pdf/2607.08382
published: '2026-07-09'
collected: '2026-07-10'
category: Other
direction: 无监督文本哈希 · 文档去重基准
tags:
- TextHashing
- UnsupervisedLearning
- DocumentDeduplication
- Benchmark
- EmbeddingQuantization
one_liner: 搭建无监督文本哈希基准H3D，统一对比7类方法在细粒度文档去重的效果效率与鲁棒性
practical_value: '- 电商/推荐场景的商品详情、UGC内容近重复去重可优先选用MinHash/SimHash等规则类哈希，无训练成本且计算开销极低，效果满足近重复匹配需求

  - RAG/Agent场景处理改写后用户Query、相似语义文档召回，可选用基于BGE embedding的量化哈希方案，语义保留度更高，适配改写内容匹配需求

  - 哈希方法选型可直接参考H3D的trade-off结论：近重复匹配选低开销规则类哈希，语义相似匹配选embedding量化类哈希，平衡效果与算力成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有无监督文本哈希方法缺乏统一的细粒度文档去重场景对比基准，不同方案的效果、效率、鲁棒性权衡关系不明确，工业选型缺乏可落地的参考依据。

### 方法关键点
搭建H3D基准，覆盖5类无学习规则类哈希（MinHash、SimHash、Winnowing等）+2类基于冻结BGE embedding的量化语义哈希（BGE-BIHash、BGE-LSHash），在CSFCube（计算机文献细粒度相似性）、RELISH（生物医学文献大规模相似搜索）两个数据集上测试，同步评估排序质量（MAP、NDCG@20）、运行效率、文本压缩下的鲁棒性。

### 关键结果
规则类哈希在近重复匹配场景效果与语义类相当，速度快2~3个数量级；语义类哈希在内容改写场景的NDCG@20比规则类平均高17%，但计算成本提升10倍以上；同时明确了不同哈希表征对应的等价相似度度量，提升方法对比的可解释性。
