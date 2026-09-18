---
title: 'Think Thrice Before Reranking: Multi-perspective Evidence and Reasoning Integration
  for Text Reranking'
title_zh: 多视角证据与推理融合的文本重排序框架MERIT-Rank
authors:
- Lijun Liu
- Zhengzong Chen
- Wenyan Li
- Yuanyuan Zhao
- Fei Huang
affiliations:
- Honor Device Co., Ltd
arxiv_id: '2609.20131'
url: https://arxiv.org/abs/2609.20131
pdf_url: https://arxiv.org/pdf/2609.20131
published: '2026-09-17'
collected: '2026-09-18'
category: RecSys
direction: 大语言模型 · 检索重排序性能优化
tags:
- Reranking
- LLM4IR
- Multi-perspective Reasoning
- Reinforcement Learning
- Policy Optimization
one_liner: 基于多视角推理融合与渐进式训练实现小参数模型重排性能超越大模型
practical_value: '- 电商搜索/推荐重排阶段可复用多视角评估框架：分别从语义匹配、用户意图满足、商品详情页证据支撑三个维度打分再融合，降低单一排序逻辑偏差，尤其适配问题型、对比型等复杂query的召回结果重排。

  - 可复用渐进式训练策略PRPO：先通过SFT对齐结构化推理格式，再用RL分阶段优化相对排序提升、绝对排序指标（如NDCG、MRR），解决多步推理任务训练易崩溃问题，适合中小参数LLM做排序类任务微调。

  - 多视角推理数据合成方案可直接复用：用强老师模型生成多视角推理链，再通过双路验证（推理有效性+排序有效性）过滤低质量样本，大幅降低人工标注成本。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于LLM的推理型重排序方法依赖单条推理轨迹，容易因推理错误传播导致排序结果偏差，且无法覆盖语义匹配、意图满足、证据支撑等多维度相关性信号，在复杂检索场景下鲁棒性差、泛化能力弱，小参数模型性能难以充分释放。

### 方法关键点
- 构建Multi-Trajectory Reasoning Space (MTRS)：从语义对齐、意图满足、证据落地三个互补视角分别生成推理链和初步排序结果，覆盖多维度相关性信号，避免单视角偏差。
- 多轨迹联合重排器：单模型统一完成多视角推理、视角内排序、多轨迹聚合、最终排序输出四个步骤，无需多模型集成，降低推理成本。
- 提出Progressive Rank Policy Optimization (PRPO)：先通过SFT学习结构化推理格式，再分两阶段RL优化：第一阶段优化格式合规性和相对排序提升，第二阶段加入NDCG、MRR等绝对排序指标，避免训练崩溃、提升收敛效率。
- 配套多视角数据合成与双路验证机制：用强老师模型生成多视角推理样本，通过「合成排序优于单视角排序」「相关文档排在头部」两个规则过滤低质量样本。

### 关键结果
在推理密集型基准BRIGHT、传统检索基准TREC-DL、BEIR上测试，对比ReasonRank、ERANK、REARANK等SOTA基线：4B参数MERIT-Rank在BRIGHT上NDCG@10达36.6，超过多数7B、32B基线，比同参数ERANK-4B高6.1%；7B版本在TREC+BEIR平均NDCG@10达65.3%，比ReasonRank-7B高3.2%；同性能下推理所需滑动窗口数比ReasonRank少2/3，推理延迟降低40%以上。

### 核心启示
结构化的多视角推理融合，比单纯堆模型参数、增加无约束推理轨迹能更高效地提升重排序的鲁棒性和性能。
