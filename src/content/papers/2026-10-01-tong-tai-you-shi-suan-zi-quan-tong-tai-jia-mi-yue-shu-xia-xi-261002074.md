---
title: 'Homomorphic Advantage Operator: Stabilizing Reinforcement Learning Under Fully
  Homomorphic Encryption Constraints'
title_zh: 同态优势算子：全同态加密约束下强化学习的稳定性优化
authors:
- Abid Mohamed Nadhir
- Ahmad Al Hanbali
- Beggas Mounir
affiliations:
- El Oued University
- King Fahd University of Petroleum and Minerals (KFUPM)
- Interdisciplinary Research Center For Smart Mobility and Logistics, KFUPM
arxiv_id: '2610.02074'
url: https://arxiv.org/abs/2610.02074
pdf_url: https://arxiv.org/pdf/2610.02074
published: '2026-10-01'
collected: '2026-10-03'
category: Agent
direction: 隐私保护强化学习 · 同态加密优化
tags:
- FHE
- Reinforcement-Learning
- Privacy-Preserving
- Bellman-Drift
- Advantage-Function
one_liner: 提出HAO框架解决FHE下深度RL的Bellman漂移导致的多项式近似发散问题
practical_value: '- 隐私保护类云端推荐/广告Agent部署时，可复用HAO的零均值中心化投影思路，用线性变换替代非线性操作，降低FHE下的计算开销与密文Bootstrapping成本

  - 基于RL的电商物流路径规划、动态商品调度等业务，可参考HAO的Bellman漂移抑制方法，避免隐私计算场景下的策略发散问题

  - 需叠加DP-SGD差分隐私的模型训练场景，可验证HAO在加噪梯度下的稳定性，提升隐私保护模型的效果鲁棒性'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
云端部署隐私敏感智能系统时，全同态加密（FHE）可实现安全密态计算，但FHE下深度RL需用多项式近似替换非线性操作，会触发Bellman漂移导致近似灾难性发散。
### 方法关键点
提出同态优势算子（HAO）稳定框架，将优势值估计的零均值中心化投影直接适配到时序差分（TD）目标，通过线性投影消除驱动Bellman漂移的统一状态值基线，保持各状态下的动作排序，无需额外非线性乘法深度，避免开销极高的密文Bootstrapping。
### 关键结果
- 所有随机种子下HAO的多项式近似安全域边界违规率为0，仅用L2正则+梯度裁剪的方案在3/5种子上违规，无稳定基线的方案83.8%的episode违规
- 表格域最优策略准确率提升18.0个百分点，叠加DP-SGD高斯梯度噪声时仍保持稳定
