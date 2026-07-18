---
title: 'Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous
  Driving'
title_zh: Chat2Scenic：基于迭代RAG的自动驾驶场景生成框架
authors:
- Yuan Gao
- Wenting Miao
- Mattia Piccinini
- Haoyu Wang
- Qunying Song
- Johannes Betz
arxiv_id: '2607.14387'
url: https://arxiv.org/abs/2607.14387
pdf_url: https://arxiv.org/pdf/2607.14387
published: '2026-07-14'
collected: '2026-07-18'
category: RAG
direction: 自动驾驶场景生成 · 迭代RAG架构
tags:
- RAG
- Iterative Generation
- DSL
- Benchmark
- Autonomous Driving
one_liner: 提出迭代RAG框架生成合规自动驾驶DSL场景脚本，性能超基线且开源配套基准
practical_value: '- 迭代RAG + 交互式反馈优化生成结果的架构可迁移到电商规则化文案生成（如合规广告文案、商品参数DSL脚本）场景，解决生成内容合规性差的问题

  - 生成结果的「可执行性/编译通过率」指标设计可复用，用于衡量推荐系统生成的结构化内容（如动态活动规则、用户标签规则）的正确性

  - 当需要基于合规文档生成结构化可执行内容时，可借鉴其将领域知识、语法规则同时注入RAG知识库的做法，提升生成准确率'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
自动驾驶系统仿真验证需要大量合规的可执行测试场景脚本，现有方案存在明显权衡：检索组装法编译率尚可但扩展性差，检索式全脚本生成法编译成功率极低，从监管规则自动生成符合DSL语法的场景脚本仍是待解难题。

### 方法关键点
1. 提出迭代式RAG框架Chat2Scenic，内置聊天界面支持交互式场景迭代优化，RAG知识库同时纳入监管规则知识与DSL语法规范，保证生成内容既合规又符合语法要求
2. 开源包含123个来自NHTSA、联合国车辆法规等来源的场景生成基准数据集，覆盖多类合规测试要求

### 关键结果数字
对比SOTA方案，Chat2Scenic编译成功率（CSR）达76.42%，框架准确率（FA）达58.17%，分别比检索组装基线高46.34pct、47.14pct，比检索全脚本生成基线高60.16pct、47.31pct，性能优势显著
