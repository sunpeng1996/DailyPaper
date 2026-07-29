---
title: 'Grevo: A Unified Generative Recommendation Framework with Evolutionary Item
  Indexing'
title_zh: Grevo：基于进化式物品索引的统一生成式推荐框架
authors:
- Huanjie Wang
- Liwei Guan
- Zekai Sun
- Hongwei Zhang
- Honghui Bao
affiliations:
- Beijing University of Posts and Telecommunications
- University of Illinois Chicago
arxiv_id: '2607.25329'
url: https://arxiv.org/abs/2607.25329
pdf_url: https://arxiv.org/pdf/2607.25329
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · 进化式Semantic ID优化
tags:
- Generative Recommendation
- Semantic ID
- Multitask Learning
- Evolutionary Indexing
- Sequential Recommendation
one_liner: 通过进化式语义ID索引优化，免耦合tokenizer训练与交替优化提升生成式推荐效果
practical_value: '- 可直接复用多任务优化trick：在现有生成式推荐模型中加入轻量SSG任务，仅通过输入前缀区分任务，额外开销小于10%，不开ID进化也能稳定提升5%-10%的推荐效果

  - SID迭代可落地路径：不用搞复杂的端到端耦合tokenizer训练，每轮用训练好的模型作为后验评估器，仅修改5%左右的高风险ID的后两层，全程兼容现有SID体系，无需修改模型架构

  - 电商动态商品库适配：优先优化行为混淆商品的ID，复用低负载码本token，小步迭代避免全局索引震荡，适合线上商品频繁上新、用户行为分布快速变化的场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐的Semantic ID（SID）要么是静态预生成，存在语义编码与用户行为模式的固有gap，要么采用tokenizer与推荐模型耦合的端到端训练，需要双模块、对齐损失与交替优化，训练不稳定、工程落地复杂度高，难以适配电商动态变化的商品库与用户行为流。

### 方法关键点
- 抛弃常驻可训练tokenizer，仅用初始静态量化器做SID bootstrap，后续将SID分配本身作为可进化离散变量，全程固定ID长度与码本空间，无需修改模型架构
- 单Encoder-Decoder多任务设计：仅用输入前缀[U]/[I]区分两个共享参数的任务，一是Behavioral SID Generation（BSG，标准生成推荐任务，输入用户历史序列输出目标SID），二是Semantic SID Grounding（SSG，输入物品语义emb输出自身SID，仅激活模型浅层，额外开销极低）
- 进化索引流程：每轮训练后用模型后验信号筛选高风险SID，候选SID仅从行为混淆邻居的token、低负载码本token生成，默认每轮最多进化5%的SID，仅修改ID后两层保证全局索引稳定
- 候选打分融合BSG行为生成概率、SSG语义匹配度、跨任务一致性三个信号，兼顾推荐效果与语义可解释性

### 关键结果
在Amazon Beauty、Sports、Toys三个公开基准数据集上，对比TIGER、LETTER、LC-Rec等SOTA生成式推荐基线：基于TIGER backbone时，Beauty数据集Recall@10从0.0648提升至0.0778（+20.1%），NDCG@10从0.0336提升至0.0412（+22.6%）；进化后的SID可直接迁移到其他生成式推荐模型，给LC-Rec直接使用进化后的ID，Recall@10提升约19%；仅开启多任务训练不开ID进化，也能带来5%-10%的效果提升。

### 核心结论
生成式推荐的核心瓶颈是SID质量而非tokenizer架构，小预算的后验驱动式ID进化比复杂的端到端耦合训练性价比高得多。
