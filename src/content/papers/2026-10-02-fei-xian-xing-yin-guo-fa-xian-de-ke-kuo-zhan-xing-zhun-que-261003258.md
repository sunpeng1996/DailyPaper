---
title: Mapping and Advancing the Scalability-Accuracy Frontier of Nonlinear Causal
  Discovery
title_zh: 非线性因果发现的可扩展性-准确率边界映射与优化
authors:
- Hendrik Suhr
- Sascha Xu
- Jilles Vreeken
affiliations:
- CISPA Helmholtz Center for Information Security
arxiv_id: '2610.03258'
url: https://arxiv.org/abs/2610.03258
pdf_url: https://arxiv.org/pdf/2610.03258
published: '2026-10-02'
collected: '2026-10-05'
category: Other
direction: 因果发现 · 效率-准确率边界优化
tags:
- Causal Discovery
- Scalability
- Combinatorial Search
- Spline
- Structure Learning
one_liner: 对比四类主流非线性因果发现算法，提出SPADE方案大幅提升组合搜索的效率与准确率边界
practical_value: '- 推荐系统用户行为因果归因时，可复用SPADE的统计量预计算复用思路，降低多特征因果图搜索的冗余计算开销

  - 大规模特征因果结构挖掘场景，可优先选择「组合搜索+预计算」架构，替代准确率存在明显短板的可微/amortized结构学习方法

  - 特征维度≤1600的中小规模因果挖掘任务，可直接复用SPADE方案，兼顾高结构准确率与秒/分钟级推理速度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有非线性因果发现四类主流算法的准确率-运行时tradeoff缺乏系统性量化对比，其中准确率表现最优的组合搜索类方法受困于重复冗余的局部打分计算，复杂度高难以落地大规模特征场景。
### 方法关键点
1. 实证对比可微结构学习、amortized结构学习、score-matching、组合搜索四类主流算法的性能瓶颈
2. 提出基于样条的打分评估方案SPADE，预计算充分统计量并在组合搜索全流程复用，其高斯变体在有界入度假设下复杂度从O(nd³)降至O(nd²+d³)
### 关键结果数字
SPADE将可扩展性-准确率边界提升数个量级：100变量16万样本任务秒级完成，1600变量2500样本任务分钟级完成，同时在合成/真实基准上保持高结构准确率
