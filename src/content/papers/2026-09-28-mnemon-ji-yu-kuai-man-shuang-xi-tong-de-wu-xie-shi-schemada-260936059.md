---
title: 'Mnemon: Raw Records, Fast Judgments, Slow Thoughts'
title_zh: Mnemon：基于快慢双系统的无写时Schema大模型Agent长期记忆框架
authors:
- Guangren Wang
arxiv_id: '2609.36059'
url: https://arxiv.org/abs/2609.36059
pdf_url: https://arxiv.org/pdf/2609.36059
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 长期记忆双系统优化
tags:
- LLM Agent
- Long-term Memory
- Dual Process
- Memory Retrieval
- No Schema
one_liner: 基于双系统认知理论拆分记忆任务，实现无写时预处理的高性价比Agent长期记忆系统
practical_value: '- 架构可复用双系统拆分思路：将RAG检索后的粗筛、相关性判断等简单yes/no任务交给专用小模型，查询生成、答案合成交给大模型，可大幅降低检索/记忆模块的
  latency 和成本，适合电商客服Agent用户记忆、用户长期行为检索等场景

  - 可放弃写时预处理方案：直接存储带时间戳的原始用户行为、对话、浏览记录，读时再做语义判断，避免写时提取丢失信息，且无需针对不同业务场景修改写入逻辑，适配多业务线共享用户历史的需求

  - 可复用ECI（有效成本指数）作为记忆/检索系统的业务评估指标：把错误修复成本和token成本结合，比单纯看准确率或token量更贴合业务成本优化目标

  - 离线背景任务构建轻量索引：生成话题时间线、值变更历史、长期指令三类索引指向原始记录，既不丢失原始信息，又能解决全局类查询（如用户近3个月所有运动鞋浏览记录）的召回问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM Agent长期记忆系统大多在写入阶段就将对话/记录提取为事实、知识图谱等结构化数据，既会浪费大量计算资源处理从未被查询的记录，又会因提前固定schema丢失原始信息，无法适配后续新增的查询需求，不同存储源还需适配不同提取逻辑，扩展性差。

### 方法关键点
- 借鉴认知科学双系统理论拆分记忆工作：System 2（大模型）负责慢任务，包括检索query生成、需求定义、答案合成；System 1（专用决策模型Jev）负责快任务，对检索到的原始记录做独立yes/no判断，如是否相关、是否过期、满足哪类需求
- 写入时无任何语义处理，仅存储带时间戳的原始记录+embedding，无固定schema，可对接任意返回带时间戳记录的存储源
- 背景离线任务合并生成话题时间线、值变更历史、长期指令三类索引，索引仅指向原始记录不替换原始数据，解决全局类查询召回不足问题
- 带明确预算的规则连接双系统，流程token消耗和latency有固定上限，不随历史长度线性增长

### 关键结果
在OmniMemEval公开评估的14个主流记忆系统中：用gpt-4.1-mini做System 2时，LoCoMo准确率91.7%（排名第一），LongMemEval-S准确率83.8%（排名第二），单问题上下文仅3.8k tokens，LoCoMo上ECI最低；用DeepSeek-V4.1-Flash做System 2时，LongMemEval-S准确率达94.4%，持平SOTA；历史长度从100K涨到10M tokens，单问题成本仅上涨11%；Jev判断黄金证据AUC达0.942，比gpt-4.1-mini高8.9个百分点，速度快3-11倍。

最值得记住的一句话：记忆系统的大部分读时工作属于可并行的简单判断任务，专用小模型读时决策的方案比写时预处理的方案准确率更高、扩展性更强、成本更低
