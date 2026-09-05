---
title: No-Regret Bayesian Optimization with Finite-Library Input-Warped Kernels
title_zh: 基于有限库输入扭曲核的无悔贝叶斯优化算法
authors:
- Edvin Ketabati Augustinsson
- Robert A. Bridges
affiliations:
- AI Sweden
arxiv_id: '2609.02993'
url: https://arxiv.org/abs/2609.02993
pdf_url: https://arxiv.org/pdf/2609.02993
published: '2026-09-02'
collected: '2026-09-05'
category: Training
direction: 贝叶斯优化 · 黑盒超参数调优
tags:
- Bayesian Optimization
- Gaussian Process
- Hyperparameter Optimization
- Input Warping
- Multi-Agent System
one_liner: 提出从有限平滑输入映射库选扭曲函数的贝叶斯优化方法，兼顾样本效率与收敛性保证
practical_value: '- 推荐/广告系统超参调优场景，可预先构建常用输入扭曲函数库（如log、幂变换等），替换固定核GP-BO，在保留调优收敛性的同时降低试错成本

  - 多Agent系统协同策略优化场景，可复用FLIWBO的有限库选择逻辑，适配高维、存在几何失配的黑盒优化问题，规避局部最优陷阱

  - 若业务场景的黑盒优化存在手动调参得到的经验变换规则，可直接纳入有限扭曲库，自动适配无需额外证明收敛性'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
GP-BO是高成本黑盒优化（如超参调优、多Agent系统设计）的主流方案，GP-UCB等有收敛保证的方法要求固定核，当输入坐标与目标几何失配时（如对数尺度超参、局部峰值目标），固定核样本效率极低，而输入扭曲能提效但会破坏原有收敛性证明。
### 方法关键点
提出FLIWBO算法，支持从有限平滑输入映射库中按任意历史依赖规则选择最优扭曲函数，自适应匹配输入几何；仅需温和假设即可保留高概率收敛保证，额外开销仅与库大小的平方根成正比。
### 关键结果
在4类基准测试中，几何失配场景下FLIWBO-UCB效果优于原始坐标GP-UCB；可逃脱甚至带先验扭曲的EI算法都无法避开的置信围栏陷阱；可复现手动log缩放带来的大部分收益，是同批次带收敛保证方法中性能最优的；在20维多Agent系统设计的高噪声高成本评估场景下验证了可行性。
