---
title: '$β$-OPSD: Deriving with Policy Optimization, Training with Self-Distillation'
title_zh: β-OPSD：基于策略优化推导与自蒸馏训练的大模型优化框架
authors:
- Jiawei Xu
- Minghui Liu
- Juzheng Zhang
- Tom Goldstein
- Furong Huang
affiliations:
- University of Maryland, College Park
arxiv_id: '2607.28582'
url: https://arxiv.org/abs/2607.28582
pdf_url: https://arxiv.org/pdf/2607.28582
published: '2026-07-30'
collected: '2026-07-31'
category: Training
direction: 大模型训练 · 自蒸馏与策略优化融合
tags:
- Self-Distillation
- Policy Optimization
- KL Regularization
- LLM Training
- Reasoning
one_liner: 将OPSD重构为KL正则化策略优化家族，通过调度logit插值和return-to-go提升稳定性与推理性能
practical_value: '- 做LLM驱动的导购Agent多轮决策、生成式推荐文案生成时，可复用β-OPSD的logit插值调度策略，避免直接对齐教师模型导致的训练不稳定，降低工程调优成本

  - 长序列生成场景（如商品卖点长文案生成、搜索query多轮改写）可引入return-to-go信用分配机制，解决局部token更新的短视问题，提升序列级生成质量

  - 做小参数模型自蒸馏/对齐时，可参考动态学生+固定教师的插值端点设计，平衡学生分布跟踪与稳定监督信号，最大化小模型效果提升幅度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
On-policy自蒸馏（OPSD）是提升LLM推理能力的主流方案，但实际应用中鲁棒性差，需要大量工程调优；现有OPSD直接对齐教师模型，没有显式控制学生向参考策略的对齐强度，更新过于激进易导致分布偏移、训练崩溃。

### 方法关键点
- 重构OPSD为KL正则化策略优化家族的β=1特例，将β作为可控正则化参数，权衡参考策略对齐与教师指导强度
- 推导最优策略为参考策略与特权教师的几何插值，通过token级logit加权插值实现，避免直接RL优化的高成本与高方差
- 引入return-to-go信用分配，将未来token的匹配误差回传至早期token，解决局部token更新的短视问题，对齐序列级优化目标
- 训练时采用线性调度的教师权重（默认0.5→0.8），逐步提升教师指导强度，形成平滑学习课程

### 关键实验
在Qwen3 1.7B/4B/8B模型上基于数学推理数据集训练，对比Base、SFT、Vanilla OPSD、GRPO等基线，在AIME2024、AIME2025、HMMT2025基准上，1.7B模型较Vanilla OPSD平均提升5.74个百分点，最高单基准提升9.16个百分点；4B、8B模型分别平均提升1.76、1.66个百分点。

### 核心结论
无需引入复杂RL机制，仅通过调度logit插值与return-to-go信用分配，即可在保留OPSD高效性的同时大幅提升其稳定性与下游性能。
