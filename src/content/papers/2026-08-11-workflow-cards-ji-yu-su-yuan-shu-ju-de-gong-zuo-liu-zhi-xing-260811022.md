---
title: 'Workflow Cards: Structured Summaries of Workflow Executions Using Provenance
  Data'
title_zh: Workflow Cards：基于溯源数据的工作流执行结构化摘要方案
authors:
- Nicola Giuseppe Marchioro
- Gabriele Padovani
- Amal Gueroudji
- Rafael Ferreira da Silva
- Wesley Brewer
- Valentine Anantharaj
- Sandro Fiore
- Renan Souza
affiliations:
- University of Trento
- Argonne National Laboratory
- Oak Ridge National Laboratory
arxiv_id: '2608.11022'
url: https://arxiv.org/abs/2608.11022
pdf_url: https://arxiv.org/pdf/2608.11022
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: LLM友好型工作流结构化文档设计
tags:
- Workflow Provenance
- Structured Documentation
- Agentic Workflow
- LLM Usability
- Model Cards
one_liner: 提出基于溯源数据的Workflow Cards模板，使LLM对工作流执行的问答质量较schema查询近乎翻倍
practical_value: '- 可复用Workflow Cards的结构化设计思路，为推荐/广告系统的A/B测试、数据预处理、模型训练上线工作流制作标准化可溯源文档，同时支持人工排查与LLM自动分析，降低问题定位成本

  - 搭建内部业务RAG知识库时，对工作流类信息优先采用统一结构化卡片存储，相比直接对接原始schema数据库查询，可使LLM回答质量提升近1倍，减少RAG答非所问、信息遗漏问题

  - 构建电商选品、广告投放类Agent的执行链路时，可用同类结构化卡片记录每步执行的参数、资源、中间结果等溯源信息，方便Agent自主复盘调整策略，也便于人工审计'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有Model Cards、Data Cards仅覆盖静态模型/数据集资产，缺失生成、转换、评估这些资产的工作流执行信息，而数据预处理、参数选择、runtime行为、资源开销等执行细节正是业务系统偏差、性能波动、可复现性问题的核心来源，同时传统溯源数据库的schema查询模式对LLM解析极不友好。
### 方法关键点
1. 梳理现有卡片类文档缺失的执行层典型溯源问题，定义标准化Workflow Cards模板，将机器可读的工作流溯源数据转换为人与LLM均可高效解析的结构化摘要
2. 对照实验测试LLM分别通过Workflow Cards、传统schema接口查询工作流溯源信息的问答效果
### 关键结果
1. 填补了现有卡片类文档的执行层信息空白
2. 无论LLM-as-a-Judge还是人工评估，Workflow Cards的问答质量较schema查询接近翻倍
