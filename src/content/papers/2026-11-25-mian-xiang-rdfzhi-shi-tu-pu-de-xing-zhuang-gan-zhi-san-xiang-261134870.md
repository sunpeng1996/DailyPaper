---
title: 'Shape-Aware Three-Way Merge for RDF Knowledge Graphs: The schema defines the
  conflict: an implementation and evaluation'
title_zh: 面向RDF知识图谱的形状感知三向合并：基于Schema的冲突判定实现与评估
authors:
- Steve Brown
arxiv_id: '2611.34870'
url: https://arxiv.org/abs/2611.34870
pdf_url: https://arxiv.org/pdf/2611.34870
published: '2026-11-25'
collected: '2026-11-28'
category: MultiAgent
direction: 多智体协作 · 知识图谱冲突合并
tags:
- Knowledge Graph
- SHACL
- Multi-Agent
- Conflict Detection
- RDF
one_liner: 提出基于SHACL形状约束的RDF知识图谱三向合并策略，落地多Agent生产存储，大幅降低人工冲突处理量
practical_value: '- 多Agent协同维护电商商品/用户知识图谱时，可引入SHACL形状约束定义冲突规则，仅对基数受限槽位触发人工判定，大幅降低人工干预量

  - 知识图谱合并场景下，优先合并Schema声明再合并实例数据，可覆盖绝大多数基数变更场景，搭配合并后校验补位解决数据类型演化盲点

  - KG合并效果评估可复用文中真阳性率、无数据丢失/伪造、无约束违规的核心指标，适配业务场景快速对齐基线'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有RDF知识图谱合并方案仅能识别顺序冲突，易遗漏语义冲突，多Agent协同编辑KG时冲突判定效率极低，基线方案会触发大量无意义人工问询。

### 方法关键点
1. 基于SHACL形状约束定义冲突规则，采用集合代数合并标准三元组，仅当槽位基数受限且两侧变更超出限制时判定为冲突；2. 无界谓词直接取并集，冲突槽位流转人工处理，合并后复用同一形状图校验结果；3. 兼容现有Context Merge基线策略，可作为扩展能力部署。

### 关键结果
对比上下文重叠基线，相同33个真实冲突下，人工问询量从845次降至33次，无三元组丢失/伪造、无SHACL违规；生产事故回放验证可覆盖所有939个重复值场景，别名冲突属于三元组层级盲区需额外链路处理。
