---
title: 'AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development'
title_zh: AutoRAGBench：面向LLM Agent自动化开发RAG系统的评测基准
authors:
- Hang Zhang
- Yuzhi Pan
- Ziyao Zhong
- Chaokun Wang
- Shuo Cao
- Zeyu Huang
- Yue Xue
- Fang Niu
- Bofan Xie
- Guanchen Ge
affiliations:
- School of Software, Tsinghua University
- Sina Weibo Corp
arxiv_id: '2611.25582'
url: https://arxiv.org/abs/2611.25582
pdf_url: https://arxiv.org/pdf/2611.25582
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent 评测 · RAG系统自动化开发
tags:
- Agent
- RAG
- Benchmark
- LLM
- Automated Development
one_liner: 首个开放代码空间下评测Agent自主从零搭建RAG系统能力的基准
practical_value: '- 可复用该基准的Agent迭代优化RAG的流程框架，将电商客服QA、商品知识问答等场景的RAG系统调优工作交给Agent自动化完成，参考单卡6小时的资源阈值适配业务资源限制，大幅降低人工调参、组件选型的工作量

  - 参考其RAG效果评测方法，采用多个独立小回答模型平均打分的策略，避免单一模型偏差，可直接用于电商场景下RAG召回段质量的自动评估，减少人工标注成本

  - 优化现有业务RAG系统时，可参考论文中Agent增量优化的思路，在保留原有核心逻辑的前提下实现效果提升，无需全量重构，平均可获得近10个点的效果增益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG是LLM落地业务场景的核心范式之一，但不同领域、不同任务的RAG需要针对性设计分片、索引、检索、重排策略，人工开发调试成本极高。当前RAG相关评测仅聚焦成品系统的效果，自动化RAG调优方案又被限制在预定义的组件与超参空间内，无法衡量LLM Agent自主从零开始设计开发RAG系统的真实能力，也无法评估其迭代优化的效率。

### 方法关键点
- 构建覆盖9类任务的评测集，横跨开放域问答、多跳文档问答、垂直领域问答、事实验证、知识图谱问答5大类场景，适配不同业务需求
- 采用隔离容器环境，分配单H800 GPU、6小时开发时限，无启动代码、无预设RAG框架，禁止访问外部数据，仅提供任务语料与训练样例
- 评测逻辑同时覆盖最终RAG系统效果与开发过程：效果层面用5个独立持留的小模型作为回答器，平均打分消除单一回答模型偏差；过程层面追踪Agent的迭代路径、资源消耗、优化效率

### 关键实验
对比9种不同Agent配置、复合Human-SOTA基线、Reference RAG、naive BM25等基线：
- GPT-6.1 Sol搭配Codex CLI取得最高平均得分56.1，超出复合Human-SOTA基线11.7分，超出Reference RAG基线9.7分
- 上述Agent在保留核心逻辑的约束下，可将7个人类设计的SOTA RAG系统平均提升16.6分
- 93.5%的Agent开发流程可通过迭代将效果至少提升1分，中位数提升幅度为5.5分

### 核心结论
LLM Agent已具备超越普通人类开发者的RAG系统开发能力，开放代码空间的自主设计能力远优于固定组件空间的自动调优效果
