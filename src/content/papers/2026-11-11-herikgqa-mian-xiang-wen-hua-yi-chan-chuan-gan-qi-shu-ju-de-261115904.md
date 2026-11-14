---
title: 'HeriKGQA: Grounded Knowledge-Graph Question Answering over Cultural Heritage
  Sensor Data'
title_zh: HeriKGQA：面向文化遗产传感器数据的落地式知识图谱问答系统
authors:
- Lingxiao Kong
- Vasileios Arampatzakis
- Vasileios Sevetlidis
- George Pavlidis
- Zeyd Boukhers
affiliations:
- Fraunhofer Institute for Applied Information Technology FIT
- University of Cologne
- Athena Research and Innovation Centre
- University Hospital of Cologne
arxiv_id: '2611.15904'
url: https://arxiv.org/abs/2611.15904
pdf_url: https://arxiv.org/pdf/2611.15904
published: '2026-11-11'
collected: '2026-11-14'
category: LLM
direction: 大语言模型 · 知识图谱问答优化
tags:
- KGQA
- SPARQL
- Grounding
- Ontology
- LLM
one_liner: 提出KG驱动的问答框架，限定LLM仅处理自然语言转译，计算交由确定性代码提升性能
practical_value: '- 可复用「LLM仅负责自然语言意图解析与答案生成、确定性逻辑交由规则/结构化查询执行」的架构，规避LLM数值计算、时序/空间属性匹配的幻觉问题，适用于电商客服问答、商品库存查询Agent等场景

  - 可在RAG/Agent落地中引入领域本体约束的意图解析流程，搭配每步错误校验机制，显著提升结构化数据查询的准确率，适配电商订单、物流、用户权益类查询场景

  - 涉及数值、时序、异常判定类的推理任务，优先将事实提取、计算逻辑下沉到grounding层，能同时提升推理准确率与响应速度，可迁移至广告效果分析、推荐效果归因类工具Agent'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
文化遗产站点的传感器数据查询需专业数据库技能，直接调用LLM处理原始传感记录易出现传感器、站点、时间维度的信息混淆，产生静默计算错误。
### 方法关键点
1. 限定LLM仅负责问题意图解析与自然语言答案生成，计算逻辑完全交由SPARQL查询与确定性代码执行，规避LLM计算幻觉
2. 基于融合W3C SOSA/SSN与CIDOC-CRM的文化遗产本体约束意图解析结果，编译为SPARQL查询后从KG获取结果
3. 搭配grounding层生成时序、空间、异常事实，每步LLM操作均设置纠错机制
### 关键结果
在5个文化遗产站点真实数据的500个问答测试集上准确率达99.0%，较同LLM的最强基线高18.2个百分点，响应速度提升近4倍；移除grounding层后准确率下降12.2个百分点，异常类问题准确率从99%降至66%
