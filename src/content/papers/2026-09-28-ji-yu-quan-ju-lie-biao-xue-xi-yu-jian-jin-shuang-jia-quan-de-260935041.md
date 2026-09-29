---
title: Mitigating Popularity Bias in Recommendation with Global Listwise Learning
  and Progressive Bi-Weighting
title_zh: 基于全局列表学习与渐进双加权的推荐系统流行度偏差缓解方法
authors:
- Tianyu Zhu
- Jiandong Ding
- Yansong Shi
- Guoqing Chen
- Jian-Yun Nie
affiliations:
- Beihang University
- Fudan University
- Tsinghua University
- University of Montreal
arxiv_id: '2609.35041'
url: https://arxiv.org/abs/2609.35041
pdf_url: https://arxiv.org/pdf/2609.35041
published: '2026-09-28'
collected: '2026-09-29'
category: RecSys
direction: 推荐系统 · 流行度偏差缓解
tags:
- PopularityBias
- InversePropensityScoring
- ListwiseLoss
- Debiasing
- LongTailRecommendation
one_liner: 提出融合全局列表式IPS与渐进双加权的流行度去偏框架，大幅提升长尾推荐效果
practical_value: '- 可直接复用IPS+多项式似然的列表式去偏损失，替换现有业务中pointwise/pairwise的IPS去偏损失，全局优化用户偏好排序的同时降低训练不稳定性，适配MF、LightGCN等各类主流推荐骨干

  - 双加权propensity平滑策略可直接替代常用的propensity硬截断（clipping）操作，无需复杂建模就能提升长尾物品propensity估计的鲁棒性，尤其适合流行度倾斜严重的电商/内容推荐场景

  - 渐进式重加权调度策略可迁移到所有样本重加权类的去偏/长尾优化任务，训练初期优先学基础表征，后期逐步加大去偏权重，避免早期重加权破坏通用表征质量'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有IPS类流行度去偏方法存在两大核心局限：一是pointwise/pairwise的局部无偏目标仅能优化单样本或两两物品偏好，无法捕捉用户全物品集上的全局偏好结构；二是propensity估计不准易引入经验偏差，且训练初期激进重加权会破坏表征学习，最终导致长尾推荐效果差、训练不稳定。

### 方法关键点
- 设计Mult-IPS框架，融合IPS与多项式似然，用softmax约束下的列表式损失建模全局无偏用户偏好，规避pointwise IPS负权重导致的训练不稳定问题，且模型无关，可适配MF、GNN等各类推荐骨干
- 提出Bi-Weighting双加权策略，参考语言模型Jelinek-Mercer平滑思路，将单个物品propensity与全局平均propensity线性插值，提升长尾物品propensity估计鲁棒性，理论证明可有效降低经验偏差上界
- 实现Progressive Bi-Weighting渐进调度策略，随训练epoch逐步提升propensity重加权的权重，平滑完成从判别式表征学习到流行度去偏的过渡，避免早期重加权破坏表征质量

### 关键实验
在Amazon、Google Local、Gowalla、Yelp、ML10M、Netflix共6个真实数据集上，对比Rel-MF、UBPR、DICE、CPR、TTEN等SOTA去偏基线，平均较最优基线提升Recall@20 9.43%、NDCG@20 14.80%；在流行度倾斜最严重的Amazon数据集上，Recall@10相对最优基线提升26.6%，训练效率与主流方法相当甚至更优。

最值得记住的结论：流行度去偏不能只靠粗暴的样本重加权，要兼顾全局偏好建模、propensity估计鲁棒性、表征学习与去偏的阶段平衡，才能同时提升效果与公平性。
