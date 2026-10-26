---
title: 'What the Query Remembers: Query Abstraction Governs Lexical and Dense Retrieval
  of Classical Arabic Poetry'
title_zh: 查询记忆特征：查询抽象度对古典阿拉伯诗歌检索的调控机制
authors:
- Omar Farouk Zouak
- Selma Mani
- Larbi Said Chikh
- Raid Abderrezak Ouahioune
affiliations:
- National School of Artificial Intelligence
arxiv_id: '2610.31821'
url: https://arxiv.org/abs/2610.31821
pdf_url: https://arxiv.org/pdf/2610.31821
published: '2026-10-22'
collected: '2026-10-26'
category: Eval
direction: 检索效果评估 · 检索器适配规则
tags:
- BM25
- Dense Retrieval
- Query Understanding
- Retrieval Benchmark
- Information Retrieval
one_liner: 量化查询词汇重合度对BM25与稠密检索器的效果影响，指出单一检索评估基准存在显著偏差
practical_value: '- 搜索场景可根据用户query与待召回内容的词汇重合度动态切换检索策略：高重合度用BM25，低重合度的抽象query用稠密编码器，提升整体召回效果

  - 做检索系统benchmark时必须覆盖不同抽象层级的query类型与评估协议，避免单一测试集导致的选型偏差

  - 做query改写优化时可量化词汇改动对不同检索器的效果影响，平衡改写的语义适配性与词汇召回率'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有检索器选型与评估通常忽略用户query的抽象度差异，针对用户仅记住部分原文（嘴边回忆）或仅记得语义（抽象查询）的场景，单一基准给出的结论存在严重偏差。
### 方法关键点
以古典阿拉伯诗歌检索为测试场景，对9款稠密编码器、BM25算法在2个语料、3种索引模式、2类评估协议下做系统性benchmark，通过控制query携带原文词汇的比例开展消融实验。
### 关键结果数字
- 高词汇重合的嘴边回忆query下，BM25的Recall@5达0.746，优于8B SOTA稠密模型的0.717
- 低词汇重合的抽象query下，BM25 Recall@5仅0.392，远低于最优稠密模型的0.748，排名跌至第8/10
- BM25对词汇重合度的敏感度远高于稠密编码器，单一评估协议的结论偏差可达39个百分点
