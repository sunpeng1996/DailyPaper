---
title: 'MultiVENT-Raw: A Benchmark for Retrieval and Reasoning over Raw Videos'
title_zh: MultiVENT-Raw：面向原始视频检索与推理的基准数据集
authors:
- Reno Kriz
- David Etter
- Alexander Martin
- Cameron Carpenter
- Debashish Chakraborty
- Hannah Recknor
- Reihaneh Iranmanesh
- Matthew Maciejewski
- Kenton Murray
- Eugene Yang
affiliations:
- Human Language Technology Center of Excellence
- Johns Hopkins University
- Georgetown University
- University of Rochester
- George Mason University
arxiv_id: '2609.28437'
url: https://arxiv.org/abs/2609.28437
pdf_url: https://arxiv.org/pdf/2609.28437
published: '2026-09-23'
collected: '2026-09-24'
category: Multimodal
direction: 多模态视频 · 检索推理基准
tags:
- Multimodal Benchmark
- Video Retrieval
- Video Reasoning
- Raw Video
- Multilingual Dataset
one_liner: 发布含12万条原始视频的多语言基准，支持视频检索与事件摘要生成任务评估
practical_value: '- 电商UGC短视频/内容检索场景可复用该基准的事件标注框架，优化无编辑原始视频的召回排序策略

  - 短视频内容理解模块可参考该基准的测试范式，补充无字幕、无元数据场景的鲁棒性验证流程

  - 多模态RAG系统可复用其「检索+生成」的两级任务设计，落地视频内容问答、事件摘要类需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前社交平台UGC、监控类无编辑原始视频占比持续提升，这类视频无脚本、字幕、叠加图文、元数据等辅助信息，现有多模态模型在其上的检索、推理能力缺乏统一评估基准。
### 方法关键点
发布多语言数据集MultiVENT-Raw，包含近12万条原始视频（总时长超5300小时），配套130个事件、222个事件导向查询，标注了视频相关性判断与关联关键事实；支持两类下游任务：1）事件相关视频检索，2）关联视频汇总生成结构化事件报告。
### 关键结果
对当前SOTA多模态模型的基准测试显示，两类任务均存在显著性能瓶颈，现有模型效果远未达到落地实用水平。
