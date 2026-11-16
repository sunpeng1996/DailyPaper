---
title: 'MEM-SQL: Memory-Empowered Text-to-SQL'
title_zh: MEM-SQL：内存增强的自然语言转SQL系统
authors:
- Xiaoqi Wang
- Wenqi Pei
- Shizheng Hou
- Yilai Liu
- Han Chen
- Boyan Li
- Yuyu Luo
- Hongyang Du
affiliations:
- The University of Hong Kong NICE Lab
- National University of Singapore
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2611.18338'
url: https://arxiv.org/abs/2611.18338
pdf_url: https://arxiv.org/pdf/2611.18338
published: '2026-11-12'
collected: '2026-11-16'
category: LLM
direction: LLM应用 · Text-to-SQL性能优化
tags:
- Text-to-SQL
- Memory-Augmented LLM
- Benchmark
- Schema Linking
- Efficiency Optimization
one_liner: 提出历史感知Text-to-SQL基准HARE与内存增强方法MEM-SQL，同步提升准确率与生成效率
practical_value: '- 分层内存设计可迁移到电商大模型Query改写、BI查询生成场景，存储常用查询模板、可复用逻辑块降低生成成本

  - On-demand Schema Linking（OSL）技巧可直接复用：仅在内存匹配失败或生成证据不足时调用全量schema/元数据，大幅降低RAG检索、推荐系统元信息加载的token开销与延迟

  - 历史复用评估逻辑可借鉴到多轮会话推荐、客服Agent场景，区分全量复用/部分复用的效果差异，针对性优化瓶颈场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有Text-to-SQL基准均独立评估单条查询，忽略同库下历史查询的可复用价值，无法衡量历史SQL适配的准确率与成本。

### 方法关键点
1. 构建历史感知Text-to-SQL基准HARE，包含1600条请求、823条验证查询，标注区分全查询适配与部分复用场景
2. 设计MEM-SQL分层内存架构，存储全查询模板、可复用SQL块、领域概念到schema的映射，仅当匹配度达标时启用对应内存层
3. 提出按需Schema Linking（OSL）机制，仅在无匹配内存层或生成证据不足时查询schema

### 关键结果
在6个LLM上测试，对比无历史的直接生成，MEM-SQL平均执行准确率从37.1%提升到50.0%，输入token减少76.6%，延迟降低68.8%；多查询复用场景为当前瓶颈，准确率从56.7%降至29.7%；OSL可通用降低其他内存设计的生成成本
