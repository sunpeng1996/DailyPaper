---
title: 'LO-FAR: A Cost-Aware Local Filter for Sparse Feature Ranking in Industrial
  Ad Recommendation'
title_zh: LO-FAR：工业广告推荐下成本感知的稀疏特征排序本地过滤器
authors:
- Egemen Erbayat
- Luis Duque
- Sohini Roychowdhury
- Mohammad Amin
- Srihari Reddy
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2607.20873'
url: https://arxiv.org/abs/2607.20873
pdf_url: https://arxiv.org/pdf/2607.20873
published: '2026-07-23'
collected: '2026-07-24'
category: RecSys
direction: 工业推荐 · 稀疏特征选择
tags:
- Sparse_Feature
- CTR_Prediction
- Feature_Selection
- Industrial_RecSys
- Embedding_Optimization
one_liner: CPU-only轻量稀疏ID-list特征排序方案，效果比肩GPU基线，耗时仅2个CPU小时
practical_value: '- 可直接复用第一阶段剪枝思路：先用LO-FAR CPU跑轻量本地预估筛掉长尾低信号稀疏特征，再用高成本交互感知方法做精细筛选，大幅降低GPU开销

  - 短ID-list稀疏特征重要性评估可直接复用其「ID展开→单ID正率预估→样本级聚合→holdout logloss排序」的流水线，不绑定下游模型，易并行落地

  - 可将该流程集成到内部特征迭代管线，无需占用GPU资源，团队可高频验证新特征价值，加快迭代 cadence

  - 特征预算约束下，40-75%的稀疏embedding存储剪枝不会明显损失CTR/CVR的Normalized Entropy增益，可参考该比例做存储优化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业广告推荐CTR/CVR模型中，稀疏ID-list特征对应的embedding表占97%以上参数，是存储、训练、推理成本的核心来源；现有稀疏特征排序方法要么需要多轮GPU重训（如排列重要性、BSN）成本高、迭代慢，要么依赖简单覆盖度 heuristic 效果差，亟需低成本、可高频迭代的第一阶段稀疏特征筛选方案。

### 方法关键点
- 完全CPU-only、模型无关，不依赖下游排序模型，每个特征独立处理可线性并行
- 流水线：采样百万级分层标注样本→拆分训练测试集→ID-list展开为单ID行并复制标签→轻量本地预估器（高频ID直接用训练集正率，低频ID用K近邻回退）→聚合回样本级预测值→按holdout logloss排序特征
- 时间复杂度O(p·n·ℓ·log(nℓ))，p为特征数，n为样本数，ℓ为平均ID列表长度

### 关键实验
基于Meta生产环境100万+交互样本、475个短ID-list稀疏特征验证，对比覆盖度heuristic、排列重要性、BSN三类基线：100-400特征预算下，CTR/CVR任务的Normalized Entropy增益与两个GPU基线持平，排序耗时仅2 CPU小时，GPU基线则需要数GPU天，计算成本仅为后者的1/40；对应可减少40%-75%的稀疏embedding存储。

### 核心结论
工业场景的特征排序不能只看离线效果，需将重跑成本、周转时间、运维复杂度作为第一优先级评估指标，简单局部过滤器在第一阶段剪枝场景下的性价比远高于重度交互感知方案。
