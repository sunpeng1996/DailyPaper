---
title: Robustness of IR Models to Collection Growth
title_zh: 信息检索模型针对文档集合增长的鲁棒性研究
authors:
- Emmanouil Georgios Lionis
- Debasis Ganguly
- Sean MacAvaney
affiliations:
- University of Glasgow
arxiv_id: '2608.23419'
url: https://arxiv.org/abs/2608.23419
pdf_url: https://arxiv.org/pdf/2608.23419
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: 检索召回 · 集合增长鲁棒性
tags:
- Information Retrieval
- Robustness
- Dense Retrieval
- Reranking
- Collection Growth
one_liner: 提出集合增长公理与MDA/MDD分类，实测各类IR模型在非相关文档新增时的鲁棒性差异
practical_value: '- 第一阶段召回优先选择MDA类模型（如SPLADE、RetroMAE），相比BM25、CDE这类MDD模型，非相关文档新增时性能下降最多可降低70%，适配电商商品库持续扩充的场景

  - 重排序阶段MDA（如pointwise Cross Encoder）和MDD（如listwise重排器）性能差异极小，可优先选择延迟更低的方案，无需为鲁棒性额外调整重排架构

  - 谨慎上线PRF类模块，其会偏向占比更高的主体集合内容，对长尾垂类query的召回效果损伤明显，若要上线需针对垂类做针对性调优

  - 业务上如果存在小体量垂类内容库，可以考虑拆分索引分库检索，避免全库检索时MDD模型的统计偏差导致垂类内容召回率下降'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生产环境的文档/商品集合永远是动态增长的，新增大量非相关内容时，理想的检索系统对原有query的效果不应出现明显下降，但目前业界缺乏对该问题的系统性评估框架和结论，传统IR鲁棒性研究多聚焦跨域、对抗样本等场景，未针对非相关文档新增的场景做针对性分析。

### 方法关键点
- 提出集合增长（CG）公理，定义新增非相关文档时，原有query的检索效果下降幅度需小于阈值ϵ才算满足鲁棒性，新增CP@10指标衡量top-k结果中原集合内容的占比
- 提出MDA/MDD分类体系：MDA（多文档无关）模型独立计算每个query-doc的相关性，不依赖集合统计或其他文档信息，包括bi-encoder、pointwise cross encoder等；MDD（多文档相关）模型依赖集合统计、其他文档内容或top-k候选上下文，包括BM25、listwise重排、PRF、CDE等
- 实验构造无主题重叠的混合测试集：将MS MARCO（8.8M文档）和TREC-COVID（171K文档，占比1.9%）合并，分别测试两类query在单库和混合库下的效果差异

### 关键结果
- 第一阶段召回：MDA模型（SPLADE、RetroMAE）在混合库下效果下降幅度比MDD模型（BM25、CDE）低70%左右，TREC-COVID垂类query的nDCG@10下降仅1.9%-4.8%，而BM25下降达22%
- 重排序阶段：MDA和MDD重排器的效果下降幅度几乎一致，差异小于0.5%，MDD重排器甚至在主体集合query上有小幅效果提升
- PRF类模块会加剧效果下降，垂类query的CP@10最高下降2个百分点，明显偏向占比更高的主体集合

**最值得记住的结论**：电商/搜索场景下持续扩充内容库时，第一阶段召回用MDA模型、重排按需选择、谨慎使用PRF，是兼顾效果和鲁棒性的最优选择。
