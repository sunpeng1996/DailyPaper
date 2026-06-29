---
title: Fast algorithms for learning a Gaussian under halfspace truncation with optimal
  sample complexity
title_zh: 半空间截断场景下具备最优样本复杂度的高斯学习快速算法
authors:
- Haitong Liu
- Deepak Narayanan Sridharan
- David Steurer
- Manuel Wiedmer
affiliations:
- ETH Zurich
arxiv_id: '2606.27298'
url: https://arxiv.org/abs/2606.27298
pdf_url: https://arxiv.org/pdf/2606.27298
published: '2026-06-25'
collected: '2026-06-27'
category: Other
direction: 截断分布学习 · 最优复杂度算法
tags:
- Gaussian Learning
- Truncated Distribution
- Sample Complexity
- Fast Algorithm
- High-dimensional Statistics
one_liner: 提出半空间截断场景高斯学习算法，样本与时间复杂度均达理论最优，规避耗时投影SGD
practical_value: '- 处理带半空间截断偏置的用户行为数据（如仅曝光TopK商品、用户仅反馈高分内容）时，可参考用相对截断参数关联截断分布与原始分布低阶矩的思路，简化原始分布参数恢复流程

  - 截断分布拟合场景可替换原有投影SGD类迭代方法，大幅降低计算开销，其运行效率仅取决于经验协方差矩阵计算速度

  - 高维用户分布建模场景下，该方法的最优样本复杂度边界可作为 baseline，评估自有截断数据处理算法的样本效率'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
高维半空间截断高斯的参数学习是统计领域基础问题，此前首个该场景多项式时间算法存在样本、时间复杂度非最优缺陷，且依赖计算开销极高的投影随机梯度下降流程，落地难度大。
### 方法关键点
1. 提出相对截断参数的全新解读，建立截断高斯低阶矩与未截断原始高斯参数的唯一映射关系，可直接完成参数恢复，无需迭代优化；
2. 算法核心计算量仅来自经验协方差矩阵求解，无额外 heavy 计算步骤。
### 关键结果
非平凡截断场景下，算法样本复杂度为$	ilde{O}(d^2/ε^2)$，时间复杂度与无截断场景的高斯学习持平，二者在维度$d$和精度$ε$维度均达到理论最优，可将输出高斯与真实分布的总变差距离控制在目标精度$ε$以内。
