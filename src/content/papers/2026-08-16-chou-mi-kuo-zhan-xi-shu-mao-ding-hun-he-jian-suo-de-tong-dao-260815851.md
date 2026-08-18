---
title: 'Dense Expands, Sparse Anchors: Channel-Asymmetric Query Expansion for Hybrid
  Retrieval'
title_zh: 稠密扩展、稀疏锚定：混合检索的通道非对称查询扩展方法
authors:
- Chunran Zhang
affiliations:
- Southwest Jiaotong University
arxiv_id: '2608.15851'
url: https://arxiv.org/abs/2608.15851
pdf_url: https://arxiv.org/pdf/2608.15851
published: '2026-08-16'
collected: '2026-08-18'
category: QueryRec
direction: 查询扩展 · 混合检索通道优化
tags:
- QueryExpansion
- HybridRetrieval
- DenseRetrieval
- SparseRetrieval
- LLM
one_liner: 提出通道非对称的混合检索查询扩展方法DESA，同时提升检索效果与降低双渠道访问深度
practical_value: '- 电商搜索混合召回场景可直接复用非对称处理逻辑：稠密向量侧用LLM生成的互补参考段落补全语义，提升长尾query的召回相关性；稀疏侧用原始query和扩展query的BM25分数乘积做锚定，不需要改动现有BM25索引架构，就能在不扩大召回集合的前提下优化排序，工程成本极低

  - 检索效果评估可参考完整列表融合+访问深度的双维度指标，避免仅依赖固定top-L的评估结果，防止截断值选择偏差导致的效果误判，尤其适合大流量搜索场景的效果&性能平衡评估

  - LLM生成参考段落的prompt设计可直接复用：要求输出保留原始query所有实体、约束、意图，仅变换表达方式的短段落，禁止扩展信息需求或编造答案，大幅降低生成噪声对检索的负面影响'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于LLM的查询扩展方法通常将生成内容同时应用到混合检索的稠密、稀疏通道，且仅在固定top-L截断下评估效果。但截断值会同时影响双渠道的召回范围和融合结果，单一截断下的效果增益可能在其他截断下反转；同时生成词会扩大稀疏检索的匹配集合，大幅增加索引访问成本，无法兼顾检索效果与执行效率。

### 方法关键点
- DESA（Dense Expansion and Sparse Anchoring）采用非对称查询扩展逻辑，基于同一组LLM生成的互补参考段落分别处理双渠道：
- 稠密侧采用正交残差扩展：保留原始query的向量方向，仅叠加参考段落带来的新增语义分量，保证扩展后的query向量与原始向量夹角不超过45度，避免语义漂移；
- 稀疏侧采用分数乘积锚定：分别计算原始query、扩展query（原始+参考段落）的BM25分数，二者乘积作为最终稀疏分数，仅保留原始query匹配的文档，避免生成词引入无关召回，同时可重排序原始匹配集合。

### 关键实验
在7个BEIR公开数据集上测试，对比原始查询、Shared扩展、HyDE、Query2doc、MuGI等基线，相对原始查询，nDCG@10提升3.82%，Recall@20提升2.38%，同时稠密、稀疏通道的访问深度分别降低36.90%、36.56%，63.31%的查询在双渠道的访问深度同时下降；对比同生成资源的QuDAR方法，效果无显著差异，但融合侧需要的条目数减少64.16%。

### 核心结论
混合检索的查询扩展要适配稠密、稀疏通道的匹配特性，做到稠密扩语义、稀疏保范围，才能同时提升效果和降低开销。
