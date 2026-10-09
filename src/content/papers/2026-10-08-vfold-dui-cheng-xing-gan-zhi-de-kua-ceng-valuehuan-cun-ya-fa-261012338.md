---
title: 'VFold: Symmetry-Aware Cross-Layer Value Cache Compression'
title_zh: VFold：对称性感知的跨层Value缓存压缩方法
authors:
- Neha Verma
- Sungwon Kim
- Kenton Murray
- Kevin Duh
affiliations:
- Johns Hopkins University
- George Mason University
arxiv_id: '2610.12338'
url: https://arxiv.org/abs/2610.12338
pdf_url: https://arxiv.org/pdf/2610.12338
published: '2026-10-08'
collected: '2026-10-09'
category: LLM
direction: LLM推理优化 · KV cache压缩
tags:
- KV cache
- LLM Inference
- Model Compression
- Attention Optimization
- Long Context
one_liner: 无需微调、无架构修改的预训练LLM跨层Value缓存压缩方案，性能损失可忽略
practical_value: '- 部署LLM驱动的电商Agent、生成式推荐、长上下文多轮对话服务时，可直接接入VFold做KV缓存优化，无需微调模型、无需修改注意力内核，即可降低25%总KV内存开销，单卡可承载的并发量提升15%

  - 复用「Value对跨层合并的容忍度远高于Key」的结论，后续做KV缓存优化可优先针对Value做压缩，避开Key受RoPE限制难以跨层共享的痛点

  - VFold与现有4bit量化、Key剪枝等压缩方案完全正交，可叠加使用，比如和KIVI 4bit组合可实现4.27倍KV缓存压缩，性能损失小于2%，适合全店商品召回、长会话用户画像等长上下文业务场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文LLM推理的瓶颈已从计算转向内存，KV缓存占用随上下文长度快速攀升，例如16K上下文、8批量的Llama3.1-8B的KV缓存可达16GB，与模型参数量内存占用相当。现有跨层KV压缩方案要么要求从零训练模型，要么推理开销大、精度衰减严重，缺乏适配预训练模型的低 overhead 方案。

### 方法关键点
- 利用注意力固有对称性：Value投影矩阵$W_V$和输出投影矩阵$W_O$之间存在线性不变性，可离线将对齐映射$T$及其逆映射分别折叠进$W_V$和$W_O$，完全不改变模型输出，无推理阶段额外开销
- 离线阶段用CCA（典型相关性分析）计算相邻层Value缓存的对齐映射，结合匈牙利算法实现头级别的最优匹配，对齐后相邻层Value的余弦相似度从接近0提升至0.85以上
- 运行时仅对超出4个注意力sink、最近128token滑动窗口的Value做跨层平均合并，存入共享缓存，避免关键信息损失

### 关键结果
- 在Llama3.1-8B、Mistral-Small-24B、Qwen3-8B三个模型上测试，50%Value缓存压缩（总KV缩减25%）的情况下，VFold可保留98%以上的全缓存性能，在RULER基准上比CommonKV最高高出14.2个百分点
- 效率层面，A100上8K上下文、256个生成token的场景下，VFold的首Token延迟（TTFT）仅比全缓存慢5ms，单Token生成延迟（TPOT）慢6.8ms，单卡可承载的最大批量提升15%
- 可与4bit KIVI量化、ThinK Key剪枝等方案正交组合，叠加后可实现最高4.27倍的KV缓存压缩，性能损失小于1%

**最值得记住的结论**：KV缓存的Value层间冗余远高于Key，利用注意力对称性做离线对齐后合并，是几乎无额外开销的长上下文LLM内存优化路径。
