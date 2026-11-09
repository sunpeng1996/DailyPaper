---
title: 'FondueQA: A Benchmark for Evaluating Parametric Compensation in Multi-Hop
  QA'
title_zh: FondueQA：多跳问答场景下参数知识补偿能力评估基准
authors:
- Laurin Schmid
- Suman Navaratnarajah
- Koel Dutta Chowdhury
- Steffen Eger
- Josif Grabocka
- Christian Frey
affiliations:
- University of Technology Nuremberg
arxiv_id: '2611.09274'
url: https://arxiv.org/abs/2611.09274
pdf_url: https://arxiv.org/pdf/2611.09274
published: '2026-11-06'
collected: '2026-11-09'
category: Eval
direction: 评估基准 · 多跳QA参数补偿
tags:
- Multi-hop QA
- Parametric Knowledge
- Benchmark
- RAG
- Evaluation
- LLM Reasoning
one_liner: 构建事实隔离的多跳QA基准，支持可控证据消融以研究LLM参数知识补偿规律
practical_value: '- 电商搜索多跳Query理解的RAG系统可参考事实隔离校验方法，避免多文档证据泄漏导致的效果评估失真

  - 冷启长尾商品/内容的RAG召回时，优先保障桥接类关联证据的召回率，这类证据缺失后参数知识更难补偿

  - 多步推理的Agent导购/客服场景，可引入实体流行度特征动态调整召回策略：长尾实体必须召回完整证据，热门实体可允许部分缺失靠参数补全

  - 构造RAG负例时可参考推理陷阱设计，加入同类竞争实体负样能更准确测试模型抗干扰能力，避免上线后推荐错配'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多跳QA基准普遍存在证据泄漏、基准污染问题，无法精准区分模型答对是靠上下文推理、参数知识记忆还是数据集漏洞，也无法控制不同推理步骤的证据缺失来研究LLM参数知识的补偿规律，导致RAG、多跳推理系统的效果评估不可靠。

### 方法关键点
- 基于Wikidata三元组和Wikipedia文档构建，要求每个推理步骤的事实唯一归属一个黄金文档，无跨文档、问题、干扰项的证据泄漏，实现精准的单文档证据消融
- 覆盖5类多跳推理结构（桥接、对比、跨属性等）共13063个问题，每个实体标注维基百科页面访问量作为流行度代理，支持参数知识可及性关联分析
- 设计两类干预实验：证据缺口（移除指定推理步骤的文档）、推理陷阱（加入同类竞争实体干扰项），可系统测试不同条件下的参数补偿效果

### 关键结果
在12款不同规模、架构的LLM上测试，核心结论：1）移除桥接证据比移除答案所在文档的EM下降更高，小模型差异更明显；2）实体流行度每提升一个数量级，证据缺失带来的EM损失下降约10pp；3）上下文存在同类竞争实体时，EM最多下降15pp，若竞争实体支持正确答案则EM最多提升25pp；4）约32-45%的案例中，模型答对多跳问题但无法单独召回缺失的原子事实。

### 核心结论
RAG系统的召回效果不能只看覆盖度，还要考虑缺失证据的推理角色、实体流行度和上下文干扰，桥接类关联证据的优先级高于答案承载文档。
