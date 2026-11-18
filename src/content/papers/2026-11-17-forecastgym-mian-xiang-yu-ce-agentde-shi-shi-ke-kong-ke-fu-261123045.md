---
title: 'ForecastGym: A Live, Controlled, and Replayable Benchmark for Forecasting
  Agents'
title_zh: ForecastGym：面向预测Agent的实时可控可复现评测基准
authors:
- Yicheng Tao
- Yuante Li
- Zipei Fan
affiliations:
- Carnegie Mellon University
- Jilin University
arxiv_id: '2611.23045'
url: https://arxiv.org/abs/2611.23045
pdf_url: https://arxiv.org/pdf/2611.23045
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Agent 预测能力可控评测
tags:
- Agent
- Forecasting
- Benchmark
- Retrieval Augmented
- LLM Evaluation
one_liner: 前置采集预测问题的实时搜索证据，支持可控可复现的预测Agent多维度对比评测
practical_value: '- 做时序类Agent（如电商销量/流量预测Agent）评测时，避免使用事后搜索+日期过滤的方案，该方案最高可导致92%的问题泄露结果，造成评测效果虚高，建议采用实时证据采集方案

  - 检索增强类Agent的效果受搜索源的影响可能远大于LLM本身的差异：切换搜索API最多带来Brier score 0.043的波动，超过测试LLM间最大分差0.027，业务优化可优先调优搜索源与query策略而非盲目换大模型

  - 预测类Agent的记忆模块可采用自生成持久化笔记方案，效果与每次重读全量历史证据相当，但可节省一半输入token，大幅降低推理成本

  - LLM预测误差大部分来自缺失公开信息，而非模型误读内容，业务上优化query生成、多源检索补全信息的收益远高于调优推理prompt'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有预测Agent评测方案存在两大核心缺陷：实时评测允许各系统独立采集证据，无法分离检索能力与推理能力的贡献；事后回溯评测依赖日期过滤历史内容，存在严重的时间泄露，无法得到可信的对比结果，难以精准归因模型、搜索源、记忆策略各组件的效果贡献。
### 方法关键点
- 两阶段架构设计：第一阶段实时采集，针对未截止的预测市场问题，每2天调用4个商用搜索API获取结果，打时间戳存储为证据状态，全程在问题截止前完成，从根源避免信息泄露
- 可控重放机制：问题出结果后，离线按时间序回放冻结的证据，支持单变量控制（固定其他变量，单独调整模型/搜索源/记忆策略），可精准归因各组件的效果差异
- 内置6种记忆策略对比模式，支持独立验证记忆模块对预测稳定性与准确性的影响
### 关键结果
第一版数据集包含150个预测市场问题、614个时间戳证据状态、131k条搜索结果。核心实验结论：① 所有测试LLM的预测准确率均落后于真实预测市场，高误差状态中近3倍误差来自缺失公开信息，仅小部分来自模型误读；② 切换搜索API最多带来Brier score 0.043的波动，超过测试LLM之间的最大分差0.027；③ 自生成持久笔记的记忆策略效果与重读全量历史证据相当，但节省一半输入token。
> 最值得记住的一句话：预测Agent能获取的证据质量，和推理用的模型本身一样重要
