---
title: Detecting Knowledge Inconsistencies Across Text, Tables, and Knowledge Graphs
title_zh: 跨文本、表格与知识图谱的知识不一致性检测
authors:
- Fanfu Wei
- Thibault Ehrhart
- Raphaël Troncy
affiliations:
- EURECOM, France
arxiv_id: '2607.25959'
url: https://arxiv.org/abs/2607.25959
pdf_url: https://arxiv.org/pdf/2607.25959
published: '2026-07-28'
collected: '2026-07-29'
category: Reasoning
direction: 跨模态知识一致性校验
tags:
- Knowledge Graph
- Text-to-SPARQL
- Knowledge Consistency
- LLM-as-Judge
- Cross-Modal Reasoning
one_liner: 提出Kontrast框架与不一致性分类体系，自动检测跨文本、表格、知识图谱的知识冲突并分类
practical_value: '- 电商商品多源信息校验场景（详情页文本、规格表、商品KG参数不一致），可复用本文的7类不一致标签体系，快速定位错误源，降低客诉

  - 搭建RAG多源信息一致性校验pipeline时，可采用「规则匹配+LLM-as-Judge」两级方案：先用SBERT做语义对齐初筛，再用小样本LLM做细分类，兼顾效率和准确率

  - 知识图谱补全场景下，可通过Text-to-SPARQL将半结构化查询转换为KG查询，空结果、结果不匹配的case可直接作为KG补全候选，大幅降低人工标注成本

  - 商品知识库更新审计场景，可复用Kontrast的流程，自动发现不同模态的信息不同步问题，提升知识库准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
维基百科、Wikidata等公开知识源是LLM预训练、RAG、开放域问答的核心输入，但同一知识常分散在文本、表格、KG三类模态，因编辑规则、更新周期差异存在大量不一致，现有冲突检测方案多聚焦纯文本模态，缺乏跨三类模态的系统性检测与分类能力，无法支撑大规模知识审计需求。

### 方法关键点
- 定义7类跨模态知识不一致标签：一致、KG精度更高、表格精度更高、答案直接冲突、时间偏移、KG缺边、KG缺节点、KG缺属性/限定符，可直接指导知识修复
- 提出Kontrast框架：1）用GRASP Text-to-SPARQL模型将表格QA问题转换为SPARQL查询Wikidata得到KG答案；2）规则层做答案归一化、SBERT语义对齐，基于召回/精度阈值初筛分类；3）难例通过15-shot LLM-as-Judge完成细分类
- 整合6个公开表格QA数据集，构建2870条样本的跨模态一致性检测基准，覆盖简单/复杂问答场景

### 关键结果
- Qwen3-30B做Text-to-SPARQL时可执行率最高达89.8%；Qwen3-235B的有效结果占比最高达63.7%，不一致率最低为61.4%
- 直接答案冲突是最常见不一致类型，占比38.7%~46.1%；粒度差异类不一致占比18.6%~22.9%，证明三类模态知识互补性极强
- 规则匹配与LLM-as-Judge的人工评估准确率均为100%，分类可靠性高

> 最值得记住：文本、表格、KG不应被视为孤立知识源，其不一致性恰恰是互相补充、修正的核心信号
