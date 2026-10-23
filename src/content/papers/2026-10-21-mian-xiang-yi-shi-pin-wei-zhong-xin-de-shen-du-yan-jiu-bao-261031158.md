---
title: 'Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep
  Research Reports'
title_zh: 面向以视频为中心的深度研究报告的Agent基准测评
authors:
- Jiahao Meng
- Qize Yang
- Yuxuan Wang
- Yunfei Chu
- Wensi Dai
- Jin Xu
- Yunhai Tong
affiliations:
- Peking University
- Alibaba Group
- Independent Researcher
arxiv_id: '2610.31158'
url: https://arxiv.org/abs/2610.31158
pdf_url: https://arxiv.org/pdf/2610.31158
published: '2026-10-21'
collected: '2026-10-23'
category: Agent
direction: 多模态Agent 深度研究报告基准评测
tags:
- Agent
- Multimodal
- Benchmark
- Video Understanding
- Evaluation
one_liner: 提出首个以视频为中心的深度研究报告Agent任务、基准OmniDR-Bench及细粒度评估框架
practical_value: '- 开放生成场景评测可复用Omni-ART分层二元指标+独立事实库校准的逻辑，解决无标准答案的生成质量评估难题，比如电商商品测评报告、直播复盘报告的自动评分

  - 短视频/直播内容分析类Agent可复用7阶段参考工作流：锚点提取→多模态证据检索→关联原视频时间戳→结构化渲染→自动校验修复，可直接落地带货卖点提取、虚假宣传校验、同款对比报告生成等场景

  - RAG+生成类业务可复用实验结论：不能只考核召回源的数量/多样性，需重点优化inline citation和对应claim的绑定逻辑，避免堆砌引用但不支撑论点的问题

  - 业务自定义评测集构建可复用ARC流程：独立证据采集→候选指标筛选→多版本报告校准→多轮人工校验，可大幅提升评测指标的区分度和可靠性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有深度研究Agent基准要么仅支持文本输入，要么视频相关任务仅聚焦短问答，无法评估以单条源视频为核心、结合外部多模态证据生成可溯源交互式深度报告的能力，而这类能力可直接支撑短视频/直播内容验证、实操教程复刻、消费决策辅助等业务场景，存在明确评测缺口。

### 方法关键点
- 定义「以视频为中心的深度研究报告生成」任务，输入为源视频+用户需求，输出为关联视频时间戳、绑定多模态证据引用的交互式HTML报告
- 设计Omni Atomic Rubric Trees（Omni-ART）评估框架，分为内容、引用、呈现3个维度，共23个通用诊断方向+任务专属二元原子指标，兼顾通用性和定制化评估需求
- 提出Audited Rubric Construction（ARC）流程，通过独立采集视频/外部多模态证据库、自动校验、行为校准、多轮人工审核构建评测集，避免评估偏差
- 开源7阶段参考Agent工作流，内置跨模态对齐、并行检索、自动修复等模块

### 关键实验
OmniDR-Bench包含50个中英双语任务，覆盖19个现实场景、共6414条评估指标；对比18种Agent配置，最优系统（Claude Opus 5）仅得63.3分，其中呈现维度平均得分81.8，内容和引用维度仅为45.4、47.8，核心瓶颈在事实覆盖、跨模态因果推理、引用与论点绑定能力。

最值得记住的结论：当前多模态研究Agent的外观表现远好于实质研究能力，能找到证据不代表能正确用好证据支撑论点。
