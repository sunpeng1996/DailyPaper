---
title: Encryption-Compatible Clustered Federated Learning via Distributed Expectation-Maximization
  over Metadata
title_zh: 基于元数据分布式期望最大化的加密兼容聚类联邦学习
authors:
- Michael Ben Ali
- Imen Megdiche
- André Péninou
- Olivier Teste
affiliations:
- UT3
- IRIT
- CNRS
- INU Champollion
- UT2J
arxiv_id: '2607.28338'
url: https://arxiv.org/abs/2607.28338
pdf_url: https://arxiv.org/pdf/2607.28338
published: '2026-07-30'
collected: '2026-08-01'
category: Training
direction: 聚类联邦学习 · 隐私保护训练优化
tags:
- Clustered Federated Learning
- Privacy Preserving
- Distributed EM
- Encryption Compatible
- Metadata
one_liner: 提出FLAMECHE框架，通过分布式EM实现加密兼容的元数据聚类联邦学习，平衡CFL三大性能维度
practical_value: '- 电商跨端联邦推荐训练场景，可复用低维元数据+分布式EM的客户端聚类方案，在不暴露用户原始行为数据的前提下实现异质性设备/用户分组，提升个性化推荐模型效果

  - 需兼容同态加密、安全多方计算等隐私机制的联邦训练任务，可借鉴仅用加法操作实现服务器更新的设计思路，大幅降低加密适配的工程复杂度与计算 overhead

  - 跨域联邦推荐的方案选型可参考CFL三元悖论（隐私/通信/计算效率）的权衡框架，结合业务对数据安全、latency、成本的优先级选择最优聚类联邦方案'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
聚类联邦学习（CFL）通过分组同分布客户端解决联邦场景数据异质性问题，但现有方法存在隐私保护、通信成本、计算效率三者不可兼得的三元悖论，低开销的元数据驱动CFL方案无法兼容主流联邦加密机制，难以落地隐私要求高的业务场景。

### 方法关键点
提出FLAMECHE框架，将元数据驱动的CFL流程重构为分布式Expectation-Maximization（EM）任务，限制服务器侧更新仅使用加法操作，在保留通信、计算效率的同时，天然适配主流安全联邦学习的加密要求。

### 关键结果
多数据集、多异质性场景的批量实验验证，FLAMECHE可稳定提升客户端模型效果，在不牺牲通信、计算效率的前提下实现加密兼容，突破传统CFL三元悖论的性能约束。
