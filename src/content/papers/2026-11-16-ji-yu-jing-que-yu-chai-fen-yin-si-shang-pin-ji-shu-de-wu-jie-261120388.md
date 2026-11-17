---
title: 'What Unlinked Aggregates Still Prove: Ranker Comparisons from Exact and Differentially
  Private Item Counts'
title_zh: 基于精确与差分隐私商品计数的无链接推荐排序器对比方法
authors:
- Chang Xu
- Hao Wang
- Gedi Zhou
affiliations:
- Duke University
- Stanford University
- Independent Researcher
arxiv_id: '2611.20388'
url: https://arxiv.org/abs/2611.20388
pdf_url: https://arxiv.org/pdf/2611.20388
published: '2026-11-16'
collected: '2026-11-17'
category: Eval
direction: 隐私保护推荐系统效果评估
tags:
- differential-privacy
- recommender-evaluation
- privacy-preserving
- e-commerce
- ranker-comparison
one_liner: 基于无用户关联的商品购买计数实现隐私约束下的推荐排序器效果对比
practical_value: '- 跨合作方推荐效果评测无用户行为-推荐关联数据时，可直接用商品级购买计数缩小排序器效果差区间，无需脱敏用户级数据

  - 差分隐私场景下优先对长尾商品做分桶统计，可提升计数数据的排序器对比有效性，小用户量场景可实现个性化排序对判定

  - 2万用户以下小流量AB测隐私受限场景，可尝试用分组精确计数完成排序器效果判定，10万以上大流量场景该方案判定成功率极低'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
电商推荐跨主体效果评测受隐私约束，无法关联用户购买行为与对应推荐列表，仅能获取聚合级商品购买计数，需基于这类受限数据完成排序器优劣判定。
### 方法关键点
1. 利用商品计数约束潜在购买用户分布，推导所有合法分配下的排序器性能差区间，区间不含0即可判定优劣；
2. 采用简化传输网络适配全量商品库，支持差分隐私计数的统一置信度保证，长尾商品分桶统计可提升判定能力。
### 关键结果
在2万、10万用户电商队列测试：① 精确计数相比无计数基线可普遍缩小性能差区间；② 2万用户队列中精确计数完成14/168组排序器对比判定，分桶差分隐私计数可完成1组个性化排序对判定；③ 10万用户队列中精确/隐私计数均无法完成个性化排序对判定。
