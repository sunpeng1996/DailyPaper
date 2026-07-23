---
title: In-Context Time Series Classification with Random Convolutional Features
title_zh: 结合随机卷积特征的上下文学习时序分类方法
authors:
- Joscha Cüppers
- Jilles Vreeken
affiliations:
- CISPA Helmholtz Center for Information Security
arxiv_id: '2607.19234'
url: https://arxiv.org/abs/2607.19234
pdf_url: https://arxiv.org/pdf/2607.19234
published: '2026-07-21'
collected: '2026-07-23'
category: Other
direction: 时序分类 · 上下文表格大模型应用
tags:
- Time Series Classification
- In-Context Learning
- Foundation Model
- Convolutional Feature
- Tabular Foundation Model
one_liner: 将MultiRocket、Hydra特征与上下文表格基模型结合，无需任务训练即可取得时序分类SOTA性能
practical_value: '- 电商用户行为时序分类任务（如异常用户识别、营销转化预判）可复用「随机卷积特征提取+表格大模型上下文推理」pipeline，省去小样本场景下的模型微调成本

  - 业务侧时序特征工程可直接借鉴MultiRocket+Hydra的特征组合方案，高效捕捉用户点击/浏览序列的局部形态、频率等隐含信息，提升特征表达效率

  - 若已落地业务专属预训练表格大模型，可直接对接传统工程提取的结构化特征，无需任务专项训练即可快速上线小样本分类能力'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
时序分类广泛应用于医疗、工业监测等场景，现有SOTA集成方案计算成本高昂；传统随机卷积变换可高效将时序映射为固定维表格特征，但仅搭配简单线性分类器，特征表达潜力未被充分挖掘，小样本场景下任务专项训练成本高。

### 方法关键点
MASHT pipeline首先通过MultiRocket和Hydra算子将时序数据转换为高丰富度的固定维表格特征，直接输入预训练上下文表格基模型完成推理，全程无需任务相关的模型微调或训练，仅需特征提取步骤。

### 关键结果
单变量时序分类任务上性能匹配SOTA基线，平均排名优于HIVE-COTE 2.0；多变量时序数据集上性能与当前最强参考方法高度可比
