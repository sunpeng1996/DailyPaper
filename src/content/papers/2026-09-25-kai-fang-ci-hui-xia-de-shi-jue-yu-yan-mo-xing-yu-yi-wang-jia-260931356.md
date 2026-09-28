---
title: Open Vocabulary Domain Unlearning
title_zh: 开放词汇下的视觉语言模型域遗忘框架
authors:
- Sumanth Udupa
- Mehrtash Harandi
- Yadan Luo
- Mahsa Baktashmotlagh
affiliations:
- The University of Queensland
- Monash University
arxiv_id: '2609.31356'
url: https://arxiv.org/abs/2609.31356
pdf_url: https://arxiv.org/pdf/2609.31356
published: '2026-09-25'
collected: '2026-09-28'
category: Training
direction: 多模态模型 · 领域遗忘优化
tags:
- Unlearning
- Vision-Language Model
- Open Vocabulary
- Few-Shot
- Parameter Efficient
one_liner: 提出开放词汇域遗忘范式及精准参数编辑框架，仅用4样本效果超基线8-shot最优结果
practical_value: '- 可复用Fisher Information mask参数隔离方法，在多模态推荐模型微调时保护通用零样本能力，仅修改特定域相关权重，降低全量微调成本

  - Targeted Manifold Scattering目标可迁移至多模态召回场景，用于擦除模型对违规/低质商品风格域的识别能力，同时不影响其他品类的召回效果

  - 少样本域遗忘方案可用于业务场景快速擦除特定敏感域知识，仅需4样本即可达到现有方案8样本效果，大幅降低标注成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有近似域遗忘（ADU）方法基于闭词汇假设，仅对微调阶段见过的类-域对生效，无法泛化到未见过的类别，存在虚假遗忘问题，真实域擦除需要与类别无关。

### 方法关键点
1. 形式化开放词汇域遗忘（OVDU）协议，要求域遗忘能力可迁移到未见过的类别；
2. 提出精准参数编辑框架，先用Fisher Information mask隔离域敏感权重，从数学层面保护基础零样本泛化能力；
3. 提出Targeted Manifold Scattering（TMS）目标，基于偏好挖掘局部打散待遗忘域的风格流形。

### 关键结果数字
在PACS、OfficeHome、DomainNet数据集上，开放词汇泛化能力大幅优于基线，仅用4个样本效果超过基线8-shot的最优结果。
