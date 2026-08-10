---
title: Addressable Memory for Video World Models
title_zh: 面向视频世界模型的可寻址记忆机制
authors:
- Xindi Wu
- Sven Elflein
- James Lucas
- Olga Russakovsky
- Laura Leal-Taixé
- Despoina Paschalidou
- Jonathan Lorraine
- Aljoša Ošep
affiliations:
- NVIDIA
- Princeton University
- University of Toronto
- Vector Institute
arxiv_id: '2608.07408'
url: https://arxiv.org/abs/2608.07408
pdf_url: https://arxiv.org/pdf/2608.07408
published: '2026-08-06'
collected: '2026-08-10'
category: LLM
direction: 大模型KV cache优化 · 免训练记忆框架
tags:
- KV cache
- RoPE
- World Model
- Memory Compression
- Long Horizon Generation
one_liner: 提出免训练可寻址记忆框架WorldTrace，解决视频世界模型长时序KV cache寻址失效问题，配套评测基准LoopBench
practical_value: '- KV cache压缩时避免直接在RoPE旋转后空间做平均，可通过为压缩槽位分配分布内虚拟位置保证寻址有效性，适配长时序Agent模拟、多轮对话推荐等场景

  - 可复用两种记忆压缩策略：时序连续场景用平滑压缩保证一致性，场景切换节点存储原始片段提升召回精度，适配电商导购、虚拟逛街等长交互场景

  - LoopBench的长距离回访一致性评测思路可迁移到长序列推荐、多轮对话推荐的历史一致性效果评估'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
自回归视频世界模型依赖KV cache存储历史帧实现视觉一致性，当生成长度超过训练horizon时，RoPE位置偏移超出训练分布导致注意力无法正确寻址历史内容；直接在RoPE旋转后空间压缩KV cache会因位置相位冲突破坏记忆有效性。

### 方法关键点
提出免训练可寻址记忆框架WorldTrace，为每个压缩后的记忆槽位分配独立的分布内虚拟位置保证寻址能力；配套两种压缩策略：WorldTrace-Field对历史做平滑压缩保证时序一致性，WorldTrace-Landmark仅在检测到场景切换时存储原始片段提升episodic召回效果；同时提出LoopBench基准评测长距离绕行后历史场景重建能力。

### 关键结果
WorldTrace-Field在LoopBench上时序一致性提升+15.5%，WorldTrace-Landmark episodic召回提升+19.5%，无需重新训练即可延长视觉一致的生成长度。
