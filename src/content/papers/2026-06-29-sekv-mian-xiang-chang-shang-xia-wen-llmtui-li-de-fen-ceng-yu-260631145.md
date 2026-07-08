---
title: 'SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context
  LLM Inference'
title_zh: SeKV：面向长上下文LLM推理的分层语义自适应KV缓存
authors:
- Amirhossein Abaskohi
- Giuseppe Carenini
- Peter West
- Yuhang He
affiliations:
- University of British Columbia
- Microsoft Research
arxiv_id: '2606.31145'
url: https://arxiv.org/abs/2606.31145
pdf_url: https://arxiv.org/pdf/2606.31145
published: '2026-06-29'
collected: '2026-07-08'
category: LLM
direction: 长上下文LLM推理 · KV缓存优化
tags:
- KV cache
- Long Context LLM
- Inference Optimization
- Semantic Memory
- SVD
one_liner: 提出分层语义分辨率自适应KV缓存SeKV，降53.3%GPU显存同时超最强语义基线5.9%
practical_value: '- 电商Agent处理长用户历史、多轮对话、长商品详情页时，可复用SeKV的分层内存架构：GPU存语义摘要+CPU存低秩SVD基，大幅降低GPU显存占用，解决长上下文推理成本过高的问题

  - 可借鉴熵引导的语义分段方法，用token surprisal（预填充阶段直接可得，无额外计算）做语义切分边界，替代固定长度chunk或规则切分，提升长文本分段的语义一致性

  - 做LLM推荐、商品文案生成等场景时，若需要从长上下文召回细节（比如用户历史评价里的具体需求），可复用动态zoom-in机制，仅按需加载query相关片段到GPU，平衡推理精度和效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM在电商多轮对话、长商品文档分析、Agent规划等场景应用广泛，但KV缓存随序列长度线性增长，全量GPU缓存成本极高；现有压缩方法要么永久丢弃token导致关键信息丢失，要么预填充阶段固定压缩策略，无法在解码时按需恢复相关片段的细粒度信息，严重影响长上下文推理精度。

### 方法关键点
- 熵引导语义分段：利用预填充阶段直接输出的token surprisal做边界信号，将上下文切分为语义连贯的span，高surprisal的边界token作为锚点全量存在GPU，无额外计算开销
- 双分辨率分层存储：每个span在GPU存轻量语义摘要用于粗粒度路由，CPU存低秩SVD基用于按需细粒度重构，避免不可逆的token丢弃
- 训练式zoom-in机制：仅训练占比<0.05%的路由参数（基础LLM全冻结），解码时动态识别query相关span，异步从CPU拉取SVD基重构token级KV，仅加载相关片段到GPU

### 关键结果
在LongBench、RULER、InfiniteBench、NIAH四个长上下文基准，对比8种主流KV缓存压缩基线，10%KV缓存预算下平均超最强语义基线SentenceKV 5.9%；128K上下文下比全量KV缓存降低53.3%GPU显存，推理吞吐量最高提升21%，精度仅比全量KV低0.8个百分点。

### 核心结论
长上下文KV缓存优化的核心不是一味压缩，而是根据query相关性动态分配显存分辨率，把细粒度内存资源只给真正需要的片段
