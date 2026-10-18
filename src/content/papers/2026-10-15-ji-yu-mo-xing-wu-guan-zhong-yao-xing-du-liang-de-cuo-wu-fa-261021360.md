---
title: Controlling the False Discovery Rate via Model-Agnostic Importance Measures
title_zh: 基于模型无关重要性度量的错误发现率控制方法
authors:
- Mengtao Wen
- Haojie Ren
- Changliang Zou
affiliations:
- School of Statistics and Data Science, Nankai University
- School of Mathematical Sciences, Shanghai Jiao Tong University
arxiv_id: '2610.21360'
url: https://arxiv.org/abs/2610.21360
pdf_url: https://arxiv.org/pdf/2610.21360
published: '2026-10-15'
collected: '2026-10-18'
category: Other
direction: 统计变量选择 · FDR控制
tags:
- FDR-Control
- Variable-Selection
- Model-Agnostic
- Cross-Fitting
- Multiple-Testing
one_liner: 提出无需协变量分布假设的MAS变量选择方法，温和条件下实现渐近FDR控制且兼具效率与性能
practical_value: '- 推荐系统高维特征筛选阶段可引入MAS方法，无需对用户/物品特征分布做假设即可控制无效特征入选的FDR，提升模型可解释性与稳定性

  - 单协变量重拆分+数据聚合的策略可复用在特征重要性评估流程中，降低不同特征重要性估计的耦合，提升高维特征筛选的效率与准确性

  - agent-X重要性的计算思路可迁移到大模型推荐的特征归因场景，解决复杂黑盒模型的特征贡献量化难问题'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
高维复杂模型（如DNN、LLM）的变量选择需控制错误发现率（FDR），传统方法依赖强模型假设，现有Model-X knockoffs方法需已知协变量分布，落地门槛高。

### 方法关键点
- MAS框架基于样本拆分策略与全新agent-X重要性度量，完全绕过协变量分布假设
- agent-X重要性通过构造常量代理变量+交叉拟合高效估计，量化原始分布与代理变量分布下的预测性能差异
- 引入单协变量重拆分策略解耦估计依赖，搭配数据聚合提升检验效力，有严格渐近FDR控制理论保障

### 关键结果
仿真与真实数据验证显示，MAS在FDR控制效果、计算效率、检验效力三个维度均优于现有同类方案
