---
title: 'DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context
  KV Cache Compression'
title_zh: DepthWeave-KV：面向长上下文的令牌自适应跨层残差KV缓存压缩算法
authors:
- Anna Cordoba
- Adam Puente Tercero
- Nerea Angulo Hijo
- Mar Linares Tercero
- Julia Barrientos
- Ainhoa Miranda
- Jesus Olivera
affiliations:
- Instituto de Investigación en Visión Artificial
arxiv_id: '2607.06523'
url: https://arxiv.org/abs/2607.06523
pdf_url: https://arxiv.org/pdf/2607.06523
published: '2026-07-07'
collected: '2026-07-08'
category: LLM
direction: LLM长上下文推理 · KV缓存压缩
tags:
- KV cache
- Long-Context LLM
- Inference Optimization
- Low-Rank Factorization
- Compression
one_liner: 无需微调基础LLM，通过跨层共享低秩基+令牌自适应残差实现8.3倍KV缓存压缩
practical_value: '- 做RAG电商导购、商品咨询类Agent的业务可直接复用该方案：无需修改基础LLM权重，就能大幅降低长上下文（商品详情、多轮对话、检索结果）的KV缓存占用，提升单卡服务并发，干草堆检索准确率仅比全缓存低2.6个点，完全满足业务需求。

  - 令牌自适应分配精度的思路可迁移到推荐系统特征压缩场景：对用户高价值行为（搜索、下单、加购）序列保留更高精度，对低价值浏览序列做激进压缩，平衡存储成本和推荐效果。

  - 免校准在线误差探测机制适合波动大的业务场景：大促、活动流量高峰时可动态调整压缩阈值，自动平衡吞吐量和生成效果，无需提前做任务专属校准或重新训练。

  - 融合CUDA内核的设计可复用在LLM排序服务优化中：将KV重建和注意力计算合并执行，减少内存读写开销，提升长用户行为序列下的排序推理速度。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长上下文LLM推理的核心瓶颈是KV缓存的内存占用与带宽消耗，现有压缩方案普遍对所有层、所有令牌采用统一压缩预算，会导致检索类任务（如精准商品属性查询、订单信息召回）出现脆性失效，严重影响依赖长上下文的电商Agent、多轮推荐对话等场景的可用性。

### 方法关键点
- 跨层残差因子分解：将相邻Transformer层划分为深度窗口，每个窗口内共享低秩KV通道基，层间差异用轻量令牌专属残差重建，避免强制层间完全共享导致的信息损失。
- 令牌自适应深度路由：基于累计注意力权重、注意力峰值、指令边界标识、历史重建误差四个特征，动态给指令、实体、检索关键令牌分配更高残差秩，普通续写令牌降低甚至关闭残差。
- 免校准在线误差追踪：每隔若干解码步对比压缩缓存与高保真缓存的注意力输出误差，动态调整压缩阈值，完全无需微调基础LLM权重。
- 融合CUDA内核：将基查找、残差反量化、注意力投影合并执行，避免中间重建KV张量写入全局内存，大幅降低带宽压力。

### 关键实验
在LongBench、Needle-in-a-Haystack、L-Eval等长上下文基准测试，对比StreamingLLM、H2O、TailorKV、MiniCache等10种SOTA压缩方案，64K上下文下：实现8.3倍KV内存减少，平均任务得分62.9%仅比全缓存低0.9个点，干草堆检索准确率96.1%，解码吞吐量达72.8 token/s，比次优方案TailorKV高12%。

### 核心结论
长上下文KV压缩不能使用统一预算，必须同时兼顾层间冗余的深度感知和关键令牌的精度保留，才能在高压缩率下避免检索类任务的效果退化。
