---
title: 'MoganBert-TR: A Turkish Encoder Foundation Model Trained from Scratch with
  a CLM-to-MLM Curriculum'
title_zh: MoganBert-TR：采用CLM转MLM课程的从零训练土耳其语编码器基础模型
authors:
- Furkan Yilmaz
- Habibe Aleyna Tasdemir
- Muhammed Faruk Gozay
arxiv_id: '2608.25768'
url: https://arxiv.org/abs/2608.25768
pdf_url: https://arxiv.org/pdf/2608.25768
published: '2026-08-26'
collected: '2026-08-27'
category: LLM
direction: 小语种基础模型 · 预训练范式优化
tags:
- Pre-training
- Encoder LLM
- CLM
- MLM
- Embedding Model
- Tokenizer
one_liner: 提出CLM→MLM两阶段预训练范式，打造SOTA土耳其语149M参数编码器及配套嵌入模型
practical_value: '- 小语种电商/广告场景做本地化LLM可复用CLM→MLM两阶段预训练范式，同等步数下检索性能比纯MLM高2.7-3.7倍，大幅降低小语种模型训练成本

  - 长上下文扩展可采用共享前缀后分支退火的方案，仅需4.3%额外成本即可获得TrGLUE+0.49的收益，性价比远高于model soup方案

  - 小语种嵌入模型可沿用「大模型教师蒸馏+多信号对比微调」的路径，149M小模型即可达到7.57B大模型99.5%的效果，大幅降低线上推理延迟'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有土耳其语编码器预训练长期采用固定MLM目标，公开预训练数据无本地化质量过滤，小语种模型性能普遍偏低。

### 方法关键点
1. 基于237.3B经过语言过滤的语料训练149M参数土耳其语编码器MoganBert-TR，采用两阶段CLM→MLM课程预训练，在WSD schedule稳定阶段切换训练目标，不调整学习率
2. 预训练后期采用分支退火策略，共享前缀训练后拆分出长上下文分支，在1024上下文窗口完成最后学习率衰减阶段
3. 配套通过大模型蒸馏+多信号对比微调得到MoganBert-Embed嵌入模型，同步训练50048词表的土耳其语Tokenizer

### 关键结果
- 两阶段预训练比纯MLM在土耳其语MS MARCO检索任务性能高2.7-3.7倍，嵌入几何方差集中度从28.1%降至11.9%
- MoganBert-TR TrGLUE得分78.41，为同类土耳其语ModernBERT最优，TabiBench代码检索领先SOTA 3.62分
- MoganBert-Embed在MTEB（土耳其语）学生模型中排第一，仅为7.57B教师模型1/51参数量即可达到其99.5%的性能
