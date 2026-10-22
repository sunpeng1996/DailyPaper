---
title: 'Generative Recommenders Forget the Long Tail: Restoring Memorization in Retrieval
  and Ranking'
title_zh: 生成式推荐的长尾遗忘问题：修复召回与排序阶段的记忆能力
authors:
- Xu Huang
- Jiancan Wu
- Hongzheng Qin
- Jiawei Feng
- Can Ye
- Wencong Zeng
- Fengze Li
- Xiang Wang
affiliations:
- University of Science and Technology of China
- Independent Researcher
arxiv_id: '2610.29298'
url: https://arxiv.org/abs/2610.29298
pdf_url: https://arxiv.org/pdf/2610.29298
published: '2026-10-21'
collected: '2026-10-22'
category: GenRec
direction: 生成式推荐 · 长尾优化
tags:
- Generative Recommendation
- Long Tail
- Beam Search
- Collaborative Filtering
- Memorization
one_liner: 提出训练无关的CAPE插件，同时修复生成式推荐召回与排序阶段的长尾遗忘
practical_value: '- 已上线生成式推荐的业务可无侵入接入CAPE，无需重训模型，仅需提前构建训练数据的item共现矩阵，额外latency仅11-16%，就能显著提升长尾效果，同时不改动原模型top1结果保障首序体验

  - 选型生成式推荐时不要盲目加宽beam：加宽50%beam会使latency上涨109%+，但长尾召回提升极低，优先选择加共现召回通道的方案ROI更高

  - 需平衡整体与长尾效果时，可调整CAPE的λ权重，或去掉tail mask将共现证据作用于所有item，优先保整体效果的同时仍能补充部分长尾收益

  - 生成式推荐排序阶段不要直接使用生成似然，做长尾优化时可将归一化后的似然与共现等记忆信号加权融合，效果远好于单一重排策略'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐用单模型替代传统召回排序级联，通过beam search解码Semantic ID实现召回，用序列似然做排序，但共享得分设计会导致长尾item被双重遗忘：beam搜索时长尾item对应前缀的子树概率低，被提前剪枝；即使进入候选集，也会被似然排到头部item之后。而长尾item占平台目录的80%以上，贡献超一半的测试目标，直接影响平台的发现价值。

### 方法关键点
- 无训练插件CAPE完全不改动原生成器和beam配置，仅在推理阶段新增两个模块：
  1. 记忆召回通道：基于训练数据的用户级item共现统计，召回beam之外Top B'个和用户历史共现最高的长尾item，用原生成器做teacher forcing得到似然得分
  2. 记忆校准排序：将min-max归一化后的生成似然、仅作用于长尾item的事件级共现证据加权融合，同时保留原生成器的top1结果不变，保障首序体验
- 仅需1个超参数λ，在验证集上选择满足整体准确率不低于原模型的前提下，长尾准确率最高的取值即可

### 关键实验
在Amazon 3个商品域、LastFM音乐域，用MiniOneRec、TIGER两个生成式推荐backbone测试，对比加宽beam、DBS、各类重排基线：
- 长尾HR@10相对原backbone提升2.5~13.3个点，相对最强同候选集重排基线提升1.6~7.3个点，整体准确率不变或提升
- 额外latency仅11%~16%，远低于加宽50%beam带来的109%+ latency涨幅

### 最值得记住的一句话
生成式推荐的长尾遗忘不是单一阶段的问题，仅优化召回或仅优化排序都达不到最优效果，必须同时在两个阶段注入item级的共现记忆信号。
