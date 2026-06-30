---
title: 'Covering the Unseen: Information Demand Coverage Optimization for Retrieval-Augmented
  Generation'
title_zh: 覆盖未满足需求：检索增强生成的信息需求覆盖优化
authors:
- Bingxue Zhang
- Jianying Jia
- Feida Zhu
affiliations:
- University of Shanghai for Science and Technology
- Singapore Management University
arxiv_id: '2606.29328'
url: https://arxiv.org/abs/2606.29328
pdf_url: https://arxiv.org/pdf/2606.29328
published: '2026-06-28'
collected: '2026-06-30'
category: RAG
direction: RAG 上下文选择 · 需求覆盖优化
tags:
- RAG
- Context Selection
- Optimal Transport
- Submodular
- Information Demand
one_liner: 提出无训练的GeoRAG框架，重构RAG上下文选择为信息需求覆盖优化，提升多维度需求覆盖率
practical_value: '- 电商多意图搜索、Agent多轮导购场景，可复用「两阶段子查询生成+反向验证加权」显式建模用户多维度需求，解决单向量embedding丢失次要子需求的问题

  - 搜索/推荐的召回后选块/选品阶段，可复用该子模贪婪选择框架，自动抑制冗余，优先填补未覆盖的需求维度，小上下文窗口场景收益更明显

  - 该方法是训练免、检索无关的后处理模块，无需标注数据，可直接接入现有RAG/搜索推荐流水线，落地成本极低

  - 结构性证明了单向量需求表示的缺陷，对多意图用户建模的架构设计有核心启发'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG上下文选择普遍假设查询的信息需求可被单个embedding向量完全表达，无论是分块排序还是传统MMR/DPP等多样性方法，都会导致选出的top-k块高度语义冗余：多跳/歧义查询的次要需求维度，即使证据已经出现在候选池中，也会因为距离主需求向量更远被系统性丢弃，该问题是单向量需求表示的结构性缺陷，和模型容量无关，亟需解决。

### 方法关键点
- 问题重构：将上下文选择从分块排序重构为**信息需求覆盖优化问题**，引入两个核心轴：Axis A建模多维度需求分布，Axis B做感知已覆盖状态的集合选择
- 需求代理建模：两阶段生成多样子查询，先生成20个候选子查询，再用最大最小余弦距离筛选出10个语义最分散的子查询；再通过反向验证加权，用「和原候选池的重叠度」「子查询结果的新颖度」过滤语义漂移和冗余子查询，构建多维度信息需求代理分布$P_Q$
- 优化求解：定义需求加权的设施选址覆盖目标，证明该目标是单调子模函数，贪婪选择可获得$(1-1/e)$的近似最优保证；用熵正则化Sinkhorn–Wasserstein距离作为边际覆盖收益的平滑代理，迭代贪婪选出k个上下文块

### 关键实验
在6个开放域QA基准（覆盖单跳、多跳推理、歧义QA、事实验证任务）测试，对比MMR、DPP、BGE-Reranker等强基线：相对于直接top-k截断，GeoRAG平均获得+6.5~+7.5 EM提升，在HotpotQA和ASQA上最大提升达+9.7 EM；多跳双需求查询的全维度覆盖率从38.6%提升到74.7%，增益在不同上下文预算、不同子查询生成器下均保持稳定。

### 核心结论
单向量需求表示存在结构性上限，任何基于查询 proximity 单调的选择器都无法覆盖分离的多维度需求，该问题和模型容量无关。
