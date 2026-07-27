---
title: 'Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement
  Learning'
title_zh: Molt：面向智能体强化学习的可扩展PyTorch原生训练框架
authors:
- Jian Hu
- Huiying Li
- Hao Zhang
- Binfeng Xu
- Yifan Zhang
- Shaokun Zhang
- Hemil Desai
- Michael Demoret
- Pavlo Molchanov
- Jan Kautz
affiliations:
- NVIDIA
arxiv_id: '2607.21653'
url: https://arxiv.org/abs/2607.21653
pdf_url: https://arxiv.org/pdf/2607.21653
published: '2026-07-21'
collected: '2026-07-27'
category: Agent
direction: Agent强化学习训练框架优化
tags:
- Agentic RL
- Training Framework
- PyTorch
- MoE
- vLLM
- Ray
one_liner: 打造代码精简易读、性能对标Megatron栈的Agent RL训练框架，支持700B级MoE大规模训练
practical_value: '- 做电商导购Agent、个性化推荐Agent的RL微调时，可直接复用Molt框架，无需自研分布式训练链路，其兼容OpenAI
  SDK的轨迹捕获能力可大幅降低现有Agent代码的改造代价

  - 训练大参数量MoE推荐/Agent模型时，可复用其token-first设计、rollout路由重放机制，避免训练-推理一致性问题导致的RL训练崩溃，减少debug成本

  - 自研RL训练框架时，可借鉴其轻量异步循环、FSDP2组合并行、直接复用上游vLLM/Ray能力的设计思路，在保证工业级性能的同时大幅降低代码复杂度'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
主流Agent RL训练框架为适配超大规模训练，分层复杂耦合度高，研究人员修改算法逻辑需穿透多层trainer、分布式后端、rollout胶水代码，迭代成本极高；同时Agent RL存在大量静默失败模式，tokenization、MoE路由、策略版本不一致会导致梯度偏差却无快速报错机制。

### 方法关键点
- 可读性优先设计，仅8.6k行RL相关代码，无冗余多后端抽象，直接复用Ray、vLLM、NeMo AutoModel上游能力，无需fork依赖
- token-first核心设计，保障三个正确性不变量：训练token与生成token完全一致、策略版本语义对齐、rollout与训练侧模型语义（含MoE路由、多模态处理）一致
- 支持两类Agent无改造接入：Gym风格Env（框架控训练循环）、ChatAgent（用户控循环，兼容OpenAI/Anthropic SDK），自动处理长上下文压缩的轨迹分段
- 支持FSDP2原生张量/专家/上下文并行，通过NCCL直接同步权重到vLLM引擎，异步流队列实现生成与训练并行无闲置，内置REINFORCE++/GRPO/GAE等多类RL estimator可选

### 关键实验
匹配所有公共参数对比SOTA Megatron-based的slime框架，在Qwen3-30B-A3B MoE模型、2节点16张H100配置下，Molt单步优化耗时119.4±2.3s，slime为109.5±10.3s，性能处于统计可比范围；已支持端到端跑通700B MoE、专家并行度256的训练任务，规模调整仅需修改配置无需架构改动。

最值得记住的一句话：复杂度不是高性能RL基础设施的必然代价，而是超大规模架构设计的路径依赖，合理复用上游成熟组件可同时实现代码精简性和工业级性能。
