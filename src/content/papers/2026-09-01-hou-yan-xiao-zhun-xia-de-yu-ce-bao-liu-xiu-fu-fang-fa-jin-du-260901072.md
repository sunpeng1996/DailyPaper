---
title: 'Let Confidence Change, Not the Prediction: Prediction-Preserving Repair for
  Post-hoc Calibration'
title_zh: 后验校准下的预测保留修复方法：仅调整置信度不改变预测结果
authors:
- Daehwan Kim
- Haejun Chung
- Ikbeom Jang
affiliations:
- Hanyang University
- Hankuk University of Foreign Studies
arxiv_id: '2609.01072'
url: https://arxiv.org/abs/2609.01072
pdf_url: https://arxiv.org/pdf/2609.01072
published: '2026-09-01'
collected: '2026-09-04'
category: Training
direction: 模型后验校准 · 预测一致性保障
tags:
- Post-hoc Calibration
- Prediction Preservation
- Confidence Calibration
- TPCR
- Model Reliability
one_liner: 提出无额外超参数的后校准适配器CORD，实现零Top-1预测更改率的同时优化校准指标
practical_value: '- 推荐/广告排序的置信度校准场景可直接复用CORD，在不改变原有排序Top结果的前提下优化置信度准确性，避免校准导致的线上排序波动

  - 无需额外训练、无超参数的设计适合快速上线，可直接挂载在现有Platt缩放、温度缩放等校准模块之后，无额外推理overhead

  - 多分类召回、粗排模型的置信度输出可套用该修复逻辑，保障召回结果集合稳定性的同时提升下游排序的置信度输入质量'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多分类后验校准方法在调整置信度的同时会改变原始Top-1预测结果，引发线上模型输出波动，而传统准确率指标无法衡量预测变更频率(TPCR)的负面影响。
### 方法关键点
1. 无训练、无超参数的后适配模块CORD，仅对校准后的概率向量做修复，不改动原有校准器的逻辑与输出；
2. 构造上保证原始Top-1类别的概率权重始终最高，剩余概率质量按校准后的条件分配给其他类别，实现零TPCR；
3. 校准集上尽可能保留原始校准输出对原预测类别的平均置信度，最大化校准效果。
### 关键结果
在CIFAR-10/100、ImageNet-1K数据集上实现零TPCR，相比直接校准输出，ECE、NLL、Brier得分全量下降，分布偏移、不同校准集大小场景下收益均稳定。
