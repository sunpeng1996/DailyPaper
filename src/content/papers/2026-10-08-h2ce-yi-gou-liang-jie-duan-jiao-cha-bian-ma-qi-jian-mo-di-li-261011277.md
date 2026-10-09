---
title: 'H2CE: Modeling Geo-Semantic Interactions for POI Reranking with Heterogeneous
  Two-Stage Cross-Encoders'
title_zh: H2CE：异构两阶段交叉编码器建模地理语义交互实现POI重排序
authors:
- Zhengwei Bai
- Moreno D'Incà
- Danielle Class
- Alessandro Moschitti
affiliations:
- Amazon
- University of Trento
arxiv_id: '2610.11277'
url: https://arxiv.org/abs/2610.11277
pdf_url: https://arxiv.org/pdf/2610.11277
published: '2026-10-08'
collected: '2026-10-09'
category: RecSys
direction: POI重排序 · 交叉编码器异构特征融合
tags:
- Cross-Encoder
- POI Reranking
- Learning to Rank
- Feature Fusion
- Two-Stage Ranking
one_liner: 提出异构双路编码+两阶段点对结合的POI重排框架，兼顾排序精度与实时推理性能
practical_value: '- 结构化数值特征处理可复用：将距离、评分、销量等数值特征做分桶语义化描述输入交叉编码器，同时保留原始数值输入专属MLP，兼顾语义关联与数值精度，适配电商多模态商品/POI重排场景

  - 两阶段重排架构可直接迁移：上游点wise模型全量打分过滤TopK候选，下游仅对TopK做pairwise对比+Copeland聚合，复杂度从O(N²)降到O(N+K²)，实测K=10时仅增加26%~60%
  latency就能提NDCG@5近2个百分点，平衡效果与性能

  - 训练优化技巧可复用：点wise训练采用多正负样本（单query16正16负）采样降低梯度方差，pairwise训练对齐推理分布仅采样TopK候选构造样本，减少无效训练提升泛化性

  - 半矩阵优化可落地：pairwise对比时仅计算K*(K-1)/2个无序对，反向结果用1-p补全，latency降26%的情况下效果损失不到0.3%，适合对时延要求高的线上服务'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
本地搜索POI重排需要同时权衡语义匹配、地理距离、评分、评论数等多源异构信号，传统XGBoost类LTR模型语义匹配能力弱，纯交叉编码器无法有效处理数值特征，全量pairwise/LLM重排时延过高无法满足线上实时服务要求，亟需兼顾精度与效率的异构重排方案。

### 方法关键点
- 异构特征编码器：双路处理数值特征，一路将距离、评分、评论数分桶为「步行可达」「优秀」等语义描述符拼入交叉编码器输入，支持语义-数值注意力交互；另一路将原始数值输入专属MLP保留精度，两路输出通过隐空间拼接聚合，替代传统加权和的晚融合，支持非线性特征交互
- 两阶段重排架构：Stage1用异构编码器对全量候选做点wise打分，选出TopK；Stage2仅对TopK做pairwise头对头对比，用Copeland聚合得到最终排序，复杂度从O(N²)降到O(N+K(K-1))
- 训练策略：点wise采用单query多正负样本采样降低梯度方差，pairwise仅采样TopK候选构造样本，对齐推理分布

### 关键实验
在5743条query的本地搜索测试集上，H2CE的NDCG@5达67.48%，比XGBoost LTR绝对提升22.82%，比零样本LLM重排提升35.89%，比微调BGE重排提升9.62%；pairwise阶段相比纯点wise模型NDCG@5提升1.98%；K=10时单A100中位数时延163ms，半矩阵优化后降到120ms，效果损失小于0.3%。

### 核心结论
多源异构特征的双路编码+有限TopK的pairwise对比，是兼顾重排精度与线上时延的高效落地路径。
