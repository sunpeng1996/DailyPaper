---
title: 'BALMS: Benchmarking Agentic LLMs for Longitudinal Mental Health Sensing'
title_zh: BALMS：面向纵向心理健康感知的Agent大语言模型基准测试
authors:
- Yu Yvonne Wu
- Arvind Pillai
- Yuliang Chen
- Yuwei Zhang
- Sudarshan Regmi
- Tess Z. Griffin
- Michael V. Heinz
- Lisa A. Marsch
- Nicholas C. Jacobson
- Andrew Campbell
affiliations:
- Dartmouth College
- University of Cambridge
arxiv_id: '2608.27219'
url: https://arxiv.org/abs/2608.27219
pdf_url: https://arxiv.org/pdf/2608.27219
published: '2026-08-27'
collected: '2026-08-30'
category: Agent
direction: Agent评测 · 长时序感知
tags:
- Agent
- Benchmark
- Longitudinal Data
- LLM-as-Judge
- Chain-of-Thought
one_liner: 首次推出面向可穿戴长时序数据的心理健康感知Agent大模型系统评测基准BALMS
practical_value: '- 长时序用户行为建模（如跨周期消费/偏好推理）可借鉴本工作结论，优先给LLM喂语义压缩特征而非原始时序数据，兼顾推理成本与效果

  - 涉及长序列证据对齐的Agent业务（如用户投诉溯源、长期偏好归因）可采用LLM-as-Judge做自动评测，大幅降低人工标注成本

  - 长时序推理类Agent任务不要盲目上零-shot方案，优先选择「强基座+CoT提示+小样本微调」的组合方案，落地效果更可控'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统心理健康评估依赖稀疏自报告问卷仅能获得健康状态快照，现有基于LLM的个人健康Agent仅支持短期可穿戴数据检索查询，缺乏长时序推理预测+证据对齐的系统评测标准。
### 方法关键点
推出BALMS基准，覆盖3个真实世界纵向可穿戴数据集，包含两类任务：闭式健康得分预测、LLM-as-Judge自动评分的推理依据生成，在5个开源/闭源LLM基座上对比评测3种Agent范式。
### 关键结果
零-shot Agent几乎无法超过简单均值基线，仅搭配强基座或输入紧凑语义特征时存在效果提升；CoT提示对推理导向基座有正向作用，但无法保证时序对齐和数值正确性，时序长度增大时效果衰减更显著。
