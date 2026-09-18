---
title: Accelerating Sharded Data Parallelism at Scale with Federated Learning
title_zh: 基于联邦学习的大规模分片数据并行训练加速方法
authors:
- Gianluca Mittone
- Marco Aldinucci
arxiv_id: '2609.20359'
url: https://arxiv.org/abs/2609.20359
pdf_url: https://arxiv.org/pdf/2609.20359
published: '2026-09-17'
collected: '2026-09-18'
category: Training
direction: 大模型分布式训练 · 通信优化
tags:
- Distributed Training
- Federated Learning
- Sharded Data Parallelism
- LLM Pre-training
- Communication Optimization
one_liner: 将联邦学习FedAvg聚合与分片数据并行融合，降低大模型大规模训练通信开销，同时提升效率与模型质量
practical_value: '- 电商/推荐领域大模型多卡预训练/微调场景，可复用FL+FSDP分组架构，将同节点/同机架GPU划为联邦组，大幅降低跨节点/跨机架通信开销，提升训练速度

  - 大规模分布式训练任务可直接复用该方法的全局batch size绑定组大小的设计，避免batch size随GPU数线性扩张导致的模型效果下降问题

  - 多业务线跨集群联合训练大模型场景，可借鉴组间FedAvg轻量化聚合逻辑，减少跨集群带宽消耗，同时满足数据不出域的隐私要求'
score: 8
source: arxiv-cs.AI
depth: abstract
---

### 动机
大模型预训练需在数千GPU上运行数月，分片数据并行（SDP）是主流加速方案，但大规模部署时跨异构互联的通信开销极高，且GPU规模扩大会导致全局batch size过大，损害模型收敛效果。
### 方法关键点
借鉴联邦学习高效通信逻辑，提出FL+FSDP、FL+HSDP两种混合训练算法：将大规模SDP集群拆分为多个松耦合联邦组，组内执行原生SDP训练，组间仅做FedAvg风格的轻量化参数聚合，同时将全局batch size绑定为联邦组大小，避免batch size随GPU数过度扩张。
### 关键结果
在512张A100上预训练Llama3.1 8B，相同超参下，两种算法比原生SDP方案数据处理速度最高提升8.04倍，评测perplexity最高降低4.48
