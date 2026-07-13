---
title: Transfer Learning for Linear Discriminant Analysis with a Shared Classification
  Signal
title_zh: 基于共享分类信号的线性判别分析迁移学习方法
authors:
- Yonghan Zhang
- Yimeng Fan
- Wenya Luo
- Jiang Hu
affiliations:
- Northeast Normal University
- Zhejiang University of Finance and Economics
arxiv_id: '2607.06936'
url: https://arxiv.org/abs/2607.06936
pdf_url: https://arxiv.org/pdf/2607.06936
published: '2026-07-08'
collected: '2026-07-13'
category: Other
direction: 迁移学习 · 高维线性判别分类优化
tags:
- Transfer Learning
- Linear Discriminant Analysis
- High-dimensional Classification
- Spiked Covariance Model
- Domain Adaptation
one_liner: 提出带共享分类信号的高维二分类LDA迁移学习框架，推导误差边界、最优权重与偏差校正方案
practical_value: '- 跨域分类场景（如不同区域用户行为分类）可复用均值分解思路，拆分共享分类信号与域特有偏差，降低跨域数据异质性影响

  - 高维小样本分类任务（如新品类目预测、冷启动用户标签判定）可参考文中加权迁移分类器的权重估计方法，提升小样本下分类准确率

  - 分类任务中目标域样本类别不平衡时，可复用文中的截距偏差校正方案，优化不平衡样本下的分类效果'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
高维小样本场景下传统LDA的样本协方差矩阵不稳定，分类效果差，且跨域迁移时未量化域间共享信号与异质性对效果的影响，缺乏可落地的权重估计与偏差校正方案。
### 方法关键点
1. 将各域类别均值差分解为跨域共享的确定性分类信号分量与域特有随机偏差分量；
2. 在尖峰协方差模型下，分别推导同构、异构协方差设定下加权迁移分类器的目标域高斯校准误差的确定性边界，量化共享信号强度、域偏差、维数样本比、尖峰结构对迁移效果的影响；
3. 给出最优迁移权重的一致数据驱动估计器，同时针对目标域类别样本不平衡导致的截距偏差提出渐近最优校正方案。
### 关键结果
推导的误差边界可精准量化各因素对迁移性能的影响，最优权重估计与偏差校正方案可在高维跨域二分类任务中稳定提升分类准确率。
