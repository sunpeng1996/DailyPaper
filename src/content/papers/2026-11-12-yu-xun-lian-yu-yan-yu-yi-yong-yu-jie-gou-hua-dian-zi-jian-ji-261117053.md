---
title: Evaluating Pretrained Language Semantics for Structured EHR Prediction Tasks
title_zh: 预训练语言语义用于结构化电子健康记录预测任务的效果评估
authors:
- Ashvin Gupta
- Brendan Delaney
- Alessandra Russo
affiliations:
- Imperial College London
arxiv_id: '2611.17053'
url: https://arxiv.org/abs/2611.17053
pdf_url: https://arxiv.org/pdf/2611.17053
published: '2026-11-12'
collected: '2026-11-14'
category: LLM
direction: 大模型医疗结构化时序数据预测
tags:
- LLM
- EHR
- LoRA
- Continued Pre-training
- Patient Encoding
one_liner: 提出tEHR框架，将预训练因果LLM适配纵向EHR预测任务，在多医疗数据集上取得最优性能
practical_value: '- 时序结构化数据可转换为自然语言描述文本流，复用预训练LLM的语义关联能力，无需从零学习ID间的关系，可迁移到电商用户行为序列建模场景

  - 领域LLM适配可复用「领域自适应持续预训练 + LoRA下游微调」两阶段范式，大幅降低小样本场景的微调成本

  - 结构化特征的语义描述、数值准确性对性能的影响远大于时序间隔的显式描述，做序列编码时优先保障属性语义、数值的正确性，无需过度优化时间差的文本化表述'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统结构化EHR预测模型将临床概念作为数据集专属token，丢弃事件自带的自然语言语义，概念关联仅能靠共现学习，无法复用预训练语言模型的先验知识。
### 方法关键点
1. 提出tEHR框架，将临床事件转换为自然语言描述组成的文本流
2. 采用两阶段适配：先做EHR领域自适应持续预训练，再用LoRA做任务特定的判别式微调，将LLM作为纵向患者编码器
3.  backbone选用Mistral-7B-v0.3
### 关键结果
在MIMIC-IV数据集4类预测任务、CPRD数据集1-12个月胰腺癌预测任务上取得整体最优性能；消融实验显示移除/错配临床描述、省略数值、跳过任意适配阶段都会导致性能下降，显式经过时间描述增益极低；学到的患者表征具备临床可解释结构，对应不同疾病风险与病史模式。
