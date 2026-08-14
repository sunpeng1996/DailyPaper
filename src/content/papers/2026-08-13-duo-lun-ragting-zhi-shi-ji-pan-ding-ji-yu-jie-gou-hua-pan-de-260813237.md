---
title: When Should Multi-Round RAG Stop? Structured Stopping Judgments and Retrieval
  Reduction in Search-R1
title_zh: 多轮RAG停止时机判定：基于结构化判断的Search-R1检索降本方案
authors:
- Weimeng Luo
affiliations:
- Unaffiliated
arxiv_id: '2608.13237'
url: https://arxiv.org/abs/2608.13237
pdf_url: https://arxiv.org/pdf/2608.13237
published: '2026-08-13'
collected: '2026-08-14'
category: RAG
direction: 多轮RAG · 停止策略优化
tags:
- Multi-round RAG
- Stopping Policy
- Search-R1
- Structured Judge
- Adaptive Retrieval
one_liner: 适配S2G结构化判断训练Qwen3.5-2B停止法官，在Search-R1上降检索量同时控制准确率损失
practical_value: '- 多轮RAG Agent的停止决策不能用独立状态分类评估，必须按轨迹首停逻辑做端到端验证，避免状态AP高但实际系统效果差的错位问题

  - 做RAG停止策略可复用「sufficiency判定+gap缺失信息标注」的结构化范式，相比纯二分类标注能大幅减少过停止错误，降低准确率损失

  - 上线前可先做可达性审计，测算当前多轮检索系统的可优化空间，避免在无降本空间的场景投入无效研发

  - 停止阈值需在独立验证集上冻结后再进测试，同时预设可接受的准确率损失阈值，平衡成本和效果风险'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多轮RAG（尤其是Search-R1这类检索增强Agent）存在停止决策难题：检索不足会导致答案缺少支撑，过度检索则会浪费算力、提升延迟，甚至额外上下文干扰把正确答案改错。现有停止策略多做独立状态分类，忽略实际线上是按轨迹中首次触发停止阈值来决策的逻辑，导致状态评估指标和实际系统效果错位，很难落地。

### 方法关键点
- 不修改原有Search-R1的推理器、检索器、语料、prompt和最大4次检索的限制，仅新增独立的停止法官模块做决策
- 复用S2G-RAG的结构化判断范式，训练Qwen3.5-2B小模型输出是否sufficient的布尔值+缺失信息gap_items列表，用结构化标注正则化训练，减少过停止
- 评估链路分四层：可达性审计（判断当前状态是否能生成正确答案）、状态排序（法官对安全停止状态的排序能力）、首停判定（实际触发停止的最早状态）、系统效果（最终准确率+检索成本）
- 阈值在独立分组验证集上冻结，预设准确率损失不超过2个百分点的非劣效门槛，避免数据泄露

### 关键结果
基于HotpotQA数据集训练，800条样本的确认测试集上，对比原生Search-R1：检索调用减少3.70%，Exact Match仅下降0.625个百分点，符合预设非劣效要求。

### 核心结论
多轮RAG的停止策略不能只看状态级精度，必须基于轨迹首停逻辑做端到端评估，且检索量下降不等于总推理成本下降，需额外考虑法官模块的算力开销
