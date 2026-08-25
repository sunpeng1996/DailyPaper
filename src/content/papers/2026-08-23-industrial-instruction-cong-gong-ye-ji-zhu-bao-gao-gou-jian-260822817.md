---
title: 'Industrial-Instruction: An End-to-End Framework for Building Instruction-Tuning
  and Benchmark Datasets from Industrial Technical Reports'
title_zh: Industrial-Instruction：从工业技术报告构建指令微调与基准数据集的端到端框架
authors:
- Parsa Bakhtiari
- Hassan Bashiri
- Alireza Khalilipour
- Masoud Nasiripour
- Moharram Challenger
arxiv_id: '2608.22817'
url: https://arxiv.org/abs/2608.22817
pdf_url: https://arxiv.org/pdf/2608.22817
published: '2026-08-23'
collected: '2026-08-25'
category: LLM
direction: LLM指令微调 · 工业数据集构建
tags:
- Instruction Tuning
- Dataset Construction
- Industrial LLM
- QA Dataset
- RAG
one_liner: 提出从异构工业技术报告生成指令微调数据集的端到端流水线，开源2个真实工业QA数据集
practical_value: '- 可复用布局感知提取+语义索引+QA生成的流水线，从电商商品手册、售后文档等异构文档生成客服Agent的指令微调数据

  - 构建业务场景数据集时可主动覆盖无关召回、单/多文档支撑等5类query-文档关系，提升RAG系统对召回噪声的鲁棒性

  - 小参数LLM（<10B）微调前可优先评估数据生成模型的成本效果 tradeoff：闭源大模型生成数据质量更高但成本高2个数量级，开源模型成本低但存在小幅知识遗忘问题'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
工业技术报告包含运维、排障等高价值知识，但结构异构（含散文、表格、规格参数），现有检索、QA流水线难以处理，且无公开的工业场景指令微调/基准数据集。
### 方法关键点
提出端到端Industrial-Instruction流水线：1. 布局感知提取保留文本、表格内容；2. 构建语义检索索引；3. 基于召回证据生成覆盖5类query-文档关系的选择题QA，经过滤得到高质量样本。同时用Qwen3-30B开源模型、Claude-Opus-4.6闭源API各生成一套数据集支持对比。
### 关键结果
基于906份松下公开文档（7525页）生成的数据集含约13.6k QA对；<10B参数开源LLM微调后，松下基准集Set-Match Accuracy从28.5%提升至42.0%，F1从46.6%提升至63.5%；Claude生成的数据集微调收益更大，但成本高2个数量级，且微调后模型无通用知识遗忘，Qwen生成的数据集存在小幅知识遗忘。
