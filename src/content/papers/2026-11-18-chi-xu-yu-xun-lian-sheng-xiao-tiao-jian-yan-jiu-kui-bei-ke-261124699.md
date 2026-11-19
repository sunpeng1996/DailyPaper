---
title: When Does Continual Pre-Training Help? A Controlled Study of Dialectal Adaptation
  for Québec French
title_zh: 持续预训练生效条件研究：魁北克法语方言适配的控制实验
authors:
- Eeham Khan
- Richard Khoury
- Leila Kosseim
affiliations:
- Concordia University
- Université Laval
arxiv_id: '2611.24699'
url: https://arxiv.org/abs/2611.24699
pdf_url: https://arxiv.org/pdf/2611.24699
published: '2026-11-18'
collected: '2026-11-19'
category: Training
direction: LLM 低资源方言适配训练优化
tags:
- Continual Pre-training
- Dialect Adaptation
- LoRA
- Low-resource Adaptation
- LLM Evaluation
one_liner: 通过9款不同规模LLM的控制实验，明确方言适配场景下持续预训练的生效条件、核心驱动因素与评估陷阱
practical_value: '- 垂直域（电商区域化运营、方言客服Agent等）LLM适配前，优先评估基模型在目标域的现有能力，能力足够的大模型无需额外做CPT，节省算力成本

  - 低资源域CPT优先优化语料组成而非盲目堆数据：适配区域方言/行业黑话时，优先加入正式出版物/权威文档类语料，比爬取大量零散UGC效果更好

  - 适配效果评估不能只看PPL或聚合指标，必须做细分任务专项评测：比如电商域适配要单独测商品标题理解、用户咨询语义理解等核心任务，避免被聚合指标掩盖能力退化

  - 相同CPT预算下中小模型的目标域能力提升幅度远高于大模型，边缘端轻量化垂域模型可优先选用中小基座+CPT方案'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Continual Pre-training（CPT）广泛用于LLM的方言/垂直域适配，但业界缺乏统一的生效边界指导，不清楚基模型能力、语料组成、评估方式三个核心因素对CPT效果的影响，聚合指标还容易掩盖能力退化，导致资源浪费或效果不达预期。

### 方法关键点
- 所有实验严格控制CPT token预算为30M，排除数据量干扰，覆盖CroissantLLM、Llama、Qwen三个系列共9款0.5B~14B参数的LLM
- 采用LoRA冻结基座权重的适配方式，对比正式语料、非正式语料、不同混合比例、留一genre ablation等多组实验
- 采用配对评估方案：同时测魁北克法语和标准法语的语法、方言表达理解、通用任务能力，拆分聚合指标做单任务评估

### 关键结果
- 基模型能力越强，CPT收益越低：最弱的CroissantLLM 1.35B的方言表达理解提升8.2pp，最强的Qwen2.5 14B反而下降2.2pp
- 语料组成远重要于数据量：30M正式语料的适配效果优于60M混合语料，其中文学类语料贡献了90%以上的方言表达理解收益，纯非正式语料会导致8/9的模型方言理解能力下降
- 评估陷阱：PPL和聚合任务指标会掩盖能力退化，比如移除文学语料后魁北克法语PPL下降34%，但方言表达理解得分下降16pp，纯正式语料CPT会导致通用阅读理解能力下降18.5pp

### 核心结论
低资源场景下CPT不是通用银弹，需先评估基模型现有能力、优先优化语料组成、采用细分任务专项评估才能获得最优收益
