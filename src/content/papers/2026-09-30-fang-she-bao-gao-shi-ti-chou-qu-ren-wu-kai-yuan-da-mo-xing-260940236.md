---
title: Comparison of techniques for fine-tuning open-weight models for entity extraction
  from radiology reports
title_zh: 放射报告实体抽取任务开源大模型微调技术对比研究
authors:
- Aawez Mansuri
- Kush Mehta
- Mohammadreza Chavoshi
- Jahanzaib Malik
- Theodorus Dapamede
- Frank Li
- Rohan Isaac
- Beatrice Brown-Mulry
- Chiratidzo Rudado Sanyika
- YoungSeok Jeon
affiliations:
- Emory University School of Medicine
- Emory University Department of Computer Science
arxiv_id: '2609.40236'
url: https://arxiv.org/abs/2609.40236
pdf_url: https://arxiv.org/pdf/2609.40236
published: '2026-09-30'
collected: '2026-10-02'
category: Training
direction: 大模型微调 · 蒸馏与合成数据效果对比
tags:
- LoRA
- Instruction Tuning
- Knowledge Distillation
- Synthetic Data
- Fine-tuning
- Entity Extraction
one_liner: 对比开源大模型实体抽取的微调策略与数据源，证实蒸馏真实数据可让模型媲美GPT-4o
practical_value: '- 做电商垂直域实体抽取（如商品属性识别、评论要素提取、Query意图标签化）时，优先用强闭源模型标注真实业务数据做知识蒸馏，效果远优于合成数据训练，可快速追平闭源模型表现

  - 相同数据量下，指令微调(IFT)比外接分类头(CH)的泛化性、输出准确率更高，若无需概率输出优先选IFT方案，训练速度也快3~10倍

  - 采用4bit NF4量化+LoRA微调12B级开源模型可在24GB消费级GPU上跑通，窄域任务仅需2000条标注数据即可达到工业可用水平，一次性训练成本不足10美元

  - 高流量业务场景优先部署微调后的开源小模型，推理成本比闭源API低8~15倍，年调用量过千即可覆盖一次性微调成本，还可规避数据泄露、API版本漂移问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
闭源大模型在放射报告实体抽取任务上表现最优，但存在隐私合规风险、API调用成本高、模型版本不可控易漂移等问题，开源模型微调是可行替代方案，但不同微调策略、训练数据源的效果差异缺乏定量对比，亟需明确最优落地路径。
### 方法关键点
- 基底模型选用Gemma-3-12B，采用4bit NF4量化+LoRA方案，训练、推理均可在单张24GB消费级GPU上运行
- 2×2析因实验设计：交叉两种适配策略（外接多标签分类头CH、生成式指令微调IFT），两种训练数据源（GPT-4o标注真实报告的蒸馏数据、GPT-4o基于少量样例生成的合成报告数据）
- 任务为颅内出血多标签分类，覆盖4个非互斥的acuity分级标签
### 关键实验结果
训练集规模最大2000条，测试集为100份放射科专家独立标注的报告，对比零样本GPT-4o、零样本Gemma-3-12B两个基线：
1. 蒸馏数据训练的指令微调模型(DIFT) macro-F1达0.845，与GPT-4o的0.850无统计学差异，比基线开源模型高0.178
2. 合成数据训练的所有模型在任意训练规模下均未超过基线开源模型，数据来源对效果的影响远大于微调方法
3. 单张L40S GPU上DIFT训练2000条数据仅需1小时39分，推理成本比GPT-4o API低8~15倍，年调用量过千即可覆盖一次性微调成本
### 核心结论
对于窄域高价值的实体抽取类任务，蒸馏真实业务数据而非生成合成数据，是让开源模型快速追平闭源模型效果的核心决定因素。
