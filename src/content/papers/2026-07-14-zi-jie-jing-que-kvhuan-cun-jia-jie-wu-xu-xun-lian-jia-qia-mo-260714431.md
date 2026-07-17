---
title: 'Smarter and Cheaper at Once: Byte-Exact KV-Cache Grafting Turns a Frozen Small
  Model into a Verified-Knowledge Flywheel'
title_zh: 字节精确KV缓存嫁接：无需训练加卡让冻结小模型更智能更经济
authors:
- Sietse Schelpe
affiliations:
- Corbenic AI
arxiv_id: '2607.14431'
url: https://arxiv.org/abs/2607.14431
pdf_url: https://arxiv.org/pdf/2607.14431
published: '2026-07-14'
collected: '2026-07-17'
category: LLM
direction: LLM推理优化 · 字节精确KV缓存复用
tags:
- KV cache
- inference optimization
- deterministic inference
- knowledge reuse
- LLM serving
one_liner: 提出字节精确KV嫁接机制，冻结小模型无需改权重即可提能力降推理成本
practical_value: '- 电商/广告高频query的RAG上下文、活动规则、商品话术可预计算为KV块固化，相同请求直接嫁接，预fill速度最高提85.6x，大幅降低大促场景的延迟和算力成本

  - 生成式推荐场景可将用户画像、历史行为摘要按用户维度预存为KV块，用户请求时直接嫁接，省去重复prefill长用户特征的开销

  - Agent技能库可将验证过的工具调用流程、推理模板存为KV块，请求时路由到对应块嫁接，无需每次重prefill长prompt，还可突破单卡上下文限制87倍，无额外显存占用

  - 注意复用边界：KV块仅在同GPU架构、同推理配置下可字节精确移植，且嫁接位置需和捕获位置一致，避免位置偏移导致精度损失'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM能力提升依赖扩大模型规模、增加算力投入，推理侧大量重复prefill相同上下文造成严重算力浪费，现有KV缓存复用方案要么近似有损、要么仅支持会话内临时生效，无法作为持久化知识资产跨实例复用，小模型的落地性价比始终受限于能力天花板和推理成本的双重约束。

### 方法关键点
- 提出字节精确的KV嫁接机制Taliesin，在固定 deterministic 配置下，捕获的KV块恢复后生成的logit与新鲜计算结果字节完全一致，KL散度为0，argmax匹配率100%
- 验证仅当KV块在与捕获时相同的位置嫁接时才能保证字节精确，位置偏移产生的误差来自模型本身的浮点位置敏感性，而非嫁接机制缺陷
- 构建Galahad知识飞轮：问题用额外推理资源求解→通过外部校验验证正确性→将对应KV块持久化存储，后续请求路由到对应块直接嫁接，全程不修改模型权重

### 关键实验
数据集采用模型预训练cutoff后发布的AIME 2025竞赛题、LiveBench基准，baseline为原生冻结Gemma-4-12B、Gemma-4-31B。核心结果：冻结Gemma-4-12B的AIME 2025准确率从80%提升到93.3%，超过原生31B的89.2%基线；相同8个原生模型无法解决的难题，推理token量从401026降至61，减少6574倍，能耗降低3000~8700倍；持久化KV存储可将可用上下文从32k扩展到285万（87倍），无额外显存占用，访问成本不随上下文深度增长；同架构下KV块可跨实例无损迁移，嫁接后效果完全一致。

最值得记住的一句话：验证后的知识以字节精确KV块形式固化后可永久零损耗复用，无需微调、无需算力扩容，是比扩大模型规模、增加推理采样性价比高50倍的能力提升路径。
