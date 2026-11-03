---
title: 'MAServeBench: Benchmarking Multi-Agent LLM Serving Systems with Hierarchical
  Collaboration Workloads'
title_zh: MAServeBench：面向多Agent LLM服务系统的分层协作负载基准
authors:
- Shengxuan Qiu
- Haochen Huang
- Shuzhang Zhong
- Zizhuo Fu
- Zebin Yang
- Jianming Tong
- Meng Li
affiliations:
- Peking University
arxiv_id: '2610.40293'
url: https://arxiv.org/abs/2610.40293
pdf_url: https://arxiv.org/pdf/2610.40293
published: '2026-10-28'
collected: '2026-11-03'
category: MultiAgent
direction: 多Agent LLM 服务性能基准测评
tags:
- Multi-Agent
- LLM Serving
- Benchmark
- Semantic Trace
- Workload Generation
one_liner: 提出可配置协作规则的多Agent LLM服务基准，生成带语义依赖的工作负载用于系统和硬件测评
practical_value: '- 搭建电商多Agent业务（智能导购、多角色内容生成、跨链路推荐决策）时，可复用分层协作负载抽象模型，量化不同协作模式（并行检索、迭代文案优化）对LLM服务的资源消耗，优化集群调度策略

  - 可复用Hierarchical Semantic Trace设计，记录多Agent调用LLM的依赖关系、上下文传递路径，针对性做KV cache共享、依赖感知调度，降低端到端任务延迟

  - 上线多Agent业务时，不要仅关注LLM推理TPS、单请求延迟指标，需锚定端到端任务SLO（如用户请求到最终响应的总耗时），避免局部资源优化反而提升整体任务超时率

  - 针对Agent协作中频繁出现的小batch、短上下文推理场景，可参考论文硬件探针结论，优先优化Gather算子、KV cache residency，提升GPU/NPU利用率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM服务基准均基于独立请求设计，无法适配多Agent系统的依赖型请求、动态上下文共享、协作驱动的并发模式，难以区分性能瓶颈来自协作规则、调度策略还是硬件能力，也无法关联硬件指标与端到端任务体验。
### 方法关键点
- 分层协作负载抽象：将多Agent工作流拆为Spawn、Fork-Join、Refinement Loop、Debate 4种可复用模板，支持独立配置协作规则与任务输入，相同任务可生成不同协作模式的工作负载
- Hierarchical Semantic Trace：分层记录任务、阶段、会话、操作四个维度的调用依赖、上下文、控制规则，支持固定工作负载下的可复现重放，隔离不同变量对性能的影响
- 任务关联测量体系：将GPU/NPU硬件指标与端到端任务SLO绑定，直接衡量优化对业务目标的影响
### 关键结果
覆盖12种主流多Agent工作流（MetaGPT、GPT Researcher等）、30种任务绑定，在A800、Ascend 910C等4种硬件上测试，核心结论：
1. 固定工作负载下，仅调整合法请求释放顺序（加同步屏障）可使端到端任务延迟上升26%~54%
2. KV预算从16GiB扩容到40GiB，多Agent场景冗余prefill降低52%，任务P95延迟下降17.5%
3. 中等负载下无屏障的DAG调度任务SLO达标率100%，加屏障后仅4%，局部优化提升7.7%TPS也可能无法改善任务达标率

> 最值得记住的话：多Agent LLM服务优化不能只看单推理指标，必须结合协作规则、端到端任务SLO做全局优化，局部硬件效率提升不等价于业务体验变好
