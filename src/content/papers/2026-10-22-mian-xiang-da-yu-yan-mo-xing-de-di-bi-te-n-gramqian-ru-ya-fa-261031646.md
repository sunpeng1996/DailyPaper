---
title: Low-Bit N-Gram Embeddings for Language Models
title_zh: 面向大语言模型的低比特n-gram嵌入压缩方法
authors:
- Stephen Chung
- Wenyu Du
affiliations:
- DualverseAI
arxiv_id: '2610.31646'
url: https://arxiv.org/abs/2610.31646
pdf_url: https://arxiv.org/pdf/2610.31646
published: '2026-10-22'
collected: '2026-10-23'
category: LLM
direction: 大语言模型 · n-gram嵌入量化压缩
tags:
- Quantization
- N-gram Embedding
- Memory Efficiency
- LLM Optimization
- Low-bit Compression
one_liner: 通过低比特量化压缩LLM的n-gram嵌入表，大幅降低内存开销同时保留几乎全部性能增益
practical_value: '- 推荐系统大规模用户/物品嵌入表可直接复用这套量化方案：4bit量化省75%内存、保留99%以上性能，优先选择Lloyd–Max码本+误差拟合缩放，效果远优于均匀量化

  - 生成式推荐、用户行为序列建模中用到的n-gram lookup表可采用混合精度分配策略：优先给bigram分配更高比特，相同内存开销下效果优于均匀比特分配

  - 节省的内存可直接用于扩容嵌入表规模：2bit量化+4倍表大小，相比原16bit小表性能增益提升22%~26%，同时还可节省46%~48%内存，适合搜推大规模嵌入场景降本提效

  - 低比特压缩后仅需短时间微调即可恢复大部分性能损失，无需重新预训练，业务上线成本极低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前大量开源LLM引入n-gram嵌入表提升性能，但这类表内存开销极高，例如DeepSeek-V4.1-Flash的Engram n-gram内存就达1960亿参数，直接缩小表规模会严重损失性能，亟需在保留性能的前提下降低n-gram表的内存占用成为落地刚需。

### 方法关键点
- 对训练好的n-gram嵌入表做低比特量化：每个表共享一个码本，每个嵌入存储1个16bit缩放因子，每个分量存储b比特的码本索引，重构时用索引取码本值乘以缩放因子得到原始嵌入
- 对比三类码本构造方案：均匀量化、正态分位数量化、Lloyd–Max量化；三类缩放因子选择：最大值缩放、RMS缩放、误差拟合缩放
- 支持混合精度分配，对不同阶的n-gram表分配不同比特数，平衡内存开销和模型性能
- 支持压缩后短微调恢复性能，也可将节省的内存扩容嵌入表规模进一步提升效果

### 关键结果
- 从零训练的nanochat、Llama、GPT-2系列模型上，4bit表节省75%内存，保留99%以上的n-gram表带来的验证损失增益；3bit表节省80%内存，保留97%增益
- 现有大模型DeepSeek-V4.1-Flash、Qwen3.8-Flash-Next上，混合精度方案节省47%-55%的n-gram表内存，perplexity上升小于1.2%，下游任务平均准确率下降小于1%
- 2bit量化+4倍表规模，比原16bit小表性能增益高22%-26%，同时还省46%-48%的内存

n-gram嵌入表量化中，缩放因子的选择对效果影响远大于码本类型，低比特量化+扩容表规模的收益远高于缩小表规模降内存
