---
title: 'HiKV: Hierarchical Importance-Aware KV Cache with Hardware Acceleration for
  LLM Decoding'
title_zh: HiKV：面向LLM解码的分层重要性感知KV缓存与硬件加速
authors:
- Chao Fang
- Jun Yin
- Man Shi
- Marian Verhelst
affiliations:
- KU Leuven
- UC Berkeley
arxiv_id: '2607.22389'
url: https://arxiv.org/abs/2607.22389
pdf_url: https://arxiv.org/pdf/2607.22389
published: '2026-07-24'
collected: '2026-07-27'
category: LLM
direction: LLM推理优化 · KV缓存压缩
tags:
- KV cache
- Hardware Acceleration
- LLM Inference
- Algorithm-Hardware Co-design
- Cache Compression
one_liner: 软硬协同设计双层粒度KV缓存压缩，实现高压缩比低精度损失的LLM解码加速
practical_value: '- 长上下文Agent/生成式推荐场景可优先复用分层压缩思路：先按token重要性粗筛缓存，再按元素重要性细筛，在1%精度损失内大幅降低内存占用，提升单卡服务并发量

  - 软件层KV cache优化可直接复用双bank（近期token+重要token）管理策略，无需硬件修改即可降低重要token误删概率，比纯滑动窗口（如StreamingLLM）的长上下文精度更稳定

  - 端侧/边缘侧部署LLM推理服务（如电商智能客服、实时生成式推荐）时，可参考HiKV的可配置排序加速器设计，仅用8%的面积开销实现7倍以上的解码速度提升'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文LLM在电商多轮客服、长文档商品总结、多轮推荐对话等场景落地时，KV cache随序列长度、batch size线性增长，成为推理内存瓶颈；现有重要性感知KV缓存仅做token级压缩，未挖掘token内部元素的冗余，且动态排序开销大，无法兼顾压缩比、精度与推理效率。

### 方法关键点
- 算法层双层正交压缩：Stage I粗粒度token级，用双bank结构（近期token bank+重要token bank）维护token重要性，仅保留固定预算内的高贡献token，重要性仅在近期bank内累加，用min-heap实现O(log B)的低开销eviction；Stage II细粒度元素级，对Q向量全局排序选top元素指导K缓存加载，对P向量分chunk并行排序选top元素指导V缓存加载，进一步降低单token内存访问量
- 硬件层设计可重构重要性排序器（RIS），复用同一电路支持Stage I的堆操作和Stage II的两种排序需求，仅增加8%的系统面积开销

### 关键结果
在LongBench的10个任务上测试4款主流LLM（Mistral-7B、Llama3-8B等），对比vanilla KV cache、StreamingLLM、H2O等baseline：精度损失<1%时总压缩比可达2~16倍，比单粒度的H2O最高多2倍压缩比；对比vanilla基线，注意力计算速度最高提升7.95倍，能耗降低90%；同等精度下，比SOTA重要性方法的外部内存访问量降低1.82~4.87倍。

最值得记住：KV缓存冗余同时存在于token间和token内部元素两个维度，分层压缩可以用极低的精度与硬件开销实现量级的推理效率提升。
