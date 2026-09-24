---
title: Memory Attention
title_zh: Memory Attention：基于令牌索引内存的注意力值构造优化方法
authors:
- Jiale Kang
arxiv_id: '2609.28399'
url: https://arxiv.org/abs/2609.28399
pdf_url: https://arxiv.org/pdf/2609.28399
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM 注意力优化 · 推理显存降本
tags:
- Attention
- Memory Offloading
- KV Cache
- LLM Inference
- Model Optimization
one_liner: 用层专属令牌内存与上下文Key组合替换注意力独立Value投影，支持CPU卸栽降低GPU显存开销
practical_value: '- 做LLM4Rec、电商Agent推理部署时，可复用MA-Offload的预取+CPU卸栽思路，将大体积静态lookup表（如item
  embedding表、Semantic ID映射表）存放于CPU，通过预取重叠传输与GPU计算，在几乎不增加 latency的前提下降低GPU显存占用

  - 自定义训练生成式推荐专属LLM时，可尝试替换标准注意力的Value投影层，采用Key+层专属令牌内存的组合构造Value，相同训练token预算下可提升下游推荐/理解任务效果，同时降低训练计算量

  - 长会话推荐、长文档检索类Agent场景可参考MA-Recall思路，仅缓存Key与历史token ID，动态重建Value，最多可降低50%的KV cache存储开销，缓解长上下文推理的显存压力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM训练与推理的算力、显存瓶颈是落地的核心限制，现有基于lookup的内存方案仅作为补充模块存在，并未替换原有计算链路的冗余组件；标准注意力的独立Value投影需要大量密集计算，存在优化空间。
### 方法关键点
- 移除标准注意力的独立Value投影层，改用上下文Key与层专属令牌内存表的加和构造Value：`V = K + Norm(M)`，其中M是按token ID查表得到的层专属令牌表示，既保留上下文依赖，又引入跨场景通用的令牌特征
- 推理时可将Norm参数预计算折叠进内存表，Value构造仅需查表和加法操作，大幅降低在线计算量
- MA-Offload：将内存表存放于CPU内存，通过预取机制让查表、CPU-GPU传输与GPU计算重叠，有效降低GPU参数存储量
- MA-Recall扩展：仅缓存Key和历史token ID，动态重建Value，可降低50%的KV cache存储
### 关键实验
基于FineWeb数据集预训练，对比标准MHA/GQA/MQA架构，相同训练token预算下：小模型下游任务平均准确率最高提升1.16个百分点，WikiText perplexity下降9.2%，2倍训练上下文长度的NIAH检索任务得分平均提升61.8%；推理侧MA-Offload比标准注意力GPU参数存储降低7.38%，总参数规模可达标准的2.08倍，预fill与decode latency与基线基本持平。
### 核心结论
注意力的Value构造不需要独立投影层，复用Key加令牌内存的设计可同时实现效果提升与显存、算力优化。
