---
title: Hierarchical Dual-Graph Retrieval for Long-form Audio Reasoning
title_zh: 面向长音频推理的层次化双图检索方法
authors:
- Eunsang Lee
- Taein Ju
- Jiyoung Lee
affiliations:
- Division of Artificial Intelligence & Software, Ewha Womans University
arxiv_id: '2610.41390'
url: https://arxiv.org/abs/2610.41390
pdf_url: https://arxiv.org/pdf/2610.41390
published: '2026-10-30'
collected: '2026-11-02'
category: RAG
direction: 长音频理解 · 多模态RAG架构优化
tags:
- RAG
- Multi-modal
- Long-form Understanding
- Graph Retrieval
- Audio Reasoning
one_liner: 提出AudioHelix双图RAG框架，融合文本与声学特征跨段关联，提升长音频推理效率与效果
practical_value: '- 做电商直播回放、播客类长音频内容的召回推荐时，可借鉴双图结构同时关联文本语义和声学特征（如情绪、语速），提升相关片段匹配精度

  - 长内容RAG系统可复用层次化跨段关联的思路，解决分散在长序列中多跳相关信息的召回问题，降低长上下文推理成本

  - 多模态内容检索场景下，可补充模态原生特征（如音频声学特征、视频视觉特征）构建关联图，提升多跳推理效果'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
大音频语言模型（LALMs）处理长音频时存在两大痛点：一是难以捕捉分散在远距离片段中的查询相关内容，二是全量处理会带来极高的计算与内存开销；现有纯文本或非图结构RAG方法会丢失声学副语言信息，也无法支撑跨段多跳推理。
### 方法关键点
提出AudioHelix层次化双图RAG框架，分别构建文本、声学两个维度的关联图，打通时间上距离较远的相关文本证据与声学证据的连接，支撑多跳推理，适配LALMs的检索增强需求。
### 关键结果
在TraceAV-Bench、MMAU-Pro、AudioMarathon三个长音频基准数据集上，效果全面优于全音频处理方案和现有RAG方法，同时大幅降低长音频推理的计算成本。
