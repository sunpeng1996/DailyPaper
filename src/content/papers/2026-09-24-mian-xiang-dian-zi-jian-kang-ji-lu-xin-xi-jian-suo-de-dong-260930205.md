---
title: A Living Benchmark for Information Retrieval from Electronic Health Records
title_zh: 面向电子健康记录信息检索的动态评测基准
authors:
- Jordan L. Cahoon
- Chloe O. Stanwyck
- Sulaiman Somani
- Philip Chung
- Kevin R Keet
- Kameron C. Black
- Andrea T. Fisher
- Sarita Khemani
- Jerry Liu
- Stephen Ma
affiliations:
- Stanford University
- Weill Cancer Hub West
- Stanford Cancer Center
- Center for Clinical Excellence Research, Stanford School of Medicine
arxiv_id: '2609.30205'
url: https://arxiv.org/abs/2609.30205
pdf_url: https://arxiv.org/pdf/2609.30205
published: '2026-09-24'
collected: '2026-09-27'
category: Eval
direction: 大模型评测 · 动态基准构建
tags:
- LLM
- Evaluation
- Benchmark
- Information Retrieval
- Dynamic Dataset
one_liner: 提出可自动生成EHR问答对的可扩展框架，构建可动态更新的临床LLM检索评测基准BRIE
practical_value: '- 动态基准生成思路可复用：垂域RAG/检索类Agent的评测无需全量人工标注，可先由领域专家校验自动QA生成器的有效性，再批量生成评测集，大幅降低更新成本，同时动态刷新可规避训练数据泄露问题

  - 多合理答案评估逻辑可迁移：针对电商用户复杂咨询、多意图query识别等存在合理答案差异的场景，可替代单一标准答案评估逻辑，降低误判率

  - 跨文档合成类任务的评测维度可复用：可借鉴其对多源信息整合类query的评估方法，定位自家RAG/推荐Agent在长上下文信息遗漏、推理错误等方面的短板'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
基于LLM的临床助手已大量落地电子健康记录（EHR）系统，其检索能力的安全性与实用性依赖严格评测，但现有静态基准存在人工标注成本高、迭代慢、易过时、无法应对数据泄露等问题。
### 方法关键点
1. 提出可扩展框架，可从纵向EHR病历中自动生成问答对
2. 经19名临床医生校验生成器的输出有效性，构建可动态维护的EHR检索评测基准BRIE，支持多合理答案生成、基准内容自动刷新
### 关键结果
在9款LLM、5种推理策略上的测试显示，当前SOTA系统在EHR检索场景下频繁遗漏关键临床信息，尤其针对需要跨多文档、多就诊记录合成推理的query，表现缺陷更明显
