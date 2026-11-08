---
title: 'SHORE: Stability-Hybrid On-Policy Reinforcement Learning for Online Bin Packing'
title_zh: SHORE：面向在线3D装箱的稳定性混合同策略强化学习
authors:
- Chang Shi
- Ann Majewicz Fey
arxiv_id: '2611.08364'
url: https://arxiv.org/abs/2611.08364
pdf_url: https://arxiv.org/pdf/2611.08364
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: 在线3D装箱 · 强化学习落地优化
tags:
- Reinforcement Learning
- 3D Bin Packing
- On-Policy RL
- U-Net
- Robotics
one_liner: 融合稳定性预测与同策略RL的在线装箱方法，提升空间利用率同时加快收敛
practical_value: '- 电商仓储装箱场景可复用「稳定性概率建模+RL」框架，替代硬规则约束，灵活平衡空间利用率与倒塌风险

  - 早期训练阶段引入模拟负样本补充稀疏的失效场景数据，可大幅加快RL模型收敛，减少真实环境交互成本

  - 部署时无需额外搜索/仿真 overhead，可直接嵌入现有机器人装箱流水线，落地成本低'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
在线3D装箱需在未知货箱到达序列下同时选择装箱对象、朝向和位置，现有方法依赖几何规则或硬稳定性掩码，无法灵活平衡风险与装箱密度，倒塌会导致整箱空间浪费。
### 方法关键点
- 提出SHORE框架，将3D U-Net学习的放置稳定性概率与同策略RL的条件收益估计融合
- 同时用真实执行结果和模拟备选动作训练稳定性模型，补充早期迭代中缺失的低概率失效场景
- 同策略Actor-Critic在动作值和策略先验中引入稳定性预测，加门控限制未成熟模型的干扰，部署无额外仿真开销
### 关键结果数字
Isaac Gym环境下仅用0.4M步达到73%空间利用率，比无稳定性建模的版本收敛快60%；60货箱集合上空间利用率达0.734，比SOTA基线GOPT高24.8%，仅以0.4%的额外放置失效概率换得更高装箱密度
