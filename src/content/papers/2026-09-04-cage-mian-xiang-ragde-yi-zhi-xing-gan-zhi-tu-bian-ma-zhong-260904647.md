---
title: 'CAGE: Coherence-Aware Graph Encoding for Retrieval-Augmented Generation'
title_zh: CAGE：面向RAG的一致性感知图编码重排框架
authors:
- Tong Qi
- Jingyu Wu
- Youbing Yin
- Spencer Hong
- Daben Liu
- Erin Babinsky
affiliations:
- Capital One
- General Intelligence Company
arxiv_id: '2609.04647'
url: https://arxiv.org/abs/2609.04647
pdf_url: https://arxiv.org/pdf/2609.04647
published: '2026-09-04'
collected: '2026-09-07'
category: RAG
direction: RAG优化 · 跨chunk一致性感知重排
tags:
- RAG
- Reranking
- GNN
- R-GCN
- Multi-hop QA
- Information Retrieval
one_liner: 将RAG召回chunk转化为异构图，建模四维度跨块一致性实现重排，提升多任务下游生成效果
practical_value: '- 电商商品问答、客服Agent的RAG系统可直接复用CAGE重排逻辑，将召回的商品参数、历史话术、售后规则等chunk构建为异构图，过滤矛盾、跨域干扰内容，避免给用户输出冲突的商品信息或服务规则

  - 多跳推理类搜索/推荐场景（如用户查询"适合玩3A游戏的联想笔记本配套的氮化镓电源功率"）可复用四维度一致性框架，优先保留具备完整推理桥接链的chunk，提升答案准确率

  - 工程实现上可复用min-out-degree加权trick，强化具体实体、数值类事实锚点的权重；单query级小图训练收敛速度<1s/query，无需全局预训练，适配低延迟在线业务要求

  - 若业务场景存在大量对抗性错误信息（如竞品恶意篡改的参数、谣言内容），可在CAGE基础上补充NLI事实校验模块，解决结构相似但事实矛盾的chunk识别问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统RAG的检索、重排阶段均独立对单chunk打分，召回的top-k集合常出现单条内容相关但整体逻辑矛盾、缺少推理桥接节点、混入跨域干扰项等问题，直接限制下游生成质量，尤其在多跳推理场景下，需跨chunk的逻辑关联才能得到正确答案，现有方法未显式建模跨chunk的一致性。
### 方法关键点
- 跨chunk一致性拆解为4个可量化维度：域内相关性、抗噪性、信息连通性、事实一致性
- 核心pipeline：1）将每个召回chunk解析为有向异构图，节点为指代消解后的实体/内容词，边为依存句法关系；2）min-out-degree重加权，放大低出度的具体实体、数值等事实锚点的权重；3）单隐层R-GCN编码，加入多样性正则避免表示坍缩，得到每个chunk的图级嵌入；4）融合query-chunk语义相似度与跨chunk结构相似度得到最终打分，完成重排
### 关键实验
在HotpotQA、2WikiMultihopQA、MuSiQue、RAMDocs四个多跳QA基准上对比monoT5、ColBERTv2、HyperGraphRAG等SOTA基线：Recall@5在2WikiMultihopQA达85.4，超Vanilla RAG 5个点；HotpotQA上Recall@5达84.2持平monoT5；下游生成Exact Match在HotpotQA上超Vanilla RAG 4.4个百分点，桥接型问题提升最显著。
### 核心结论
RAG的召回效果上限并非单chunk的相关性，而是召回集合的整体结构一致性和逻辑完整性，跨chunk一致性是比单chunk相关性更重要的下游生成准确率影响因素
