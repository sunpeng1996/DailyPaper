---
title: 'MAPS: Macro-Adaptive Parallel Reasoning for Regulating Search Momentum in
  Retrieval-Augmented Generation'
title_zh: MAPS：调控RAG搜索动量的宏观自适应并行推理框架
authors:
- Xinze Li
- Dingwen Zhang
- Zhenghao Liu
- Yukun Yan
- Shuo Wang
- Yu Gu
- Ge Yu
- Maosong Sun
affiliations:
- Northeastern University
- Tsinghua University
arxiv_id: '2610.29792'
url: https://arxiv.org/abs/2610.29792
pdf_url: https://arxiv.org/pdf/2610.29792
published: '2026-10-21'
collected: '2026-10-22'
category: RAG
direction: RAG检索优化 · 意图漂移缓解
tags:
- RAG
- Query Intent Drift
- Parallel Reasoning
- Search Momentum
- Multi-hop Retrieval
one_liner: 提出推理解耦+多方向并行检索的RAG框架，调控搜索动量缓解查询意图漂移
practical_value: '- 多轮检索场景可复用「搜索动量」指标，量化历史查询轨迹的意图偏移程度，作为检索终止、方向校准的触发信号，适合电商导购、多轮搜索等场景

  - 迭代式RAG系统可借鉴推理解耦设计：仅保留已获取的结构化知识、精炼推理状态，丢弃历史子查询与原始推理链，降低历史偏差传导

  - 复杂query（如电商多属性搜索、导购咨询）的召回优化，可采用并行子查询生成方案：先识别互补检索方向，再生成子query并行召回，减少迭代轮次提升效率

  - 业务效果可参考：多轮检索中并行子查询比单链迭代检索平均提效22%以上，多跳场景性能最高提升15%+，适合客服Agent、商品多维度检索等落地场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有迭代式RAG通过交替推理和检索解决多跳信息获取问题，但存在两个核心痛点：一是历史子查询的偏差会沿推理链持续传导，导致查询意图逐步漂移，远离原始需求；二是单链迭代的检索方向单一，探索多样性不足，容易陷入局部最优检索路径，无法覆盖所需的全部互补信息。
### 方法关键点
- 定义**搜索动量**：量化历史子查询语义偏移的累积效应，验证迭代越深，后续子查询方向与累积动量的对齐度越高，偏差被放大的概率越大
- 推理解耦设计：每轮迭代仅保留已获取的结构化知识集合、精炼后的核心推理状态，完全丢弃历史子查询与原始推理轨迹，切断偏差传导路径
- 并行检索范式：每轮先识别N个互补的检索方向，对应生成多个独立子查询并行召回，再合并多源检索结果更新知识与推理状态，避免单条偏差路径垄断搜索方向
### 关键实验结果
在NQ、PopQA、2WikiQA、HotpotQA、MuSiQue、GPQA共6个覆盖单跳、多跳、推理型QA的基准测试，对比Self-RAG、IRCOT、Search-o1、ParallelSearch等SOTA基线：
- 采用Qwen3-32B作为backbone时，平均性能较最优基线提升6.8%，多跳QA场景最高提升15.7%
- 采用Qwen3.6-35B-A3B作为backbone时，平均性能较最优基线提升5.8%
- 迭代轮次较单链检索方法平均减少22%，简单query可提前终止检索
### 核心结论
迭代式RAG的性能瓶颈往往不是单轮检索能力不足，而是历史检索轨迹的偏差被持续放大导致的意图漂移，从架构层面切断偏差传导比单纯优化单轮子查询质量收益更高
