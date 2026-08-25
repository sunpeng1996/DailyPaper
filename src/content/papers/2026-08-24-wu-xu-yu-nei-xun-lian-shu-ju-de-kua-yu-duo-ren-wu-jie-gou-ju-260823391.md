---
title: Cross-Domain, Multi-Task Data-to-Text Generation without In-Domain Training
  Data
title_zh: 无需域内训练数据的跨域多任务结构化数据转文本生成
authors:
- Yifei Song
- Kun Efimov-Zhang
- Claire Gardent
affiliations:
- CNRS/LORIA
- Université de Lorraine
arxiv_id: '2608.23391'
url: https://arxiv.org/abs/2608.23391
pdf_url: https://arxiv.org/pdf/2608.23391
published: '2026-08-24'
collected: '2026-08-25'
category: LLM
direction: 大模型跨域生成 · 知识蒸馏
tags:
- Data-to-Text
- Knowledge Distillation
- Cross-Domain
- Data Augmentation
- Low-Resource NLP
one_liner: 提出带结构保留增强的DDKD蒸馏方法，无需域内训练数据即可实现跨域多任务D2T生成，效果优于零样本与域外微调
practical_value: '- 电商场景无域内标注数据时，可复用DDKD蒸馏方案，用大模型零样本能力做教师、小模型做学生，低成本落地商品参数转详情文案、运营报表转自然语言解读等D2T任务

  - 结构化数据（如商品属性表、用户行为统计报表）做训练增强时，可借鉴结构保留增强策略，通过子采样、扰动输入结构提升小模型泛化性，无额外标注成本

  - 跨域迁移D2T能力时，优先选用结构增强的蒸馏方案，比单纯堆目标域无标注数据成本更低、效果提升更明显'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有D2T（结构化数据转文本）方案要么依赖域内标注数据，要么直接调用大模型零样本推理成本高、效果不稳定，无法适配域、生成目标、输入结构差异大的跨域无标注场景。
### 方法关键点
1. 对比零样本推理、域外数据微调两种基线方案，提出数据驱动知识蒸馏（DDKD）框架：以大模型零样本生成的伪标签为监督，蒸馏得到小尺寸的D2T模型
2. 引入结构保留增强策略，对输入结构化数据做子采样、扰动，保留核心结构的同时低成本扩充训练样本
### 关键结果
- 1.7B参数规模下，DDKD在5个基准测试集上效果一致优于零样本推理和域外微调
- 蒸馏得到的小模型在2个领域效果超过参数量大得多的微调模型，剩余3个领域效果相当
- 结构增强策略比单纯扩大目标域真实输入规模成本更低、效果提升更显著
