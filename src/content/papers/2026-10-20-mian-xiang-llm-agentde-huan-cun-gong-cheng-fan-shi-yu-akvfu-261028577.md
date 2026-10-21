---
title: Cache Engineering for Agents
title_zh: 面向LLM Agent的缓存工程范式与AKV服务引擎
authors:
- Tianyu Fu
- Ruoxi Wang
- Zihan Min
- Zhongqi Ren
- Zhihao Li
- Tengxuan Liu
- Shengxu Mu
- Hanling Zhang
- Yu Wang
affiliations:
- Tsinghua University
- The Chinese University of Hong Kong
arxiv_id: '2610.28577'
url: https://arxiv.org/abs/2610.28577
pdf_url: https://arxiv.org/pdf/2610.28577
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: Agent推理优化 · KV cache工程
tags:
- KV cache
- LLM Agent
- Inference Optimization
- Serving System
- Cache Policy
one_liner: 提出无需修改交互轨迹的Agent KV缓存操作范式及配套AKV服务引擎，兼顾任务效果与推理效率
practical_value: '- 电商多轮导购Agent、会话推荐场景可直接复用tool-response滚动丢弃策略：优先保留用户交互、Agent推理过程KV，丢弃过时工具返回结果，无需修改上下文文本即可降低推理成本，同时避免重Prefill带来的精度损失

  - 现有Agent服务框架可复用AKV的扩展前缀树+段批注意力设计：对外兼容现有标准LLM API，内部解决历史依赖的KV缓存复用问题，无需重构业务代码即可落地缓存优化

  - 长周期用户兴趣建模的LLM4Rec场景可复用repos操作：调整历史交互KV的位置编码，突破模型上下文窗口限制，无需重复Prefill全量历史序列即可支撑更长交互链路的推理

  - 业务场景的缓存策略可通过RSI递归自优化：基于业务效果回标自动迭代缓存保留规则，相比人工设计规则可额外降低约7%的推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长周期LLM Agent推理中，KV cache的存储与I/O开销占总API成本的82.4%，传统上下文裁剪/摘要方案会修改交互轨迹前缀，导致后续缓存失效、触发高成本重Prefill，且激进裁剪容易丢失关键信息造成任务精度下降，陷入成本与效果的两难困境。
### 方法关键点
- 定义3种原子KV缓存操作：append（新增KV）、drop（选择性排除指定KV不修改文本轨迹）、repos（基于RoPE旋转调整保留KV的位置编码，无需重计算），实现对活跃KV的直接控制，避免缓存失效
- 配套AKV服务引擎：对外提供兼容现有标准LLM API的无状态接口，内部通过扩展基数树跟踪带操作历史的缓存状态，段批注意力可在单次Prefill中恢复缺失缓存，解决历史依赖的缓存复用、驱逐、恢复问题
- 支持两种缓存策略迭代方式：可基于任务特性人工设计规则，也可通过递归自优化（RSI）自动搜索最优策略，还可将缓存管理作为工具开放给Agent自主决策
### 关键结果
在BCP、GAIA-Text、SWE-Verified等4个Agent benchmark、3款不同规模LLM上测试：
- 工具响应滚动丢弃策略对比传统阈值触发的上下文摘要方案，平均任务得分提升1.7个点，平均推理成本降低27.7%
- AKV引擎相比基线服务，输出吞吐量提升1.18倍，P95请求延迟加速1.51倍
- RSI自动优化的缓存策略相比人工设计规则，额外降低7.1%的推理成本
### 核心结论
直接操作KV缓存而不修改文本交互轨迹，是破解长周期Agent推理成本与效果矛盾的核心可行路径
