---
title: 'Train Smarter, Not Harder: Switching Signal-Guided Training in Active Learning'
title_zh: 主动学习下的切换信号引导训练：兼顾效果与效率的训练策略优化
authors:
- Nagham Omar
- Maya Rozenshtein
- Evgeny Mishlyakov
- Avigdor Gal
affiliations:
- Faculty of Data and Decision Sciences, Technion
arxiv_id: '2609.06806'
url: https://arxiv.org/abs/2609.06806
pdf_url: https://arxiv.org/pdf/2609.06806
published: '2026-09-05'
collected: '2026-09-10'
category: Training
direction: 主动学习 · 训练策略自适应优化
tags:
- Active Learning
- Training Efficiency
- Fine-tuning
- Model Calibration
- Text Classification
one_liner: 提出基于模型稳定信号自适应切换重训/微调的主动学习训练框架HybridAL，大幅节省训练成本且效果不劣
practical_value: '- 迭代式标注训练场景（如用户反馈冷启动、小样本类目识别）可复用自适应切换训练策略：前期小批量标注后全量重训拟合分布，稳定后用微调降本

  - 两类切换信号可直接复用：低成本场景用验证集精度变化ΔAcc快速判断稳定点，高要求场景用权重谱指数变化Δα保障校准效果

  - 推荐系统周期重训场景可参考逻辑：新特征/新流量上线初期全量重训，分布稳定后切增量微调，兼顾效果和训练成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
主动学习迭代过程中，每次新增标注数据后选择全量重训还是基于上轮checkpoint微调的策略长期被忽略，固定全量重训成本极高，固定微调则无法适配早期标注分布的剧烈变化，难以兼顾效率与效果。

### 方法关键点
1. 提出HybridAL自适应训练调度方案，实时监测模型稳定信号，标注分布剧烈波动的前期用全量重训保证拟合效果，模型轨迹稳定后自动切换为微调降低训练成本
2. 提供两类互补切换信号：基于模型权重的谱指数变化Δα、基于验证集的精度变化ΔAcc，覆盖不同效率-校准trade-off需求

### 关键结果数字
在3类encoder backbone、6个文本分类任务上，宏观F1相比全量重训/微调劣化幅度不超过0.010，最高节省49%训练时间，校准效果（NLL）显著优于固定轮次切换的方案
