---
title: 'Beyond Fixed Depths and Widths: Optimizing Textual Decoding Tries in LLM-based
  Generative Recommendation'
title_zh: 超越固定深度宽度：LLM生成式推荐的文本解码前缀树优化
authors:
- Jingzhe Liu
- Hanbing Wang
- Jiliang Tang
- Liam Collins
- Tong Zhao
- Neil Shah
- Mingxuan Ju
affiliations:
- Michigan State University
- Snap Inc.
arxiv_id: '2607.16633'
url: https://arxiv.org/abs/2607.16633
pdf_url: https://arxiv.org/pdf/2607.16633
published: '2026-07-18'
collected: '2026-07-21'
category: GenRec
direction: 生成式推荐 · 解码Trie结构优化
tags:
- Generative Recommendation
- Decoding Trie
- Term ID
- LLM4Rec
- Beam Search
one_liner: 提出BONSAI框架联合优化文本term ID与解码trie，最高相对SOTA提升21.6%
practical_value: '- 优化现有term ID的解码trie结构无需修改ID语义，仅用最小集覆盖重排ID词序即可获得7~9%的性能提升，落地成本极低

  - 放弃固定长度item ID范式，采用自适应变长ID：语义简单的商品用短ID降低解码复杂度，语义复杂的商品用长ID减少信息损失

  - 生成式推荐训练可采用SFT+GRPO RL两阶段范式，RL阶段针对多ID/长ID商品优化，能额外带来6~10%的相对提升

  - 解码trie浅层节点需严格控制分支因子，优先用覆盖度高的公共特征做上层拆分，减少早期解码错误带来的级联损失'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于文本term ID的生成式推荐仅关注ID语义质量，忽略解码trie的结构设计：固定长度ID会导致语义丰富的商品信息损失，trie浅层分支过大会大幅降低约束beam search的成功率，最终拖累推荐效果。

### 方法关键点
- 明确解码trie的两个核心优化目标：自适应变长ID长度（匹配商品语义丰富度）、浅层节点约束分支因子（降低早期解码错误概率）
- BONSAI框架四步流程：1）LLM过滤商品元数据，提取高信息量特征词；2）递归用最小集覆盖算法构建trie，每层选最少的特征拆分当前节点商品集，自动控制分支因子与深度；3）SFT微调LLM，用最长ID做监督学习序列推荐；4）GRPO强化学习优化，对齐同一商品的所有合法ID路径，直接优化推荐准确率

### 关键实验
在亚马逊Beauty、Sports、Toys三个公开数据集上，对比SASRec、GRLM、OneRec-Think等SOTA基线，BONSAI相对最优基线GRLM最高提升21.6%；仅用最小集覆盖重排现有GRLM的ID词序，也能拿到7~9%的性能提升；RL阶段相对SFT阶段额外获得6~10%的相对提升。

### 核心结论
生成式推荐的item表示设计不能只关注语义质量，需和底层解码搜索结构联合优化，微小的结构调整即可带来显著的性能收益。
