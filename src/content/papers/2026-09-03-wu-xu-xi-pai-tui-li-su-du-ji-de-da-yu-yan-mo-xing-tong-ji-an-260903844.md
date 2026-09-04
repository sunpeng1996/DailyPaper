---
title: 'Flip, Don''t Shuffle: Watermarking LLMs at the Speed of Inference'
title_zh: 无需洗牌：推理速度级的大语言模型统计水印方案
authors:
- Simone Ceppi
- Ignacio Sanchez
affiliations:
- European Commission Joint Research Centre
arxiv_id: '2609.03844'
url: https://arxiv.org/abs/2609.03844
pdf_url: https://arxiv.org/pdf/2609.03844
published: '2026-09-03'
collected: '2026-09-04'
category: LLM
direction: LLM 推理优化 · 统计水印技术
tags:
- Watermark
- LLM Inference
- GPU Optimization
- vLLM
- O(1) Complexity
one_liner: 提出无状态伯努利水印SBW，O(1)复杂度，推理开销<1%，检测效果与主流方案等价
practical_value: '- 生产侧LLM服务加水印可直接复用开源SBW库，集成vLLM仅带来<1%额外开销，几乎无性能损失，适配生成式商品文案、Agent回复等场景的内容溯源需求

  - GPU优化trick可直接迁移：用计数器型随机数生成器（CBRNG）替换全局shuffle操作、用Jenkins整数哈希替换查表哈希，消除中间显存分配，大幅降低轻量计算任务的GPU
  overhead

  - 生成式推荐场景若需对生成的Semantic ID、推荐理由、商品文案做溯源，SBW的无状态设计兼容分布式推理，无需额外维护状态，适配高并发推荐服务架构'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前全球监管要求LLM生成内容需可溯源，现有统计水印方案（KGW、SynthID）要么需要全局词表shuffle（O(VlogV)复杂度），要么需要多轮重加权，推理开销大且占用额外显存与KV cache竞争，高并发部署下的「水印税」问题严重，亟需几乎无开销的生产级水印方案。

### 方法关键点
- 核心将绿表构建从全局shuffle改为每个token独立的伯努利试验，用支持GPU原生加速的CBRNG（Philox 4x32-10）基于上下文种子和token ID直接计算是否属于绿表，O(1)复杂度，无中间张量分配
- 用Jenkins整数哈希替换传统置换表查表哈希，纯ALU指令计算避免GPU缓存失效，null分布校准效果提升1.8×，生成文本多样性更高
- 无状态设计支持全词表self-salt，兼容分布式推理，可直接编译为单个融合CUDA kernel，集成进vLLM的logits处理流

### 关键结果
实验基于C4验证集，用Qwen3-8B、Falcon-7B测试，对比KGW、SynthID两个主流方案：SBW在所有batch size下推理开销<1%，比SynthID快2×，比KGW快6000×以上，零额外显存占用；检测ROC-AUC与主流方案差异<0.01，z-score分布等价，δ≤2的实用配置下perplexity损失可忽略。

最值得记住的一句话：LLM水印的性能开销不是统计水印的固有缺陷，而是传统全局序列操作的设计导致的，基于局部独立计算的架构可以几乎消除水印税。
