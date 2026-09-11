---
title: 'TimelyRAG: Semantic-Temporal Hybrid Retrieval for Time-Critical Question Answering
  in Overlapping-Evolving Documents'
title_zh: TimelyRAG：面向重叠演化文档时间敏感问答的语义时序混合检索
authors:
- Youngeun Nam
- Joeun Kim
- Hwanjun Song
- Susik Yoon
- Jae-Gil Lee
- Byung Suk Lee
affiliations:
- KAIST
- Korea University
- University of Vermont
arxiv_id: '2609.11572'
url: https://arxiv.org/abs/2609.11572
pdf_url: https://arxiv.org/pdf/2609.11572
published: '2026-09-10'
collected: '2026-09-11'
category: RAG
direction: 时间感知RAG · 时序重排优化
tags:
- RAG
- Temporal Retrieval
- Time-sensitive QA
- Reranking
- Benchmark
one_liner: 提出检索器无关的语义时序混合RAG框架与首个重叠演化监管QA基准，最高提升nDCG@10达28.6%
practical_value: '- 电商/客服场景的规则、商品售后、促销政策等迭代型知识库可直接复用两阶段检索逻辑，在现有召回层后加轻量时序重排，无需修改原有召回底座，即可解决多版本条款的时效匹配问题

  - 可直接套用自适应权重α(Q)的设计：带明确时间的query（如"2023年618的满减规则"）加大时序权重，无明确时间的query默认偏语义匹配，避免硬时效过滤误伤非时效需求，不影响通用场景效果

  - 工程落地开销极低，单query仅新增2ms左右CPU耗时，完全适配高QPS的线上搜索、智能客服场景，无需额外GPU资源

  - 构建内部时效知识库评测集时，可参考TimelyQABench的自动生成+多模型校验流程，快速生成高语义重叠的多版本规则QA对，降低人工标注成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有时间敏感RAG仅支持各版本完全独立的离散演化场景，而政策、规则、电商条款等多是重叠演化场景——大部分内容不变，仅局部条款迭代，语义相似度极高，传统检索要么拿最新版本但不匹配query对应的历史时效，要么召回语义相似但时效无效的版本，无法满足时间敏感问答的准确性要求，比如用户问2020年入学的毕业要求，召回2025年的版本就会答错。

### 方法关键点
- 两阶段检索架构，检索器无关：第一阶段用任意稀疏/稠密召回器得到Top-N候选，第二阶段做时序重排，不修改原有召回逻辑
- 时序兼容性计算：提取query的插入/事件时间、文档的插入/事件时间，计算query时间与文档条款有效区间的距离，落在有效区间内距离为0，否则随偏离程度递增，归一化后转成时序得分
- 自适应权重α(Q)：query含明确时间、时间粒度越细（比如精确到天），时序得分权重越高，否则默认偏语义得分，无时效query效果不受损
- 发布TimelyQABench：首个覆盖法律、校规、公司政策、服务条款4个监管领域的重叠演化QA基准，含1.2万条标注实例，文档语义重叠度达0.61-0.73，远高于现有时序QA数据集

### 关键实验结果
在自建TimelyQABench上对比BM25、BGE-M3等主流召回器，最高提升nDCG@10达28.6%、Hit@10达19.1%；在离散演化的TS-Retriever数据集上同样取得一致提升；在无时序需求的通用FiQA数据集上效果与基线完全持平；单query新增延迟仅2ms左右。

**最值得记住的一句话**：对于内容高重叠的迭代型文档场景，仅靠语义匹配无法解决时效准确性问题，轻量的clause级时序重排就能用极低开销带来显著效果提升
