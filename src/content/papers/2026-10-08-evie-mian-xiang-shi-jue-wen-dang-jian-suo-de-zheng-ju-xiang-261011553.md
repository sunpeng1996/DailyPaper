---
title: 'EVIE: Evidence-Vector-Informed Embeddings for Visual Document Retrieval'
title_zh: EVIE：面向视觉文档检索的证据向量感知嵌入框架
authors:
- Zifei Wang
- Wei Wen
- Qiang Ji
- Qian-Wen Zhang
- Ruizhi Qiao
- Xing Sun
affiliations:
- Tencent IMA Product Center
- Tencent Youtu Lab
arxiv_id: '2610.11553'
url: https://arxiv.org/abs/2610.11553
pdf_url: https://arxiv.org/pdf/2610.11553
published: '2026-10-08'
collected: '2026-10-09'
category: RAG
direction: 多模态RAG · 视觉文档检索优化
tags:
- Visual Document Retrieval
- Multi-modal RAG
- Matryoshka Representation Learning
- Index Compression
- Knowledge Distillation
- MaxSim
one_liner: 融合证据感知监督、嵌套嵌入与压缩索引，优化视觉文档检索精度-存储平衡
practical_value: '- 训练阶段证据判定数据治理可复用：用多模态judge对召回候选打标，全证据样本扩为正例、部分证据样本排除出负损失，可过滤14.4%的无效监督信号，适合电商商品海报、详情页等多模态检索场景的训练数据优化

  - Prefix-MRL嵌套嵌入训练可直接迁移：一次训练得到64~2048共6种维度的嵌入，无需重新编码，可根据业务存储预算灵活选择维度，适配不同规模的向量检索库部署

  - HAC索引压缩方案可落地：结合空间正则的层级聚类压缩页token，存储语义质心直接支持MaxSim单阶段检索，128倍压缩下仅损失不到5个点的nDCG@10，适合C端低延迟多模态检索场景

  - 资源受限场景的参数选择结论可复用：同存储预算下优先选择更多低维质心而非更少高维质心，nDCG@10可提升0.7个百分点以上，降低检索系统资源成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有视觉文档检索方案存在明显缺陷：OCR+文本检索链路丢失布局、图表关联等视觉信息，单向量多模态检索粒度不足匹配细粒度查询，多向量MaxSim检索则存在存储开销过高、训练监督噪声大的问题，无法同时满足高精度和低存储的部署需求，难以支撑电商、企业知识库等场景下的多模态文档（商品海报、财报、详情页）检索落地。

### 方法关键点
- 证据判定数据治理：用多模态judge对挖掘的候选打标，全证据样本扩为正例，部分证据样本排除出负损失，过滤14.4%的无效监督信号
- 双向师生蒸馏+Prefix-MRL：对称列表式蒸馏将8B教师的排序能力迁移到4.5B学生，嵌套Matryoshka表示学习让单个checkpoint支持6种维度的嵌入输出，无需重新编码
- HAC层级聚簇索引压缩：加入空间正则的聚类将页token压缩为K个语义质心，直接支持MaxSim单阶段检索，无需保留原始向量或重排序

### 关键结果
在138个任务的4个公开基准集上测试，EVIE-8B在ViDoRe V3上nDCG@10达66.75，超SOTA基线1.43个点；4.5B版本加HAC压缩后，在3.81GiB/百万页的存储下（比原始多向量索引压缩128倍），nDCG@10仍达59.58，同存储下超WeMM-9B基线2.16个点；7.63GiB存储下nDCG@10达62.06，超基线4.64个点。

**最值得记住的一句话**：多模态检索的精度-存储平衡优化，需同时从训练监督降噪、灵活表示学习、索引结构压缩三个维度协同发力，才能在可控资源下取得最优效果
