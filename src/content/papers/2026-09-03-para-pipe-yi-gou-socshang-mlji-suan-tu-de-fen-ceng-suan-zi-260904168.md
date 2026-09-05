---
title: 'Para-Pipe: Exploiting Hierarchical Operator Parallelism of ML Computational
  Graphs on SoCs'
title_zh: Para-Pipe：异构SoC上ML计算图的分层算子并行优化框架
authors:
- Yujie Zhang
- Huiying Lan
- Ehsan Aghapour
- Zhiyuan Ning
- Peng Zan
- Weidong Shao
- Anuj Pathania
- Tulika Mitra
arxiv_id: '2609.04168'
url: https://arxiv.org/abs/2609.04168
pdf_url: https://arxiv.org/pdf/2609.04168
published: '2026-09-03'
collected: '2026-09-05'
category: Other
direction: 异构SoC ML推理性能与能效优化
tags:
- SoC Optimization
- Operator Parallelism
- Inference Optimization
- Pipeline Scheduling
- Energy Efficiency
one_liner: 提出分层映射框架Para-Pipe，在异构SoC上实现ML推理吞吐、延迟与能效的帕累托最优平衡
practical_value: '- 边缘端部署LLM/端侧推荐小模型时，可参考分层并行+流水线融合策略，平衡推理延迟和吞吐，降低端侧功耗

  - 多计算单元（CPU/GPU/NPU）混合部署推理服务时，可借鉴算子级并行度动态调优方法，减少跨核通信开销

  - 端侧实时推荐/广告推理场景，可参考帕累托最优配置生成方法，根据业务SLO选择最适配的调度策略'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
边缘异构SoC上的复杂ML推理场景中，传统流水线方案仅优化吞吐，无法满足高并行复杂模型的低延迟需求，单独优化吞吐或延迟会导致另一指标劣化，同时存在通信开销高、能效低的问题。
### 方法关键点
提出Para-Pipe分层映射框架，在流水线架构中融合阶段内、跨阶段的算子并行能力，通过动态微调流水线各阶段的并行度，自动在吞吐和延迟之间做trade-off，同时大幅降低处理器间通信开销。
### 关键结果
在搭载ARM big.LITTLE CPU+GPU的Amlogic SoC、搭载深度学习加速器+2个DSP的黑芝麻科技SoC上均生成多组帕累托最优配置；Amlogic SoC上的吞吐最优配置相比纯流水线策略能效提升11.0%，相比非流水线并行执行能效提升23.3%。
