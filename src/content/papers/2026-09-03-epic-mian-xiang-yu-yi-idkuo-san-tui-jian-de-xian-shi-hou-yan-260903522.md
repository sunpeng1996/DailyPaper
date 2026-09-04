---
title: 'EPIC: Explicit Posterior Item Conditioning for Semantic ID Diffusion Recommendation'
title_zh: EPIC：面向语义ID扩散推荐的显式后验物品条件建模
authors:
- Tuan-Binh Tran
- Thanh Tam Nguyen
- Quoc Viet Hung Nguyen
- Dung D. Le
- Tung Kieu
- Thanh Trung Huynh
affiliations:
- VinUniversity
- Griffith University
- Aalborg University
arxiv_id: '2609.03522'
url: https://arxiv.org/abs/2609.03522
pdf_url: https://arxiv.org/pdf/2609.03522
published: '2026-09-03'
collected: '2026-09-04'
category: GenRec
direction: 生成式推荐 · Semantic ID 扩散优化
tags:
- Semantic ID
- Generative Recommendation
- Diffusion Model
- Sequential Recommendation
- Item-level Modeling
one_liner: 为语义ID扩散推荐引入显式物品级竞争，冻结预训练backbone即可稳定提升效果
practical_value: '- 可直接复用加性轻量化设计，冻结现有Semantic ID生成式推荐backbone，仅新增0.4M级别的物品级适配模块即可提升效果，无需全量重训，上线成本极低

  - 借鉴去噪过程中实时构造可行候选集+个性化后验反馈的思路，替换传统生成SID后再重排的流程，可召回被token级生成过早剪枝的高 relevance 候选，尤其适配长尾物品推荐场景

  - 工程上可通过SID倒排索引加速可行候选集检索，无需全量扫库，同时可根据业务延迟要求调整SID解析的位置数，在精度和耗时之间灵活trade-off'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Semantic ID扩散推荐仅在token级别做去噪决策，局部看似合理的token生成可能过早排除符合用户偏好的物品，且被排除的物品无法通过后续重排恢复，存在token-物品推理gap，导致推荐精度受损。

### 方法关键点
- 每步去噪时根据已解析的SID位置构造可行候选集，结合用户历史交互给候选集物品打分，得到显式个性化物品后验分布
- 将物品后验分布边缘化到未解析的SID位置，通过歧义感知门控和token级预测结果残差融合，引导后续token生成
- 仅训练新增的物品级适配模块，预训练扩散backbone完全冻结，无需额外的backbone前向传播，计算开销低

### 关键实验
在4个Amazon公开数据集（Beauty、Sports、Toys、Musical）上对比10+主流基线，在16组指标（Recall@5/10、NDCG@5/10）上全部取得最优，相对次优方法的NDCG@5最高提升16.8%，NDCG@10最高提升14.1%；仅需微调0.39M参数，比全量微调参数量减少94.3%，推理延迟仅增加34%。

### 核心结论
对于Semantic ID生成式推荐，在去噪过程中引入物品级偏好指导，比生成完成后再做重排的收益高得多。
