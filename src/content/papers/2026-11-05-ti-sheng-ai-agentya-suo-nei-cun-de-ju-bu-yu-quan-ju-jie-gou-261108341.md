---
title: Enhancing Local and Global Structure in Compressed AI Agent Memory
title_zh: 提升AI Agent压缩内存的局部与全局结构保留能力
authors:
- Henry Han
affiliations:
- Baylor University
arxiv_id: '2611.08341'
url: https://arxiv.org/abs/2611.08341
pdf_url: https://arxiv.org/pdf/2611.08341
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 记忆压缩与结构保留优化
tags:
- AgentMemory
- VectorQuantization
- EmbeddingCompression
- ProductQuantization
- StructurePreservation
one_liner: 提出无监督局部感知量化LAQ，同压缩率下同时保留Agent内存的近邻检索精度与全局主题结构
practical_value: '- 做Agent长记忆/用户行为记忆存储时，可引入L（局部保真度）、G（全局保真度）作为无标签压缩效果评估指标，无需下游任务标注即可同时衡量近邻检索、主题聚类/会话删除等全局操作的准确性，避免仅优化recall@10导致的全局结构崩坏

  - 现有OPQ向量索引可直接替换为LAQ量化索引，无需修改存储大小、检索链路，即可提升全局主题聚类、用户分层、会话级记忆删除的准确率，适配电商客服Agent、用户长兴趣建模等场景

  - 向量压缩优化时，可在原有近邻损失基础上补充远邻交叉对的hinge loss约束，能在几乎不损失近邻召回的前提下，大幅降低跨类别/主题的向量漂移，适合需要做商品聚类、兴趣群体划分的推荐场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前AI Agent依赖embedding向量存储记忆，大规模场景下必须压缩，但现有方案仅优化近邻检索精度（如recall@10），会严重破坏全局结构：96字节/段落的重打分二值码recall@10可达0.97，但10.1%的段落会漂移到错误主题，无法满足记忆合并、批量删除、主题映射等依赖全局距离关系的操作，且缺乏无标签的全局压缩效果评估方法。
### 方法关键点
1. 定义两个无标签保真度：局部保真度L是chance-corrected recall@10，衡量近邻保留效果；全局保真度G是30%-50%邻域的一致性平均值，衡量全局结构保留效果，仅需采样2000个样本即可估算，不受内存规模限制。
2. 证明1-ν_k（不同规模邻域的保留率）上界与远近交叉对的秩违反率平方根成正比，以此构造hinge损失，在标准OPQ量化基础上优化远邻交叉对的顺序保留。
3. 提出的LAQ量化仅修改OPQ码本，不改变PCA基、旋转矩阵、存储大小、检索逻辑，完全兼容现有OPQ查询链路，无额外推理开销。
### 关键实验结果
在FinQA、LoCoMo、Multi-Doc-2025、FinDER等4个记忆数据集测试：
- 52个所有held-out运行中LAQ的G均高于基线OPQ，提升幅度0.005~0.038；L在46个运行中更高，剩余6个L损失不超过0.0023。
- 128字节/段落配置下，OPQ有8.3%的段落漂移到错误主题，LAQ仅3.5%，主题一致性从0.80提升到0.91；12个Multi-Doc-2025运行中LAQ的G为7个同大小量化器最高。
- 可扩展到百万级段落，一次训练仅需175秒，证据召回率与OPQ无统计差异（p=0.84）。
### 核心结论
向量压缩不能只优化近邻召回，全局结构保留由远邻的相对顺序决定，可通过无监督优化在几乎不损失近邻精度的前提下大幅提升。
