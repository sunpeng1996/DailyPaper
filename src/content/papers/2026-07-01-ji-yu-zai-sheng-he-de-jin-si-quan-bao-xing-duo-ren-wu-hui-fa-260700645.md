---
title: Approximate full-conformal multi-task regression with reproducing kernels
title_zh: 基于再生核的近似全保形多任务回归方法
authors:
- Davidson Lova Razafindrakoto
- Alain Celisse
- Jérôme Lacaille
affiliations:
- Université Paris 1 Panthéon-Sorbonne
- Laboratoire SAMM
- Safran Aircraft Engines
arxiv_id: '2607.00645'
url: https://arxiv.org/abs/2607.00645
pdf_url: https://arxiv.org/pdf/2607.00645
published: '2026-07-01'
collected: '2026-07-06'
category: Training
direction: 多任务回归 · 保形预测区间构造
tags:
- Multi-task Regression
- Conformal Prediction
- RKHS
- Prediction Interval
- Kernel Method
one_liner: 提出基于RKHS的近似全保形多任务回归方案，解决全保形预测区计算不可行问题，性能优于拆分保形预测
practical_value: '- 电商多任务预估场景（如CTR+CVR+客单价联合建模）可引入保形预测区间，量化预测不确定性，辅助大促流量分配、动态调价决策

  - 全保形预测计算量过高时，可借鉴本文RKHS约束下的近似区间构造思路，在保证置信度满足要求的前提下大幅降低计算开销

  - 任务间协方差已知/可估计两种场景的适配方案，可直接复用至多任务排序、多目标广告投放模型的不确定性建模模块'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
全保形预测可生成指定置信度的数据依赖型预测区间，可靠量化输出不确定性，但通用场景下需要训练无限多预测器，计算完全不可行，多任务回归场景下尚无低成本可落地的近似方案。
### 方法关键点
1. 基于向量值函数的RKHS框架，构造包含真实全保形区间的近似预测区，大幅降低计算复杂度
2. 分别设计适配任务间协方差矩阵已知、未知（需从数据估计）两种业务常见场景的构造方案
3. 理论上给出近似区间体积的上界，保证近似区间的紧密度不会过松
### 关键结果
仿真实验中，两种场景下的近似方案预测区间体积均显著优于拆分保形预测，同时完全满足预设的置信度覆盖率要求
