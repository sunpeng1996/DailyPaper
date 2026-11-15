---
title: Evaluation of Music Version Retrieval Methods for Setlist Identification in
  Live Concerts
title_zh: 面向现场演唱会曲目单识别的音乐版本检索方法评估
authors:
- Andres Ferraro
- Albin Correya
affiliations:
- Nowon AG, Switzerland
arxiv_id: '2611.17070'
url: https://arxiv.org/abs/2611.17070
pdf_url: https://arxiv.org/pdf/2611.17070
published: '2026-11-12'
collected: '2026-11-15'
category: Eval
direction: 音频检索 · 算法基准评测
tags:
- Audio Retrieval
- Embedding
- Benchmark Evaluation
- Vector Search
- Low-Resource Retrieval
one_liner: 在ASID基准上评测多类音乐版本检索方法，验证低维嵌入NAVE可兼顾精度与低存储成本
practical_value: '- 高噪声大规模向量召回场景可优先验证低维嵌入方案，在召回模块用256维替代1024维嵌入，可降低4倍存储与检索时延同时不损失精度，适配千万级以上候选库场景

  - 连续时序内容（如直播内容检索、用户长会话行为召回）可前置有效/无效内容门控预处理，既能提升识别边界精度，还能降低无效计算量

  - 工业界多方案选型可复用该评测范式，先在公开/业务自建基准上做横向对比，再做线上成本与收益的tradeoff验证'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现场演唱会曲目单识别需应对低音质、演出改编差异、长时序处理、大规模检索四大挑战，现有音乐版本检索方案的实际适配效果缺乏系统评测。
### 方法关键点
基于ASID基准横向对比三类版本检索系统：传统方案Re-MOVE、对比学习方案CLEWS、自研神经音频版本嵌入模型NAVE；额外评测音乐/非音乐门控预处理的优化效果。
### 关键结果数字
NAVE、CLEWS性能大幅优于Re-MOVE；NAVE仅用256维嵌入，比CLEWS的1024维存储减少4倍，同时检索精度更优；音乐门控预处理可小幅提升检测精度与时序覆盖度，还能优化标准指标未覆盖的识别边界效果。
