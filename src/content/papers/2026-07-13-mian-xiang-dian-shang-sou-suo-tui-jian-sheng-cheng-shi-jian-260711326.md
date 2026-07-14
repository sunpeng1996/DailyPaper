---
title: Prompt Generation Technical Report
title_zh: 面向电商搜索推荐生成式检索的Prompt Generation配置驱动框架技术报告
authors:
- Dan Ou
- Gui Ling
- Hao Wan
- Hongbin Zhou
- Jialiang Cheng
- Jiangnan Pang
- Silu Zhou
- Wei Shi
- Weichen Ye
- Wenming Zhang
affiliations:
- Taobao Search Team
arxiv_id: '2607.11326'
url: https://arxiv.org/abs/2607.11326
pdf_url: https://arxiv.org/pdf/2607.11326
published: '2026-07-13'
collected: '2026-07-14'
category: GenRec
direction: 生成式推荐 · 特征处理与训练部署一致性
tags:
- Generative Retrieval
- Prompt Engineering
- Training-Serving Alignment
- Feature Processing
- LLM4Rec
one_liner: 通过声明式JSON配置解耦特征处理与模型架构，实现生成式检索快速迭代、部署与推理
practical_value: '- 可直接复用PG的四类特征（文本/Embedding/组合/序列）+三类处理组件（预处理器/投影器/融合器）的抽象设计，大幅降低生成式检索场景下特征迭代的代码改动量

  - 可参考双JSON配置（特征配置+模板配置）的设计思路，从框架层面统一离线训练与在线推理的特征处理逻辑，避免训练服务特征偏移

  - 工程上可复用训练-服务闭环事件追踪机制，直接落盘线上请求的原始特征用于离线训练，可实现99%以上的特征一致性

  - 长用户行为序列的生成式推荐场景可复用PG的特征压缩（mean/MLP融合）方案，在不损失效果的前提下压缩prompt长度，满足线上latency要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式检索在工业界落地时，特征处理逻辑与模型架构强耦合，每次特征迭代都需要修改训练、推理代码，跨场景复用性差，且容易出现训练服务特征偏移，叠加严格的线上延迟要求，导致生成式检索的规模化落地效率极低。

### 方法关键点
- 抽象四类通用特征：文本特征、预计算Embedding特征、组合特征、序列特征，覆盖电商搜索推荐场景所有异构特征需求
- 采用两类JSON声明式配置作为唯一真值：`prompt_feature.json`定义特征类型、数据源、处理逻辑；`prompt_template.json`定义prompt结构，彻底解耦特征处理与模型架构
- 提供三类可组合处理组件：预处理器（映射/分桶等）负责特征归一化，投影器（MLP等）负责Embedding维度对齐，融合器（mean/concat_MLP/attention等）负责多特征融合，支持特征灵活组合与压缩
- 实现训练-服务闭环事件追踪机制，落盘线上请求的原始特征用于离线训练，从根源解决训练服务特征偏移问题

### 关键结果
在淘宝搜索、淘宝推荐、3个开源基准共5个场景验证，仅调整配置即可提升所有场景的离线检索效果；淘宝搜索线上A/B测试实现订单量+0.47%、GMV+0.51%的显著提升；特征一致性达到99%以上，PG带来的额外推理开销可忽略。

### 核心结论
生成式检索落地的核心瓶颈从来不是模型效果，而是特征迭代效率与训练服务一致性，可配置的通用框架是规模化落地的关键。
