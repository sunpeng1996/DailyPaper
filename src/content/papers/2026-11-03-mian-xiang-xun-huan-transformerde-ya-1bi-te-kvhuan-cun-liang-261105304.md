---
title: 'LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers'
title_zh: 面向循环Transformer的亚1比特KV缓存量化方法LoopVQ
authors:
- Minsoo Cheong
- Sungjoo Yoo
affiliations:
- Seoul National University
arxiv_id: '2611.05304'
url: https://arxiv.org/abs/2611.05304
pdf_url: https://arxiv.org/pdf/2611.05304
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: LLM推理优化 · KV cache量化
tags:
- KV cache
- Quantization
- Looped Transformer
- Vector Quantization
- SGLang
one_liner: 利用循环Transformer KV缓存跨步冗余实现亚1比特量化，大幅提升推理效率与精度保留率
practical_value: '- 业务若使用循环Transformer类轻量LLM做Agent推理/生成式推荐文案生成，可直接复用LoopVQ的跨循环步VQ分组方案，将KV缓存压缩到0.5bit以内，大幅提升单卡并发量、降低推理成本

  - 普通LLM的KV缓存量化可借鉴「利用不同推理步/层的量化敏感度差异做加权码本微调」的思路，在低比特量化下减少精度损失，尤其适配长上下文RAG、长链推理场景

  - 工程实现可参考其SGLang适配方案，将KV缓存分页存储，最近窗口存BF16、历史页存量化索引，平衡精度和性能，适合电商长会话推荐、多轮Agent交互场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
循环Transformer通过复用同组层参数实现了极高参数效率，同等性能下参数量仅为普通LLM的几分之一，非常适合端侧/高并发推理场景，但每步循环都需要存储独立KV缓存，缓存大小随循环步线性增长，成为内存瓶颈；现有面向普通LLM的KV量化方法未利用循环步间的冗余，低于1bit时精度损失严重，无法落地。
### 方法关键点
- 循环轴向量量化：将多个连续循环步的同组通道拼接为一个子向量做VQ，共享同一个编码索引，相同比特下重构误差降低近50%
- 循环感知码本微调：冻结模型权重，以全精度模型输出的KL散度为目标微调码本，适配不同循环步的量化敏感度差异（早期循环步误差会传递到后续所有步，敏感度更高）
- 工程适配：在SGLang中实现分页缓存，前若干sink token和最近窗口用BF16存储，历史token存量化索引，定制attention kernel直接从索引+对应循环步的码本切片重构KV，无额外开销
### 关键结果
在GSM8K、MATH500、长链推理、RULER NIAH长上下文任务上测试，对比CQ、TaSQ等通用KV VQ基线：
- 0.5bit下，LoopVQ结合TaSQ在Ouro-2.6B上平均精度仅比BF16低1.16pp，远低于基线28.77pp的精度损失；0.25bit下仍能保留BF16 86%以上的平均精度
- 32K上下文下单卡解码延迟降低近50%，Ouro-1.4B、2.6B的峰值服务吞吐分别提升4.3倍、6.1倍
> 最值得记住的话：针对模型结构特有的冗余做定制化量化，能在更低比特下实现远优于通用方案的精度-效率 tradeoff
