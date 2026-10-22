---
title: 'MemoryTax: The Bitter Lesson of Agent Memory'
title_zh: 《MemoryTax：Agent 记忆系统的苦涩教训》
authors:
- Zedong Peng
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2610.29823'
url: https://arxiv.org/abs/2610.29823
pdf_url: https://arxiv.org/pdf/2610.29823
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent 记忆系统性价比实测
tags:
- Agent Memory
- Cost Efficiency
- Mem0
- Zep
- LLM Agent
one_liner: 实测证明预构建 Agent 记忆是弱模型的昂贵补丁，强模型用原生搜索工具性价比更高
practical_value: '- 针对业务所用 LLM 能力分层选记忆方案：用 GPT-4o-mini 级小模型可上 Mem0 类预构建记忆，用 GPT-6/Claude
  Opus 级强模型直接做原始上下文检索即可，成本更低。

  - 记忆系统效果上限由构建记忆的模型能力决定，不要指望强推理模型补全弱模型提取记忆时丢失的信息，构建记忆尽量用同级别或更强的模型。

  - 多模态电商 Agent 场景不要提前压缩原始数据（如商品图 caption、会话原文），留给强模型自带的搜索工具读取，准确率更高成本更低。

  - 仅当单份历史会话需要响应超 500 次查询时，再考虑投入成本预构建 Mem0/Zep 类记忆，否则全上下文或 BM25 检索性价比更高。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前 Agent 记忆系统（如 Mem0、Zep）普遍提前预提取存储信息，但 Sutton 提出的「苦涩教训」指出通用可扩展方法最终会超过专用设计方案，当 LLM 能力足够强时，预构建记忆是否还有价值、性价比如何缺乏严谨实证。

### 方法关键点
- 对比 7 种记忆/检索方案：全上下文、BM25、Mem0、Zep、Pi 编码 Agent、Codex、Claude Code
- 覆盖 3 档能力模型：GPT-4o-mini、GPT-6 Luna、Claude Opus 5.5
- 全链路统计成本：包含记忆构建、模型调用、embedding 全环节的官方定价，以及 152 个问题的回答准确率

### 关键结果
基于 LoCoMo 基准的 419 轮长会话、152 个记忆类问题测试：
1. 弱模型场景下 Mem0 准确率 78%略高于全上下文的 74%，但仅记忆构建成本就超过全上下文整次运行的总成本；
2. 强模型场景下 Claude Opus 5.5 搭配 Pi Agent 准确率达 99%，成本仅为同模型全上下文方案的 39%，88 个无图片证据的问题下两者准确率差仅 1%；
3. 记忆系统准确率上限由构建记忆的模型决定，用 GPT-4o-mini 构建的 Zep 记忆，哪怕换 Claude Opus 读取准确率也仅 45%，远低于 Opus 自建记忆的 87%。

最值得记住的一句话：强模型需要的不是精心设计的预构建记忆，而是更好的原始记录搜索工具。
