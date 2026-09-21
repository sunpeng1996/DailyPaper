---
title: 'CrystalMO-TuRBO: Multi-Objective Trust-Region Bayesian Optimization for High-precision
  Joint Crystal Structure Refinement'
title_zh: CrystalMO-TuRBO：面向高精度联合晶体结构精修的多目标信任域贝叶斯优化
authors:
- Joseph Agada
- Yishu Wang
- Arpan Biswas
affiliations:
- University of Tennessee, Knoxville
- Bredesen Center for Interdisciplinary Research
- Department of Materials Science and Engineering
- University of Tennessee - Oak Ridge Innovation Institute
arxiv_id: '2609.20592'
url: https://arxiv.org/abs/2609.20592
pdf_url: https://arxiv.org/pdf/2609.20592
published: '2026-09-17'
collected: '2026-09-21'
category: Other
direction: 材料科学 · 多目标贝叶斯优化应用
tags:
- Bayesian Optimization
- Multi-Objective Optimization
- Trust Region
- Inverse Problem
- Materials Science
one_liner: 提出多目标信任域贝叶斯优化框架解决多模态衍射数据联合晶体结构精修的非凸优化难题
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统晶体结构精修依赖局部搜索，在多模态衍射数据对应的非凸、高噪声、参数强相关优化空间中表现受限；X射线与中子数据联合精修需手动设置多目标权重，易产出次优解。
### 方法关键点
1. 构建CrystalMO-TuRBO多目标信任域贝叶斯优化架构，将X射线、中子数据的拟合偏差设为独立优化目标，转化为归一化最大化问题；
2. 采用两阶段优化策略：阶段1跨多标量化函数并行执行信任域贝叶斯优化做全局探索，定位参数空间高潜力区域；阶段2在收缩的局部区域内做精细化调优，满足高精度解的要求。
### 关键结果
在单晶Ho2Ti2O7的实验衍射数据集上验证，相比传统精修方法与贝叶斯优化基线，收敛性、鲁棒性、参数精度均有明确提升。
