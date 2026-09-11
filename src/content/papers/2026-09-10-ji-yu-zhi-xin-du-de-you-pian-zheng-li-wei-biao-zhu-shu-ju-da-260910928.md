---
title: AUC Maximization from Biased Positive-unlabeled Data with Confidence
title_zh: 基于置信度的有偏正例-未标注数据AUC最大化方法
authors:
- Atsutoshi Kumagai
- Tomoharu Iwata
- Hiroshi Takahashi
- Taishi Nishiyama
- Kazuki Adachi
- Yasuhiro Fujiwara
affiliations:
- NTT, Inc.
arxiv_id: '2609.10928'
url: https://arxiv.org/abs/2609.10928
pdf_url: https://arxiv.org/pdf/2609.10928
published: '2026-09-10'
collected: '2026-09-11'
category: Training
direction: 弱监督学习 · PU AUC优化
tags:
- PU-Learning
- AUC-Maximization
- Weak-Supervision
- SAR-Setting
- Imbalanced-Classification
one_liner: 利用正例置信度修正标注偏差，实现有偏PU场景下的AUC最大化且无需强假设
practical_value: '- 推荐/广告排序场景下，若负样本难以获取（如未点击不能直接作为负样本、隐私限制无法获取负标注），可基于少量带置信度的正样本+海量未标注数据训练AUC最优排序模型，避免SCAR假设不成立导致的性能衰减

  - 正样本置信度不需要严格校准，只要是真实后验概率的严格单调递增变换就有效，多轮模型打分、人工标注置信分、业务规则输出的风险分均可直接使用，无需额外概率校准，降低落地成本

  - 可复用损失构造思路，给有偏正样本（如仅头部热门商品有点击正样本、长尾商品正样本缺失）按「置信度/样本被标注概率」加权，修正样本选择偏差，提升长尾商品排序性能

  - 训练时对估计的标注概率做最小值裁剪（如裁剪到0.01）即可稳定训练，无需复杂超参调整，工程落地难度低'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
AUC是不平衡分类/排序任务的核心指标，但电商欺诈检测、广告点击预估、医疗诊断等实际场景往往无法获取可靠负标注，仅能拿到正样本和未标注数据（PU数据）。现有PU-AUC方法均假设标注正样本无偏（SCAR假设），但实际中正样本普遍存在选择偏差（SAR场景，如热门商品更容易被曝光产生点击正样本、仅已知类型的恶意流量会被标注），现有SAR场景PU方法需要强分布假设，且不支持AUC优化。

### 方法关键点
- 利用标注正样本自带的置信度（样本为正的后验概率）修正选择偏差，推导得到有偏PU数据下的AUC风险无偏估计器，无需对数据分布、标注机制做强假设
- 理论证明即使置信度是真实后验的任意严格单调递增变换，最小化该风险仍能得到贝叶斯最优AUC排序，不需要置信度严格校准
- 训练流程：首先用PU数据训练分类器估计每个样本的标注概率$p(o=1|x)$，再按「置信度/标注概率」给正样本加权，计算带权重的平滑AUC损失优化排序模型；优化时可忽略和类先验、正样本标注率相关的常数项，无需估计这两个难获取的参数

### 关键实验
在8个真实数据集（4个图像、2个表格、2个人工标注置信度数据集）上对比8个基线方法，在正样本占比5%-20%的不平衡场景下，比SCAR假设的PUAUC方法平均提升2.1个百分点，比SAR场景PU方法（PUSB、PG）平均提升3.8个百分点；即使置信度经过幂变换或加高斯噪声，性能波动不超过1个百分点，鲁棒性极强。

### 核心结论
有偏PU场景下做AUC最大化，只要正样本带有序关系正确的置信度，就能无需强假设得到最优排序，是极适合工业落地的弱监督排序方案
