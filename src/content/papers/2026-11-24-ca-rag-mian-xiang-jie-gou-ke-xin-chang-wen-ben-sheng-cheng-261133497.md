---
title: 'CA-RAG: Constraint-Aligned Retrieval for Structurally Faithful Long-Form Generation'
title_zh: CA-RAG：面向结构可信长文本生成的约束对齐检索框架
authors:
- Vimal Kumar Kumar
- Meghana Kshirsagar
- Conor Ryan
affiliations:
- Lero – The Research Ireland Centre for Software
- University of Limerick
arxiv_id: '2611.33497'
url: https://arxiv.org/abs/2611.33497
pdf_url: https://arxiv.org/pdf/2611.33497
published: '2026-11-24'
collected: '2026-11-26'
category: RAG
direction: 检索增强生成 · 结构化约束对齐
tags:
- RAG
- Long-Form Generation
- Structural Alignment
- Knowledge Graph
- Ontology
one_liner: 将本体结构约束与政策KG依赖注入检索查询，提升合规长文本生成的结构完整性
practical_value: '- 电商/广告合规文案、用户协议、平台规则等长文本生成场景，可直接复用CA-RAG的检索前约束注入思路，在语义检索基础上叠加业务本体、规则KG的约束引导，避免必填条款遗漏

  - 复用其分层评估方案：先单独评测检索端的结构召回覆盖率，再评估生成端效果，可快速定位生成遗漏是检索证据缺失还是解码问题，降低排查成本

  - 分章节生成的设计可直接迁移到电商长文案生成场景，每个章节使用独立检索证据与约束，降低长上下文干扰，提升结构可控性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG仅基于语义相似度召回证据，在合同、合规报告、政策文案等强结构约束的长文本生成场景下，常遗漏必填的结构条款，导致生成内容合规性不足；传统方案仅在生成端注入约束，无法从根源解决检索阶段的证据缺失问题。
### 方法关键点
- 两阶段约束构造：先通过语义匹配从业务本体中召回对应章节的结构约束（如必填字段、章节属性），再从政策KG中召回关联的规则依赖（如REQUIRES、PROHIBITS类关系）
- 约束对齐查询构造：将本体约束、KG规则与原始查询拼接后再执行召回，从检索阶段引导证据向结构要求对齐，而非仅做语义扩展或重排序
- 分章节独立生成：每个章节使用专属的约束与召回证据，降低长上下文干扰，可选轻量RLHF优化文风一致性
### 关键实验结果
在教育、医疗、金融三个合规域，对比标准RAG、SELF-RAG、FLARE-RAG等基线，k=6时检索端Precision@k从0.5268提升至0.5692，pooled Recall@k从0.5402提升至0.5950，F1@k从0.5389提升至0.5672；生成端在9组模型-域配置中6组拿到最优可靠性，比仅在生成端注入约束的方案合规性高0.0043。
### 核心结论
合规类长文本生成的很多遗漏问题不是LLM解码能力不足，而是检索阶段就未获取到符合结构要求的证据，检索端做结构对齐比单纯生成端加约束更能从根源降低遗漏风险。
