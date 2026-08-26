---
title: 'Wontopos Tablet 2: Measuring Multilingual and Multimodal Memory Retrieval
  Without Lexical Matching'
title_zh: Wontopos Tablet 2：无词汇匹配的多语言多模态记忆检索评测
authors:
- Sunwoo Kim
affiliations:
- Wontopos L.L.C.
arxiv_id: '2608.23920'
url: https://arxiv.org/abs/2608.23920
pdf_url: https://arxiv.org/pdf/2608.23920
published: '2026-08-24'
collected: '2026-08-26'
category: Eval
direction: RAG记忆系统 · 多模态多语言评测
tags:
- Memory Retrieval
- Multimodal RAG
- Multilingual Retrieval
- Benchmark
- Long Context
one_liner: 公布无词汇匹配的生产级多模态记忆引擎Tablet 2的多语言、长文本记忆检索全量评测结果
practical_value: '- 跨境电商多语言商品检索可放弃依赖图片caption的匹配方案：实验显示加英文caption会使其他13种语言的检索效果平均下降11.4个点，无caption的纯语义检索对小语种更友好，无需提前做多语言标注

  - 电商Agent/客服Agent的长记忆系统可复用无LLM依赖的re-ask机制：允许最多3次排除已召回结果的重查，在百万级记忆语料上可提升BEAM-1M得分8.9个点，小语料提升1.2个点，可根据业务语料规模灵活配置重查阈值，且检索过程确定性高、可预计费

  - 多语言检索效果评估可新增BM25基准做校验：BM25的跨语言得分仅在同源/同文字语言间有传递性，其余场景接近0，可快速定位当前检索方案是否存在词汇匹配依赖的缺陷，避免虚高的评测结果

  - 做记忆系统/检索系统对比时要严格控制变量：Reader模型、重查预算、上下文扩展策略都会显著影响最终得分，跨系统对比时必须固定这些变量，不能仅看头对头的得分排名做选型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前RAG记忆系统的评测通常混淆检索能力与下游Reader模型的推理能力，且极少针对无词汇匹配的多语言多模态检索场景做严格校验；现有基准普遍不披露Reader选型、重查策略等关键变量，导致跨系统得分可比性差，同时跨境电商等场景的多模态检索需要摆脱词汇匹配的语种限制，适配无文本标注的商品图片等非结构化数据。
### 方法关键点
- 被测对象Tablet 2为纯语义检索架构，全程无BM25、关键词匹配或内置LLM，支持文本、图片混合存储检索
- 评测分两类场景：长文本记忆基准（LongMemEval-S、BEAM-1M），固定Judge配置，对Reader模型、重查预算、上下文扩展做控制变量 ablation；多语言多模态检索基准，构造无caption图片语料，用最优配置的BM25做对照基线，覆盖14种高低资源语言
- 重查机制不依赖LLM改写Query，仅排除已召回结果做多轮检索，保证检索确定性、可预计费
### 关键结果
- 长文本场景：LongMemEval-S得分95.7%，中位数检索延迟393ms；BEAM-1M得分67.5%，开启重查比关闭提升8.9个点，切换Reader模型可带来2个点的得分波动
- 多模态场景：70个跨语言检索单元格中BM25平均得分19%，54个单元格得0；Tablet 2平均得分95.2%，无caption场景下14种语言平均recall@5达91.4%，跨语言表现远优于普通稠密检索基线
- 负结论：为图片添加英文caption会使其他13种语言的检索效果平均下降11.4个点，低资源语言斯瓦西里语、泰卢固语recall@5仅53%、64%

记忆系统的评测得分没有绝对意义，Reader模型、重查预算等未披露变量带来的得分波动往往超过不同系统间的真实差距，跨系统对比仅在所有配置固定时才有参考价值
