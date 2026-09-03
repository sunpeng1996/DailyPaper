---
title: 'Polish ModernBERT: The Long and Short of Polish Language Understanding'
title_zh: 波兰语ModernBERT：适配长短上下文的波兰语理解编码器
authors:
- Michał Perełkiewicz
- Sławomir Dadas
- Rafał Poświata
- Małgorzata Grębowiec
affiliations:
- National Information Processing Institute, Warsaw, Poland
arxiv_id: '2609.01379'
url: https://arxiv.org/abs/2609.01379
pdf_url: https://arxiv.org/pdf/2609.01379
published: '2026-09-01'
collected: '2026-09-03'
category: LLM
direction: 小语种Encoder-only LLM优化
tags:
- ModernBERT
- Encoder-only
- Long Context
- Multilingual
- Polish NLP
one_liner: 推出4款不同规格波兰语ModernBERT编码器，性能优于现有基线，配套开源长上下文评测基准
practical_value: '- 小语种电商/推荐场景做文本理解、召回语义编码时，可参考ModernBERT的预训练配方适配小语种，相比RoBERTa能在更少参数下获得更高性能

  - 长上下文Encoder选型可参考该工作的参数优化方法，8K上下文版本比同规格RoBERTa内存占用更低、延迟更优，适合长文本（商品详情、多轮会话等）语义表征

  - 构建小语种NLP评测集可复用其长上下文多任务基准的构建思路，覆盖垂直场景的判别类任务'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前Encoder-only Transformer在判别、表征学习任务上仍具备高性价比，但波兰语现有编码器多基于老旧的BERT/RoBERTa架构，缺乏高性价比的长上下文版本，也缺乏对应长场景评测基准。

### 方法关键点
基于ModernBERT预训练配方做阶段式选择实验适配波兰语，推出Base/Large两个规模、512/8K两种上下文窗口的共4款编码器，同时开源覆盖法律主题分类、意识形态倾向预测、剧情事实一致性校验、人权违规评估4类任务的长上下文评测基准。

### 关键结果数字
在30个任务上整体性能优于所有参评波兰语编码器，Base-8K、Large-8K版本得分分别达83.99、85.11；长上下文任务上Base版较RoBERTa-8K基线从67.47提升至77.15，参数减少22%，Large版从75.88提升至78.49；推理时内存占用、延迟均优于同规格RoBERTa基线，300M参数以下的Base-8K版本在波兰语检索基准上取得最优结果。
