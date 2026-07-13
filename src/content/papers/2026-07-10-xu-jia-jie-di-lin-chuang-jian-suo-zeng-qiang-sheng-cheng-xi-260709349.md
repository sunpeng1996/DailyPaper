---
title: 'Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented
  Generation'
title_zh: 虚假接地：临床检索增强生成系统中的实体归因失败
authors:
- Cedric Caruzzo
- Donggeun Yoo
- Tae Soo Kim
affiliations:
- Lunit
arxiv_id: '2607.09349'
url: https://arxiv.org/abs/2607.09349
pdf_url: https://arxiv.org/pdf/2607.09349
published: '2026-07-10'
collected: '2026-07-13'
category: RAG
direction: RAG评估 · 实体归因错误检测
tags:
- RAG
- Hallucination
- Entity Attribution
- Evaluation
- Clinical LLM
one_liner: 发现RAG系统中现有评估无法检测的实体归因错误类型虚假接地，给出检测方案与生产场景发生率
practical_value: '- 电商/广告RAG场景（商品问答、营销文案生成）可新增实体归因校验步骤，验证生成内容的商品属性/活动规则是否匹配查询目标实体，避免A商品的参数/优惠套用到B商品上，尤其适配新品、长尾商品等召回内容稀疏的场景

  - RAG召回阶段优先实现实体级过滤，确保召回内容的核心实体与查询实体匹配，而非仅做语义相似度匹配，可大幅降低虚假接地风险，完整的目标实体召回能将DG率压制到6.4%以下

  - 现有RAG评估体系（如RAGAS）需补充实体归因维度校验，现有校验仅能检测无依据幻觉、内容与召回文档不一致问题，无法识别跨实体内容错配的结构性盲区，该问题在所有垂直领域均存在'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG评估仅校验生成内容是否与召回文档一致、是否有真实引用，完全未检查内容对应的实体是否与查询实体匹配，会出现把B实体的真实证据套到查询A实体上的错误，这类错误能通过所有现有自动化校验，在临床等高风险场景危害极大，此前无系统研究。

### 方法关键点
- 定义**Deceptive Grounding（DG，虚假接地）**：生成内容所有事实均来自召回文档，但全部归属于错误实体，不属于传统幻觉或一致性错误
- 设计2D因子基准测试，控制查询实体召回完整性、非目标实体召回内容的完整度两个变量，覆盖13个通用/医疗领域LLM
- 提出**Entity-Attribution Verification（EAV，实体归因校验）**方案：逐claim核对支撑文档的核心实体是否与查询实体一致

### 关键实验结果
- 对抗场景下13个模型DG率跨度8%~87%，医疗微调模型最高达86.7%，领域微调反而放大该问题
- 真实生产的临床RAG系统整体DG率7.8%，新获批药品（召回内容稀疏）DG率达13.6%
- EAV检测DG的精度97.0%、召回率98.7%，无现有评估框架支持该校验

### 核心结论
RAG系统的生成内容可以同时做到事实准确、有真实引用、完全符合召回文档，但在实体层面完全错误，现有评估框架存在结构性盲区。
