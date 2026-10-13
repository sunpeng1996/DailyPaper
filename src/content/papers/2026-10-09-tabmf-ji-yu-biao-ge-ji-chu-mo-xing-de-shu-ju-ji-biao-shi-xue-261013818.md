---
title: 'TabMF: Learning Dataset Representations with Tabular Foundation Models'
title_zh: TabMF：基于表格基础模型的数据集表示学习方法
authors:
- Rafiq Kamel
- Nicolas Atienza
- Aziz Fouché
- Nicola Cancedda
- Josif Grabocka
affiliations:
- University of Technology Nuremberg (UTN)
- Neuralk
arxiv_id: '2610.13818'
url: https://arxiv.org/abs/2610.13818
pdf_url: https://arxiv.org/pdf/2610.13818
published: '2026-10-09'
collected: '2026-10-13'
category: Training
direction: 表格大模型 · 数据集表示学习
tags:
- Tabular Foundation Model
- Contrastive Learning
- Dataset Representation
- Pre-trained Model
- Transfer Learning
one_liner: 复用预训练表格基础模型，通过架构感知读出层与对比后训练生成高性能数据集表示
practical_value: '- 电商用户行为、交易、商品属性等表格类数据集的检索、分布偏移监测可复用TabMF架构，基于现有预训练表格FM快速生成数据集表示

  - 跨业务数据集做模型/超参数迁移时，可先通过TabMF生成的数据集向量匹配相似场景数据集，降低新业务冷启动成本

  - 用合成数据集随机视图做对比增强的训练思路，可复用在小样本表格类推荐模型的微调阶段'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有数据集表示方案依赖人工构造元特征或专门训练的独立编码器，泛化性有限，无法灵活适配数据集检索、分布偏移监测等上层任务。
### 方法关键点
1. 基于已完成预测预训练的表格基础模型（TFM）作为backbone，新增架构感知的数据集级读出层，将样本级输出聚合为固定维全局表示
2. 构造合成监督数据集的随机视图作为对比样本，开展对比后训练，端到端适配数据集表示任务
### 关键结果
在6个未知真实数据集的任务上，仅冻结TFM训练读出层即可达到有竞争力的效果；基于TabICLv2、TabPFN-2.5的两个TabMF实例，在所有参与评估的学习型/传统数据集表示方法中取得最优综合性能，在数据集检索、精简基准构建、分布偏移严重度评估三类任务上优势尤为突出
