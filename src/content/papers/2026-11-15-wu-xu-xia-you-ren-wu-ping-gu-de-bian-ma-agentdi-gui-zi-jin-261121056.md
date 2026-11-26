---
title: Evaluation-Free Recursive Self-Improvement for Coding Agents
title_zh: 无需下游任务评估的编码Agent递归自进化框架
authors:
- Zhe Ren
- Guowei Rong
- Yimeng Chen
- Nanbo Li
- Piotr Piękos
- Mateusz Ostaszewski
- Dandan Guo
- Jürgen Schmidhuber
affiliations:
- Jilin University
- King Abdullah University of Science and Technology (KAUST)
arxiv_id: '2611.21056'
url: https://arxiv.org/abs/2611.21056
pdf_url: https://arxiv.org/pdf/2611.21056
published: '2026-11-15'
collected: '2026-11-26'
category: Agent
direction: Agent 无下游评估的递归自进化
tags:
- Self-Improving-Agent
- Coding-Agent
- ELITE
- Recursive-Self-Improvement
- Evaluation-Free
one_liner: 提出探索-整合范式ELITE，零下游评估实现编码Agent自进化，最高提速8.8倍
practical_value: '- 做电商/推荐Agent的Prompt、工作流迭代时，可复用ELITE的多分支并行探索+机制整合范式，无需每次修改都跑全量AB测，大幅降低迭代成本，同时避免过拟合单一业务指标

  - 可复用确定性有效性门控设计，仅对Agent修改做语法、接口、核心流程的冒烟测试，前置过滤绝大多数无效修改，减少无效AB测的流量浪费

  - 若需要打造跨业务场景复用的通用Agent（如同时适配搜索、推荐、广告场景的用户意图理解Agent），优先采用这种无下游评估的机制整合方案，进化出的能力迁移性显著优于靠业务指标筛选的方案'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自进化编码Agent普遍依赖下游任务评估做候选选择，不仅需要反复执行下游任务带来极高的评估成本，还容易导致进化结果过拟合固定评估数据集，跨场景迁移能力差，业界亟需无需下游任务评估也能实现有效自进化的方案。

### 方法关键点
- 采用Explore-then-Integrate（ELITE）范式，每代从同一父Agent并行生成多个聚焦式改进的可执行子版本，全程不依赖下游任务反馈；
- 基于代码实现层面的互补性、冗余性、冲突性做机制级整合，将多个子版本的兼容改进合并为一个连贯的后代Agent，而非直接选择得分最高的单个子版本；
- 仅用确定性结构/运行有效性校验（语法、接口、核心流程冒烟测试）过滤无效修改，完全不使用下游任务得分、求解轨迹指导进化决策。

### 关键实验
在SWE-bench Pro 60任务子集上对比DGM、HGM两个依赖评估的SOTA自进化框架：ELITE将初始Agent成功率从60.0%提升到85.6%，仅比DGM低1.1个百分点、比HGM低2.7个百分点，但进化耗时比DGM降低8.8倍、比HGM降低3.2倍，全程零下游任务评估；跨基准迁移时，ELITE在SWE-bench Verified、Polyglot上分别达到73.3%、69.3%，迁移效果显著优于两个基准。

### 核心结论
Agent自进化的决策粒度可以从全版本候选下沉到实现机制层面，无需下游效果评估就能实现高效、高迁移性的能力迭代。
