---
title: 'ExecRetrieval: Measuring the Functional-Correctness Gap in Code-Embedding
  Retrieval'
title_zh: ExecRetrieval：代码嵌入检索的功能正确性差距度量
authors:
- Aaryan Kapoor
- Md Abdullah Al Hafiz Khan
affiliations:
- Kennesaw State University
arxiv_id: '2609.01865'
url: https://arxiv.org/abs/2609.01865
pdf_url: https://arxiv.org/pdf/2609.01865
published: '2026-08-31'
collected: '2026-09-04'
category: Eval
direction: 代码检索评测 · 功能正确性度量
tags:
- Code Retrieval
- Embedding Evaluation
- RAG Benchmark
- Functional Correctness
- Coding Agent
one_liner: 构建含执行验证近克隆错误变体的代码检索基准，量化现有嵌入模型的功能判别能力缺口
practical_value: '- 垂类高准确率要求RAG（如电商规则、客服话术、代码库）召回后必须加下游正确性校验环节，不能仅依赖语义相似度

  - 构建垂类检索/推荐评测集时，可参考单编辑近克隆负例构造法，比随机负例更易定位模型召回盲区

  - 排序层可在语义相似度特征外新增功能正确性打分分支，优先提升top1召回的准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有代码检索基准未在候选池中加入可控、经执行验证的近克隆错误变体，无法衡量嵌入模型对功能正确与近相似错误代码的区分能力，而该能力是Coding Agent、代码RAG系统效果的核心影响因素。

### 方法关键点
构建ExecRetrieval基准，包含939个Python任务，每个任务对应1个经执行验证的正确实现，以及最多4个经单编辑机械突变生成的执行验证错误干扰项；评测23种稠密嵌入配置+BM25，采用配对McNemar检验与查询级bootstrap区间做统计验证。

### 关键结果数字
头部托管系统exec@10可达1.00，但exec@1仅0.331；头部系统的rank1错误中91.5%~99.4%为配对错误变体，67%~78%的查询中正确实现得分低于至少1个配对干扰项。
