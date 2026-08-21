---
title: Do Sequential Recommendation Benchmarks Really Require Higher-Order Sequence
  Modelling?
title_zh: 序列推荐基准是否真的需要高阶序列建模能力？
authors:
- Aleksandr V. Petrov
- Praveen Chandar
- Paul N. Bennett
- Hugues Bouchard
- Mounia Lalmas
affiliations:
- Spotify
arxiv_id: '2608.19833'
url: https://arxiv.org/abs/2608.19833
pdf_url: https://arxiv.org/pdf/2608.19833
published: '2026-08-20'
collected: '2026-08-21'
category: RecSys
direction: 序列推荐 · 基准有效性评估
tags:
- Sequential Recommendation
- Benchmark Evaluation
- Capacity Probe
- Pairwise Transition
- Recency Weighting
one_liner: 通过无高阶建模的简单探针验证多数主流序列推荐基准无需高阶序列建模能力
practical_value: '- 做序列推荐模型迭代前，先拿PCTM/SeqRules这类简单pairwise探针做基线，避免为了刷基准硬堆高阶模型做无用功

  - 可以直接复用PCTM的设计：离线统计带距离衰减的item转移概率，在线加权融合多历史item的转移得分+流行度校正，冷启动场景下速度快效果好

  - 内部搭建序列推荐benchmark时，加入pairwise探针作为及格线，只有超过这条线的高阶模型收益才是真实有效的，避免benchmark失效'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前序列推荐领域越来越多采用Transformer等大模型架构捕捉高阶序列依赖，但主流基准的性能增益到底是否真的来自高阶建模一直存疑，很多时候仅靠流行度、pairwise转移、近因效应就能达到相当效果，需验证现有基准是否真的需要高阶建模能力。

### 方法关键点
- 设计两类无高阶序列建模的容量探针：一是优化后的SeqRules（传统序列规则，引入近因衰减、IDF加权等调优项）；二是新增PCTM（概率协同转移模型），离线统计带距离衰减的item到item转移概率，用贝叶斯平滑处理稀疏转移，在线对用户历史每个item的转移概率做近因加权对数求和，叠加流行度校正项，全程无嵌入学习、无序列编码器。
- 以两个探针的最优结果作为pairwise性能上限，若Transformer类模型无法超过该上限，则说明该基准无法体现高阶建模价值。

### 关键实验
采用eSASRec官方评估协议，在Beauty、Sports、Toys3个亚马逊数据集、MovieLens-1M、MovieLens-20M共5个基准上对比eSASRec、SAS+等Transformer基线：前4个数据集上pairwise上限比eSASRec高4.4%~38.4%，仅MovieLens-20M上eSASRec超出pairwise上限27.3%。

### 核心结论
仅在小数据集上超过普通基线的序列建模创新没有实际意义，必须先超过强pairwise近因探针的性能上限才能证明高阶建模的价值。
