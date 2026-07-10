---
title: 'Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE'
title_zh: Jet-Long：基于动态双焦RoPE的高效零样本长上下文扩展方法
authors:
- Haozhan Tang
- Zerui Wang
- Yuxian Gu
- Song Han
- Han Cai
affiliations:
- NVIDIA
arxiv_id: '2607.07740'
url: https://arxiv.org/abs/2607.07740
pdf_url: https://arxiv.org/pdf/2607.07740
published: '2026-07-07'
collected: '2026-07-10'
category: LLM
direction: LLM长上下文扩展 · RoPE优化
tags:
- RoPE
- Long-Context-LLM
- Zero-Shot
- Inference-Optimization
- FlashAttention
one_liner: 无需微调的零样本长上下文扩展方案，兼顾长短上下文性能，推理开销可忽略
practical_value: '- 电商RAG导购、多轮用户对话Agent、长周期用户行为序列生成式推荐场景，可直接集成Jet-Long，无需微调即可将现有RoPE架构LLM的上下文窗口从32K扩展到128K，完全保留原生短上下文性能的同时提升长序列任务准确率

  - 工程落地可复用其KV cache免修改的校正旋转设计，无需调整现有KV缓存结构，对接推理引擎的改造量极小，单batch生成开销≤4%基本可忽略

  - 超参数无需逐场景 tuning，直接取默认w0=2048即可达到接近最优效果，大幅降低上线前的AB测试成本

  - 混合注意力架构LLM也可直接适配Jet-Long，无需额外微调即可获得10pp左右的长任务准确率提升，适合大参数量生成式推荐场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有零样本长上下文扩展方法均固定单一缩放因子，激进缩放会损失短上下文保真度，保守缩放则无法支撑超长序列；而长上下文预训练/微调成本高、数据稀缺，还易导致短上下文性能退化，零样本扩展是开源LLM落地的主流需求，尤其RAG、Agent、长序列推荐场景对长上下文能力的需求迫切。

### 方法关键点
- 动态双焦RoPE设计：保留固定大小的本地RoPE保真窗口，远程窗口的分组缩放因子G随当前序列长度动态计算（G=max(1,⌈L/预训练窗口⌉)），保证远程旋转角度始终处于训练分布内，序列长度≤预训练窗口时完全等价于原生模型
- KV cache无修改方案：利用RoPE的角度可加性，对查询和缓存Key做实时校正旋转，无需改写KV缓存，生成阶段不会因序列长度变化触发缓存重计算
- 容斥注意力合并：通过3次FlashAttention调用实现双焦注意力的精确路由，融合为单个CuTe kernel，大幅降低推理开销

### 关键实验
在Qwen3-1.7B/4B/8B（原生32K窗口）上测试到128K上下文，对比DNTK、YaRN、DCA、Self-Extend等SOTA基线：RULER准确率分别领先最强基线4.79/2.18/2.03pp，HELMET-RAG、PG-19困惑度均为最优；H100上长上下文Prefill吞吐量达到FA2的1.28~1.39倍，单batch生成开销≤4%；适配混合注意力架构Jet-Nemotron后，RULER平均准确率提升10~11pp。

### 核心结论
动态双焦RoPE从根本上解决了零样本长上下文扩展的长短性能tradeoff，几乎无推理 overhead，是现有RoPE-based LLM长上下文扩展的首选落地方案。
