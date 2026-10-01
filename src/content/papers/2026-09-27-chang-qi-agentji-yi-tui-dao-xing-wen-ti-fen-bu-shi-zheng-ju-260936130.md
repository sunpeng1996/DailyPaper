---
title: 'Memory Is a Derivation: The Distributed-Evidence Paradox in Long-Term Agents'
title_zh: 长期Agent记忆推导性问题：分布式证据悖论与审计框架
authors:
- Hongjun Liu
- Chen Zhao
affiliations:
- New York University
arxiv_id: '2609.36130'
url: https://arxiv.org/abs/2609.36130
pdf_url: https://arxiv.org/pdf/2609.36130
published: '2026-09-27'
collected: '2026-10-01'
category: Agent
direction: Agent 长期记忆可靠性与验证
tags:
- Long-term Agent
- Memory Validation
- Factuality Audit
- Distributed Evidence
- Semantic Validation
one_liner: 提出DERIVAUDIT审计框架，揭示长期Agent记忆写入的分布式证据悖论，优化记忆验证可靠性
practical_value: '- 搭建电商导购/用户画像Agent的记忆模块时，不要仅依赖记忆自带的引用做有效性校验，可扩展检索写前12条BM25召回的历史交互记录，能挽回60%因引用不全被误拒的有效记忆，提升用户需求感知准确率。

  - 记忆写入校验需加入语义义务检查，不能只验证孤立事实的真实性，还要校验事实间的组合关系（比如用户说想买A又喜欢B，不要直接生成「用户要一起买A和B」的错误记忆），避免幻觉污染推荐策略。

  - 注意平衡验证粒度，不要过度拆分验证点，否则会引入累积验证噪声误删有效记忆，可优先用compact relation视图做组合校验，平衡无效记忆检测率和有效记忆保留率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长期LLM Agent需将交互历史压缩为持久记忆跨任务复用，但现有记忆写入机制存在两类核心缺陷：有效记忆因引用不全被误拒、单条合理的事实组合后生成历史不支持的错误记忆，错误记忆进入持久层后会持续干扰后续Agent决策，现有验证方法未同时覆盖证据扩展、组合语义校验需求，可靠性不足。

### 方法关键点
- 提出DERIVAUDIT审计框架，从三个维度校验记忆合法性：1）证据范围：对比仅引用片段、扩展检索最多12条写前BM25召回历史（总上限16条）两种证据视图，区分无效记忆和引用不全的有效记忆；2）组合有效性：将记忆拆分为语义义务（所有事实、关系、限定词都需被支持），校验整体语义而非孤立事实；3）准入可靠性：评估不同验证策略对有效记忆保留、无效记忆过滤的效果，以及错误准入的下游影响。
- 设计分布式证据对照实验，控制证据分布（单片段/多片段分散）和记忆有效性，验证分布式证据悖论的存在。

### 关键结果
基于LoCoMo、HaluMem-Medium两个公开数据集的400条真实记忆写入数据测试：扩展写前历史可挽回近60%仅靠引用判断为无效的有效记忆，仍有17-21%记忆扩展后仍无效；现有验证模型对无效记忆的准入率高达59-89%，仅扩展证据范围甚至会升高部分模型的无效记忆准入率；组合感知的扩展历史验证可提升引用补全的有效记忆保留率，但无法稳定降低无效记忆准入率，错误记忆和被误拒的有效记忆都会使下游任务失败率升高80pp以上。

最值得记住的一句话：长期Agent记忆不是历史的快照，而是从交互历史推导的结论，可靠的记忆写入既要找全证据，也要校验证据是否支持记忆的完整语义，而非仅检查孤立事实。
