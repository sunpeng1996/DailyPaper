---
title: Structuring MoE Expert Selection for Agentic Reinforcement Learning
title_zh: 面向智能体强化学习的结构化MoE专家选择框架
authors:
- Bolian Li
- Ting-Yao Hu
- Cheng-Yu Hsieh
- Sanjoy Chowdhury
- Oncel Tuzel
- Raviteja Vemulapalli
affiliations:
- Apple
- Purdue University
arxiv_id: '2610.07332'
url: https://arxiv.org/abs/2610.07332
pdf_url: https://arxiv.org/pdf/2610.07332
published: '2026-10-04'
collected: '2026-10-08'
category: Agent
direction: Agent 强化学习 · MoE 路由优化
tags:
- MoE
- Reinforcement Learning
- Agent
- Routing Control
- LLM Training
one_liner: 提出层级路由控制框架优化MoE路由，大幅提升智能体RL任务表现与推理效率
practical_value: '- 做LLM Agent MoE微调/RL训练时，可直接引入层级路由控制：turn层对齐操作语义、token层保证局部一致性，无需修改原生MoE架构即可实现涨点提效

  - 遇到MoE RL训练不稳定问题时，可复用熵门控机制：监测policy熵波动超限时切断路由控制梯度，避免训练崩塌，适配PPO/GRPO等多种主流RL算法

  - 长路径交互Agent业务（如电商导购、用户运营Agent）可按操作语义（查询/下单/咨询等）给轨迹打标签，作为路由正则信号，同时提升任务成功率、降低推理延迟

  - MoE推理优化可利用路由一致性规律，同语义段复用已加载的expert权重，减少显存调度开销，最高可提升40%+推理吞吐量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期LLM Agent普遍采用MoE架构降低推理开销，但现有RL训练方法忽略MoE路由与Agent语义轨迹的天然对齐关系，无约束的路由扰动会导致任务性能瓶颈、推理效率下降，同时MoE RL训练容易发生不稳定崩塌问题，业内尚无成熟的协同优化方案。

### 方法关键点
- 层级路由控制：turn层通过最大化路由分布与操作标签的互信息，鼓励同语义操作（如READ/CREATE/UPDATE）复用同组专家、不同操作分离专家集合；token层仅当相邻token路由相似度高于阈值时正则约束路由一致性，保留语义边界的路由切换需求，无需修改原生MoE架构。
- 熵门控机制：实时监测RL训练过程中的policy熵，仅当熵值落在预设稳定区间时才启用路由控制梯度，避免辅助损失干扰主任务优化导致训练崩塌。

### 关键结果
在AppWorld、AutomationBench两个Agent基准上，对比PPO/GRPO/LOOP/GiGPO等主流RL算法，所有基线加本框架后任务成功率均提升10个点以上，最高提升12.9个点；推理吞吐量提升41.1%，单轮轨迹生成耗时降低22.3%，同时训练稳定性大幅提升。

**最值得记住的一句话**：Agent轨迹的语义结构本身就是优化MoE专家容量的高效信号，不需要额外引入标注成本就能同时实现性能与效率的双重提升。
