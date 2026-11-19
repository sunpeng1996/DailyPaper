---
title: 'Chorus: Shared N-gram Embeddings with Layer-wise Adaptation'
title_zh: Chorus：支持层级适配的共享N-gram嵌入方法
authors:
- Stephen Chung
- Wenyu Du
affiliations:
- DualverseAI
arxiv_id: '2611.23386'
url: https://arxiv.org/abs/2611.23386
pdf_url: https://arxiv.org/pdf/2611.23386
published: '2026-11-16'
collected: '2026-11-19'
category: LLM
direction: LLM训练优化 · N-gram嵌入内存压缩
tags:
- N-gram Embedding
- Memory Efficiency
- LLM Optimization
- Ember Optimizer
- Layer-wise Adaptation
one_liner: 通过共享单组N-gram表加层级适配，以87%更小的表容量超过现有n-gram方法性能
practical_value: '- 推荐系统序列建模可复用共享n-gram+层适配架构：取消每层独立的n-gram表，统一查表后加层专属投影/门控，节省嵌入内存同时满足层间差异化需求

  - 训练大规模ID类嵌入（用户/物品/Semantic ID表）可直接复用Ember优化器，相比AdamW减少99.2%的优化器状态内存，无需降低性能即可支撑更大规模的表

  - 生成式推荐/QueryRec场景的LLM微调可接入Chorus模块，仅增加少量计算即可提升实体召回、搜索词补全的效果，尤其适合商品/搜索词等高频n-gram的业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM插入n-gram嵌入表提升性能的方案普遍为每层配置独立表，内存开销随层数线性增长，且层间相同序列的知识无法复用；直接全局共享单表又无法适配不同层的差异化计算需求，实际效果远逊于分层独立表方案，亟需兼顾内存效率与性能的n-gram嵌入设计。

### 方法关键点
- 全局仅维护一组共享n-gram表，单次查询后经卷积精炼得到统一嵌入z_t，输入层与所有中间层复用该结果，避免重复查表开销
- 每层加专属适配逻辑：用当前层隐状态生成通道门控对z_t重加权，再经层专属投影层映射到适配当前层计算的表示空间，兼顾共享与差异化需求
- 搭配Ember优化器训练n-gram表，仅存储每行/每列的二阶矩标量，替代AdamW的全量二阶矩存储，大幅降低训练阶段的优化器内存开销

### 关键结果
在ClimbMix、FineWeb数据集上对比Engram、FactorEngram、TN-gram等主流方案：
- 1.2B参数的Chorus表效果超过9.6B参数的所有基线，表容量缩小87%；20M~9.6B全表规模区间下均取得最低验证损失
- 18层133M参数模型上，22个下游任务平均得分超过最强基线0.003，其中Wikidata QA实体召回准确率领先7pct以上
- 搭配Ember优化器相比AdamW节省99.2%的表优化器内存，无性能损失

### 核心结论
共享嵌入加轻量层级适配的思路，比每层独立配置大表的内存效率高一个数量级，是大嵌入表扩容的核心可行方向
