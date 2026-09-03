---
title: 'ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding'
title_zh: ShallowStream：先浅编码建索引再深度推理的流式视频理解框架
authors:
- Jitai Hao
- Ke Yang
- Qiang Huang
- Jun Yu
affiliations:
- 哈尔滨工业大学（深圳）
arxiv_id: '2609.02780'
url: https://arxiv.org/abs/2609.02780
pdf_url: https://arxiv.org/pdf/2609.02780
published: '2026-09-02'
collected: '2026-09-03'
category: Multimodal
direction: 多模态大模型 · 流式推理优化
tags:
- MLLM
- KV cache
- Streaming Inference
- Efficient Reasoning
- Video Understanding
one_liner: 用MLLM浅层做流式帧编码建轻量索引，查询时全深度推理，性能持平SOTA同时大幅降本提效
practical_value: '- 流式场景（如电商直播实时理解、用户行为流召回、广告实时素材分析）可复用“浅层高频率建索引 + 低频率查询时全深度计算”的架构，大幅降低稳态算力成本

  - 检索路由可借鉴轻量query-logit门设计，无需额外训练路由模型，仅用预训练LLM/MLLM的next-token logit差即可判断是否需要召回历史上下文

  - 长序列KV cache优化可复用浅层KV做检索的思路，浅层语义足够完成相关性匹配，无需保留全层KV即可实现高效历史召回，大幅降低内存开销

  - 多样性召回策略可直接迁移到推荐/搜索的长序列召回场景，用token投票+max-min多样性选择平衡相关性和覆盖度，提升召回准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前流式视频理解场景存在工作负载不对称的特点：视频帧持续流入，而查询请求稀疏。现有方案普遍对每帧执行全深度MLLM预填充，不仅算力开销极高，还会导致KV cache快速膨胀，大量预计算的深层状态从未被访问，造成资源浪费，同时端到端延迟过高，无法满足直播互动、AR导购、实时内容审核等场景的低延迟需求。

### 方法关键点
- 浅编码建索引：流式处理阶段仅用MLLM前P层（远小于总层数）处理输入帧，保留浅层KV构建全历史轻量索引，跳过深层计算大幅降低稳态开销
- 轻量检索门：查询时用固定路由prompt生成二分类logit，通过logit差判断是否需要召回历史证据，无需额外训练路由模型
- 多样性证据检索：门控触发召回时，用浅层注意力分数做token级投票排序，结合max-min多样性选择策略筛选高相关低冗余的历史帧，仅对选中帧做全深度推理
- 可选长集群压缩：内存不足时对久远历史做聚类压缩，固定内存开销同时保留历史检索能力

### 关键结果
在OVO-Bench、StreamingBench两个主流流式视频评测集上，对比HERMES、OASIS等SOTA方案，ShallowStream性能持平的前提下，单帧预填充延迟最高降低52.1×，每10s查询一次的端到端延迟最高降低11.9×；开启可选长集群压缩后，1024帧长序列场景下GPU峰值内存稳定在18GiB左右，内存开销远低于同类方案。

最值得记住的一句话：对于高频流入、低频查询的不对称流式工作负载，利用浅层网络输出即可完成高准确率的相关性检索，将高成本的全深度计算延迟到查询时仅针对必要样本执行，是兼顾效果与成本的核心优化思路。
