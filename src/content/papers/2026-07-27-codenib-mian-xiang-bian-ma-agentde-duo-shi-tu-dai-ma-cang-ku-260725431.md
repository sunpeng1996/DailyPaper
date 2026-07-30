---
title: 'CodeNib: A Multi-View Data System for Serving Repository Context to Coding
  Agents'
title_zh: CodeNib：面向编码Agent的多视图代码仓库上下文服务数据系统
authors:
- Zhongming Yu
- Hengjia Yu
- Boqin Yuan
- Shuting Zhao
- Yizhao Chen
- Aryan Dokania
- Mihir Jagtap
- Jiayu Chang
- Yitong Ma
- Yash Jayswal
affiliations:
- UC San Diego
- Stanford University
- UC Riverside
- University of Southern California
arxiv_id: '2607.25431'
url: https://arxiv.org/abs/2607.25431
pdf_url: https://arxiv.org/pdf/2607.25431
published: '2026-07-27'
collected: '2026-07-30'
category: Agent
direction: Agent 代码仓库上下文服务优化
tags:
- Coding Agent
- Multi-View Index
- Context Serving
- Vector Search
- Incremental Update
one_liner: 构建多视图可复用代码仓库上下文服务系统，大幅降低编码Agent的上下文获取延迟与Token开销
practical_value: '- 多视图索引复用思路可迁移到商品库/内容库的增量更新场景：针对不同召回需求（词法/语义/结构）拆分独立索引，增量更新时仅修改对应视图索引，降低全量重构开销

  - 上下文有效性边界管控方法可复用在RAG链路：针对不同检索操作定义明确的索引有效期阈值，平衡检索准确率与响应延迟

  - 上下文压缩策略可迁移到推荐系统的用户/物品序列建模：基于任务保留核心特征的同时降低序列Token长度，减少大模型推理开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有编码Agent获取代码仓库上下文依赖独立索引、语言服务与任务本地历史，存在重复检索成本高、全生命周期开销不透明的问题，且代码仓库频繁迭代时索引更新延迟高。

### 方法关键点
1. 为每个代码仓库commit构建可复用的词法、稠密向量、结构三类独立视图，输出映射到仓库相对源码范围；
2. 支持代码编辑时的跨版本视图增量更新，通过统一runtime对外提供排序检索、符号导航、限定上下文三类服务；
3. 基于操作类型定义明确的视图有效性边界。

### 关键结果
1. 100次快照迭代下，图索引、向量索引的中位数更新速度相比全量重构分别快8.7倍、25.4倍；
2. 1000次请求中63%匹配静态导航场景，中位数请求延迟比实时服务低4.7倍；
3. 5类模型测试下，上下文选择策略相比grep/read方案保留同等定位能力的同时减少50%-87%的轨迹Token。
