---
title: 'On-Demand Attention: Language Models Know When to Recall'
title_zh: 按需注意力：让大语言模型自主判断何时调用全局注意力
authors:
- Haibo Feng
- Ruiqi Liang
- Hanyang Peng
- Shiqi Yu
affiliations:
- Southern University of Science and Technology
- Peking University
- Peng Cheng Laboratory
arxiv_id: '2609.20734'
url: https://arxiv.org/abs/2609.20734
pdf_url: https://arxiv.org/pdf/2609.20734
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: LLM长上下文推理 · 注意力优化
tags:
- On-Demand Attention
- Long Context Inference
- KV Cache
- Efficient Decoding
- vLLM
one_liner: 仅训练轻量召回头实现LLM长上下文推理时按需切换局部/全局注意力，大幅提速同时保留性能
practical_value: '- 长上下文Agent/电商推荐场景（如用户全生命周期行为建模、长对话导购）可复用ODA架构，仅训练20-30M参数的召回头，无需改动LLM底座权重，快速实现推理提速，适配业务低侵入要求

  - vLLM侧的GPU端条件执行实现方案可直接复用，避免CPU-GPU同步开销，将注意力切换的额外耗时压缩到最低，适配线上高吞吐服务要求

  - 召回头的训练思路可迁移到RAG/搜索推荐的检索决策场景：用当前局部计算结果预测全量召回的收益，仅在收益为正时触发高成本的全量检索/重排序，降低整体链路耗时'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文推理是Agent、RAG、生成式推荐等业务的核心依赖，但全注意力解码每步都要读取完整上下文KV，随context长度增长成本呈O(n²)上升，成为业务落地的性能瓶颈；现有动态注意力方案大多需要联合训练底座，侵入性高，难以复用成熟开源模型。

### 方法关键点
- 采用局部优先的解码流程：每步先做局部注意力（仅读取初始s个token+最近w个token，匹配StreamingLLM范式），再用召回头预测调用全局注意力的收益，超过阈值才触发全局注意力重计算
- 仅训练轻量召回头，底座权重完全冻结：召回头输入为上一步选中的隐藏态、当前token embedding、当前局部注意力输出的隐藏态，用Huber回归拟合成本调整后的全局注意力收益（以局部/全局注意力的next token NLL差为监督信号）
- 完整保留历史KV cache，避免局部注意力导致的信息丢失，全局注意力可随时访问全量上下文；在vLLM中实现GPU端条件执行，避免跨设备同步开销

### 关键实验
在RULER16K、LongBench v1数据集上验证，覆盖Qwen3 1.7B/8B、Qwen3.5 2B、Gemma-4-12B-it等多模型系列，对比基线为全注意力、固定局部注意力。Qwen3-1.7B在RULER16K上仅41.6%的步骤调用全局注意力，性能从局部注意力的19.23提升到81.17，接近全注意力的81.94；128K输入、1K输出场景下，解码FLOPs降低76%，单请求吞吐达原生全注意力的1.98倍。

**最值得记住的一句话**：大模型自身的解码隐态已经包含了是否需要访问全局上下文的信号，无需改动底座即可通过轻量探针实现高效的按需计算
