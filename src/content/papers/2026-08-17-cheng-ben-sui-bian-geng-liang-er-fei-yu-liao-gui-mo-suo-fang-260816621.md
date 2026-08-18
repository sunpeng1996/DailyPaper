---
title: 'Cost Scales with Change, Not Corpus Size: Incrementally Maintaining an Evolving
  Semantic Substrate'
title_zh: 成本随变更量而非语料规模缩放：演化语义基底的增量维护方法
authors:
- Yusuke Takahashi
- Kyle Wild
- Asako Uraki
affiliations:
- Musashino University
- Asia AI Institute
- Endgame Labs, Inc.
arxiv_id: '2608.16621'
url: https://arxiv.org/abs/2608.16621
pdf_url: https://arxiv.org/pdf/2608.16621
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: RAG 语义索引增量维护
tags:
- RAG
- incremental SVD
- semantic substrate
- orthogonal Procrustes
- embedding migration
one_liner: 提出增量SVD+正交Procrustes的语义基底维护方案，成本仅和变更量挂钩而非语料规模
practical_value: '- 电商商品/内容向量库增量更新场景可复用增量低秩SVD方案，避免全量重算，大语料下运维成本可降20倍以上，尤其适合更新慢、查询多的业务场景

  - 升级embedding模型时无需全量重嵌，仅抽取10%左右代表性样本做正交Procrustes对齐，即可恢复0.95以上的余弦相似度一致性，大幅降低模型迭代成本

  - 高查询量的电商客服Agent、商品检索RAG系统可采用摄入时语义编译模式替代查询时语义重建，平摊计算成本，查询量超过盈亏平衡点时性价比显著更高

  - 语义基底的正交化设计可优化embedding各向异性问题，提升召回相似度准确性，可直接复用在现有召回的向量后处理环节'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前主流RAG与Agent问答系统普遍采用查询时语义重建（QSR）模式，每次查询都重复执行检索、语义解析步骤，计算成本随查询量线性增长，且一致性、可审计性差；摄入时预编译语义基底的方案虽能解决上述问题，但语料更新、embedding模型迭代时全量重算SVD/重嵌成本过高，长期被认为难以落地，亟需低成本的增量维护方案。

### 方法关键点
- 定义语义基底为语料embedding矩阵截断SVD后的top-k右奇异向量正交基，查询仅需将query投影到该基底后计算余弦相似度，成本远低于QSR
- 语料新增/修改时采用增量低秩SVD更新，仅依赖变更数据，复杂度与语料规模无关，定期重正交化控制基底漂移
- embedding模型升级时，仅取少量锚点样本分别用新旧模型嵌入，求解正交Procrustes问题得到旋转矩阵，直接将旧基底对齐到新空间，无需全量重嵌
- 给出语义编译模式相对QSR的盈亏平衡点计算公式，可根据业务的语料规模、更新频率、查询量判断是否适用

### 关键实验
基于合成数据集（维度256，秩32，语料从3k增长到9k共50次更新）对比全量重SVD基线：单更新成本低33.7倍，累计成本低23.8倍，主角度漂移低于10⁻¹¹度，recall@10保持1.0；embedding模型迁移场景下，仅重嵌10%语料即可恢复0.95的平均余弦相似度。

### 核心结论
语义基底的维护成本仅和变更量挂钩，和语料规模无关，大而稳定的语料采用增量维护方案性价比极高。
