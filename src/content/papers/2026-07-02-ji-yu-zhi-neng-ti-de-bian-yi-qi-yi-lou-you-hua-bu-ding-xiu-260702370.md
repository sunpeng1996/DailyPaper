---
title: Understanding Agent-Based Patching of Compiler Missed Optimizations
title_zh: 基于智能体的编译器遗漏优化补丁修复效果研究
authors:
- Batu Guan
- Zirui Wang
- Shaohua Li
affiliations:
- The Chinese University of Hong Kong
arxiv_id: '2607.02370'
url: https://arxiv.org/abs/2607.02370
pdf_url: https://arxiv.org/pdf/2607.02370
published: '2026-07-02'
collected: '2026-07-05'
category: Agent
direction: 编码Agent · 代码优化补丁生成
tags:
- Coding Agent
- LLVM
- Compiler Optimization
- Knowledge Augmentation
- RAG
one_liner: 系统评测编码Agent修复LLVM遗漏优化的效果，提出历史知识增强方法提升泛化对齐性
practical_value: '- 做Agent领域特定任务优化时，可复用「历史提交检索+蒸馏」的知识增强范式，提升输出与业务预期的对齐度

  - 做Agent任务效果评估时，不能只看单case通过率，需新增同类场景泛化覆盖度的评测维度

  - 涉及领域规则迭代类业务（如推荐规则、广告审核规则补全），可参考本文构建真实问题基准的方法'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
编译器遗漏优化修复需耗费大量研发人力，现有编码Agent修复方案的泛化能力未被系统验证，仅能修复单case、无法覆盖同类场景是核心痛点。
### 方法关键点
1. 构造真实LLVM遗漏优化问题基准，从优化覆盖范围维度对比Agent生成补丁与开发者补丁的效果
2. 采用历史知识增强技术，通过检索+蒸馏过往LLVM优化PR，提升Agent修复的泛化对齐性
### 关键结果
当前编码Agent仅能覆盖开发者预期优化范围的部分场景，仅少量场景下泛化能力超过人工参考补丁；引入历史知识增强后，Agent与开发者预期对齐的泛化能力显著提升，在真实IR场景下可产生实际收益。
