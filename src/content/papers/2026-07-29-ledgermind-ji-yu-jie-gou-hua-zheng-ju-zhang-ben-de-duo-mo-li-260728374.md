---
title: 'LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structured
  Evidence Ledger'
title_zh: LedgerMind：基于结构化证据账本的多模态代理溯源约束推理框架
authors:
- Enjun Du
- Hange Zhou
- Chenxu Du
- Siyi Liu
- Zirong Chen
- Ziyu Zheng
- Yongqi Zhang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The University of Hong Kong
- Tsinghua University
- University of Sussex
arxiv_id: '2607.28374'
url: https://arxiv.org/abs/2607.28374
pdf_url: https://arxiv.org/pdf/2607.28374
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: 多模态Agent可信推理 · 结构化证据溯源
tags:
- Multimodal Agent
- Provenance Constraint
- Hallucination Mitigation
- Trajectory Faithfulness
- Structured Ledger
one_liner: 提出结构化证据账本实现多模态Agent溯源约束推理，同步提升准确率与轨迹可信度
practical_value: '- 电商多模态导购Agent可借鉴结构化证据账本设计，将工具返回的商品参数、用户行为、OCR结果等归一化为带溯源的条目，推理决策仅允许引用活跃条目，从结构层面避免商品属性、价格等信息幻觉

  - RAG+Agent的商品咨询场景可复用三层接地校验逻辑：先做支持覆盖率校验，再做Entity Consistency Check (ECC)、Numeric
  Coherence Check (NCC)，解决“引用ID正确但内容与证据不符”的虚假接地问题

  - 多步推理Agent调度可采用自适应双路径分发器，简单查询（如包邮规则、基础参数）走直接路径降本，复杂查询（如跨商品对比、定制化方案推荐）走全流程，避免过度推理改写正确答案

  - Agent自修复模块放弃自由文本改写逻辑，仅开放预定义操作（刷新证据、重试工具、切换路径、终止输出等），保证修复过程不会新增无来源的幻觉内容'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多模态Agent多步推理轨迹当前仅用最终准确率评估，无法区分正确答案来自真实证据、语言先验还是错误抵消；现有框架的自由文本轨迹混存工具输出、模型推理内容，即使加引用要求也存在「虚假接地」问题（引用ID正确但实体/数值与证据不符），自由文本自修复还会引入新幻觉，简单查询过度推理反而降低准确率。

### 方法关键点
1. 以结构化证据账本为核心状态，每个工具输出归一化为带来源、类型、置信度、生命周期、依赖关系的条目，推理和决策仅允许引用活跃账本条目，溯源是结构约束而非prompt要求
2. 三层接地协议：支持覆盖率校验（内容词重叠度达标）、ECC（结论实体必须在引用证据中）、NCC（结论数值符合证据对应类型的容忍范围）
3. 自适应双路径分发器：简单查询走直接路径降本，复杂查询走全流程，避免过度推理
4. 事件触发的校验修复引擎，仅允许7种预定义操作，满足溯源非放大保证，修复不会新增无来源内容

### 关键实验
在VTC-Bench、MMMU、Hard-200等7个多模态基准测试，对比各MLLM原生CoT输出（同工具预算）：Gemini-3-Flash在VTC-Bench达58.9% SOTA，较原生提升12.4pp；Hard-200集上各MLLM准确率提升11.2~19.7pp；MC-Search链对齐指标HPS从31.35%提升至57.82%，RD从0.89降至0.54，轨迹可信度同步提升。

最值得记住的一句话：Agent可信推理的核心不是靠prompt要求引用，而是从状态层面把溯源约束做进执行流程里。
