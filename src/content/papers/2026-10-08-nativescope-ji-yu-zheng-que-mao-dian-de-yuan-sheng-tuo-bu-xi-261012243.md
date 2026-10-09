---
title: 'NativeScope: Relation-Localized Retrieval over Native Topology with a Correct
  Anchor'
title_zh: NativeScope：基于正确锚点的原生拓扑关系局部检索
authors:
- Long Wang
arxiv_id: '2610.12243'
url: https://arxiv.org/abs/2610.12243
pdf_url: https://arxiv.org/pdf/2610.12243
published: '2026-10-08'
collected: '2026-10-09'
category: RAG
direction: RAG 关系约束检索效率优化
tags:
- RAG
- Dense Retrieval
- Long Context
- Memory System
- Relational Retrieval
one_liner: 提出先基于锚点和原生拓扑限定检索范围再排序的RAG方法，大幅提升固定预算下召回
practical_value: '- 电商商品问答、广告文案检索场景可复用「先锚定范围再排序」逻辑：比如用户查询某商品保修政策时，先锚定到「售后服务」章节做范围内检索，既提升召回准确率，又降低token消耗，提升LLM回答质量

  - Agent长时会话记忆检索可直接复用3种原生关系算子：用户提到「上一轮说的退换货规则」时，用before算子锚定对应对话轮，检索前后N轮内容，无需遍历全会话，大幅降低检索延迟

  - 上线必须增加锚点置信度兜底策略：当上游锚点识别置信度低于阈值时，自动回退到全量Dense RAG，避免硬过滤导致目标内容被排除，实验显示自动锚点下记忆域召回仅35.50%，远低于全量检索的50.50%

  - 范围内排序无需额外改造：完整query排序的NS-FullQ与目标词排序的NativeScope效果无统计显著差异，直接复用现有语义排序逻辑即可，无需额外做query拆分，降低落地成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Dense RAG将文本视为扁平结构做全局语义匹配，忽略数据原生的章节归属、会话边界、内容顺序等结构信息，固定token预算下易召回大量无关内容，对带位置约束的查询（如某章节内的信息、某对话轮之前的内容）检索效率极低。

### 方法关键点
- 将带锚点的关系查询拆解为(A, r, B)三元组：A为锚点坐标，r为原生关系算子，B为目标检索内容
- 预设3种可直接落地的关系算子：belonging（锚点所属同一容器，如同章节、同会话）、before/after（锚点前后最多8个原生单元，如前后8个段落、8轮对话）
- 先通过关系算子筛选符合条件的原生单元，映射到对应文本chunk后，仅在限定范围内做语义排序，固定token预算为1024
- 两个变体：NativeScope用目标词B排序，NS-FullQ用完整query排序，共用同一套范围筛选逻辑

### 关键实验
- 数据集：基于QASPER构造100条文档域查询，基于LongMemEval构造100条记忆域查询，共200条受控样本
- 对比baseline：全量Dense RAG、锚点±8单元的固定窗口检索
- 核心结果：正确锚点下，NativeScope在文档域召回达89.28%，较全量Dense RAG提升42.75pct；记忆域召回达72.50%，提升22.00pct；NS-FullQ与NativeScope效果无统计显著差异；自动Top-1锚点下记忆域召回暴跌至35.50%，低于全量Dense RAG的50.50%

### 核心结论
只要能获取可靠的锚点坐标和原生结构关系，先做范围硬过滤再做语义排序的收益远高于优化排序逻辑本身，锚点准确率不足时必须回退全量检索
