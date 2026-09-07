---
title: 'AtomRec: Evolving Atomic Memory for Agentic Recommendation'
title_zh: AtomRec：面向智能体推荐的可演进原子记忆框架
authors:
- Peiyu Hu
- Weihai Lu
- Siying Gu
- Zhuodong Liu
- Zhaokai Luo
- Yuean Niu
- Zhiyong Wang
- Jia Wang
affiliations:
- 西安交通利物浦大学
- 小红书
- 北京大学
- 华东师范大学
- 北京交通大学
arxiv_id: '2609.04882'
url: https://arxiv.org/abs/2609.04882
pdf_url: https://arxiv.org/pdf/2609.04882
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: 智能体推荐 · 记忆机制优化
tags:
- Agentic_Recommendation
- LLM_Memory
- Collaborative_Signal
- Dynamic_Memory
- Semantic_Link
one_liner: 基于可演进原子协作记忆的智能体推荐，相对SOTA平均提升8.5%
practical_value: '- 记忆结构设计可复用：将用户/物品记忆拆分为内容、关键词、标签、上下文、嵌入、链接6个结构化字段，替代粗粒度用户画像，避免偏好信息丢失，适配电商长周期用户兴趣建模

  - 语义协作链接技巧：用嵌入召回候选记忆+LLM生成语义关联（如偏好演进、主题共享）替代传统标量相似度边，提升召回的可解释性，可直接复用到冷启动用户的兴趣关联场景

  - 动态记忆演进机制：新交互触发相似度高于阈值的历史记忆字段级更新（保留时间戳不变），既保留兴趣演化轨迹又补充新特征，尤其适合兴趣漂移明显的内容/电商推荐场景

  - 工程优化点：记忆构造、链接、演进操作可异步离线执行，仅将证据路径摘要输入在线排序模块，额外在线开销可控，可低成本集成到现有LLM推荐链路'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有智能体推荐的记忆机制多将用户/物品信息压缩为粗粒度摘要，用标量协作边关联，既无法保留细粒度偏好演化阶段，也难提供可解释的召回证据，随着用户兴趣漂移，历史有效信息容易被覆盖丢失，长期推荐精度和可解释性均受限。

### 方法关键点
- 原子记忆构造：将每个用户/物品记忆建模为包含内容、时间戳、关键词、语义标签、上下文描述、嵌入、关联链接7个字段的结构化原子单元，各字段作为独立操作对象支持精准检索、修订
- 语义协作链接构建：新增记忆时先通过嵌入相似度召回TopK邻近记忆，再用LLM识别语义关联（如共享主题、偏好演进、跨域迁移）生成带解释的关联链接，替代传统标量权重边
- 动态记忆演进：新记忆关联的历史记忆若满足链接命中或相似度高于阈值的触发条件，仅对其语义字段做更新，保留原始时间戳以留存兴趣时序轨迹
- 上下文感知协作检索：推荐时基于当前query召回初始相关记忆后，沿语义链接做多跳扩展生成证据路径，输入LLM完成候选排序

### 关键实验
在Amazon Books、Goodreads、MovieTV、Yelp四个公开基准上对比LightGCN、SASRec、P5、MemRec等10个传统、LLM、智能体推荐基线，相对最优基线平均提升8.5%，在高偏好漂移用户群上相对MemRec提升达13.9%，所有提升均通过显著性检验。

### 核心结论
让推荐记忆可重组而非仅仅更精细，是构建更具可解释性、自适应性的智能推荐体的核心方向
