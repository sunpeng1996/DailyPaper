---
title: 'When Greedy Is Sorting: Exact and Certified Ideal Rankings for Novelty Metrics'
title_zh: 新颖性多样性指标的精确可证理想排序：贪心等价于多链归并
authors:
- Kehan Liu
- Zhaoyun Chen
- Xianquan Yan
affiliations:
- National University of Singapore
arxiv_id: '2611.10576'
url: https://arxiv.org/abs/2611.10576
pdf_url: https://arxiv.org/pdf/2611.10576
published: '2026-11-07'
collected: '2026-11-10'
category: Eval
direction: 多样性排序评估 · 新颖性指标计算
tags:
- diversity-ranking
- alpha-nDCG
- ERR-IA
- evaluation-metrics
- ranking-optimization
one_liner: 提出ChainMerge算法实现单意图下多样性指标理想排序精确求解，重叠场景提供最优性证书
practical_value: '- 电商/内容推荐的多样性评估环节，若商品/内容仅归属单个类目/标签，直接替换原有贪心计算α-nDCG的逻辑为ChainMerge，大候选集下评估速度可提升17~25000倍，显著降低离线评测算力消耗

  - 做线上多样性重排序服务时，单类目场景下可直接用ChainMerge的虚拟得分堆归并逻辑生成最优排序，无需每轮全量扫描候选集，延迟更低，可支撑更高的QPS

  - 多意图重叠的多样性AB实验中，可通过前缀LP验证当前评估指标分母的最优性，避免指标本身的近似误差导致实验结论误判，TREC数据显示95%以上场景下贪心近似的分母是全局最优的

  - RAG检索的结果多样性评估也可复用该方法，加速α-nDCG类多样性指标的计算，提升RAG系统的迭代效率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
α-nDCG、ERR-IA等新颖性/多样性评估指标的理想排名计算是NP难问题，现有工业界常用的O(nK)贪心近似方案，既存在效率瓶颈（大候选集下计算成本极高），也无法证明近似结果的最优性，容易导致多样性评估结论不可靠，影响算法迭代和AB实验判断。
### 方法关键点
- 界定可精确求解边界：当每个候选item最多对应1个意图（行支持度为1）时，多样性指标的最优排序可转化为固定预算下的边际收益递减分配问题
- 提出ChainMerge算法：先对每个意图组内的item按收益降序排列，计算每个位置的虚拟得分（α-DCG下为收益乘以(1-α)^(r-1)，ERR-IA下为意图先验乘以第r个item的首次满足概率），再用最大堆做多链归并得到全局最优top-K排序，时间复杂度仅O(n + K log G)
- 多意图重叠场景：证明行支持度≥3时α-DCG最优求解为NP难，提出多项式规模的前缀LP松弛得到最优值上界，可作为当前可行排序的最优性证书，同时提供无求解器的投影边界方案
### 关键实验结果
- 测试数据集：TREC 2009-2012 Web多样性评测集、MIND-small新闻推荐数据集
- 对比基线：现有评估工具的贪心近似算法、穷举/DP精确解
- 核心数字：单意图下ChainMerge与精确解完全一致，在MIND数据集上比贪心快17~1011倍，二进制增益场景下最多快25427倍；重叠场景下前缀LP证明189/198个TREC查询的贪心分母是全局最优，证书平均gap仅0.0213%，不会改变评测排行榜的获胜者和99.5%的pairwise序
### 核心结论
单意图场景下多样性指标的贪心理想排序等价于多链归并，是精确最优的，多意图场景下的近似误差几乎不会影响评测结论
