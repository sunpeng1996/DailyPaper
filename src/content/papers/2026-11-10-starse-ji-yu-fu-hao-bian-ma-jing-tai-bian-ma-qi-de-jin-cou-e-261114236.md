---
title: 'StaRSE: Compact Russian Sentence Embeddings with a Sign-Coded Static Encoder'
title_zh: StaRSE：基于符号编码静态编码器的紧凑型俄语句嵌入模型
authors:
- Boris Malashenko
- Ivan Jarsky
- Egor Soldatov
- Vladislav Luzhnov
- Sviatoslav Stumpf
- Vladislav Shmatkov
- Viacheslav Shalamov
- Andrey Stankevich
- Valeria Efimova
affiliations:
- ITMO University, Saint Petersburg, Russia
arxiv_id: '2611.14236'
url: https://arxiv.org/abs/2611.14236
pdf_url: https://arxiv.org/pdf/2611.14236
published: '2026-11-10'
collected: '2026-11-12'
category: RAG
direction: 文本嵌入 · 低延迟压缩优化
tags:
- sentence embedding
- static embedding
- model compression
- information retrieval
- low latency inference
one_liner: 移除部署端Transformer推理，实现体积仅11.3MiB、低延迟的高性能俄文静态句嵌入模型
practical_value: '- 低延迟嵌入场景可复用「离线预计算token符号向量+范数、在线仅做lookup+mean pooling」的架构，大幅降低CPU推理时延

  - 静态嵌入优化可借鉴「先从预训练Transformer初始化、再用对比学习直接优化符号投影token表」的两阶段训练范式

  - 小体积部署场景可参考符号位存储token方向的压缩方法，在可控精度损失下将嵌入模型体积压缩80%以上'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
Transformer上下文句嵌入推理成本高，CPU部署、高频更新、大语料计算等场景下时延和存储成为瓶颈，现有静态句嵌入性能差距较大。
### 方法关键点
1. 部署阶段完全移除Transformer推理，token方向以符号位存储、范数单独存储，句编码仅需lookup后对范数缩放的符号向量做mean pooling
2. 从ruBERT-base初始化，先在俄文相邻句、任务构造句对上微调，再通过对比学习阶段直接优化符号投影token表
### 关键结果数字
在RuMTEB基准上任务平均得分51.16，比最强静态基线高7.98；模型体积仅11.3MiB，单句CPU平均时延0.08ms，相比同性能上下文编码器体积压缩79.7%，时延降低94.4%
