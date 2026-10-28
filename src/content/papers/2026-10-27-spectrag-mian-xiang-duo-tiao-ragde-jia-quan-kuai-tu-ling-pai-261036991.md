---
title: 'SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop
  Retrieval-Augmented Generation'
title_zh: SpectRAG：面向多跳RAG的加权块图令牌预算上下文选择框架
authors:
- Zafer Sahinoglu
- Abdulazeez Mohammed
- Buse Yaren Kazangirler
- Cahit Berkay Kazangirler
affiliations:
- Mitsubishi Electric US
- Mitsubishi Electric Innovation Center (MELIC)
- Karabuk University
arxiv_id: '2610.36991'
url: https://arxiv.org/abs/2610.36991
pdf_url: https://arxiv.org/pdf/2610.36991
published: '2026-10-27'
collected: '2026-10-28'
category: RAG
direction: 多跳RAG · 图增强上下文检索优化
tags:
- RAG
- Multi-hop Reasoning
- GraphRAG
- Context Selection
- Spectral Graph
one_liner: 基于加权块图和谱传播的多跳RAG检索框架，以更低索引开销超越现有GraphRAG基线
practical_value: '- 可直接复用其token-budgeted上下文选择逻辑，替代固定top-k检索策略，按LLM上下文窗口配额动态选chunk，最大化窗口利用率，适合电商导购、售后客服等Agent的RAG场景

  - 加权块图的多信号边融合方法可迁移到业务场景，除语义相似度外，可新增商品类目层级、用户浏览路径、同单共现等业务特有边信号，提升跨商品多跳检索的召回准确率

  - 相比LightRAG依赖LLM做实体抽取的方案，SpectRAG的chunk级图构建无需额外实体抽取步骤，索引开销最高降低6倍，适合中小规模业务知识库快速落地GraphRAG'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统top-k稠密检索存在三大缺陷：易返回冗余chunk浪费有限上下文窗口、遗漏多跳推理所需的桥接证据、完全忽略文档层级、实体关联、引用关系等结构信息，无法满足需要跨多段、多文档证据的复杂推理场景；而现有GraphRAG方案大多依赖LLM做实体抽取，索引构建成本高、存储开销大，落地门槛高。
### 方法关键点
- 离线阶段构建加权chunk图，边权重融合6类互补信号：语义相似度、同文档相邻关系、章节层级归属、共享实体、LLM生成的chunk可回答效用问题相似度、引用/超链接关系，再基于归一化图拉普拉斯计算每个chunk的32维谱坐标，编码其在图社区中的结构位置
- 在线检索阶段先用RRF融合稠密检索、BM25、效用问题匹配结果得到高召回种子集，再通过2跳BFS扩展到最多200个候选chunk
- 结合谱空间相似度、个性化PageRank对候选重打分，最后在固定token预算约束下，综合相关性、图 proximity、簇覆盖率、文档覆盖率、冗余惩罚选择最终上下文，优先保留高置信核心证据，剩余配额回填补充信息
### 关键实验
在MultiHopRAG、UltraDomain等多跳/长文档QA数据集上，对比NaiveRAG、LightRAG、HyDeRAG等基线：
- 索引开销比LightRAG低6倍（MultiHopRAG数据集上仅46MB vs 274MB），节点数减少2.8~6.6倍，推理速度更快
- MultiHopRAG数据集上Recall@5达65.2，比LightRAG高15.7个百分点；EM达72.0，比NaiveRAG高6.8个百分点；MRR达70.4，比LightRAG高8.9个百分点
-  pairwise对比NaiveRAG，生成答案的多样性维度赢率达55%
### 核心结论
RAG检索的核心目标不是召回单条最相关的chunk，而是在有限token预算下，构建一个相关、多样、结构连通、足以支撑推理的上下文集合，最大化整体效用。
