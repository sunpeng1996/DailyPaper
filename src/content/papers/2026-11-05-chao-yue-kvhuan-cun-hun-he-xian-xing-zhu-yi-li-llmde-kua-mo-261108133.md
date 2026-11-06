---
title: 'Beyond K/V Caches: Cross-Model State Handoff in Hybrid Linear-Attention LLMs'
title_zh: 超越KV缓存：混合线性注意力LLM的跨模型状态移交框架
authors:
- Jiacheng Cai
- Tao Zhang
- Siqi Liang
- Yun Dai
- Ziqian Zeng
affiliations:
- South China University of Technology
arxiv_id: '2611.08133'
url: https://arxiv.org/abs/2611.08133
pdf_url: https://arxiv.org/pdf/2611.08133
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: LLM推理优化 · 跨模型状态转移
tags:
- KV cache
- Linear Attention
- Inference Optimization
- State Transfer
- Prefill Acceleration
one_liner: 提出支持KV缓存/循环状态/卷积历史的跨模型状态移交框架，混合线性注意力LLM切换省超20倍预填充耗时
practical_value: '- 电商/Agent场景常用大小模型级联路由架构，可借鉴HST方案，小模型处理后的上下文直接移交大模型，无需大模型重复Prefill，长会话/长商品文案场景可大幅降低推理延迟，提升用户体验

  - 业务若使用混合线性注意力模型（如Qwen3.5系列），可直接复用HST的Conv对齐保序、REC结构化映射、FA缓存离线合并的trick，无需修改预训练权重即可实现跨模型状态转移，迁移成本极低

  - 长上下文RAG问答、商品多轮导购Agent场景上下文多在16K以上，实测16K上下文下模型切换速度可达21倍以上，能显著降低大模型调用成本，同时保障任务效果保留率在90%左右'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
工业级LLM部署常采用大小模型级联、路由切换的架构平衡成本与效果，但长会话场景下模型切换时目标模型需要对已处理上下文重复Prefill，上下文越长冗余计算成本越高。现有跨模型状态转移方案仅支持全注意力层的KV缓存迁移，而混合线性注意力模型还包含循环状态（REC）、卷积历史（Conv）两类状态，三类状态的耦合干扰大幅提升跨模型转移难度，且单纯降低REC重建误差反而可能升高后续生成的KL散度，影响任务效果。
### 方法关键点
- 提出Hybrid State Transfer（HST）框架，同时支持KV缓存、REC、Conv三类状态的跨模型转移，全程冻结源/目标模型预训练权重
- REC采用分组结构化映射，Conv对齐时保留历史时序顺序，避免误差传导至后续REC更新
- 基于下游任务连续性做功能校准，KV缓存的LoRA增量训练后离线合并为线性映射，部署时无额外推理开销
- 4B→27B场景额外增加状态条件的低秩REC校正模块，进一步提升任务保留率
### 关键实验
基于Qwen3.5系列模型，在ARC-Challenge、HellaSwag、WinoGrande、MMLU、GSM8K五个基准测试，对比Ridge、CacheBridge、CacheLink三类基线：
- 4B→27B平均任务保留率达89.88%，超最优基线3.56个百分点；9B→27B平均任务保留率达94.11%，超最优基线7.10个百分点
- 16K合成上下文场景下，4B→27B、9B→27B的切换速度分别达21.66倍、21.91倍，大幅降低Prefill延迟
### 核心结论
跨模型状态转移的核心目标是下游任务连续性，而非单纯降低单状态重建误差，优化方向要对齐最终生成效果而非中间指标
