---
title: 'MERGED: Multimodal Entity Resolution via Generated Expert Reasoning Distillation'
title_zh: MERGED：基于生成式专家推理蒸馏的多模态商品实体对齐框架
authors:
- You-Lin Chen
- Kyoungjun Park
- Bin Xu
- Prithviraj Sen
- Pedro Herrero-Vidal
affiliations:
- Amazon, United States
arxiv_id: '2609.01913'
url: https://arxiv.org/abs/2609.01913
pdf_url: https://arxiv.org/pdf/2609.01913
published: '2026-09-01'
collected: '2026-09-03'
category: RecSys
direction: 多模态商品实体对齐 · 大模型蒸馏
tags:
- Multimodal Entity Resolution
- Knowledge Distillation
- DPO
- SFT
- VLM
- E-commerce
one_liner: 零人工标注下通过多教师VLM推理蒸馏+SFT+DPO训练7B小模型，电商实体对齐效果超32B大模型且成本降6倍
practical_value: '- 电商实体对齐/商品归一场景可复用这套零人工标注蒸馏方案：用2个大VLM做教师，共识样本做SFT、分歧样本经meta-judge标注后做DPO，无需人工标注即可快速上线小模型

  - 业务规则迭代时无需重新全量训练：基于已训练好的基线checkpoint，仅需10K样本重新过一遍SFT+DPO即可适配新的实体关系定义，迭代周期从数月压缩到数天

  - 推理对齐度优化可参考：蒸馏时不仅迁移标签，同时迁移大模型的结构化推理过程，能同时提升指标和推理可信度，降低模型决策黑盒问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商商品实体对齐是目录去重、关联推荐、替代商品露出的核心基础，但业务规则随场景、市场、合规要求动态迭代，传统方案依赖人工标注，周期长达数月且标注噪声高；零/少样本调用大VLM虽能快速适配，但成本、时延无法满足日均千万级的工业生产需求，亟需兼顾低标注成本、高性能、低推理开销的落地方案。

### 方法关键点
- 蒸馏框架分两阶段：多教师VLM同时标注商品对并输出推理过程，多教师标签+推理一致的高置信样本用于SFT训练7B小模型基线，对齐任务目标
- 教师分歧样本视为难例，经meta-judge VLM评估推理合理性后生成偏好对，用于DPO训练强化难例判别能力，同时提升推理与标签的对齐度
- 规则迭代适配方案：基于旧规则训练的checkpoint，仅需生成10K新规则下的样本重跑SFT+DPO即可完成适配，无需从零训练

### 关键实验
基于亚马逊内部多语言电商数据集，含100K+样本覆盖8种语言、18个国家，测试集为6K人工标注样本：
1. 7B小模型经MERGED训练后PR-AUC达90.96%，比同架构用人工标注训练高13.79%，比32B零样本VLM高6.32%，推理成本仅为32B模型的1/6
2. 适配新的变体匹配规则时，仅需10K样本微调即达89.48% PR-AUC，比零样本高6.97%，远超从零训练的效果
3. 推理与标签对齐度达92.82%，比32B零样本VLM高10%以上

### 核心结论
大模型蒸馏不仅可以迁移标签，同步迁移结构化推理过程+DPO优化难例，能让小模型在零人工标注的情况下超过大模型效果，同时大幅降低推理成本。
