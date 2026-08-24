---
title: 'SPARCL: Spectral Partitioned Analytic Continual Learning'
title_zh: SPARCL：基于谱分区的解析式持续学习方法
authors:
- James Hartley
- Zeropy Surio
- Daniel Whitmore
- Hannah Clarke
- Thomas Reed
affiliations:
- University of Sheffield
arxiv_id: '2608.21307'
url: https://arxiv.org/abs/2608.21307
pdf_url: https://arxiv.org/pdf/2608.21307
published: '2026-08-21'
collected: '2026-08-24'
category: Training
direction: 解析式持续学习 · 谱分解抗遗忘
tags:
- Continual Learning
- Spectral Decomposition
- Ridge Regression
- Class Incremental Learning
- Closed-form Update
one_liner: 通过谱分解冻结核子空间旧分类器参数，解决解析持续学习无样本回放下的旧类漂移问题
practical_value: '- 电商推荐增量更新用户/类目分类器时，可复用谱分区思路，冻结存量高能量特征维度的旧分类器权重，避免全量重训导致的旧类目识别准确率下跌

  - 无样本回放的增量训练场景下，可借鉴自相关矩阵分解+仅更新残差块的方案，降低增量训练的存储成本与计算开销

  - Agent场景下的增量技能学习，可引入该方法保证旧技能核心逻辑不漂移，同时支持新技能的快速闭式更新，无需梯度迭代'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
解析式持续学习用闭式岭更新替代梯度迭代，是无样本回放类增量学习的高效方案，但现有方法即便用精确递归求解器仍存在旧类漂移问题，原有梯度覆盖导致遗忘的逻辑无法解释该现象，根因是新旧任务共享自相关算子逆矩阵，新任务样本加载到旧类主特征方向会稀释谱分布、扰动旧类logits。

### 方法关键点
提出SPARCL，将运行时自相关矩阵分解为高能量核心与残差两个子空间，冻结核心子空间中的旧类分类器组件，仅通过递归最小二乘更新残差块，可选对残差做随机投影扩展，具备旧类logits核心贡献的可证明不变性，更新过程为闭式计算。

### 关键结果
在冻结ViT-B/16的实验设置下，于CIFAR-100、CUB-200、ImageNet-R、ImageNet-A数据集上，填补了传统解析学习器与强表征匹配器之间的绝大部分性能差距，可与Fly-CL等稀疏特征去相关方法互补。
