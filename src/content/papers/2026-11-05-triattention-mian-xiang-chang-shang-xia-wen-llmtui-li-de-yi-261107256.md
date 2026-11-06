---
title: 'TriAttention: Unified Sparse Mixed-Precision Attention for Long-Context LLM
  Inference'
title_zh: TriAttention：面向长上下文LLM推理的统一稀疏混合精度注意力
authors:
- Hanzhi Zhang
- Qiao Zhang
- Qinglei Cao
- Heng Fan
- Yan Huang
- Kewei Sha
- Yunhe Feng
affiliations:
- University of North Texas
- Saint Louis University
arxiv_id: '2611.07256'
url: https://arxiv.org/abs/2611.07256
pdf_url: https://arxiv.org/pdf/2611.07256
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: 长上下文LLM · 混合精度注意力推理优化
tags:
- Long-Context LLM
- Attention Optimization
- Mixed Precision
- KV Cache
- Inference Acceleration
one_liner: 针对长上下文LLM推理，联合稀疏跳过与4/8bit混合精度，最高实现2.65倍端到端加速且无损精度
practical_value: '- 可复用三档位（跳过/4-bit/8-bit）分块精度分配策略，优化电商场景长用户行为序列的RAG检索、历史注意力计算延迟，适配长会话Agent、长商品文本理解场景

  - 可借鉴对角线距离编码的轻量策略存储方式，配置存储开销不随序列长度增长，可直接嵌入现有推荐系统的LLM排序、个性化文案生成模块，无额外存储成本

  - 离线校准+全局预算分配的精度选择框架可复用，固定算力下优先给精度敏感的注意力头分配更高精度，平衡推荐生成质量与推理成本，适配大流量搜索推荐推理场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有长上下文LLM推理的注意力优化大多单独采用稀疏跳过或量化策略，未区分不同注意力交互的精度敏感度：要么跳过关键信息导致精度下降，要么统一采用高精度导致算力浪费，难以平衡长上下文推理的速度与质量。

### 方法关键点
- 三档位分块计算：将注意力块划分为跳过、4-bit计算、8-bit计算三类，仅对精度敏感的近对角线块分配8-bit，容忍低精度的远块用4-bit，无价值块直接跳过
- 轻量距离编码：用两个对角线距离边界参数编码每个头的精度配置，存储开销不随上下文长度增长，避免元数据占用过多共享内存
- 敏感度引导全局分配：离线校准每个头的精度/跳过误差，全局统一分配算力预算，优先给误差敏感的头分配更高精度和更长上下文窗口
- 跨阶段执行优化：prefill阶段生成压缩量化的KV缓存，decode阶段直接复用，大幅减少重复读存开销

### 关键实验
基于Llama-3.2-3B-Instruct在A100上测试，对比BF16基线、MInference、FlexPrefill等SOTA方案：64K上下文下实现端到端生成速度最高2.65倍提升，比Torch注意力最高快7.88倍，峰值显存降低24.8%；长上下文QA任务F1值与BF16基线差异小于1个百分点，通用任务精度无明显损失。

### 核心结论
注意力优化要同时决策「哪些交互要保留」和「保留的交互用什么精度计算」，而非单独优化稀疏或量化，才能在固定算力下最大化长上下文推理效率。
