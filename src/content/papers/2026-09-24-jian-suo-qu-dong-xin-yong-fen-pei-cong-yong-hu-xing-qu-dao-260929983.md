---
title: 'From Interests to Semantic IDs: Retrieval-Grounded Credit Assignment for Generative
  Recommendation'
title_zh: 检索驱动信用分配：从用户兴趣到Semantic ID的生成式推荐
authors:
- Mengdan Zhu
- Yufan Zhao
- Yao Zhao
- Sophie Di
- Tao Di
- Yulan Yan
- Sridhar Iyer
- Liang Zhao
affiliations:
- Emory University
- Microsoft
- Cornell University
arxiv_id: '2609.29983'
url: https://arxiv.org/abs/2609.29983
pdf_url: https://arxiv.org/pdf/2609.29983
published: '2026-09-24'
collected: '2026-09-27'
category: GenRec
direction: 生成式推荐 · Semantic ID信用分配
tags:
- Generative Recommendation
- Semantic ID
- Credit Assignment
- Reinforcement Learning
- Retrieval
one_liner: 通过检索验证生成的用户兴趣，为生成式推荐的推理轨迹提供细粒度信用分配信号
practical_value: '- 带推理轨迹的Semantic ID生成式推荐可直接复用本方案的过程监督逻辑：无需训练额外奖励模型，用冻结的商品检索器验证生成的兴趣query，仅为命中目标的兴趣段分配正向奖励，解决RL阶段SID
  exact match奖励稀疏问题

  - 推理阶段生成的结构化兴趣可直接作为召回query补充候选池，也可基于兴趣召回的候选集构建小范围前缀trie，约束SID解码空间，既提升召回覆盖又降低解码延迟

  - 优化文本+离散ID的异构输出LLM推荐模型时，可采用分奖励信号组内标准化的方案：SID匹配、轨迹合法性、检索命中三类奖励分别做组内归一化，避免不同尺度奖励的互相干扰

  - Semantic ID解码阶段复用前缀trie约束逻辑，过滤无效SID输出，减少候选集校验的工程开销'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前带推理轨迹的Semantic ID生成式推荐普遍采用SID exact match作为RL奖励，大商品库下奖励极度稀疏：同组采样轨迹全部未命中目标SID时组内优势为0，无有效学习信号；奖励相同的轨迹无法区分推理质量，存在信用分配缺口，难以优化推理段生成效果。

### 方法关键点
- 训练分三阶段：阶段1对齐SID token与文本、行为语义；阶段2用SFT让模型输出固定结构推理轨迹（历史摘要+多条兴趣query）后接目标SID；阶段3采用检索驱动的组相对PPO优化
- 三类独立奖励分别组内标准化：SID exact match奖励作用于全序列；轨迹合法性奖励作用于推理段；检索命中奖励仅分配给命中目标的兴趣query段，未命中轨迹的负向奖励平摊到所有兴趣段
- 推理支持三种模式：直接生成SID推荐；用生成的兴趣query做召回补充；基于兴趣召回候选集构建小范围前缀trie，约束SID解码空间

### 关键结果
在Amazon Reviews的Video Games、Office Products、Industrial三个品类数据集上对比12种基线，相对仅用SID+轨迹奖励的基线，Recall@10提升15.5%~39.6%，NDCG@10提升18.5%~61.5%；检索信号可重新激活最高37.8%的SID无信号训练组，补充有效学习信号。

### 核心结论
生成式推荐的中间推理输出只要可被外部系统（如检索器）验证，就能获得无需额外标注的细粒度过程监督信号，大幅降低RL优化的难度。
