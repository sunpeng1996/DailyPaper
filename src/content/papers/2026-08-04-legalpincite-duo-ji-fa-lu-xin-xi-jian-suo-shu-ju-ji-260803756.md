---
title: 'LegalPincite: Multi-level Legal Information Retrieval Dataset'
title_zh: LegalPincite：多级法律信息检索数据集
authors:
- Theresia Veronika Rampisela
- Henrik Palmer Olsen
- Giovanni Colavizza
affiliations:
- University of Copenhagen
- Department of Communication, University of Copenhagen
- Faculty of Law, University of Copenhagen
arxiv_id: '2608.03756'
url: https://arxiv.org/abs/2608.03756
pdf_url: https://arxiv.org/pdf/2608.03756
published: '2026-08-04'
collected: '2026-08-08'
category: Other
direction: 法律信息检索 · 多粒度评测数据集构建
tags:
- Information Retrieval
- Legal AI
- Dataset Construction
- Multi-granularity Retrieval
- Evaluation Benchmark
one_liner: 发布无数据泄漏、带多级标注的大规模欧盟法院法律信息检索数据集
practical_value: '- 构建垂直领域RAG/检索系统时，可参考其mask查询中泄露信息的预处理方法，避免评测时性能虚高

  - 多粒度检索的评测范式可迁移到电商商品/评论/详情页的多粒度召回效果验证，支持段落到商品、段落到详情段落等多场景评测

  - 构建垂直领域检索数据集时，可复用其全量语料而非仅标注相关片段的思路，评测结果更贴近真实业务表现'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有公开法律IR数据集存在三类缺陷：缺少段落级引用标注、查询文本自带引用信息导致数据泄漏、语料仅保留含引用的段落，评测场景过度简化且不真实，易导致检索模型性能虚高，无法匹配真实法律场景下需精准定位到具体段落的pincite检索需求。
### 方法关键点
基于欧盟法院（CJEU）公开判决构建大规模多粒度法律IR数据集，核心设计包括：
1. 对查询做引用信息mask处理，消除数据泄漏；
2. 语料保留所有段落而非仅含引用的片段，贴近真实检索场景；
3. 提供案例级、段落级双维度真值标注，部分标注经过法律专家验证。
### 关键结果
支持三类多粒度检索任务的开发与严谨评测：case-to-case、paragraph-to-case、paragraph-to-paragraph，数据集已开源至Hugging Face。
