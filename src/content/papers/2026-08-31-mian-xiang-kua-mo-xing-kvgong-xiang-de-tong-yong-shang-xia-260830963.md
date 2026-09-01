---
title: A Universal Context-Reuse Layer for Cross-Model KV Sharing
title_zh: 面向跨模型KV共享的通用上下文复用层
authors:
- Yi Li
- Dongming Jiang
- Yi Zhao
- Bingzhe Li
affiliations:
- University of Texas at Dallas
arxiv_id: '2608.30963'
url: https://arxiv.org/abs/2608.30963
pdf_url: https://arxiv.org/pdf/2608.30963
published: '2026-08-31'
collected: '2026-09-01'
category: LLM
direction: LLM推理优化 · 跨模型KV缓存共享
tags:
- KV_cache
- LLM_inference
- Cross_model_optimization
- Multi_agent
- Prefill_optimization
one_liner: 实现跨架构/尺寸/模型家族的KV缓存转换，削减多模型场景prefill冗余开销
practical_value: '- 多Agent电商客服/导购场景：不同能力等级Agent调用不同尺寸LLM时，可复用前置大模型处理用户历史、检索商品/订单信息生成的KV缓存，大幅降低后续小模型prefill延迟，提升交互响应速度

  - 模型级联生成式推荐/文案生成场景：先调用大模型做语义理解，后续小模型生成推荐结果/文案时直接复用大模型的KV翻译结果，在损失极小精度的前提下降低推理成本

  - 长上下文RAG推荐场景：检索到的大量商品文档仅需一次prefill生成KV，后续不同用途（排序、解释、选品）的小模型都可通过翻译复用该KV，避免重复处理长文档的高额开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前多LLM协作（模型级联、多Agent、RAG多阶段处理等）场景广泛存在，但每个模型处理相同上下文时都要独立完成prefill生成KV缓存，冗余计算极高；现有KV缓存复用仅能在同模型下生效，不同架构、尺寸、家族的模型无法复用彼此的KV，长上下文场景下延迟和成本浪费尤其严重。

### 方法关键点
- 核心思路是将KV缓存从模型本地临时资产视为可迁移的计算资源，通过训练翻译层将源模型生成的KV转换为目标模型可直接使用的格式，无需目标模型重新prefill全量上下文
- 翻译层可针对不同源-目标模型对训练，优化目标不需要完全对齐原生KV的数值，仅需保证目标模型推理效果满足业务要求，平衡翻译开销和精度损失
- 系统支持降级策略，当翻译效果不达标时自动回退到原生prefill流程，不影响业务稳定性

### 关键实验
在三类典型场景下测试：1）同家族Qwen2.5-7B→Qwen2.5-1.5B，LongBench2准确率比原生1.5B提升6.89pp，16K-32K上下文下prefill延迟从288.3ms降至53.8ms，效率提升5.4倍；2）跨家族Qwen2.5-1.5B→Gemma-2-2B，4K上下文下prefill延迟降低67.05%，解码困惑度与原生Gemma基本持平；3）跨家族大到小Llama3.1-70B→Qwen2.5-7B，准确率仅比原生Qwen2.5-7B低1.7pp，延迟从899ms降至138ms，效率提升6.5倍。

KV缓存不只是单模型的推理中间状态，更是可以跨模型迁移、存储、复用的计算资产，是未来异构多LLM系统和多Agent系统的核心优化方向之一。
