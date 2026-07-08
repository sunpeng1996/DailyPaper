---
title: Gemma 4 Technical Report
title_zh: Gemma 4 开源多模态大模型技术报告
authors:
- Gemma Team
- Sherif El Abd
- Vaibhav Aggarwal
- Robin Algayres
- Alek Andreev
- Olivier Bachem
- Ian Ballantyne
- Cormac Brick
- Victor Cărbune
- Michelle Casbon
affiliations:
- Google DeepMind
arxiv_id: '2607.02770'
url: https://arxiv.org/abs/2607.02770
pdf_url: https://arxiv.org/pdf/2607.02770
published: '2026-07-01'
collected: '2026-07-08'
category: LLM
direction: 开源多模态大模型 · 效率与推理优化
tags:
- LLM
- MoE
- Multimodal
- KV cache
- Quantization
- Speculative Decoding
one_liner: 推出2.3B-31B参数开源多模态模型族，带思考模式、无编码器架构及多项效率优化
practical_value: '- 长上下文优化trick可直接复用：本地滑动窗口+全局注意力按5:1配比、p-RoPE、KV cache共享、全局层复用key作为value，降低37.5%KV缓存开销，适合推荐系统用户长序列建模、多轮对话Agent的上下文存储

  - 量化感知训练（QAT）落地方案可直接借鉴：移动端混合int2/int4量化、服务端Q4_0量化，精度损失极小的前提下大幅降低内存占用，适合端侧推荐/Agent的轻量部署

  - 12B无编码器多模态架构可复用：用轻量投影层直接映射原始音频/图像块到LLM嵌入空间，减少多模态模块内存碎片化，适合电商多模态商品理解、多模态搜索的端到端落地

  - 思考模式+多Token预测 speculative decoding设计，可在低延迟下提升推理能力，适合电商客服Agent、推荐理由生成等场景'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前开源大模型普遍存在多模态能力弱、复杂推理性能不足、长上下文内存开销大、部署成本高的问题，迫切需要兼顾能力、效率、多模态支持的开源基座，适配从端侧到云端的不同部署场景。

### 方法关键点
- 架构设计：覆盖2.3B/4.5B/12B/31B稠密模型，以及26B总参数/3.8B激活参数的MoE模型，全系列原生支持文本、图像、音频多模态输入；12B版本采用无编码器架构，直接用轻量投影层映射原始音频/图像块到嵌入空间，省去独立音视频编码器。
- 效率优化：长上下文采用5:1本地-全局注意力配比+p-RoPE+KV cache共享+全局层key复用为value，降低37.5%KV缓存开销；内置多Token预测drafter头支持speculative decoding，提升推理速度；全系列提供QAT量化版本，移动端混合int2/int4、服务端Q4_0量化，内存占用最大降低80%以上。
- 能力增强：新增思考模式，生成回复前先输出推理轨迹，大幅提升数学、编码等复杂任务性能。

### 关键结果
在Arena文本评测中Gemma4 31B Elo达1451，是当前最强开源稠密模型，性能比肩参数大数十倍的MoE模型；STEM、多模态、长上下文基准全面领先Gemma3 27B，E2B小模型参数仅为Gemma3 27B的1/10，性能基本持平；12B无编码器模型音视频理解能力媲美带独立编码器的同规模模型，音频模块内存占用降低78%。

**最值得记住的一句话**：Gemma 4 是当前兼顾能力、效率、开源协议友好度的最优多模态基座，极适合业务侧定制化微调落地。
