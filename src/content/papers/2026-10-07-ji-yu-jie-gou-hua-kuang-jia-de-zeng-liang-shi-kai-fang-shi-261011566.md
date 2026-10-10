---
title: Incremental Open-Ended Deep Research with Structured Harness
title_zh: 基于结构化框架的增量式开放式深度研究系统
authors:
- Meilin Chen
- Hongyuan Bao
affiliations:
- Xiaohongshu Inc.
- Zhejiang University
arxiv_id: '2610.11566'
url: https://arxiv.org/abs/2610.11566
pdf_url: https://arxiv.org/pdf/2610.11566
published: '2026-10-07'
collected: '2026-10-10'
category: Agent
direction: Agent 开放式深度研究增量更新
tags:
- LLM Agent
- Open-Ended Deep Research
- Incremental Update
- Structured Harness
- Evaluation Framework
one_liner: 提出增量开放式深度研究范式与结构化框架，保报告质量同时大幅降本、提升连续性
practical_value: '- 电商行业报告、品类趋势分析、竞品监控等需要定期更新的场景，可复用Structured Harness设计，将现有报告拆分为大纲、章节、关联证据的结构化存储，增量更新时仅修改变动部分，无需全量重写，可降低token消耗与搜索成本

  - 证据池复用逻辑可迁移到RAG系统的增量更新，对已爬取的网页/文档设置相似度阈值做批量刷新，仅内容变动超过阈值时触发重新解析和召回，减少重复爬取与计算开销

  - 长期迭代的Agent任务（如用户长期兴趣跟踪、行业动态持续监控）可参考SST、LCT的评估框架，从效果、连续性、成本三个维度做全链路效果评估'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有开放式深度研究（OEDR）系统均为一次性从零生成报告，在行业分析、趋势监控、竞品追踪等需要定期更新报告的场景下，全量重写不仅浪费大量搜索与模型计算资源，还会导致报告结构、内容前后不一致，无法满足知识持续迭代的业务需求。

### 方法关键点
- 提出Incremental-OEDR范式，将报告视为持续演化的状态，基于上一版报告+新增信息做增量更新，而非全量重写
- 设计Structured Harness框架：1）结构化表示：把报告拆分为大纲、章节、关联证据三层结构，作为增量操作的基础；2）结构化检索：支持按需求定向读取历史报告的指定模块及对应证据；3）结构化证据池：持久化存储所有证据的URL、内容、更新时间，自动批量刷新旧证据，仅对内容相似度低于阈值的部分做diff分析，新检索的证据自动入库复用；4）结构化生成：仅编辑变动章节，保留原有结构和有效内容
- 搭建时间维度评估框架，包含单步更新任务（SST）和长链更新任务（LCT），从报告质量、连续性、研究成本三个维度做全链路评估

### 关键实验
在DeepResearch Bench、DeepConsult两个权威基准上测试，对比MS-Agent等SOTA OEDR系统，开源配置下：内容级ROUGE-L F1最高提升0.51，大纲级EM F1最高提升0.63，token消耗最高降低33%，搜索调用次数最高降低61%，同时报告质量与基线持平甚至更优。

### 核心结论
对需要持续迭代的长周期Agent任务，结构化的历史状态复用是兼顾效果、一致性和成本的核心路径。
