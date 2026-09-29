---
title: 'UniCache: Task- and Type-Aware KV Cache Compression for Unified Multimodal
  Models'
title_zh: UniCache：面向统一多模态模型的任务与类型感知KV缓存压缩框架
authors:
- Wanqi Yang
- Yuexiao Ma
- Mei Xie
- Xiawu Zheng
- Shiwei Liu
affiliations:
- Max Planck Institute for Intelligent Systems
- ELLIS Institute Tübingen
- Tübingen AI Center
- Nanyang Technological University
- Xiamen University
arxiv_id: '2609.32831'
url: https://arxiv.org/abs/2609.32831
pdf_url: https://arxiv.org/pdf/2609.32831
published: '2026-09-26'
collected: '2026-09-29'
category: Multimodal
direction: 多模态大模型 · KV Cache 压缩优化
tags:
- KV Cache
- Multimodal LLM
- Inference Optimization
- Compression
- Training-Free
one_liner: 训练无感的统一多模态模型KV缓存压缩框架，兼顾高压缩率与多任务推理效果
practical_value: '- 多模态Agent、AI商品图生成/编辑、生成式推荐等场景部署统一多模态模型时，可直接复用UniCache方案，80%压缩率下几乎无损，长上下文吞吐量最高提升1.78倍，显存占用降低80%

  - 离线校准注意力分布匹配压缩策略的思路可迁移到单模态LLM推荐/Agent场景：注意力集中的KV段（如用户Query、Semantic ID序列）用token逐出策略，注意力分散的段（如商品详情、长文本）用量化策略，平衡压缩率和推理效果

  - 长上下文生成场景可复用任务感知时序调度逻辑：理解类任务用固定KV保留率，生成/编辑类任务随推理阶段动态降低总保留率，早期保证生成质量，后期提升推理速度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
统一多模态模型同时支持视觉理解、文生图、图像编辑三类核心任务，是多模态Agent、生成式内容生产的核心底座，但随着上下文长度增长，KV缓存的存储和访问开销成为推理性能的核心瓶颈。现有KV压缩方法针对单模态、固定任务场景设计，忽略不同任务、不同语义类型KV缓存的重要性差异，统一压缩策略容易丢失关键信息，高压缩率下要么丢失源图像细节，要么无法遵循用户指令，无法适配多任务场景的要求。
### 方法关键点
- 任务感知缓存分段：按当前任务类型拆分不同语义类别的KV段，将边界KV、当前生成latent KV设为保护段不参与压缩，仅对指令KV、源图像特征KV等条件KV段做压缩处理
- 离线策略分配：通过离线校准不同任务-KV类型对的注意力集中度，注意力集中的段（如指令KV）用token逐出策略，注意力分散的段（如源图像VAE特征KV）用量化策略，避免单一策略的劣化问题
- 注意力引导动态预算分配：按各KV段的注意力质量占比动态分配压缩预算，保证高重要性段分配更多存储空间，避免平均分配导致的关键信息丢失
- 任务感知时序调度：理解类任务用固定KV保留率，生成/编辑类任务随推理阶段动态降低总保留率，适配条件KV注意力权重随推理推进逐步下降的规律
### 关键实验
在BAGEL、SenseNova-U1两款主流统一多模态模型上测试，对比H2O、KIVI、StreamingLLM等5种主流KV压缩方案，在理解/编辑任务80%压缩率、生成任务60%压缩率下，效果与全KV基线几乎一致，20K长上下文场景下吞吐量最高提升1.78倍，KV缓存显存占用降低80%。
### 核心结论
针对多模态大模型的KV压缩不能采用一刀切的统一策略，必须结合任务类型、KV段的语义属性和注意力分布匹配差异化压缩方案，才能兼顾高压缩率和多任务推理质量。
