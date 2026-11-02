---
title: 'MemSteer: Turning User Histories into Supervision for Agent Memory Optimization'
title_zh: MemSteer：基于无标注用户历史的Agent记忆系统自动优化框架
authors:
- Jie Huang
- Cuiling Lan
- Qize Yu
- Xiulian Peng
- Yan Lu
affiliations:
- Peking University
- Microsoft Research Asia
arxiv_id: '2610.39276'
url: https://arxiv.org/abs/2610.39276
pdf_url: https://arxiv.org/pdf/2610.39276
published: '2026-10-28'
collected: '2026-11-02'
category: Agent
direction: Agent 记忆系统自动化优化
tags:
- Agent_Memory
- Synthetic_QA
- Memory_Optimization
- RAG
- LLM_Agent
one_liner: 无标注用户历史自动生成带证据QA对，实现媲美人工标注的Agent记忆设计优化
practical_value: '- 个性化Agent记忆优化可直接复用这套无标注QA生成流程，无需人工标注测试集，大幅降低自定义记忆系统调优成本，尤其适配电商用户会话、浏览历史等无标注数据场景

  - 可复用分层故障诊断逻辑：将记忆系统错误分为存储失败、检索失败、回答失败三类，针对性优化召回、切片规则等模块，比盲目调参效率更高，适合RAG类推荐/导购Agent的错误归因

  - QA生成的双校验流程（来源审计+盲答恢复）可直接用于推荐场景合成训练数据生成，过滤低质量合成样本，提升SFT/RLHF的样本质量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent记忆系统优化依赖人工标注的QA对作为监督信号，标注成本极高，且不同用户的历史数据特性差异大，单一记忆设计无法适配所有用户，亟需无需人工标注的记忆系统自动优化方案。

### 方法关键点
- 构建用户历史关系图，采样关联子图作为素材包，生成带来源跨度引用的证据支撑回答计划，基于计划生成对应问题
- 双校验机制过滤低质量QA：先做来源一致性审计，再做盲答恢复校验，只有答案可被素材包准确复现、证据覆盖完整的QA对才会被保留
- 配套MemSteer-Opt优化器：基于QA测试结果做故障分层诊断，区分存储、检索、回答三类错误，针对性迭代优化记忆的存储粒度、检索策略、上下文拼接规则，无需更新模型参数

### 关键实验
在ATM-Bench和RHELM两个公开记忆基准测试，对比Base-BM25基线，MemSteer-Opt将ATM-Bench的Question Score提升13.4分，Hard多跳集提升20.9分；RHELM准确率在无外部数据时提升4.1分，有外部数据时提升6.6分，效果与人工标注QA引导的优化基本持平，生成的监督信号还可直接给M*、MemEvolve等现有记忆优化器使用，均有明显效果提升。

### 核心结论
无标注用户历史本身就可以作为高质量的监督信号来源，无需人工标注就能完成Agent记忆系统的针对性调优，效果接近人工标注水平。
