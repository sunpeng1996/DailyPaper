---
title: Better Nearest Neighbor Graph Indices via (Efficient) LLM-Guided Pruning
title_zh: 基于LLM引导的高效剪枝优化近邻图检索索引
authors:
- Fangzhou Wu
- Haike Xu
- Sandeep Silwal
affiliations:
- University of Wisconsin–Madison
- MIT
arxiv_id: '2609.36359'
url: https://arxiv.org/abs/2609.36359
pdf_url: https://arxiv.org/pdf/2609.36359
published: '2026-09-28'
collected: '2026-09-30'
category: RAG
direction: RAG检索优化 · LLM引导近邻图剪枝
tags:
- ANNS
- Semantic Retrieval
- LLM Pruning
- HNSW
- DiskANN
- RAG
one_liner: 提出离线LLM引导的近邻图剪枝框架LGP，解决ANNS几何-语义不匹配问题，提升检索效率与效果
practical_value: '- 可直接复用LGP框架优化电商商品/内容语义检索的向量索引，离线阶段对HNSW/DiskANN做剪枝，不增加查询时延即可提升召回准确率，尤其适配低时延业务场景

  - 核心成本控制trick可复用：仅在两跳邻域内筛选替换候选，先通过结构信号（可达性、冗余度）初筛再送LLM，大幅降低离线LLM调用成本，适配百万/千万级向量规模的业务索引

  - 业务选型参考：搜索宽度越窄（低时延场景）LGP收益越高，文本类检索平均NDCG@10提升超24%，多模态检索提升超11%，可优先在首屏搜索/推荐场景落地'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于向量几何关系构建的近邻图ANNS索引，与下游检索的语义相关性评估目标存在本质不匹配，查询时的LLM重排只能缓解召回候选集本身的缺陷，无法解决图结构导致的相关文档漏召问题，而增大搜索预算会大幅提升查询时延，亟需在离线索引阶段优化结构来平衡几何导航效率和语义相关性。

### 方法关键点
- 基于现有HNSW/DiskANN等几何索引做局部优化，不修改查询逻辑，完全兼容现有检索-重排管线
- 候选集构造仅取节点的两跳非邻域节点，先通过结构指标（新增两跳可达性、邻域冗余度）初筛得到短名单，控制LLM调用的上下文长度和成本
- LLM语义选择环节输入当前节点文档、现有邻域上下文，筛选能补充新语义信息的候选节点
- 边替换优先删除冗余度高、新增可达性低的原有边，保持图的稀疏度和几何导航性不变，无查询时额外开销

### 关键实验
在文本检索基准BRIGHT、多模态检索基准M-BEIR上测试，对比原生DiskANN/HNSW基线：
- BRIGHT数据集：贪心搜索NDCG@10平均提升24.4%，重排后提升26.0%，相同检索质量下可减少50%的距离计算量
- M-BEIR多模态数据集：贪心搜索NDCG@10平均提升11.7%，重排后提升13.2%
- 搜索宽度越低收益越高：宽度为10时BRIGHT贪心搜索NDCG@10提升32.3%，适配低时延场景

离线优化向量索引结构解决几何-语义不匹配，比仅靠查询时重排能获得更高的检索效率和效果上限。
