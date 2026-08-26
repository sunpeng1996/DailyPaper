---
title: 'AdaWidth: Query-Adaptive Embedding Width for Dense Retrieval'
title_zh: AdaWidth：面向稠密检索的查询自适应嵌入宽度方法
authors:
- Shubing Yang
- Dongfang Zhao
affiliations:
- University of Washington
arxiv_id: '2608.23862'
url: https://arxiv.org/abs/2608.23862
pdf_url: https://arxiv.org/pdf/2608.23862
published: '2026-08-24'
collected: '2026-08-26'
category: RecSys
direction: 稠密检索·查询自适应嵌入维度优化
tags:
- Dense Retrieval
- Embedding Compression
- Query Adaptive
- Orthogonal Transformation
- Efficient Retrieval
one_liner: 通过正交前缀适配器和查询级轻量路由，以更少嵌入维度实现SOTA稠密检索效果
practical_value: '- 电商搜索召回环节可直接复用正交前缀适配器方案：仅用少量参数对现有Embedding做正交旋转，把判别信号集中到前序维度，不改变原向量相似度，无精度损失风险，还能兼容现有前缀截断降维方案

  - 可借鉴轻量路由的设计思路：基于首阶段窄前缀排序的序统计特征（如top10和top11的分差、得分熵）判断是否需要升维重排，仅对难查询分配更多计算资源，平衡精度和latency

  - 理论结论可直接用于容量规划：所需嵌入维度随语料大小对数增长、随召回深度对数下降，可根据业务语量级、召回topK数提前预估所需维度，不用盲目上高维Embedding浪费存储和计算'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
高维Embedding是稠密检索的核心，但检索时无需计算所有维度，现有降维方案要么对所有查询统一截断前序维度、浪费简单查询的计算资源，要么为每个查询选择分散的维度子集、需要存储全量Embedding且读取效率低，而不同查询稳定排序所需的维度差异极大，统一维度会造成大量冗余计算。

### 方法关键点
- 正交前缀适配器：用Householder反射乘积构造正交变换矩阵，对查询和文档Embedding做相同旋转，将判别信号集中到前序维度，且不改变全维度下的内积，原编码器完全冻结，无需重训
- 轻量查询路由：先以固定窄前缀（如64维）做首次排序，提取排序结果的序统计特征（如top分差、得分熵等18维特征），用梯度提升树预测是否需要升维重排，仅对可能改变top10结果的查询使用更宽前缀
- 理论推导前缀充分性：所需维度随语料大小对数增长、随召回深度对数下降，符合实际观测的维度需求分布

### 关键结果数字
在6个检索任务（4个BEIR文本任务+2个VQA知识检索任务）、5个不同大小的冻结编码器上测试，对比前缀截断、Matryoshka Adaptor等基线，AdaWidth匹配SOTA的NDCG@10时，每个查询的维度用量减少55%~84%；64维下的效果超过Matryoshka Adaptor 256维的效果，适配器仅需1万~20万参数，远低于基线方案。

最值得记住的一句话：不同查询的检索难度差异极大，把信号集中到前缀、按查询难度动态分配维度，是比统一降维效率高得多的稠密检索优化方案
