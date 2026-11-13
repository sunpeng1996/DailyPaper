---
title: Two mathematical models of knowledge distillation
title_zh: 知识蒸馏的两种数学解释模型
authors:
- Audrey Xie
- Ludwig Schmidt
- John Duchi
affiliations:
- Stanford University
arxiv_id: '2611.17230'
url: https://arxiv.org/abs/2611.17230
pdf_url: https://arxiv.org/pdf/2611.17230
published: '2026-11-12'
collected: '2026-11-13'
category: Training
direction: 模型训练 · 知识蒸馏理论解析
tags:
- Knowledge Distillation
- Optimization
- Generalization
- SGD
- Model Compression
one_liner: 从数学层面证明知识蒸馏的收益来自优化速度提升而非泛化能力增强
practical_value: '- 做小模型蒸馏时无需追求泛化增益，可直接将蒸馏作为加速小模型收敛、降低训练成本的技术手段，无需过度调优teacher的泛化能力

  - 电商/广告场景蒸馏轻量化排序/召回模型时，可基于该结论调整训练流程：优先保证蒸馏对齐teacher输出，无需额外增加提升泛化的正则项浪费训练资源

  - 大模型微调后蒸馏到小模型上线的场景，可直接用该结论做训练速度预估，合理分配训练算力，缩短模型迭代周期'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有知识蒸馏的效果归因存在两大对立假说，一派主张收益来自泛化能力提升，一派认为来自优化效率提升，缺乏严谨的数学论证明确其核心价值来源。
### 方法关键点
构建两类数学模型开展理论分析：1）针对SGD训练的广义线性模型，推导蒸馏训练的收敛速率边界；2）针对秩1矩阵近似任务，刻画蒸馏训练收敛速度优于原生监督训练的目标矩阵约束条件。
### 关键结果
理论证明知识蒸馏的收益仅来自更平滑的优化landscape带来的收敛速度提升，无额外泛化增益；广义线性模型场景下蒸馏训练的收敛速度渐近快于原生监督训练，真实数据集实验完全验证上述理论结论。
