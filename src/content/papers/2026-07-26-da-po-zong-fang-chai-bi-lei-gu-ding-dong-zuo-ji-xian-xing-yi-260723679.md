---
title: 'Breaking the Total Variance Barrier: Sharp Sample Complexity for Linear Heteroscedastic
  Bandits with Fixed Action Set'
title_zh: 打破总方差壁垒：固定动作集线性异方差老虎机的紧样本复杂度界
authors:
- Heyang Zhao
- Tianyuan Jin
- Weixin Wang
- Vincent Y. F. Tan
- Pan Xu
- Quanquan Gu
affiliations:
- University of California, Los Angeles
- National University of Singapore
- Duke University
arxiv_id: '2607.23679'
url: https://arxiv.org/abs/2607.23679
pdf_url: https://arxiv.org/pdf/2607.23679
published: '2026-07-26'
collected: '2026-07-29'
category: Other
direction: 异方差线性老虎机 · 样本复杂度优化
tags:
- Linear Bandit
- Heteroscedastic Noise
- Sample Complexity
- Regret Bound
- Exploration Strategy
one_liner: 提出两种方差自适应异方差线性老虎机算法，首次打破√Λ regret壁垒，得到调和均值依赖的紧上下界
practical_value: '- 推荐/广告动态探索场景可复用方差感知消除式探索策略，优先采样低噪声动作，降低探索regret

  - 异方差噪声场景（如用户点击反馈方差随场景波动）下的在线学习，可替换原有基于总方差的regret界计算逻辑，用调和均值依赖的界做探索预算评估

  - 固定候选集的在线决策（如固定商品池的个性化探索）可直接参考VAEE算法的信息增益最大化探索逻辑，提升样本效率'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有异方差线性老虎机研究以总噪声方差$Λ$刻画样本复杂度，即便半数轮次噪声接近0时$Λ$量级仍不变，该依赖非最优，无法适配噪声分布不均的实际场景。
### 方法关键点
针对固定动作集场景：1. 面向大动作集提出VAEE（方差感知消除式探索）算法，在未淘汰候选动作中主动选择信息增益最大的动作探索；2. 面向有限动作集提出方差感知的G最优设计探索变体，同时推导该场景下的匹配下界。
### 关键结果
首次打破$√Λ$壁垒，得到调和均值依赖的simple regret上界：大动作集下regret阶为$}{\cal{O}}(d \cdot [\sum_{t=1}^T 1/\sigma_t^2 - }{\cal{O}}(d) 项]^{-1/2})$，有限动作集下为$}{\cal{O}}(\sqrt{d\log|A|} \cdot 同前项)$，上下界近乎匹配，样本效率显著优于原有$Λ$依赖算法
