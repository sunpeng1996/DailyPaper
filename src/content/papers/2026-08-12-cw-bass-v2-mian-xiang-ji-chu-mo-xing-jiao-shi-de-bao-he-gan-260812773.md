---
title: 'CW-BASS v2: Saturation-Aware Pseudo-Label Selection for Semi-Supervised Segmentation
  under Foundation-Model Teachers'
title_zh: CW-BASS v2：面向基础模型教师的饱和感知半监督分割伪标签选择方法
authors:
- Ebenezer Tarubinga
arxiv_id: '2608.12773'
url: https://arxiv.org/abs/2608.12773
pdf_url: https://arxiv.org/pdf/2608.12773
published: '2026-08-12'
collected: '2026-08-15'
category: Other
direction: 半监督学习 · 伪标签筛选优化
tags:
- Pseudo Labeling
- Semi-Supervised Learning
- Confidence Calibration
- Foundation Model
- Confidence Saturation
one_liner: 提出适配大模型置信度饱和特性的伪标签选择方法，优化半监督训练效果
practical_value: '- 大模型蒸馏/半监督打标场景可复用饱和感知逻辑：对LLM/多模态大模型输出的高置信伪标，先通过held-out验证集计算置信准确率，再决定筛选策略，避免确认偏差

  - 伪标签筛选可直接套用「预定义阈值判断+自适应置信下限兜底」的双路径框架，无需为不同任务单独调参

  - 多模态搜索/商品图文打标场景，可复用无偏类别噪声估计方法，降低人工标注成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
传统半监督语义分割的伪标签筛选规则适配弱ResNet教师模型，当DINOv2等基础模型作为教师时，置信度极易饱和，原有严格筛选规则反而会损害训练性能。

### 方法关键点
1. 提出饱和感知伪标签选择框架CW-BASS v2，先通过held-out集计算教师高置信样本集的准确率$\pi_{kept}=Pr[correct|c≥\tau]$
2. 当$\pi_{kept}$满足预设阈值时采用严格筛选，否则回落至可证明保留率小于1的自适应置信下限，全程无需针对mIoU调参

### 关键结果数字
饱和基准集上追平UniMatch V2性能：Pascal VOC 1/8标注率下达87.4 mIoU，Cityscapes性能差距小于0.5；高置信集不可靠场景（ADE20K）下比UniMatch V2高1.5 mIoU
