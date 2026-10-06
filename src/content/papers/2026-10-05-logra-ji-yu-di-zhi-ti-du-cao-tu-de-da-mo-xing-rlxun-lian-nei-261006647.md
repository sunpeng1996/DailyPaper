---
title: 'LoGRA: Scaling LLM Reinforcement Learning with Low-Rank Gradient Sketches'
title_zh: LoGRA：基于低秩梯度草图的大模型RL训练内存优化方法
authors:
- Shaokun Zhang
- Yifan Zhang
- Jian Hu
- Yueying Li
- Hao Zhang
- Binfeng Xu
- Jan Kautz
- Yi Dong
affiliations:
- NVIDIA
arxiv_id: '2610.06647'
url: https://arxiv.org/abs/2610.06647
pdf_url: https://arxiv.org/pdf/2610.06647
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: LLM RL训练 · 内存优化
tags:
- Reinforcement Learning
- Gradient Compression
- Memory Optimization
- LLM Training
- LoRA
one_liner: 通过低秩梯度压缩与预测KL步控，降低LLM RL训练内存最多45.7%，支持单节点训练27B模型
practical_value: '- 做LLM4Rec/Agent的RLHF/RL tuning时，可直接复用LoGRA的低秩梯度压缩方案，在相同GPU资源下支持训练更大规模的生成式推荐/Agent模型，无需额外堆卡

  - 预测KL步控机制可迁移到所有RL训练场景，通过动态调整更新幅度避免RL训练过程中策略崩溃，大幅提升长周期RL训练稳定性，适配电商推荐多轮反馈调优需求

  - 梯度压缩+直接更新全量权重的模式，相比LoRA无额外推理 overhead，适合训练完成后需要直接部署的线上推荐/广告大模型场景，不需要修改现有推理链路'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RL已成为LLM能力迭代的核心手段，但RL训练内存开销远高于SFT，梯度和优化器状态占比可达参数的数倍，严重限制了大模型RL训练的落地门槛；现有LoRA等参数高效方法存在额外适配器推理开销，梯度压缩方案又普遍存在训练不稳定、更新幅度过大导致策略崩溃的问题。

### 方法关键点
- 设计低秩梯度草图LoGRA：对注意力和MLP权重矩阵，用随机投影矩阵将梯度压缩为低秩sketch，反向传播时直接累加压缩后的梯度，无需存储全量梯度；更新时用低秩矩阵乘积近似全量梯度更新，直接写入原权重无残留适配器
- 配套预测KL步控机制：更新前先估计当前更新带来的策略KL散度变化，动态缩放更新幅度，将KL控制在预设预算内，避免更新过大导致的策略偏移
- 支持低开销策略同步：仅需传输低秩sketch和随机投影种子，大幅降低训练节点和rollout节点的通信开销

### 关键结果
在数学推理任务上对比Dense Adam基线，1.5B模型平均内存降21.8%，7B模型降45.7%，推理精度无损失；单8卡H100节点可稳定训练27B模型超1100步，而Dense Adam直接OOM；相比同秩LoRA，内存占用低45.6%，推理无额外开销。

**最值得记住的一句话**：梯度压缩+KL步控的组合，可在不损失精度、不增加推理开销的前提下，大幅降低LLM RL训练的硬件门槛
