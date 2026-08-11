---
title: 'Temporal Misgrounding in Legal RAG: A Versioned-Corpus Benchmark for French
  Tax Law'
title_zh: 法律RAG时间错配问题：面向法国税法的版本化语料基准
authors:
- Rose Cymbler
- Daniel Guez
- Laurent Fabre
affiliations:
- Talia, Paris, France
- Databricks
arxiv_id: '2608.09393'
url: https://arxiv.org/abs/2608.09393
pdf_url: https://arxiv.org/pdf/2608.09393
published: '2026-08-10'
collected: '2026-08-11'
category: RAG
direction: RAG · 时间感知检索优化
tags:
- RAG
- Temporal Retrieval
- Benchmark
- Versioned Corpus
- Legal QA
one_liner: 提出法国税法版本化语料基准FiscalQA Pro，解决RAG时间敏感场景的版本错配问题
practical_value: '- 电商活动规则、运费政策、价保规则等时间敏感类RAG场景，可复用版本化语料+时间索引的架构，避免用当前生效规则答复历史/未来时效的用户咨询

  - 评估时间敏感RAG效果时，优先采用原子化正则、数值容差的确定性打分方法，规避LLM-as-judge自带的时间偏差问题

  - 多版本语料检索的性能瓶颈优先排查第一阶段召回，版本选择模块当前可做到接近99%的准确率，优化投入产出比更高'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有RAG默认语料为静态，在法律等存在多版本时效约束的场景下，会系统性检索到当前生效但实际不适用的内容，即时间错配问题，缺乏对应评测基准与解决方案参考。

### 方法关键点
1. 构建FiscalQA Pro基准：包含1938-2031年共93年32436条法国税法条款版本，配套209条专家标注的时间推理问题
2. 采用原子化真值块（正则匹配、带容差数值校验）做确定性打分，避免LLM-as-judge自带的时间偏差
3. 对比测试参数知识、静态RAG、自研多版本索引端到端检索器的效果

### 关键结果
- 大模型参数知识平均严格准确率仅3.0%，静态当前版本语料RAG准确率2.7%，正确版本召回率0%
- 自研无先验多版本检索器平均严格准确率达98.3%，已知对应条款的消融版本准确率达99.1%，剩余瓶颈来自第一阶段召回而非版本选择
