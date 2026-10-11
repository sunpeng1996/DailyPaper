---
title: Density Ratio Estimation with Stein Displacement Fields
title_zh: 基于Stein位移场的密度比估计方法
authors:
- Song Liu
affiliations:
- University of Bristol
arxiv_id: '2610.12437'
url: https://arxiv.org/abs/2610.12437
pdf_url: https://arxiv.org/pdf/2610.12437
published: '2026-10-08'
collected: '2026-10-11'
category: Other
direction: 分布偏移估计 · 密度比建模
tags:
- Density Ratio Estimation
- Distribution Shift
- Stein Operator
- Convex Optimization
- Inference
one_liner: 将密度比估计与位移场建模结合，通过单次凸优化同时得到分布偏移的统计与动力学描述
practical_value: '- 推荐系统遇到训练/线上分布偏移、跨域推荐分布差等场景时，可借鉴该方法同时输出密度比与迁移变换，避免单独估计后转换带来的误差累积

  - 预训练的用户行为采样器、生成式推荐item生成器出现线上效果偏移时，可复用push-forward算法免全量重训校正模型，大幅节省算力成本

  - 做用户/物品表征非线性ICA解耦时，可复用pull-back逐层拟合变换的思路，降低复杂变换的训练难度与收敛门槛'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
密度比、位移场是两类互补的分布偏移分析工具，现有方案需分别估计，互相转换需额外后处理；且传统密度比估计在分布差异大时存在「密度鸿沟」，稳定性差。
### 方法关键点
1. 用作用于基分布的位移场参数化密度比，将对数比建模为基分布Stein算子作用于位移场的负值（加归一化常数），仅通过单次凸优化即可同时输出分布偏移的统计（密度比）、动力学（位移场）双维度描述
2. 迭代「估计-迁移」步骤得到两类推理算法：push-forward可免重训校正预训练采样器，pull-back可逐层拟合变换模型，将目标分布数据向基分布拉近
### 关键结果
在基于仿真的推理分布偏移、非线性独立成分分析任务上验证了方法的效果收益与适用边界
