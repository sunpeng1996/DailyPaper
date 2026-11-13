---
title: Discovering Effective Agent Memory Designs through Program Evolution
title_zh: 基于程序进化的Agent内存最优设计自动发现框架
authors:
- Xinheng Ding
- Seyyed Saeid Cheshmi
- Ziyang Zhang
- Tairan Chen
- Wenya Xie
- Yu Hou
- Rui Zhang
- Zirui Liu
affiliations:
- University of Minnesota
- Stevens Institute of Technology
arxiv_id: '2611.17068'
url: https://arxiv.org/abs/2611.17068
pdf_url: https://arxiv.org/pdf/2611.17068
published: '2026-11-12'
collected: '2026-11-13'
category: Agent
direction: Agent 长时记忆系统自动优化
tags:
- Agent_Memory
- Program_Evolution
- LLM_Agent
- Memory_Optimization
- RAG
one_liner: 提出MAPE全程序进化框架自动发现Agent内存设计，较手动基线精度升12%成本降65%
practical_value: '- 可直接复用两个验证有效的内存设计模式：保留原始对话作为可检索证据避免摘要丢失细节，按查询意图路由到不同证据合成模板提升信息利用率，适配电商导购、客服等对话Agent场景

  - 控服务成本可优先将计算从build阶段的LLM预提取记忆，转移到query阶段的按需处理，适配用户历史多、单历史查询次数少的场景，能降40%-90% LLM调用量且精度损失极小

  - Query-Routed Scaffolding（RQS）模块可直接移植到现有RAG/记忆系统，仅修改后处理逻辑就能获得2.8%-9.3%的绝对精度提升，落地成本极低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent内存系统高度依赖人工设计，多数优化仅关注精度忽略服务成本，且难以跨场景、跨模型迁移，缺少系统化自动搜索最优内存架构的通用方法。

### 方法关键点
- 将内存系统拆分为build/retrieve/compose三个可编程阶段，从无记忆的最小种子启动迭代进化，支持纯精度优化（MAPE-A）和精度-成本联合优化（MAPE-P）两种目标
- 迭代采用诊断-提案闭环：先定位当前程序的失败模式，再基于历史存档的有效设计生成新候选，全量保留所有候选的代码、效果、失败归因避免局部最优
- 最终基于帕累托最优筛选可落地的无明显性能瓶颈的设计

### 关键实验
在LoCoMo、LongMemEval两个长时记忆基准上测试，对比Mem0、A-Mem、Zep等5种人工设计内存系统：
- MAPE-A精度最高较基线提升12%，MAPE-P在精度仅降2.76%的情况下，服务成本仅为最优手动基线的35%
- 进化出的RQS模块移植到5种现有内存系统，全部获得2.8%-9.3%的绝对精度提升
- 最优设计跨GPT-4.1 mini、Qwen3-30B两个backbone、跨两个基准均能保留核心效果增益

**最值得记住的结论**：多数人工设计的内存系统因丢弃原始对话导致信息丢失，优先保留原始可检索证据+按意图后处理的收益远高于复杂的预构建记忆结构
