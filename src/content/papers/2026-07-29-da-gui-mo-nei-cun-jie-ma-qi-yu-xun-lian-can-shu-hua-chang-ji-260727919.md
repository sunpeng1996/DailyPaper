---
title: 'Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory'
title_zh: 大规模内存解码器：预训练参数化长时记忆模块
authors:
- Rubin Wei
- Jiaqi Cao
- Jiarui Wang
- Junming Zhang
- Qipeng Guo
- Bowen Zhou
- Zhouhan Lin
affiliations:
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
- Tsinghua University
arxiv_id: '2607.27919'
url: https://arxiv.org/abs/2607.27919
pdf_url: https://arxiv.org/pdf/2607.27919
published: '2026-07-29'
collected: '2026-07-31'
category: LLM
direction: 大模型 · 参数化长时记忆优化
tags:
- Parametric Memory
- LLM Scaling
- Distributed Faiss
- Knowledge Distillation
- Long-term Memory
one_liner: 将参数化长时记忆扩至6.9B参，小基座配大内存比纯扩基座省39%参数且效果更优
practical_value: '- 垂直领域适配可复用该方案：无需全量微调基座，训练小参数化内存模块插拔即可，效果优于LoRA、CPT，适合电商/导购大模型的领域切换，避免灾难性遗忘

  - 大规模kNN构造可直接复用分布式Faiss管道：OPQ压缩+索引分片+并行检索的设计，可解决大规模RAG、语义召回场景下的超大语料索引检索瓶颈

  - 稀疏kNN分布存储的trick可直接落地：仅存阈值以上的token-prob对，存储量降低250倍，大幅降低大规模预训练/检索场景的存储与IO成本

  - 参数分配可参考小基座+大内存的高性价比方案：相同效果下参数占用减少30%以上，推理时两个模块可并行跑降低latency，适合低算力场景的电商Agent落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Decoder-only LLM将长时记忆与推理耦合在同一参数集，无法独立扩展内存容量，领域适配易出现灾难性遗忘，记忆模块无法跨模型复用。此前Memory Decoder仅在1B参、百万级tokens语料下验证，大规模下kNN分布构造、存储的瓶颈未被解决。
### 方法关键点
- 分布式Faiss管道：通过OPQ将4096维隐态压缩至256维，结合索引分片、GPU并行检索，解决207B tokens语料下的kNN分布构造瓶颈
- 稀疏kNN分布存储：仅保留概率大于阈值的token-prob对，存储量降低250倍，配合分布式流式加载，支持300B tokens规模的内存预训练
- 训练推理范式：内存模块预训练采用KL散度对齐kNN分布+CE语言建模混合损失，推理时与冻结基座的next token分布加权插值，无需在线检索
### 关键结果
- 通用场景：Pythia-410M搭配6.9B通用内存，17项基准平均得分37.34，超过Pythia-12B的37.24，总参数少39%
- 领域场景：1.7B垂直内存（生物/法律/金融）接入0.6B-14B的Qwen3基座，领域平均得分提升9分以上，14B基座下生物领域提升17.96分，效果远超LoRA、CPT、RAG基线
- 跨模型迁移：仅用20%标准训练预算适配词汇表，即可为OLMo-2/3-7B带来4.26/7.77分的领域效果提升
### 核心结论
独立scaling预训练长时记忆，是比纯扩大模型基座参数效率高得多的性能提升路径
