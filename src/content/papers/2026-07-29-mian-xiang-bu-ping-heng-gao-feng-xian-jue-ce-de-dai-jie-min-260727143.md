---
title: 'Cost-Sensitive Conformal Prediction and Human-in-the-Loop Abstention for Imbalanced
  High-Stakes Decision Support: A Multi-Domain Benchmark'
title_zh: 面向不平衡高风险决策的代价敏感共形预测与人在环弃权多域基准
authors:
- Manpreet Singh
- Akshatha Srikantha
- Shyamal Lakhanpal
affiliations:
- Boston University
- University of California, Irvine
- University of Maryland, College Park
arxiv_id: '2607.27143'
url: https://arxiv.org/abs/2607.27143
pdf_url: https://arxiv.org/pdf/2607.27143
published: '2026-07-29'
collected: '2026-07-31'
category: Other
direction: 不平衡分类 · 共形预测 · 人在环决策
tags:
- Conformal Prediction
- Imbalanced Classification
- Cost-sensitive Learning
- Uncertainty Quantification
- Human-in-the-loop
one_liner: 通过3150组实验验证Mondrian CP可大幅提升不平衡场景小类覆盖率，结合代价控制弃权降低高风险决策成本
practical_value: '- 电商欺诈检测、恶意流量识别等不平衡分类场景，可将现有marginal CP替换为Mondrian CP，快速提升小类样本覆盖率，降低漏判带来的业务损失

  - 高风险决策链路（如大额交易判定、广告投放审核）可引入Mondrian CP+代价控制弃权机制，在给定人工审核预算下最小化整体决策成本

  - 部署人在环决策系统时，可参考论文的阈值计算方法，提前测算不同场景下人工复核的成本盈亏平衡点，优化人力配置'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
信用评分、欺诈检测、工业安全等高风险决策场景普遍存在严重类别不平衡、错判成本不对称问题，标准marginal CP虽能保证整体覆盖率，但对稀有高代价小类的覆盖率极低，部分数据集下甚至不足0.5%，无法满足业务需求。
### 方法关键点
搭建多域基准，覆盖15个真实世界不平衡表格数据集、7种分类模型、3种概率校准方法，累计开展3150组实验，对比marginal CP、类条件（Mondrian）CP、不同弃权机制的效果。
### 关键结果
Mondrian CP可有效恢复小类覆盖率，相比marginal CP平均提升61.7个百分点（p<1e-80）；Mondrian CP结合代价控制弃权机制，在真实人工审核预算下，相比标准决策边界、置信度拒识、风险控制拒识方案预期决策成本显著降低，同时可量化各数据集下将歧义样本转交人工审核的成本盈亏阈值。
