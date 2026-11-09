---
title: 'RPEG: Training Reasoning Language Models Scalably and Cost-Effectively'
title_zh: RPEG：可扩展低成本的推理大语言模型训练框架
authors:
- Maciej Besta
- Leonard Schmidt
- Pierre Pang
- Patrik Okanovic
- Robert Gerstenberger
- Torsten Hoefler
affiliations:
- ETH Zurich
arxiv_id: '2611.09207'
url: https://arxiv.org/abs/2611.09207
pdf_url: https://arxiv.org/pdf/2611.09207
published: '2026-11-06'
collected: '2026-11-09'
category: Training
direction: 大模型训练 · 推理LLM RL训练优化
tags:
- RLHF
- Reasoning-LLM
- Distributed-Training
- GPU-Optimization
- PPO
one_liner: 提出图驱动的推理大语言模型RL训练框架RPEG，性能较现有系统最高提2倍，硬件利用率升30%
practical_value: '- 做LLM驱动的Agent、生成式推荐的RLHF/GRPO微调时，可直接复用RPEG的「管道结构+执行调度联合优化」思路，替代分开优化的传统方案，降低训练算力成本

  - 其分层性能建模（覆盖计算/通信/内存/机架-节点-GPU层级效应）可迁移到自有分布式LLM训练集群的调度器，显著提升多机多卡场景下的GPU利用率

  - 有界异步、阶段融合、Actor-Critic共享等结构优化trick，可直接套用到业务侧小参数推理LLM的微调流程，降低step latency、加快模型迭代速度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RL已成为推理大语言模型（RLM）训练的核心，但RLM训练管道耦合多模型、异构阶段、跨步状态和复杂异步依赖，现有系统仅优化局部环节，整体难以扩展且成本极高：前沿RLM训练消耗数百万GPU小时，Agent类任务token用量更是普通对话的4~15倍，亟需全链路的训练优化方案。
### 方法关键点
- 提出RLM Pipeline Execution Graph（RPEG）：一种数据中心的图中间表示，将管道结构（有界异步、Actor-Critic共享等）和执行优化（阶段融合、细粒度调度、多维模型并行）纳入统一可搜索配置空间，而非仅优化固定管道的硬件映射。
- 配套全链路分析性能模型：联合捕获计算、通信、内存以及机架、节点、GPU层级的硬件效应，通过硬件实际校准替代厂商标称峰值，可快速评估大量候选调度计划。
- 实现事件驱动分布式运行时：基于节点完成事件调度执行，适配不同集群硬件配置，同时保证训练语义和精度不受损。
### 关键结果
在最高256张GH200 GPU的集群上测试：对比ReaL端到端性能最高提升2×；对比verl单step latency最高降低2.48×；硬件利用率最高提升30%，训练精度与VERL基线差异仅0.47%，优化器开销可忽略。
### 核心结论
RLM训练优化不能孤立优化单模型或单阶段性能，必须将管道结构和执行调度作为统一变量联合优化，才能同时提升训练性能和硬件利用率。
