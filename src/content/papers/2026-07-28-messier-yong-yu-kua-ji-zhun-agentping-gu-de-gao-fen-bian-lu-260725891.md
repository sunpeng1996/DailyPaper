---
title: 'Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation'
title_zh: Messier：用于跨基准Agent评估的高分辨率统一语料库
authors:
- Stefan Krsteski
- Charlotte Meyer
- Guillaume Allegre
- Tony O'Halloran
- Alexandre Sallinen
affiliations:
- Andromede AI
arxiv_id: '2607.25891'
url: https://arxiv.org/abs/2607.25891
pdf_url: https://arxiv.org/pdf/2607.25891
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: Agent 跨基准统一评估语料构建
tags:
- Agent Evaluation
- Benchmarking
- Corpus
- LLM Agent
- Capability Measurement
one_liner: 整合30个Agent评估基准、近百万条记录的标准化统一评测语料库
practical_value: '- 构建内部Agent（电商客服、导购、工单处理等）评测体系时，可复用其标准化schema，统一建模model、scaffold、环境、验证器、聚合规则5个维度，确保不同任务的评测结果可横向对比

  - 多步骤流程类Agent的评测不要仅用all-pass聚合规则，需同时上报单个验证维度的通过率，既可以避免掩盖部分能力的迭代提升，也能更精准定位Agent的能力短板

  - 做Agent选型或能力迭代对比时，可直接复用该语料的公开能力排序结果（尤其是工具调用、企业工作流类任务），无需重新跑全量基准，大幅降低评测成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Agent评估领域存在严重的基准碎片化问题，不同基准的任务设定、验证规则、打分聚合逻辑差异极大，跨基准结果不可比；现有评估数据集要么覆盖场景窄、要么粒度仅到任务级，无法支撑细粒度能力分析，重新跑全量评测的成本极高（单次大规模扫测可达4万美元），大量重复计算造成资源浪费。

### 方法关键点
- 设计统一数据schema，对Agent（model+scaffold）、交互环境、任务、验证器、聚合规则做标准化建模，每个任务额外标注SOC职业分类、NAICS行业分类，支持分领域切片分析
- 整合24个公开基准的历史评测结果，补充6个低覆盖专业领域（法律、临床、量子算法设计等）的5个主流Agent跑测结果，所有记录保留验证器级细粒度数据
- 内置支持反事实重打分、IRT能力建模、任务难度预预测等下游分析能力，新基准扩展无需修改核心合并逻辑

### 关键结果
- 语料总规模达957253条记录，覆盖30个基准、714个Agent、11891个任务、74205个验证器，规模远超同类数据集
- 基于语料训练的IRT能力模型和Epoch ECI排名的Spearman ρ达0.81，其中编程领域0.77、数学领域0.84，能力排序可信度高
- 反事实打分验证：all-pass聚合规则会严重压低通过率，如法律基准HarveyAI-Lab的all-pass通过率仅0.2%，但平均单验证维度通过率达28.8%，且会改变Agent排名
- 各领域Agent进展不均：函数调用能力已接近饱和（前沿准确率0.97），企业工作流类任务准确率仅0.57，是当前最大短板

### 核心结论
Agent评估的最终分数对聚合规则高度敏感，仅靠单值通过率会掩盖大量真实能力信息，细粒度的验证器级记录是可信跨基准对比的基础
