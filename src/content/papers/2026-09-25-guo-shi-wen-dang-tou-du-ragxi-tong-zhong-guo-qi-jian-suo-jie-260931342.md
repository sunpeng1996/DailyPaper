---
title: 'Stale-Document Poisoning: When Outdated Retrieval Overrides Correct Model
  Answers'
title_zh: 过时文档投毒：RAG系统中过期检索结果覆盖模型正确答案的风险
authors:
- Md Shamim Ahmed
- Lukas Galke Poech
- Richard Röttger
affiliations:
- University of Southern Denmark
arxiv_id: '2609.31342'
url: https://arxiv.org/abs/2609.31342
pdf_url: https://arxiv.org/pdf/2609.31342
published: '2026-09-25'
collected: '2026-09-28'
category: RAG
direction: RAG 过时文档投毒风险与缓解
tags:
- RAG
- Temporal_Validity
- Stale_Poisoning
- Knowledge_Conflict
- Hybrid_Reranker
one_liner: 构建跨4领域的知识反转基准，揭示RAG过时文档投毒机制并验证时效感知方案的缓解效果
practical_value: '- 电商/政策类RAG系统不要仅靠文档发布时间排序，需给所有动态更新的知识（活动规则、商品参数、平台政策）标注明确的生效/失效时间边界，70B+大模型可精准识别该边界，大幅降低过时信息输出率

  - RAG重排模块可复用论文的混合重排思路，在语义相似度特征基础上叠加时效性元特征，在日期准确的场景下可降4~10个百分点的错误率，尤其适合促销规则、商品迭代这类更新频繁的场景

  - 设计RAG prompt时不要强制要求模型完全服从检索结果，需预留时效性校验逻辑，否则过时信息导致的错误率会提升2倍以上'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG原本用于解决LLM参数知识过时的痛点，但检索到的外部文档本身可能已失效，这种非恶意的过时文档会覆盖LLM原本正确的答案，该风险此前未被系统量化，仅靠发布时间排序的传统RAG无法有效规避。
### 方法关键点
- 构建317条经官方来源验证的知识反转基准，覆盖医疗、法律、软件、平台政策4领域，每条标注明确的生效/失效时间、新旧正确答案、对应官方文档
- 采用控制变量实验：固定文档内容仅变更查询时间，分离文档内容与时效性对结果的影响
- 测试两类缓解方案：给文档补充明确的有效性边界提示、采用语义相似度+时效性特征的混合重排
### 关键结果
- 无强制服从检索的指令时，过时文档可翻转30% Llama、37% Qwen的正确答案，新增服从指令后比例升至66%、75%，跨领域投毒率范围为17%-91%，而匹配的最新有效文档采纳率达97%-100%
- 仅标注文档发布日期时模型时效识别提升有限，若明确给出失效时间边界，70B/72B级大模型可100%正确切换对应答案
- 时效感知混合重排在日期元数据准确的场景下，可降低4.6~10.0个百分点的投毒率

> 最值得记住的一句话：可靠的RAG需要选择性认知信任，不仅要判断检索内容是否相关，更要判断它是否仍然适用
