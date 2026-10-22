---
title: 'SOAR: Social and Opinion-Aware Recommendations'
title_zh: SOAR：融合社交与评论观点的POI推荐模型
authors:
- Giannis Christoforidis
- Apostolos N. Papadopoulos
affiliations:
- Aristotle University of Thessaloniki
arxiv_id: '2610.29556'
url: https://arxiv.org/abs/2610.29556
pdf_url: https://arxiv.org/pdf/2610.29556
published: '2026-10-21'
collected: '2026-10-22'
category: RecSys
direction: POI推荐 · 社交+评论情感融合
tags:
- POI Recommendation
- Sentiment Analysis
- Graph Embedding
- Social Network
- Review Mining
one_liner: 融合用户社交关系、评论语义与情感信号，提升POI推荐的个性化精度
practical_value: '- 可复用排序trick：采用「基础推荐分 + 好友信号加权偏移」的逻辑，将好友评论正向占比乘以基础分的标准差叠加到原得分，既保留全局排序的合理性，又强化社交个性化，可直接迁移到社交电商、本地生活推荐场景

  - 低成本语义落地流程：中小业务场景可直接复用「轻量SBERT生成评论嵌入 + Faiss聚类关联相似内容」的方案，不需要复杂的大模型微调，平衡计算成本与语义表征效果

  - 社交关系边界结论：业务中仅需采集1层好友关系即可拿到最优社交推荐效果，扩展至2-hop好友会带来8倍左右的性能损耗，同时稀释个性化信号，收益为负'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
传统POI推荐仅依赖用户-位置签到数据，忽略社交关系、评论语义与情感等强个性化信号，公共口碑与用户好友的评价往往存在显著差异，无法适配用户的个性化偏好，尤其无法捕捉用户对POI特定维度的好恶，导致推荐准确率低、个性化不足。

## 方法关键点
- 语义表征：采用SBERT轻量预训练模型（all-MiniLM-L6-v2）生成评论语义嵌入，通过Faiss构建相似评论关联图，捕捉不同POI的共性特征
- 情感计算：调用DistilBERT预训练情感分类模型对评论做二分类标注，区分正负向评价
- 多图融合：合并用户社交图、用户-POI签到图、评论相似图为统一异构图，采用RandNE算法生成节点的统一嵌入表示
- 个性化排序：基础排序分由用户嵌入与POI嵌入的内积计算，再叠加好友评论正向占比的加权偏移（权重为基础分的标准差），平衡全局流行度与社交个性化信号

## 关键实验
在Yelp公开数据集（700万+评论、15万+POI、用户平均10个好友）上测试，对比未融合社交与评论信号的基线模型：Top-1准确率提升4.09pct，Top-5准确率提升4.13pct，Top-10准确率提升8.17pct；仅用1层好友关系的版本相比2-hop（好友的好友）版本推理速度提升7.6倍，效果无明显下降。

## 核心结论
用户好友的评价权重远高于公共口碑，加入多跳社交关系不仅不会提升推荐效果，还会带来显著的性能损耗，业务中无需扩展多跳社交关系做推荐。
