---
title: 'Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language
  Modeling'
title_zh: Auto-Research Arena：语言建模自主研究系统的多目标基准框架
authors:
- Xi Chen
- Chongjian Ge
- Yiran Xu
- Yiqun Mei
- Henrik I. Christensen
- Hao Tan
- Ziwen Chen
- Hanwen Jiang
affiliations:
- University of California San Diego
- Adobe Research
arxiv_id: '2610.35866'
url: https://arxiv.org/abs/2610.35866
pdf_url: https://arxiv.org/pdf/2610.35866
published: '2026-10-26'
collected: '2026-10-27'
category: Agent
direction: 自主研究Agent · 多目标基准评估
tags:
- Autonomous Research Agent
- Benchmark
- LLM Optimization
- Constrained Optimization
- Idea Discovery
one_liner: 提出覆盖9类LLM全生命周期效率目标的自主研究基准，支持框架评估与可复用优化思路挖掘
practical_value: '- 做LLM4Rec/业务Agent优化时，可复用「准入+目标」双层约束框架：先定义业务效果准入阈值（如推荐点击率下降不超过1%），再优化效率目标（如推理延迟、显存占用），避免为效率牺牲核心业务指标

  - 做自主优化Agent架构选型时，优先验证简单Sequential Search基线，无需盲目堆叠复杂多Agent/树状搜索架构，论文证明简单基线效果超过多数复杂方案，可大幅降低工程成本

  - 做多场景LLM优化时，可复用跨目标成果迁移思路：比如先优化得到小参数量模型，再在其基础上优化推理延迟，可叠加增益且无需从零开始探索

  - 低成本挖掘LLM优化点时，可参考「短训练预算搜索+跨idea组合」模式：小范围搜索得到的优化点组合后可稳定提升全量训练的模型效果，节省探索成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有自主研究系统的基准大多聚焦单一目标（如最小化验证损失），无法评估系统在多维度优化需求（模型大小、训练效率、推理延迟等）下的通用能力，也难以产出可跨场景复用的优化思路，需要统一的多目标评估框架推动自主研究系统落地。

### 方法关键点
- 采用「准入门槛+优化目标」分离的约束优化范式：所有候选方案需先满足BPB<1.05的质量准入要求，再针对9类覆盖LLM全生命周期的效率目标（参数量、训练token数、FLOPs、KV cache大小、解码延迟等）做优化，避免无意义的效率-质量tradeoff
- 支持跨目标成果复用：不同目标搜索产出的优化思路存入idea库，后续新优化任务（如质量提升）可直接复用、组合已有思路，降低探索成本
- 内置轻量Sequential Search基线：单路径逐次验证修改，保留有效改进后再迭代，无复杂编排逻辑

### 关键实验结果
基于631M token的ClimbMix数据集，对比7类研究框架（AutoScientists、Arbor、GEAR、TPE等），用Claude Opus 5和GPT-6 Astra两款基座测试：
1. 简单Sequential Search基线在两款基座上均排总榜第二，超过多Agent、进化搜索等复杂方案；专门针对单目标优化的TPE排名垫底，泛化性差
2. 多目标搜索产出32个有效优化点，归为9个idea家族，组合后同参数量下held-out BPB从0.9295降到0.9112（降1.97%），同FLOPs下训练损失降2.78%
3. 10分钟短训练搜索得到的优化方案，优势可延续到5倍时长的全量训练，最多可节省43.3%的训练token

### 最值得记住的一句话
复杂的自主研究Agent编排架构不一定比简单的逐次迭代基线效果好，多目标约束下的探索能产出更具复用价值的优化思路
