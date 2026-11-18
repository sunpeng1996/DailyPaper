---
title: 'From Imperfective Paradox to Moorean Absurdity: Single-Chain Reasoning Lock-In
  and Multi-Candidate Verbalization Across Aspectual and Pragmatic Ambiguity'
title_zh: 单链推理锁定效应与多候选言语化消解体貌及语用歧义研究
authors:
- An-Sheng Jhang
affiliations:
- Dongguan University of Technology
arxiv_id: '2611.22188'
url: https://arxiv.org/abs/2611.22188
pdf_url: https://arxiv.org/pdf/2611.22188
published: '2026-11-17'
collected: '2026-11-18'
category: Reasoning
direction: 大模型推理优化 · 多候选言语化协议
tags:
- LLM Reasoning
- Prompt Engineering
- Ambiguity Resolution
- Multi-Candidate Verbalization
- Model Calibration
one_liner: 提出多候选言语化（MCV）协议缓解大模型单链推理过早锁定单一评估标准的偏差
practical_value: '- 做Agent复杂决策时可复用MCV模式：单轮prompt要求生成K个候选判断+权重，无需多次调用，既缓解单链CoT过早锁定偏差，也比多次采样节省推理成本

  - 处理Query理解、商品属性歧义、用户评价语义歧义场景时，可采用MCV的等权聚合（MCU）替代单输出判断，降低单一语义标准导致的分类错误

  - 确定性解码（temperature=0.0）场景下可直接复用MCV框架：通过候选间上下文条件依赖实现多视角探索，避免greedy解码的模式坍缩问题

  - 做模型效果评估时，可同时采集离散标签、单值概率、多候选聚合三类结果，避免单一评估指标掩盖模型的标准选择偏差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大模型在体貌蕴含、语用歧义判断任务中，单链推理+单输出瓶颈会导致过早锁定单一评估标准，出现双向偏差：要么过度投射目标事件完成状态，要么因隐含多标准要求直接输出极端判断，现有单输出评估范式无法区分是模型语义能力不足还是评估标准选择偏差。

### 方法关键点
- 提出Multi-Candidate Verbalization（MCV）协议：单轮prompt要求模型输出K=5个概率估计+对应权重，衍生等权聚合（MCU）、自加权聚合（MCW）两种读out方式，无需额外训练
- 设计4组预注册实验覆盖中英文体貌歧义、摩尔语用歧义场景，所有核心实验在Qwen3-8B-Q8_0上用temperature=0.0确定性解码执行，避免采样随机性干扰
- 统计层面采用Holm步降法控制家族错误率，缺失值用最坏情况Manski边界处理，保证结论的统计严谨性

### 关键结果
- 英文体貌任务中，MCV的MCU方案将单链CoT的完成状态过度投射率降低25.00pp，将无终止事件的判断准确率损失挽回91.25pp
- 摩尔语用歧义任务中，MCU-CF方案比单链CoT的语义一致性判断准确率提升26.64pp，其中多候选协议本身贡献17.31pp增益
- 跨5个大模型的泛化实验显示，MCV在90%以上的预注册假设槽位上取得统计显著的效果提升，格式解析成功率接近100%

### 核心结论
大模型的很多推理“错误”本质是单输出瓶颈导致的评估标准锁定偏差，无需微调、仅通过多候选言语化的prompt工程即可大幅缓解。
