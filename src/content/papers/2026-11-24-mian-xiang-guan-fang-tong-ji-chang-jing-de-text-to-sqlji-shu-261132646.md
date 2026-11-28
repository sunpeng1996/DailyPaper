---
title: A Text-to-SQL Benchmark for Official Statistics
title_zh: 面向官方统计场景的Text-to-SQL基准数据集
authors:
- Lucas Lageweg
- Karen Goes
- Tom van den Broek
- Frank Pijpers
- Paul Groth
- Jan-Christoph Kalo
affiliations:
- University of Amsterdam
- Statistics Netherlands
arxiv_id: '2611.32646'
url: https://arxiv.org/abs/2611.32646
pdf_url: https://arxiv.org/pdf/2611.32646
published: '2026-11-24'
collected: '2026-11-28'
category: Eval
direction: 大模型文本转SQL · 评估基准构建
tags:
- text-to-SQL
- benchmark
- knowledge graph
- LLM evaluation
- multilingual
one_liner: 构建适配官方统计宽表+元数据KG场景的LOCuST文本转SQL基准及评估指标
practical_value: '- 业务端自然语言转数仓查询（如运营自助查经营数据）场景，可借鉴将表元数据、维度编码语义结构化存入KG，作为RAG的外部知识源，提升text-to-SQL准确率

  - 评估text-to-SQL效果时可复用observation F1思路，不单纯校验返回结果对错，而是匹配查询逻辑与真值的重合度，更合理评估模型能力

  - 多语言数据查询场景可参考LOCuST的双语表+语义KG的构建框架，适配不同语种用户的自然查询需求'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有text-to-SQL基准无法适配官方统计场景：官方统计以数千张宽表形式开放，列与值均为编码，语义存储在独立元数据而非关系型schema中，政策制定、企业分析等场景的自然查询需求难以被满足。
### 方法关键点
1. 构建LOCuST基准，包含荷兰统计局2000+英/荷双语表，配套语义KG存储表、指标、维度编码的标签、定义、层级、单位信息，作为text-to-SQL的外部知识支撑
2. 覆盖多类专家标注查询任务，包含原始值检索、求和、占比计算、多表关联等聚合类型
3. 新增observation F1评估指标，即使查询返回结果不同也可衡量其逻辑与真值的匹配度
### 关键结果
测试多款SOTA LLM，其在该场景下生成正确SQL的表现普遍较差。
