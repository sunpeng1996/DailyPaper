---
title: 'Leaf Values as Coordinates: Exact Contrastive Explanation for Gradient-Boosted
  Ensembles'
title_zh: 叶值作为坐标：梯度提升集成模型的精确对比解释方法
authors:
- Emanuele Luzio
affiliations:
- Independent Researcher
arxiv_id: '2608.19127'
url: https://arxiv.org/abs/2608.19127
pdf_url: https://arxiv.org/pdf/2608.19127
published: '2026-08-19'
collected: '2026-08-20'
category: Other
direction: 树模型可解释性 · 对比解释
tags:
- GBDT
- Contrastive Explanation
- Recourse
- Model Interpretability
- Tabular Data
one_liner: 将梯度提升集成模型的叶值视作坐标，生成完全精确的对比解释与可落地决策整改建议
practical_value: '- 电商/广告场景的GBDT排序、准入策略模型，可直接复用该方法做精确解释，快速定位影响样本打分的关键树分裂节点，辅助策略迭代

  - 面向用户的决策解释场景（如资质驳回、活动准入拒绝），可基于该方法生成仅包含用户可修改特征的整改建议，大幅提升建议可落地性

  - 模型合规审计场景，可利用其1e-15级的决策还原精度，离线校验模型决策逻辑，无需依赖在线模型服务'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
梯度提升集成（GBDT、XGBoost等）是电商推荐、风控、流量准入场景的主流模型，现有对比解释方法多为近似结果，生成的整改建议常包含年龄、历史违约等用户不可修改特征，实用性差。
### 方法关键点
将每棵树的输出叶值视作坐标，把样本映射为R^M空间的向量，模型打分等价于该坐标的无加权和，天然具备加性特征；对比两个样本的决策差异时，仅在叶节点不同的树对应坐标存在差值，可直接定位差异来源，无需额外拟合、采样或假设。
### 关键结果
- 模型决策还原误差低至6.2×10^-15，审计无需依赖原模型服务
- 信用数据集上，解释的用户修改成本与真实度权衡为帕累托最优
- 仅允许修改用户可操作特征时，建议有效性保留58%，远超基线的41%
