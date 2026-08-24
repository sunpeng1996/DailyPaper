---
title: 'EDGE: a closed-form directed test for the calibration of probabilistic binary
  classifiers'
title_zh: EDGE：面向概率二分类器校准的闭式定向检验方法
authors:
- Ebrahim Khaled Ebrahim
- Ahmed El-Kotory
affiliations:
- Department of Statistics, Alexandria University, Egypt
arxiv_id: '2608.20511'
url: https://arxiv.org/abs/2608.20511
pdf_url: https://arxiv.org/pdf/2608.20511
published: '2026-08-20'
collected: '2026-08-24'
category: Eval
direction: 二分类模型校准度评估方法
tags:
- Calibration
- Binary Classifier
- Logistic Regression
- Model Evaluation
- Statistical Test
one_liner: 提出无需重训练重采样的闭式概率二分类器校准显著性检验方法EDGE，性能优于现有分箱类检验
practical_value: '- CTR/CVR等推荐广告二分类预估模型的校准度检验可直接复用EDGE，替换现有ECE评估，无需调参可嵌入交叉验证流水线，快速区分真实校准偏差与噪声

  - 分箱+预定义平滑基投影的思路可借鉴到稀疏特征场景下的模型离线评估，规避传统Stukel检验在稀疏样本下20%~28%的失效问题

  - 明确所有分箱类校准评估（含ECE）的适用边界：高频剧烈校准偏差场景需改用全局统计量，避免评估误判'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有概率二分类器常用的分箱期望校准误差（ECE）仅为描述性统计，无零分布无法区分校准偏差是真实存在还是噪声，且依赖分箱策略；基于重训练的校准检验存在稀疏样本下不可计算、耗时高无法嵌入交叉验证的问题。

### 方法关键点
提出EDGE闭式定向校准检验，基于可靠性图的分箱预测-观测表，将标准化分箱残差投影到预定义的平滑校准失真形状基上，零分布为卡方变量加权和的闭式解，仅需一次数据遍历+小规模特征分解，无需重训练、重采样、调参。

### 关键结果数字
22个可检测场景中19个场景下性能领先或持平其他分箱类检验；稀疏样本下EDGE始终可计算，对比Stukel检验20%~28%的失效概率优势显著；所有分箱类检验（含ECE）均不适用高频剧烈校准偏差场景。
