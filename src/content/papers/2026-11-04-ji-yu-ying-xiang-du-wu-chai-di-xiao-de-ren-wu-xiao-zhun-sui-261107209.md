---
title: Task-Calibrated Random Features via Influence-Based Error Cancellation
title_zh: 基于影响度误差抵消的任务校准随机特征方法
authors:
- Shinto Eguchi
arxiv_id: '2611.07209'
url: https://arxiv.org/abs/2611.07209
pdf_url: https://arxiv.org/pdf/2611.07209
published: '2026-11-04'
collected: '2026-11-07'
category: Other
direction: 核方法优化 · 随机特征校准
tags:
- Random Features
- Kernel Method
- Error Cancellation
- Calibration
- Kernel Ridge Regression
one_liner: 提出任务校准随机特征TCRF，通过任务相关影响度抵消采样误差，适配多类下游核任务
practical_value: '- 大规模核回归排序/用户画像建模场景，可复用TCRF校准思路降低随机傅里叶特征近似误差，提升核方法线上推理效率

  - 电商用户行为分布异动检测等场景，可采用TCRF优化核Stein差异计算精度，降低采样噪声影响

  - 计算预算有限时优先给普通随机特征分配算力，仅任务精度要求高、预算充足时引入TCRF校准模块'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
随机傅里叶特征通过蒙特卡洛近似核积分，仅部分采样误差会传导到下游任务，现有无差别误差优化方案浪费算力，无法针对性抵消任务相关误差。
### 方法关键点
1. 提出TCRF方法，基于任务特定影响度构造频率矩平衡权重，权重在核条目间共享，闭式解匹配经典最小距离校准，生成可复用的任务校准空间
2. 引入指数倾斜正权重保留特征半正定性，支持更高校准秩；针对核岭回归、核Stein差异分别设计误差抵消策略，可完全抵消一阶方差
### 关键结果
大频率预算下核岭回归近似精度显著提升，固定替代假设下核Stein差异近似误差降低；交叉验证岭参数下增益收窄，Stein零假设附近优先给普通随机特征分配预算效果更好
