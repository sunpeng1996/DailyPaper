---
title: 'Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness
  Evolution'
title_zh: Video-RSI：基于Harness演化的视频理解Agent递归自提升框架
authors:
- Bingjun Luo
- Jialin Guo
- Siqi Li
affiliations:
- Tsinghua University
- Harbin Engineering University
arxiv_id: '2609.37950'
url: https://arxiv.org/abs/2609.37950
pdf_url: https://arxiv.org/pdf/2609.37950
published: '2026-09-28'
collected: '2026-10-12'
category: Agent
direction: Agent自演化 · 视频理解
tags:
- Agent Self-Improvement
- Video Understanding
- Harness Evolution
- Cost-aware Optimization
- Frozen LLM
one_liner: 固定大模型权重下通过主动视频调查与成本感知Harness演化同步提升视频理解准确率与推理效率
practical_value: '- 迭代多模态Agent时无需优先做全量微调，可先优化执行harness逻辑，固定LLM权重大幅降低迭代成本，同时快速验证策略效果

  - 故障诊断不要仅依赖历史执行trace，可回溯原始样本做主动调查，明确区分漏采样、感知错误、逻辑误用三类根因，避免盲目修改规则

  - 策略上线筛选可复用双目标门控规则：要么准确率提升且算力/请求成本增幅不超预设阈值，要么成本下降且准确率损失在业务容忍范围内，平衡效果与开销

  - 电商短视频/直播理解、商品视频内容检索场景可复用结构化感知+证据关联图的设计，降低重复抽帧成本，同时提升时序类、关系类查询的准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视频理解Agent的执行harness直接决定观测采集与推理逻辑，但仅依赖历史执行trace的迭代无法区分故障根因（采样缺失/感知错误/逻辑误用），且迭代时仅以准确率为目标容易导致观测成本飙升，在固定LLM权重的约束下很难同步实现效果提升与成本优化。

### 方法关键点
- 单冻结LLM同时承担Solver（执行视频问答任务）和Editor（故障诊断与harness代码修改）角色，全程不更新模型权重
- 主动视频调查模块：遇到故障时回溯原始训练视频，针对性发起多维度观测请求验证根因，输出跨样本可复用的harness修改方案
- 双目标成本感知门控：候选harness在私有验证集测试，仅保留两类优化：①准确率提升且帧处理量增幅≤10%；②帧处理量降幅≥20%且准确率损失不超过1个样本

### 关键实验
在MLVU、LongVideoBench、Video-MME、EgoSchema4个主流长视频理解基准测试，对比VideoSeek、VideoHarness-RSI等同基座基线：MLVU测试集上准确率提升4.8pp，帧处理量降低27.2%；LongVideoBench上准确率持平，帧处理量降低42.8%；相比仅依赖trace迭代的版本，MLVU准确率最高提升8.2pp。

### 核心结论
固定大模型权重时，针对执行harness的观测逻辑、证据复用、推理流程做迭代优化，可实现效果和效率的双重提升，无需依赖全量微调或RL训练。
