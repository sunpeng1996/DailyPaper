---
title: Automated Discovery Has No Universally Superior Harness
title_zh: 自动化发现系统不存在通用最优执行框架
authors:
- Akshat Gupta
- Jermaine Lei
- Alexander Lu
- Gopala Anumanchipalli
- Leshem Choshen
affiliations:
- UC Berkeley
- MIT
- MIT-IBM Watson AI Lab
arxiv_id: '2607.18235'
url: https://arxiv.org/abs/2607.18235
pdf_url: https://arxiv.org/pdf/2607.18235
published: '2026-07-20'
collected: '2026-07-21'
category: Agent
direction: Agent 自动发现框架选型优化
tags:
- Autonomous Discovery
- LLM Harness
- Evolutionary Search
- Adaptive Compute Allocation
- LLM Evaluation
one_liner: 通过310万次LLM rollout实验验证无通用最优自动发现harness，提出自适应算力分配策略提效
practical_value: '- 做LLM驱动的Agent迭代任务（如电商文案生成、选品策略迭代）时，不要迷信通用开源框架，需把框架选型作为超参数针对业务场景调优

  - 迭代类任务算力分配可复用自适应剪枝策略：初期并行多个框架方案，根据早期表现剪枝弱方案，算力向优质方案倾斜，降本提效

  - 对比不同迭代框架效果时需做足够多重复试验，避免单次随机波动导致选型错误，高成本任务先做小批量验证再放大'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM驱动的自主发现系统（如OpenEvolve、TTT-Discover）常被当作通用harness使用，但由于运行成本高、随机性强，现有对比试验样本量不足，无法区分方法收益和随机波动，也未验证框架的跨场景通用性。
### 方法关键点
将两类主流发现harness拆解为存档、父节点选择、探索策略、预算分配等核心组件，组合出30个算力匹配的候选harness，在12组模型-问题对场景下开展超310万次LLM rollout的多轮重复试验，统计验证不同框架的效果差异。
### 关键结果
1. 无任何固定harness能在所有场景下稳定最优，OpenEvolve变体效果普遍弱于更简单的替代方案
2. 提出的自适应算力分配策略比随机选固定框架效果更优，也优于非自适应的框架集成
3. 框架早期进展可预测最终性能，为自适应剪枝策略提供可行性支撑
