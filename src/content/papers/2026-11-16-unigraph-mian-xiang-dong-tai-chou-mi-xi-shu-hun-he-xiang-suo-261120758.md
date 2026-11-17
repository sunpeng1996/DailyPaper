---
title: 'UniGraph: A Unified Graph-based Index for Dynamic Hybrid Dense-Sparse Vector
  Retrieval'
title_zh: UniGraph：面向动态稠密稀疏混合向量检索的统一图索引
authors:
- Keyu Chen
- Xiaoyao Zhong
- Jiabao Jin
- Peng Cheng
- Wangze Ni
- Jingkuan Song
- Heng Tao Shen
affiliations:
- Tongji University
- Zhejiang University
arxiv_id: '2611.20758'
url: https://arxiv.org/abs/2611.20758
pdf_url: https://arxiv.org/pdf/2611.20758
published: '2026-11-16'
collected: '2026-11-17'
category: RAG
direction: 混合向量检索 · 图索引优化
tags:
- Hybrid Retrieval
- Graph Index
- ANNS
- Dense-Sparse Retrieval
- RAG
one_liner: 提出支持查询级动态权重的统一混合图索引，大幅提升混合检索的Recall-QPS性价比
practical_value: '- 电商搜索/推荐混合召回场景可复用α-cover建图思路，将多组召回权重下的近邻合并为单图，避免多套索引的存储冗余

  - 查询侧α自适应路由策略可直接落地，根据查询对语义/词汇匹配的偏好选择稠密/稀疏索引作为入口，降低检索链路时延

  - 稠密优先剪枝trick可直接复用：先算稠密分量，结合预存的稀疏向量范数估算混合距离下界，跳过无必要的精确稀疏距离计算，实测提10%左右QPS几乎无损召回

  - 业务有动态调整召回权重需求时（如大促期优先匹配营销词、日常优先语义匹配），无需重建索引，直接调整查询侧α参数即可，大幅降低运维成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有稠密稀疏混合检索要么采用双路召回后重排的架构，容易漏过仅在混合排序下排名靠前的候选，高召回下需要拉取大量候选导致吞吐量不足；要么基于固定权重构建混合图，无法适配查询级动态的语义/词汇匹配权重需求，难以满足生产环境动态混合检索的诉求。

### 方法关键点
- 建图阶段：采用α-cover采样0~1区间的多个混合权重，合并各权重下的Top-kg近邻，按出现频率筛选保留M度以内的边，单图即可支持所有查询权重无需重建
- 查询阶段：采用α自适应路由策略，α≤0.5（词汇匹配优先）走稀疏索引入口，α>0.5（语义匹配优先）走稠密索引入口，减少图遍历步数
- 剪枝优化：采用稠密优先的混合距离估算逻辑，预存稀疏向量范数，若估计距离超过当前结果集阈值则跳过精确稀疏距离计算，降低计算开销

### 关键结果
在NQ、MS MARCO等5个BEIR基准数据集上，对比双路HNSW+SINDI、固定权重混合图等7个基线：混合权重场景下Recall@100≥0.95时QPS比最快基线高27.6%~52.3%；固定权重场景下QPS是最快基线的1.18~2.85倍，仅比双路索引多占5%左右存储空间，目前已在蚂蚁集团生产环境落地。

### 核心结论
混合稠密稀疏检索不需要维护多套索引或固定权重，通过多权重近邻合并的统一图可以同时兼顾动态权重灵活性和高召回下的吞吐量。
