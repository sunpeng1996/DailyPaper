---
title: 'Agentic AutoRAG: RAG Pipeline Optimization through Reasoning-Driven Agents'
title_zh: Agentic AutoRAG：基于推理驱动Agent的RAG流程自动优化
authors:
- Lasse B. Strand
- Robert Jakob
- Kevin O'Sullivan
- Markus Kreft
affiliations:
- ETH Zurich
arxiv_id: '2610.08452'
url: https://arxiv.org/abs/2610.08452
pdf_url: https://arxiv.org/pdf/2610.08452
published: '2026-10-06'
collected: '2026-10-07'
category: RAG
direction: RAG流程优化 · Agent驱动
tags:
- RAG
- LLM Agent
- Hyperparameter Optimization
- Pareto Optimization
- Multi-objective Tuning
one_liner: 基于故障归因双Agent与模型知识库，少样本高效搜索RAG配置的准确率-成本帕累托前沿
practical_value: '- 业务侧优化商品问答、客服知识库、商家规则等RAG pipeline时，可复用诊断-提案双Agent框架，将错误归因到召回/生成环节，避免盲目搜参，大幅降低调优成本

  - 多目标优化场景（如推荐的准确率/时延/成本、RAG的效果/成本）可借鉴知识库预筛候选的思路，提前将公开模型排名、定价、业务约束喂给Agent，减少无效试错

  - RAG效果评估可复用自动生成带金标span测试集的方法，自动筛选能区分不同配置的测试用例，无需人工标注即可得到可信的优化目标'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG是LLM落地外部知识的核心方案，但配置RAG需要在分块、Embedding、召回、重排、生成等十几个耦合维度调参，现有搜参方法（贝叶斯优化、贪心搜索等）仅看聚合得分，不分析错误原因，试错成本高，且很难平衡准确率和推理成本的trade-off，对电商、广告等需要大规模部署RAG的场景，调优效率和成本控制需求迫切。

### 方法关键点
- 预生成冻结测试集：从目标语料自动生成带金标span的多跳问题，筛选能区分不同RAG配置的用例，所有试跑共用同一测试集保证结果可比
- 诊断-提案双Agent循环：每轮试跑后，Diagnoser把错误归因到召回（金标span未召回）或生成（召回但答错），输出精简诊断报告；Proposer基于诊断、历史试跑结果、内置模型知识库（公开排名、token定价）选择下一个测试配置，避免无效重复试错
- 多目标优化：支持同时优化准确率和单query成本，直接输出帕累托前沿供业务选择合适运营点

### 关键结果
在3个多跳QA基准上对比随机搜索、MO-TPE贝叶斯优化等基线，仅10轮试跑就达到基线30轮的效果；在医疗语料的成本感知模式下，准确率达77%，比最强基线的71.5%高5.5个百分点，单query成本仅为基线的58%，若对齐基线71.5%的准确率，成本仅为基线的22%。

最值得记住的一句话：给黑盒超参搜索加入领域知识和错误归因，能让RAG调优的效率和性价比提升数倍。
