---
title: 'SABET-QA: Temporal Knowledge Graph Question Answering'
title_zh: SABET-QA：面向时序知识图谱的问答框架
authors:
- Brahim Touayouch
- Mirette Moawad
- Dmitry Akulov
affiliations:
- QuickSort Research, Paris, France
- ENS Paris-Saclay, École Polytechnique, France
arxiv_id: '2608.20083'
url: https://arxiv.org/abs/2608.20083
pdf_url: https://arxiv.org/pdf/2608.20083
published: '2026-08-20'
collected: '2026-08-21'
category: Reasoning
direction: 时序知识图谱 · 多步推理问答
tags:
- Temporal-Knowledge-Graph
- QA
- Multi-hop-Reasoning
- Semantic-Alignment
- Iterative-Reasoning
one_liner: 提出具备迭代推理、双向实体时序打分的时序知识图谱问答框架，提升多步复杂时序查询性能
practical_value: '- 电商带时序约束的搜索场景（如「618期间比XX销量高的家电」类查询）可复用双向实体-时序对齐打分机制，提升多约束召回准确率

  - Agent调用结构化时序知识（如用户行为时序图谱、商家运营时序数据）时，可借鉴slot-aware语义对齐模块，减少知识调用的语义偏差

  - 复杂多步推理任务可引入可微工作记忆做渐进式假设迭代，替代单通推理pipeline，提升复杂查询鲁棒性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
时序知识图谱问答（TKGQA）需要对时间敏感事实做推理，现有基于嵌入的方法依赖单通推理pipeline，无法应对多步复杂时序查询的需求。
### 方法关键点
1. 设计双向实体-时序打分机制，结合slot-aware上下文模块对齐问题语义与时序KG嵌入，跨多跳迭代优化推理状态；
2. 引入可微工作记忆实现渐进式假设精炼，有标注数据时可补充辅助时序边界作为粗粒度监督，降低训练数据要求。
### 关键结果
在CronQuestions、Complex-CronQuestions、MultiTQ、TimeQuestions四个公开数据集上表现全面优于强基线，尤其在复杂多步时序查询任务上提升幅度显著。
