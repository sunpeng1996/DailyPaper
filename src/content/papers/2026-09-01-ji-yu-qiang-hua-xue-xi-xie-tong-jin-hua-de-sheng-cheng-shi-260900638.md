---
title: 'It Takes Two to Match: Co-Evolving Generative Retriever with Reinforcement
  Learning'
title_zh: 基于强化学习协同进化的生成式检索框架CoGR
authors:
- Runpeng Dai
- Kaili Huang
- Changsung Kang
- Ciya Liao
affiliations:
- University of North Carolina at Chapel Hill
- Apple
arxiv_id: '2609.00638'
url: https://arxiv.org/abs/2609.00638
pdf_url: https://arxiv.org/pdf/2609.00638
published: '2026-09-01'
collected: '2026-09-02'
category: RecSys
direction: 生成式检索 · 双端协同进化强化学习
tags:
- Generative Retrieval
- Reinforcement Learning
- GRPO
- Keyword Generation
- Co-evolution
one_liner: 训练双LLM分别生成查询与物品关键词，通过SFT+交替GRPO实现协同进化，兼容现有倒排索引基建
practical_value: '- 现有基于关键词的电商搜索、广告检索系统可无缝复用这套框架，无需替换倒排索引基建，迁移成本极低，可先用SFT阶段快速上线 baseline

  - RL 奖励设计可直接复用：查询端直接采用检索F1作为奖励，物品端采用反事实边际奖励，仅计算单物品修改的影响，避免全量重算的高额工程开销

  - 双端交替固定优化的范式可迁移到双塔召回等其他双端对齐任务中，有效缓解训练不稳定问题，提升表征空间对齐度

  - 针对歧义、拼写错误、小语种query场景，可直接给query生成器补充现有搜索结果作为上下文，无需修改模型架构即可提升检索效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有工业界检索方案中，传统 lexical 匹配语义表达能力弱，dense 检索和生成式检索要么兼容性差，要么需要替换整套基建，落地成本高；过往LLM增强检索方案大多仅优化查询端，未同时对齐查询与物品端的表征空间，效果上限有限。
### 方法关键点
- 训练两个独立LLM分别作为查询端、物品端关键词生成器，生成的关键词直接通过倒排索引匹配，完全兼容现有关键词检索基建，匹配后采用BM25排序
- 两阶段训练流程：第一阶段SFT初始化，先生成物品端初始关键词，再将相关物品的高频关键词作为查询端训练目标，保证初始表征空间对齐
- 第二阶段协同进化RL，交替固定一端的索引优化另一端：查询端直接以检索F1作为GRPO奖励，物品端采用反事实边际奖励（仅计算单物品关键词修改带来的F1变化），大幅降低计算开销
- 训练过程中约束生成关键词数量上限，避免候选集过大影响线上 latency
### 关键结果
在Apple内部APP Marketplace数据集（13.5k训练query、3.96w个APP）、公开电商搜索WANDS数据集上，对比10个稀疏、稠密、生成式检索基线，CoGR-4B的F1相比最强基线分别提升10.9%、36.1%。
> 最值得记住的一句话：双端协同优化的收益远高于单独优化查询端，兼容现有基建的生成式检索方案能大幅降低落地门槛，快速拿到业务收益
