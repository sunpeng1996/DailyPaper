---
title: 'AutoIndex: Learning Representation Programs for Retrieval'
title_zh: AutoIndex：面向检索的可学习文档表示程序优化框架
authors:
- Sam O'Nuallain
- Nithya Rajkumar
- Ramya Narayanasamy
- Hanna Jiang
- Shreyas Chaudhari
- Andrew Drozdov
affiliations:
- University of Massachusetts Amherst
- Databricks Mosaic Research
arxiv_id: '2607.18603'
url: https://arxiv.org/abs/2607.18603
pdf_url: https://arxiv.org/pdf/2607.18603
published: '2026-07-21'
collected: '2026-07-22'
category: RAG
direction: RAG检索优化 · Agent程序合成
tags:
- AutoIndex
- Retrieval Optimization
- Program Synthesis
- BM25
- Agent
- RAG
one_liner: 双Agent迭代搜索索引前文档预处理程序，固定BM25下跨8类检索任务实现效果显著提升
practical_value: '- 电商搜索、站内RAG场景可直接复用双Agent架构：用分析Agent定位检索BadCase根因，代码Agent生成定制化的文档预处理（商品标题/描述重写、冗余规格信息过滤）规则，不需要改动检索器内核即可快速迭代效果

  - 可直接套用分层BadCase采样方法：将验证query分为锚点（初始版本召回成功当前版本失败）、召回违规、小margin正例三类，大幅降低Agent分析的噪声，避免过拟合个别零散case

  - 电商商品索引优化可参考文本重加权技巧：对商品核心字段（标题、核心属性、营销标签）做重复加权，不需要改动BM25的字段权重参数即可实现域加权效果，适配现有检索系统的存量架构'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有检索系统的文档预处理（分块、归一化、字段拼接、冗余过滤）通常是人工设定的静态规则，未被作为独立优化目标；过往研究要么聚焦检索器、排序模块的优化，要么用网格搜索调整少量预处理超参数，无法自动化探索复杂的预处理变换空间，难以适配异质检索任务的差异化需求。

### 方法关键点
- 迭代优化闭环：固定检索器、排序规则、索引后端，仅将文档预处理程序作为优化目标，以离线检索指标（Recall@100）作为反馈信号，迭代筛选最优变换
- 双Agent分工：分析Agent仅持有读权限工具（检索、读文档、grep搜索），从分层采样的三类BadCase（锚点、召回违规、小margin正例）中定位当前预处理的失败根因；代码Agent基于分析报告和历史搜索记录，生成多个可执行的候选预处理程序
- 候选筛选机制：每个候选程序执行后重建索引，在验证集上评估，仅保留指标提升超过阈值的候选；若存在多个优质候选，尝试融合其变换逻辑，验证后选取最优

### 关键实验
在CRUMB基准的8类异质检索任务上测试，固定BM25作为检索器，对比全文档BM25基线，平均Recall@100提升8.4%，nDCG@10提升8.3%，最高增益分别达30.5%、43.6%；对比通用均匀分块基线，所有公开任务效果均大幅领先；学习到的预处理程序可迁移到密集检索场景，在StackExchange任务上Recall@100提升18.3%。

> 最值得记住的结论：索引预处理不是静态的基础设施，而是可独立优化的核心检索性能提升点，Agent驱动的程序合成可以低成本挖掘其优化空间。
