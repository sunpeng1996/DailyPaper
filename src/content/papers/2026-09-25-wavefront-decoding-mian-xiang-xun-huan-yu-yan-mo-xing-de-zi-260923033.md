---
title: 'WaveFront Decoding: Parallelized Self-Speculative Decoding for Looped Language
  Models'
title_zh: WaveFront Decoding：面向循环语言模型的并行自推测解码框架
authors:
- Hyeongju Ha
- Jae-Joon Kim
affiliations:
- Seoul National University
arxiv_id: '2609.23033'
url: https://arxiv.org/abs/2609.23033
pdf_url: https://arxiv.org/pdf/2609.23033
published: '2026-09-25'
collected: '2026-09-29'
category: LLM
direction: 大语言模型推理 · 自推测解码优化
tags:
- Speculative Decoding
- Looped LM
- Decoding Optimization
- KV Cache
- Parallel Inference
one_liner: 无需训练无需修改模型的循环语言模型自推测解码方案，较自回归解码最高提速4.81倍
practical_value: '- 端侧Agent、电商生成式推荐（商品文案/个性化push文案）场景如果采用Looped LM部署，可直接接入WFD解码，无需额外训练或微调模型，即可获得2~4倍的推理吞吐提升，有效降低部署成本

  - 长上下文生成场景（如基于用户长期历史的个性化内容生成）下，搭配跨循环KV共享使用WFD，可进一步将Huginn类P/R/C架构Looped LM的吞吐提升至4.8倍，同时精度损失控制在1个百分点以内

  - 现有自推测解码的工程实现可参考WFD的波前调度思路，将草稿生成与校验阶段的计算合并批量处理，消除两阶段切换的空闲开销，相比传统Draft-then-Verify方案可稳定提升27%左右的吞吐'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Looped LM（循环语言模型/通用Transformer）通过复用相同权重的循环块实现高有效深度，参数量仅为同性能固定深度Transformer的几分之一，十分适合端侧Agent、低成本生成式推荐等场景部署；但原生自回归解码生成单个token需要执行T次串行循环块调用，时延随T线性增长，严重抵消了其参数效率优势。传统两阶段自推测解码DtV（Draft-then-Verify）分草稿生成、批量校验两个串行阶段，仍然存在大量空闲资源，并行性挖掘不足。

### 方法关键点
- 提出波前调度机制：将不同位置、不同循环深度的token状态组成对角波前，在同一次循环块批量调用中同时完成新token浅层草稿生成、旧token深度递进和深层校验，完全消除两阶段的串行边界，提升资源利用率
- 无侵入适配：无需额外训练、无需修改模型权重、无需外接独立草稿模型，兼容全栈式、P/R/C两种主流Looped LM架构
- 瓶颈优化：搭配跨循环KV共享技术，缓解波前内多深度token访问不同KV槽带来的流量随波宽、上下文长度暴增的问题，进一步提升长上下文场景的性能

### 关键实验
在Ouro-2.6B（全栈式）、Huginn-3.5B（P/R/C式）两个公开Looped LM上，基于Spec-Bench 6类任务测试，对比自回归解码（AR）、DtV基线：
- 无KV共享时，WFD较AR分别提速2.42×、3.54×，较DtV稳定提升1.27倍吞吐
- 搭配跨循环KV共享，Huginn上最高提速达4.81×，GSM8K、MATH-500任务精度损失小于0.7个百分点
- 接受率在0.6~0.95区间内，WFD性能始终优于所有块长配置的DtV方案，鲁棒性更强

### 核心结论
Looped LM的参数效率要落地为实际部署的时延优势，核心是将串行的循环调用转化为可批量的并行任务，而非单纯依赖参数量缩减。
