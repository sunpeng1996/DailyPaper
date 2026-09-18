---
title: Beyond Similarity through Zero-Token Geometric Graphs for Multi-Hop RAG
title_zh: 基于零Token几何图的多跳RAG优化框架G3RAG
authors:
- Zeliang Li
- Xiaofen Xing
- Kailing Guo
- Xiangmin Xu
affiliations:
- South China University of Technology
- Foshan University
arxiv_id: '2609.19622'
url: https://arxiv.org/abs/2609.19622
pdf_url: https://arxiv.org/pdf/2609.19622
published: '2026-09-17'
collected: '2026-09-18'
category: RAG
direction: 多跳RAG · 零开销几何图构建
tags:
- RAG
- Multi-hop QA
- Graph Construction
- Zero Token
- Geometric Embedding
one_liner: 基于文档向量几何属性构建零Token开销的Graph RAG，平衡检索相关性与新颖性，提升多跳QA效果
practical_value: '- 电商客服/商品导购Agent的多跳RAG场景可直接复用零Token建图逻辑，省去LLM实体抽取的高额离线成本，同时规避实体抽取幻觉引入的噪声

  - 召回/相关推荐场景需平衡相关性与新颖性时，可直接用cosθ·sinθ作为关联边权重，替代纯余弦相似度排序，提升长尾优质内容的触达率

  - 可复用高密度hub抑制的trick：对热门/高相似度密度节点加指数衰减惩罚，避免检索/推荐结果陷入热门内容闭环，缓解信息茧房问题

  - 在线检索/推荐阶段可复用「高置信种子过滤+单步可控扩散」逻辑，相比多轮随机游走推理延迟降低70%以上，适配低延迟业务要求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多跳RAG需要平衡查询相关性与证据新颖性以弥合语义gap，现有方案存在两个核心痛点：纯稠密检索仅召回语义相似的同质内容，陷入「相似度陷阱」无法获取多跳关键证据；Graph RAG依赖LLM做实体抽取构建图谱，离线Token成本极高，且易召回无关内容陷入「新颖性陷阱」。
### 方法关键点
- 离线零Token建图：仅基于文档向量的几何属性构建纯文档节点图，边权重定义为cosθ·sinθ，同时量化向量方向一致性（相关性）与正交性（新颖性），仅保留相似度在[0.1, 0.7]区间的有效边
- 拓扑度惩罚：对全局相似密度高的hub节点施加指数衰减惩罚，将对称边转为有向转移边，引导检索流向长尾高信息增益节点扩散
- 在线可控扩散：先通过稠密检索+轻量LLM过滤得到高置信种子节点，仅执行单步矩阵乘法完成扩散，无需多轮随机游走，推理效率极高
### 关键结果
在MusiQue、2WikiMultiHopQA、HotpotQA三个多跳QA数据集上，对比Naive RAG、LightRAG、HippoRAG2等基线：平均F1较最强基线最高提升4.26个点，难度最高的MusiQue数据集上F1最高提升5.76个点，关键答案文档命中率平均领先3.5个点；建图零Token开销，相比HippoRAG2建图时间压缩90%，仅需24G GPU显存（同类Graph RAG需344G）。
### 核心洞见
平衡检索相关性与新颖性的本质是在向量空间寻找方向一致性与正交性的最优解，无需依赖LLM实体抽取即可实现高效多跳证据检索
