---
title: How Sparse Probability Maps Shape Mixture-of-Experts Routing
title_zh: 稀疏概率映射对MoE路由机制的影响研究
authors:
- Tomás Brogueira
- Marcos Treviso
- Miguel Couceiro
affiliations:
- Técnico, Universidade de Lisboa
- INESC-ID
- Instituto de Telecomunicações
- ELLIS Unit Lisbon
- Gandara AI
arxiv_id: '2610.06677'
url: https://arxiv.org/abs/2610.06677
pdf_url: https://arxiv.org/pdf/2610.06677
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: MoE路由 · 稀疏概率映射优化
tags:
- MoE
- Sparse Routing
- sparsemax
- entmax
- normmax
- Probability Map
one_liner: 对比四类概率映射的MoE路由表现，揭示映射与学习分数共同决定专家参与模式
practical_value: '- 业务中用MoE做大模型推荐/广告生成/Agent推理时，若需要弹性调整算力，可将路由层的softmax替换为sparsemax，训练时固定K=2，推理时可在K=2~8范围内按需调整，损失波动仅0.02nats，远低于softmax的0.58nats，适配流量峰谷的算力调度需求

  - 若要实现MoE路由动态选择专家数量，不能仅替换稀疏概率映射，需额外增加约束控制路由分数的top-2 gap分布，使其匹配映射的稀疏阈值，否则稀疏性会在训练后消失，比如1.5-entmax训练后几乎不会降低有效专家数

  - 设计MoE负载均衡策略时，不能仅统计名义选择的专家负载，需统计实际分配正权重的专家负载：normmax-2的名义负载CV与softmax接近，但实际贡献负载CV高出14%，仅统计名义负载会低估负载不均问题，造成算力浪费'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统MoE路由采用softmax+top-K固定选择K个专家，无法根据token需求动态调整专家数；sparsemax、entmax、normmax等稀疏概率映射理论上可自适应给部分专家赋零权重，实现动态专家参与，但业界缺乏对这类稀疏性训练后留存效果、路由行为决定因素的系统性研究。

### 方法关键点
- 控制变量训练300M、1B两个规模的Llama 3架构top-2 MoE语言模型，仅替换路由层概率映射，其余架构、训练数据、平衡损失完全对齐；
- 从概率保留率、有效专家参与数、路由分数分布与映射稀疏阈值的匹配度三个维度诊断路由行为；
- 测试模型对推理阶段调整K值的鲁棒性。

### 关键结果
基于10B token DCLM-baseline数据训练，对比softmax、1.5-entmax、sparsemax、2-normmax四类映射：1B规模下，1.5-entmax丢弃的概率质量比softmax少30%但99.95%token仍使用2个专家，normmax-2可让21%的token仅用1个专家；训练时K=2，推理时将K调整为8，sparsemax损失仅上涨0.02nats，远低于softmax的0.58nats。

### 核心结论
MoE路由的自适应稀疏性并非由概率映射单独决定，而是映射的稀疏阈值与路由学习到的分数分布共同作用的结果。
