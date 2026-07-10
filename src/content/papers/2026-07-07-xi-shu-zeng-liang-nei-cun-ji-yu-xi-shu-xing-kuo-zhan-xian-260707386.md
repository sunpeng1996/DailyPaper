---
title: 'Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity'
title_zh: 稀疏增量内存：基于稀疏性扩展线性RNN的状态容量
authors:
- Loïc Cabannes
- Pierre-Emmanuel Mazaré
- Gergely Szilvasy
- Matthijs Douze
- Maria Lomeli
- Ilze Amanda Auzina
- Justin Carpentier
- Gabriel Synnaeve
- Hervé Jégou
affiliations:
- Meta FAIR
- Inria Paris & ENS-PSL University
- University of Tübingen
arxiv_id: '2607.07386'
url: https://arxiv.org/abs/2607.07386
pdf_url: https://arxiv.org/pdf/2607.07386
published: '2026-07-07'
collected: '2026-07-10'
category: LLM
direction: LLM架构 · 长上下文内存优化
tags:
- Linear RNN
- Sparse Memory
- Long Context
- Gated DeltaNet
- Product Key Memory
one_liner: 通过稀疏寻址将线性RNN隐状态容量提升3个数量级，同等算力下长上下文性能显著优于GDN
practical_value: '- 电商/推荐Agent长周期用户行为记忆可复用SDM架构：稀疏读写+固定算力大内存的设计替代KV cache，解决长序列行为建模时算力随长度线性上涨的问题

  - 生成式推荐的海量item语义存储可借鉴可学习初始内存设计：预训练阶段将item语义写入内存，推理时零额外开销调用，无需额外RAG检索

  - 长序列用户建模可复用Product Key Memory稀疏寻址方案：在不提升训练推理算力的前提下，扩容用户行为记忆状态，提升长周期行为召回准确率

  - 工程上可复用SDM的chunk-wise并行训练+fp8/int4快照量化方法：大幅降低大内存状态模型的训练显存开销，适配长序列微调场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
线性RNN（如Mamba2、GDN）虽然单token算力固定、理论上支持无限长序列，但受限于稠密状态更新的算力瓶颈，隐状态容量极小，长上下文召回性能远弱于带KV cache的Transformer；直接扩容状态会导致算力线性上涨，无法落地到长序列业务场景。

### 方法关键点
- 基于GDN架构改造，将稠密键值外积更新替换为对N槽位显式内存表的稀疏读写，采用Product Key Memory的双拆分索引方案，寻址复杂度仅为O(√N + W²+R²)，W/R为每步读写的槽位数，算力与总槽数N无关
- 仅对top-W选中的写槽位执行门控增量更新，未选中槽位保持不变，同等FLOPs下可将状态容量提升3个数量级
- 支持可学习初始内存M0，预训练阶段即可存储通用知识，推理时无额外开销

### 关键结果
- 同等参数和FLOPs约束下，1.4B规模SDM在RULER长上下文基准得分31.2，较GDN的20.0提升11.2；8B规模SDM训练损失优于全注意力Transformer，RULER得分50.2，较GDN的34.2提升16
- 代码任务上，SDM在1M token长度下PPL仍持续下降，显著优于Mamba2和GDN

> 最值得记住的结论：线性RNN的长上下文性能本质由状态容量决定，稀疏化是固定算力下扩容状态、兼顾长上下文能力与推理效率的核心路径
