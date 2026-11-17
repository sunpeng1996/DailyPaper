---
title: Reducing Batch Makespan for LLM Agent Workloads through Inference-Environment
  Coordination
title_zh: 推理-环境协同降低LLM Agent工作负载批处理完成时间
authors:
- Wei Feng
- Meiling Chen
- Boxiao Chen
- Lu Liu
- Bin Zi
- Libin Ye
- Xingyu Lu
- Lei Xu
- Jun Zhou
affiliations:
- Ant Group Ling Team
arxiv_id: '2611.16661'
url: https://arxiv.org/abs/2611.16661
pdf_url: https://arxiv.org/pdf/2611.16661
published: '2026-11-11'
collected: '2026-11-17'
category: Agent
direction: Agent 批量任务执行效率优化
tags:
- LLM Agent
- Batch Scheduling
- KV Cache
- Inference Optimization
- Environment Interaction
one_liner: 针对交替推理与环境交互的Agent批量任务，提出全链路协同优化方案，批处理耗时最高降65%
practical_value: '- 优化电商/推荐场景批量Agent任务（如批量生成营销文案、批量用户行为模拟、推荐效果评测）时，可先基于历史任务数据计算KV
  cache与循环状态的内存分配比，再设置合理并发度，避免内存瓶颈导致的重计算耗时

  - 多机推理部署时，可采用带负载约束的一致性哈希（LBCH）路由，将同一条Agent轨迹的请求调度到同一worker，既能保证KV cache复用，又能避免单worker负载过高

  - 当Agent依赖的外部工具/接口有配额限制时，可将任务准入和环境执行的并发度解耦，再用CAAS调度策略优先推进已完成多轮交互的长链任务，缩短批处理长尾耗时

  - 优化多轮Agent任务调度时，可优先调度最近处理过的同轨迹请求，避免缓存被提前淘汰，同时降低前缀匹配的计算开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent的批量任务（如基准评测、合成数据生成、RL rollout）是大模型迭代的核心流程，现有优化多聚焦单请求延迟，忽略批处理整体完成时间（makespan）；且Agent任务交替执行LLM推理与环境交互，传统推理调度未结合交互侧约束，容易出现内存分配失衡、缓存复用率低、环境资源瓶颈拉长长尾等问题，直接拖慢模型迭代效率。

### 方法关键点
- 负载感知的混合缓存分配：基于历史任务轨迹的平均上下文长度，建模KV cache与循环状态的内存需求，平衡两者的GPU内存分配比例，同时给出参考并发度，兼顾并行度与缓存复用率
- 轨迹感知的推理调度：用带负载约束的一致性哈希（LBCH）路由保证同轨迹请求优先调度到同一worker，再用路由前缀（RP）调度策略优先处理最近服务过的轨迹请求，降低缓存淘汰概率与调度开销
- 推理-环境协同：解耦任务准入与环境执行的并发度限制，避免环境配额不足导致推理侧闲置；提出CAAS调度策略，优先调度已完成多轮交互的长链任务的环境请求，缩短批处理长尾

### 关键实验
基于蚂蚁Ling-3.0-Flash、Ling-3.1-Flash模型，在BFCL、SWE-bench、WideSearch、MCP-Atlas四个基准上测试，对比原有调度方案，批处理makespan降低10.4%~65.0%，且任务评测得分无损失；该方案已落地到Ling-3.x全系列的训练评测流程，大幅提升模型迭代效率。

### 最值得记住的一句话
Agent批量任务优化不能只关注推理侧，需结合任务轨迹特征、环境资源约束做全链路协同，才能最大化整体执行效率。
