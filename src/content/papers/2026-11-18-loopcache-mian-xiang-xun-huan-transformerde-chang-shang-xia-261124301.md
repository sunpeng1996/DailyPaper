---
title: 'LoopCache: Accelerating Long-Context Self-Speculative Decoding for Looped
  Transformers'
title_zh: LoopCache：面向循环Transformer的长上下文自投机解码加速框架
authors:
- Zizhuo Fu
- Haochen Huang
- Shengxuan Qiu
- Linye Wei
- Ziyu Tang
- Runsheng Wang
- Meng Li
affiliations:
- Peking University
arxiv_id: '2611.24301'
url: https://arxiv.org/abs/2611.24301
pdf_url: https://arxiv.org/pdf/2611.24301
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: LLM推理优化 · KV cache 自投机解码
tags:
- KV cache
- Self-Speculative Decoding
- Looped Transformer
- Long Context
- Inference Acceleration
one_liner: 通过动态草稿更新、循环KV调度和浅层KV解耦实现循环Transformer长上下文解码数倍提速
practical_value: '- 长上下文Agent、生成式推荐场景可复用循环KV调度策略，将单步KV访问量限制为单份，大幅降低长用户行为序列/多轮对话prompt下的内存带宽瓶颈，提升响应速度

  - 自投机解码场景可借鉴置信度引导的动态草稿更新逻辑，基于新老token的logit差设置阈值更新草稿，避免过时轨迹的无效计算，提升投机接受率，降低推理延迟

  - 可复用跨层KV相似性的设计思路：仅为对KV变化敏感的浅层保留独立缓存，深层KV跨循环共享，既能保证生成质量，又能控制内存开销，适合业务侧低资源部署需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Looped Transformer通过共享权重的循环块实现高有效深度，是小模型增强推理、长horizon Agent能力的主流架构之一，但现有波式自投机解码方法存在两大痛点：一是仅在固定循环层生成草稿，忽略中间层预测变化，浪费大量算力在过时轨迹上；二是不同循环层的token批处理需要单次读取R倍KV缓存，长上下文下内存流量激增，完全抵消流水线收益，甚至比普通自回归解码更慢。
### 方法关键点
- 置信度引导的动态草稿更新：监控中间循环层的预测变化，仅当新预测与旧草稿的logit差超过设定阈值时才更新草稿，同时剪枝过时的后续推测token，避免预测反复切换的有害开销
- 循环KV缓存调度：全局步骤按固定周期循环访问不同循环层的KV缓存，单步仅读取1份全前缀KV，将KV流量降到和普通自回归解码一致；拆分投机分支和验证分支，投机分支共享当前周期KV生成草稿，验证分支在对应KV周期做无损精确校验，保证输出分布不变
- 选择性浅层KV解耦：针对浅层KV跨循环差异大、深层差异小的特性，仅为前2层左右的浅层保留独立KV访问，其余层共享周期KV，以极小的额外开销提升草稿接受率
### 关键实验
在Ouro、Huginn、Raven系列共6款循环Transformer上测试，上下文长度覆盖4K~128K，对比AR、DtV、WFD、LoopSpec等基线，平均实现10.25×/14.56×速度提升超过WFD/LoopSpec，比普通AR和DtV分别快5.12×/2.52×，不同batch size下性能衰减远低于基线
> 核心结论：长上下文下自投机解码的性能瓶颈往往不是计算量，而是KV缓存的内存访问流量，优化KV访问优先级远高于提升流水线并行度
