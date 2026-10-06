---
title: 'From Valid to Useful: Post-Verification Acquisition for Recursive Self-Improving
  Recommendation'
title_zh: 《从有效到有用：递归自优化推荐的验证后样本选择框架》
authors:
- Tonmoy Hasan
- Taylor Foust
- Shao Tang
- Leonardo Neves
- Aman Gupta
- Hiroto Udagawa
- Helder Dias
- Daniel Silva
- Rohan Ramanath
affiliations:
- Nubank
arxiv_id: '2610.04302'
url: https://arxiv.org/abs/2610.04302
pdf_url: https://arxiv.org/pdf/2610.04302
published: '2026-10-03'
collected: '2026-10-06'
category: RecSys
direction: 递归自优化推荐 · 合成训练样本选择
tags:
- Sequential Recommendation
- Recursive Self-Improvement
- Data Augmentation
- BALD
- Active Learning
one_liner: 提出分歧感知的验证后样本选择框架DA-RSIR，无需额外标注即可大幅提升递归自优化推荐效果
practical_value: '- 做序列推荐合成数据增强时，不要直接全量保留验证通过的合成样本，可先限制每个真实源序列的贡献上限，避免高频源占比过高导致的分布偏移

  - 合成样本选择可复用BALD+MC dropout的分歧评分方案，不需要额外训练质量打分模型、也不需要人工标注，工程落地成本低效果稳定

  - 筛选合成样本时不要只选高置信/高分歧的极端样本，均匀采样低/中/高分歧区间的样本可同时提升NDCG和Recall两类核心指标，适配多目标优化需求

  - 递归自优化迭代时，单轮DA-RSIR的效果就超过5轮全量保留样本的迭代收益，适合算力有限的业务场景快速迭代'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有递归自优化推荐（RSIR）仅做合成序列的一致性验证，全量保留所有通过验证的样本，导致生成更多有效样本的源序列权重被过度放大，同时样本价值和下游模型提升效果不挂钩，容易出现错误强化、部分指标下降的问题。

### 方法关键点
- 引入验证后样本选择独立环节，完全保留原有RSIR的合成生成、一致性校验逻辑，仅改动训练样本筛选步骤
- 用MC dropout估计模型对合成序列每个位置的预测分歧，基于BALD的目标项贡献计算序列级分歧得分，无需额外标注或教师模型
- 按源序列分组后，将验证通过的样本划分为低/中/高三个分歧区间，每个区间均匀采样1个代表，同时限制每个源序列的最大贡献样本数，避免分布偏移

### 关键实验
在4个公开序列推荐数据集（Amazon Toys/Beauty/Sports、Yelp）、3个主流序列模型（SASRec/CL4SRec/FEARec）上测试：24组（模型×数据集×指标）对比中，DA-RSIR在23组取得最优，对比全量保留的RSIR基线平均提升NDCG@10 5.1%、Recall@10 6.6%，所有提升均统计显著；单轮DA-RSIR迭代的效果超过RSIR 5轮迭代的最优收益；仅限制样本量不加分歧选择就能超过基线，结合分歧跨区间采样效果最优。

### 核心结论
递归自优化推荐中，合成样本的筛选逻辑和验证逻辑同等重要，仅靠验证无法保证合成样本的训练价值，跨分歧区间采样比仅选高/低置信样本收益更稳定。
