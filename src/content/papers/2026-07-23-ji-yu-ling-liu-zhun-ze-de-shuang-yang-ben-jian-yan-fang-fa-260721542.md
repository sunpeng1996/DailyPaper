---
title: Zero-Flow Two-Sample Tests
title_zh: 基于零流准则的双样本检验方法
authors:
- Yakun Wang
- Leyang Wang
- Song Liu
- Taiji Suzuki
affiliations:
- University of Bristol
- RIKEN AIP
- University of Tokyo
arxiv_id: '2607.21542'
url: https://arxiv.org/abs/2607.21542
pdf_url: https://arxiv.org/pdf/2607.21542
published: '2026-07-23'
collected: '2026-07-26'
category: Other
direction: 统计方法 · 双样本分布差异检验
tags:
- Two-Sample Test
- Distribution Shift Detection
- Statistical Calibration
- Neural Witness
- Zero-Flow Discrepancy
one_liner: 提出基于零流差异的双样本检验ZF2ST，兼顾结构化分布差异检验效力与统计校准有效性
practical_value: '- 可复用ZFD指标检测推荐系统线上/线下样本分布漂移、训练/测试集分布差异，提前预警模型效果衰减

  - 拆分witness学习与假设评估的架构设计可直接迁移到分布漂移检测工具实现，支持灵活更换特征提取模型同时保证统计有效性

  - 高结构化分布变化检验能力可用于A/B实验分组均衡性校验，排查分组是否存在用户特征、行为分布偏差'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
高维场景下传统双样本检验对局部/结构化分布差异的有限样本检验效力不足，引入神经网络优化检验能力的方案常破坏统计校准性。

### 方法关键点
1. 基于零流准则定义零流差异（ZFD）作为分布差异统计量，理论证明其有效性；
2. 提出零流双样本检验（ZF2ST）流程，通过学习两组样本的局部分布错位方向判定分布差异；
3. 拆分witness学习与假设评估环节，支持灵活使用神经网络作为witness同时保证I类错误校准，提供回归型、功效最大化型两种witness学习方案。

### 关键结果
在合成数据与图像数据集实验中，ZF2ST对结构化分布变化的检验效力优于现有方案，同时保持校准良好的I类错误率。
