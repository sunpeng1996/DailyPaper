---
title: Adaptive Inference Batching using Policy Gradients
title_zh: 基于策略梯度的自适应推理批处理调度算法
authors:
- Ruslan Sharifullin
affiliations:
- Stanford University
arxiv_id: '2607.05272'
url: https://arxiv.org/abs/2607.05272
pdf_url: https://arxiv.org/pdf/2607.05272
published: '2026-07-06'
collected: '2026-07-07'
category: Agent
direction: Agent 推理服务调度优化
tags:
- Reinforcement Learning
- Policy Gradient
- Inference Serving
- Batching
- Multi-GPU
one_liner: 提出策略梯度驱动的自适应推理批处理策略，多GPU场景较轮询调度性能提升3.5倍
practical_value: '- 多GPU部署LLM/推荐大模型推理服务时，可复用REINFORCE Agent的异构请求路由逻辑，将长短请求分GPU调度消除队头阻塞，最高可获3.5倍性能提升

  - 奖励函数可参考分权重的SLA适配思路：对低延迟要求的请求（如电商实时搜索推理）设置更高延迟惩罚权重，优先保障核心请求SLA

  - 单GPU推理场景无需引入复杂RL调度，优化后的静态批处理策略性价比更高，可避免不必要的算法复杂度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型等复杂ML推理服务需要平衡高吞吐与低延迟，行业通用的静态批处理策略刚性强，无法适配动态流量模式，多GPU异构请求场景下队头阻塞问题突出，传统启发式调度难以达到全局最优。

### 方法关键点
- 将自适应批处理问题建模为MDP，状态空间含归一化队列长度、距上次批处理时间、请求类型、GPU状态共8维特征；单GPU动作空间为批大小选择，多GPU场景为「目标GPU+批大小」联合决策
- 奖励函数设计为「当前吞吐 - 加权请求延迟总和」，对低延迟要求的快请求设置10倍于慢请求的延迟惩罚，直接对齐业务SLA需求
- 策略网络采用「输入投影+多头注意力+MLP」结构，对比REINFORCE与PPO两种策略梯度算法，REINFORCE在该短 horizon 场景下收敛速度更快

### 关键实验
基于自定义离散事件模拟器，覆盖泊松流量、极端突发流量、Azure Functions真实生产trace、多GPU异构请求4种场景，对比静态批处理、轮询、最短队列等基线：单GPU场景RL与最优静态策略性能接近，提升不足1%；多GPU异构场景下REINFORCE Agent较轮询调度性能提升348%（3.5倍），较短队列调度高48%，同时实现比最短队列高60%的吞吐、比轮询低25%的延迟，严格满足3s SLA要求。

最值得记住的结论：单GPU推理调度用优化后的静态批处理足够高效，RL的核心价值集中在多GPU异构请求的联合路由与批组合优化场景。
