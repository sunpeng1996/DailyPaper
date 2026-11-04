---
title: Modular and Efficient Approximate Nearest Neighbors Search with Vectorium and
  kANNolo
title_zh: 基于Vectorium和kANNolo的模块化高效近似最近邻搜索库
authors:
- Silvio Martinico
- Franco Maria Nardini
- Cosimo Rulli
- Rossano Venturini
affiliations:
- University of Pisa
- Institute of Information Science and Technologies (ISTI), CNR Italy
- Linkup Technologies
arxiv_id: '2611.03927'
url: https://arxiv.org/abs/2611.03927
pdf_url: https://arxiv.org/pdf/2611.03927
published: '2026-11-02'
collected: '2026-11-04'
category: Other
direction: 向量检索 · 模块化开源ANN库
tags:
- ANN
- Vector Search
- Quantization
- HNSW
- IVF
- Rust
one_liner: 两个开源Rust ANN库，统一支持三类向量表征，性能超越FAISS、hnswlib等主流实现
practical_value: '- 向量检索选型可直接复用这两个MIT协议的开源库，统一支持稠密/稀疏/多向量接口，性能优于FAISS IVF、hnswlib，适配商品召回、用户向量检索、RAG知识库检索、多模态检索等多场景

  - 工程架构可借鉴其编译期特化的分层设计，将向量表征、量化器、距离函数、索引结构解耦，新增量化器或表征无需修改上层索引代码，无运行时overhead

  - 性能优化可复用其PQ查表布局优化、RABITQ编码、稀疏向量DotPacking8压缩等trick，在几乎无精度损失前提下，将检索吞吐量提升1~2倍，内存占用降低50%以上'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现有ANN检索库普遍存在两个核心痛点：一是硬编码索引结构、量化器、向量表征的组合，扩展性差，新增组件需要大量重复开发；二是仅支持单类向量表征（绝大多数仅支持稠密向量），无法适配当前业务中稠密Embedding召回、稀疏语义检索、多向量ColBERT类检索等多场景混合需求，不同表征的优化无法复用。
## 方法关键点
- 架构拆分为两层开源Rust库：下层Vectorium为数据管理层，抽象向量视图、距离函数、量化器、数据集四类独立组件，内置11种量化器（覆盖f32到亚比特编码），统一支持稠密、稀疏、多向量三类表征，所有组合在编译期完成特化，无运行时额外开销
- 上层kANNolo为索引层，泛化实现HNSW、IVF两类主流ANN索引，支持任意Vectorium的量化器、表征、距离函数组合，同时提供两阶段重排索引，可自由拼接任意一阶索引和重排数据集，适配混合表征检索场景
- 距离计算依赖Rust编译器自动向量化，仅对特殊打包编码使用显式SIMD，无需手写多指令集适配代码，性能接近手工优化的行业实现
## 关键实验
在7个公开数据集上对比FAISS、hnswlib、PYANN等6个稠密系统、5个稀疏系统：稠密数据12个数据集-精度对中9个取得最优内存-吞吐权衡，99%精度下两阶段HNSW吞吐量是hnswlib的2.5~3.3倍，索引体积仅为后者的1/2；稀疏数据所有3个测试集上，基于Vectorium的SEISMIC、SEISMICWAVE为最快方案，kANNolo索引体积最小，两阶段索引比PYANN快5.2~48.4倍，内存仅为其1/3。
## 核心结论
模块化分层+编译期特化的设计可以在不损失ANN检索性能的前提下，实现多表征、多量化、多索引的灵活扩展，大幅降低检索系统的维护和迭代成本。
