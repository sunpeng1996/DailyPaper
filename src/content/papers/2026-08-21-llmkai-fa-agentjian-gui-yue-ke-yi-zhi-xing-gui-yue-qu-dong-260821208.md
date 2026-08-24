---
title: 'Specification Portability Across LLM Development Agents: Cross-Agent Compatibility
  in Specification-Driven Software Migration'
title_zh: LLM开发Agent间规约可移植性：规约驱动软件迁移的跨Agent兼容性
authors:
- Oleg Grynets
- Oleksii Ilchuk
- Dariia Zatulna
- Vasyl Lyashkevych
affiliations:
- EPAM Systems
arxiv_id: '2608.21208'
url: https://arxiv.org/abs/2608.21208
pdf_url: https://arxiv.org/pdf/2608.21208
published: '2026-08-21'
collected: '2026-08-24'
category: MultiAgent
direction: 多Agent协作 · 规约可移植性优化
tags:
- MultiAgent
- Specification Portability
- Software Migration
- Cross-Agent Compatibility
- RAG
one_liner: 以Oracle到PostgreSQL迁移为测试任务，验证跨Agent规约复用的性能衰减特征及可行优化路径
practical_value: '- 多Agent协作链路中不可默认规约是Agent中立的，需针对每个下游Agent做单独规约适配，避免效果陡降

  - RAG增强的规约摄入是多Agent场景下通用的效果优化策略，可优先落地验证

  - 跨Agent规约适配优先选择针对性改写方案，而非盲目压缩规约长度，改写收益更稳定'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前规约驱动的LLM开发Agent已广泛落地，但不同Agent生成的规约是否可跨Agent复用、是否会导致效果衰减缺乏量化验证

### 方法关键点
以Oracle到PostgreSQL的SQL迁移为受控任务，分两阶段实验：1）在1006个PL/SQL文件上验证规约优先的迁移管线效果；2）基于1802组Oracle-PostgreSQL对应脚本，测试Amazon Kiro、Google Gemini、GitHub Copilot等多Agent的跨Agent规约复用表现，采用Token F1、SQL语法有效性、AST相似度等多维度指标评估

### 关键结果数字
- 规约大小无法预测实现质量，跨Agent规约复用存在显著的Agent依赖型性能衰减，极端场景下Gemini直接使用Kiro生成的规约时，Token F1仅0.035、SQL语法有效性仅2.33%
- 规约改写可大幅提升Gemini跨Agent适配效果，压缩无通用收益，RAG增强摄入是Gemini和Copilot均适用的帕累托最优策略
