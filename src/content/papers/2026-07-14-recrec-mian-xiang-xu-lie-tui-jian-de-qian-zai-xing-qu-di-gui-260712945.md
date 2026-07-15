---
title: 'RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation'
title_zh: RecRec：面向序列推荐的潜在兴趣递归推理框架
authors:
- Wenhao Deng
- Junchen Fu
- Hanwen Du
- Alexandros Karatzoglou
- Ioannis Arapakis
- Hangjun Guo
- Kaiwen Zheng
- Yongxin Ni
- Joemon M. Jose
arxiv_id: '2607.12945'
url: https://arxiv.org/abs/2607.12945
pdf_url: https://arxiv.org/pdf/2607.12945
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 序列推荐 · 潜在兴趣推理优化
tags:
- Sequential Recommendation
- Recursive Reasoning
- Latent Interest
- Context Compression
- Supervised Learning
one_liner: 提出无RL的序列推荐递归推理框架RecRec，解耦推理与预测突破原有单状态瓶颈
practical_value: '- 序列推荐建模可复用多向量兴趣表征思路，替代传统单用户向量，覆盖更多维度用户潜在兴趣，提升召回/排序阶段的兴趣匹配度

  - 可借鉴推理与预测解耦架构，推理深度可在上线后根据算力资源动态调整，无需重新训练即可适配不同流量层级的性能要求

  - 兴趣多样性正则项可直接迁移到用户兴趣建模模块，缓解兴趣表征同质化冗余问题，提升序列推荐泛化性'
score: 8
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有推理增强型序列推荐方法多将推理与预测耦合在单d维状态中，限制推理深度，且大多依赖RL多阶段pipeline，优化复杂度高、落地难度大
**方法关键点**：提出无RL的RecRec框架，采用两阶段监督训练：1. Context Compressor蒸馏backbone隐状态为少量潜在兴趣向量，引入Interest Diversity Regularizer保证各兴趣表征覆盖用户不同行为维度；2. Recursive Reasoner在独立中间隐空间迭代优化兴趣表征，深度监督机制支持推理时任意调整推理深度无需重训
**关键结果**：在4个真实数据集上性能超过所有SOTA推理增强型序列推荐方法，其中3个数据集上推理深度超过训练深度时仍能获得持续效果收益
