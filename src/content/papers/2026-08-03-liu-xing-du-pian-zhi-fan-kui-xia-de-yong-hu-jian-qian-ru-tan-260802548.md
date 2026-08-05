---
title: 'Between-User Collapse Under Popularity-Biased Feedback: A Centered-Covariance
  Theorem and Computable Phase Boundary'
title_zh: 《流行度偏置反馈下的用户间嵌入坍缩：中心协方差定理与可计算相变边界》
authors:
- Sahil Medepalli
affiliations:
- Independent Researcher
arxiv_id: '2608.02548'
url: https://arxiv.org/abs/2608.02548
pdf_url: https://arxiv.org/pdf/2608.02548
published: '2026-08-03'
collected: '2026-08-05'
category: RecSys
direction: 推荐系统 · 嵌入坍缩与流行度偏置
tags:
- collaborative filtering
- popularity bias
- embedding collapse
- BPR
- feedback loop
one_liner: 证明流行度偏置BPR训练会引发用户嵌入坍缩，推导得到可计算的坍缩-扩张相变边界
practical_value: '- 可直接复用论文给出的相变边界公式，基于已训模型embedding、商品交互计数、训练超参数快速判断当前系统是否处于强坍缩区间，无需跑反馈模拟，大幅降低排查成本

  - 业务部署级正则强度下用户间嵌入坍缩幅度极小，不会显著影响推荐指标，无需额外针对该现象做复杂的干预优化，避免冗余开发

  - 流行度偏置引发的各向异性坍缩仅在正则强度过高、已损害推荐效果的场景下生效，调参时不用额外为规避该坍缩刻意调整正则权重'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有研究仅从行为层面分析推荐反馈环的用户同质化效应，对流行度偏置训练如何改变协同过滤用户嵌入空间几何结构的机制尚不清晰，也缺乏该几何效应对推荐指标实际影响的量化验证。
### 方法关键点
引入均值中心化用户协方差$C$衡量用户间可区分度，替代过往使用的非中心化二阶矩；理论证明固定物品池下，流行度偏置BPR训练会让$C$收敛到与物品噪声协方差$Q$成正比的稳态，引发用户间嵌入向噪声底坍缩；推导基于超参数$(\alpha,\lambda_{neg},\gamma,d)$的闭式可计算相变边界，区分坍缩/扩张区间。
### 关键结果
在MovieLens-25M上验证理论方向性预测；业务部署级正则强度下坍缩幅度很小，未反映在任何测得的推荐指标上；仅正则强度高到损害推荐效果时，才会出现$\alpha$驱动的各向异性坍缩；基于理论的部署时修复干预未提升推荐质量，实测可部署超参数设置远距强坍缩区间。
