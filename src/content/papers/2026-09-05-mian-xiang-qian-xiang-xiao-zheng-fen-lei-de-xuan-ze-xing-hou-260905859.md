---
title: Selective Posterior Margin Regularization for Forward-Corrected Classification
title_zh: 面向前向校正分类的选择性后验边缘正则化方法
authors:
- Zexing Zhang
- Jichao Li
- Tianyang Lei
- XiongYi Lu
- Yang Kewei
affiliations:
- College of Systems Engineering, National University of Defense Technology
arxiv_id: '2609.05859'
url: https://arxiv.org/abs/2609.05859
pdf_url: https://arxiv.org/pdf/2609.05859
published: '2026-09-05'
collected: '2026-09-09'
category: Training
direction: 带噪标签学习 · 分类模型鲁棒训练
tags:
- noisy-label learning
- forward correction
- posterior regularization
- robust classification
- regularization
one_liner: 提出选择性后验边缘正则化SPMR，提升类条件标签噪声下前向校正分类鲁棒性
practical_value: '- 电商推荐/搜索的带噪标注分类训练场景，可直接引入SPMR正则化，替代硬标签修正，避免误修正引入额外噪声

  - 处理众包标注的用户行为标签（如点击/转化标签的类条件噪声）时，可复用「基于后验分布差异分级调整梯度权重」的思路，降低噪声标签对模型的干扰

  - 无需新增模型组件，仅在原有前向校正损失基础上添加正则项，工程实现成本低，可快速接入现有分类训练pipeline'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
类条件标签噪声场景下，前向校正方法虽将标签转移矩阵嵌入似然计算，但小样本下模型仍易记忆污损标签，且修正后似然得到的干净类别反向后验top候选区分度低，直接硬修正标签易引入误差。
### 方法关键点
提出SPMR正则化，保留前向校正目标的同时仅当反向后验最高类别与观测标签不一致时触发更新：选取反向后验最高的类别，用top2后验的间隔对成对边缘进行缩放，弥散冲突（间隔小）的样本权重极低，同时沿局部最小范数logit方向放大成对边缘，不强制修正所有冲突标签。
### 关键结果
5个已知转移矩阵的基准测试中，SPMR比全量前向校正精度高2.5-7.0pp，比加Mixup+早停的前向校正高0.7-2.5pp，可迁移到估计转移矩阵、人工标注、不同架构等场景。
