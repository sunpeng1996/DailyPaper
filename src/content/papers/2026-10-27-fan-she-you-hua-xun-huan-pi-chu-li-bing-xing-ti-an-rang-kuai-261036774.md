---
title: 'Batching the Reflective Optimization Loop: Parallel Proposals Make GEPA Faster
  and Better'
title_zh: 反射优化循环批处理：并行提案让GEPA更快更优
authors:
- Jialin Zhang
- Lakshya A Agrawal
- Shangyin Tan
- Donghyun Lee
- Lutfi Eren Erdogan
- Dan Klein
- Koushik Sen
- Alex Dimakis
- Matei Zaharia
affiliations:
- University of California, Berkeley
arxiv_id: '2610.36774'
url: https://arxiv.org/abs/2610.36774
pdf_url: https://arxiv.org/pdf/2610.36774
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: Agent优化 · 反射循环并行化
tags:
- GEPA
- Reflective Optimization
- Agent Tuning
- Parallel Batching
- Prompt Evolution
one_liner: 为反射优化器GEPA引入并行提案批处理机制，同预算下提速3~4倍且泛化性能更优
practical_value: '- 优化业务Agent/Prompt时可直接复用开源GEPA的PxNSampling插件，无需修改核心逻辑，仅配置P（父代数量）、N（每父代突变数量）参数，对接Ray/Modal等并行执行框架即可落地，大幅降低Prompt迭代耗时

  - 电商推荐话术生成、Query改写等场景的Prompt优化，可采用批量提案后再统一验证的策略，减少迭代过程中对验证集的自适应调整次数，降低过拟合风险，提升线上泛化效果

  - 并行参数选型可参考场景特征：单场景单目标优化（如特定品类的推荐理由生成）优先调大N（单父代多突变），多品类多目标的通用Agent优化可同步调大P和N（多父代并行探索）

  - 若使用API驱动的Agent优化，可适当提高max_concurrency配置匹配服务商配额，进一步放大并行批处理的提速收益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
原有GEPA反射优化器采用串行循环，每次迭代仅生成1个候选、等评估完成后才进入下一轮，大量并行算力被闲置，复杂任务优化耗时长达数小时；同时频繁基于单轮验证集反馈调整搜索方向，容易过拟合验证集，泛化性能差。

### 方法关键点
- 提出P×N并行采样策略：每步从帕累托前沿采样P个父代候选，每个父代生成N个突变候选，所有P*N个候选并行发起评估，仅支付1次迭代 overhead
- 批内候选先做小批量评估筛选，通过筛选的候选再并行执行全量验证集评估，最终更新帕累托前沿
- 配套runtime模型可根据worker池规模、候选接受率预测不同并行度的提速比，指导参数选型和资源分配

### 关键结果数字
实验在LiveBench-Math（5000次metric调用预算）、HoVer多跳检索（3000次metric调用预算）两个任务上对比串行GEPA基线：
- 最高提速3~4倍，大部分配置的优化耗时降到基线的1/2以下，最快可降至1/4~1/3
- LiveBench-Math测试准确率从68.9%提升至72.1%（2×2配置），HoVer测试全召回率从49.0%提升至60.0%（8×1配置）
- 同预算下泛化gap从9pp降至2pp，单位美元/metric调用的效果产出效率更高

> 最值得记住的一句话：反射优化的并行批处理不是单纯的工程提速手段，还能通过减少验证集自适应调整次数提升泛化性能，是兼顾效率和效果的低成本优化方案。
