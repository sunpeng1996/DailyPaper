---
title: 'When2Think: Learning Difficulty-Aware Length Control for Efficient Hybrid
  Reasoning Models'
title_zh: When2Think：面向高效混合推理模型的难度感知推理长度控制框架
authors:
- Jaejun Shim
- HyunJin Kim
- Young Jin Kim
- JinYeong Bak
affiliations:
- Sungkyunkwan University
- Microsoft
arxiv_id: '2609.19671'
url: https://arxiv.org/abs/2609.19671
pdf_url: https://arxiv.org/pdf/2609.19671
published: '2026-09-16'
collected: '2026-09-18'
category: Reasoning
direction: 大模型推理 · 自适应计算分配
tags:
- Hybrid Reasoning
- Efficiency Optimization
- Reward Shaping
- Reinforcement Learning
- Difficulty Awareness
one_liner: 提出无额外奖励模型的难度感知后训练框架，优化推理模型的精度-效率权衡
practical_value: '- 电商智能客服、复杂query理解场景可借鉴IDAC机制，给不同难度的用户请求（如简单查物流vs复杂售后咨询）动态分配推理深度，降低token消耗同时提升准确率

  - 电商导购Agent、RAG系统可复用离线预计算样本难度的方案，提前对常见query聚类打难度分，运行时直接调用难度标签控制推理长度，无需在线查询参考模型，降低延迟

  - 做生成式推荐的RLHF优化时，可复用Batch-Wise Standardized Advantage的critic-free训练方案，无需单独训练critic模型，减少训练开销同时提升收敛稳定性

  - 端侧Agent、离线批量推理任务可优先接入该框架，对小参数推理模型的优化增益最明显，可在小模型上拿到接近大模型的效果同时降低推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前大推理模型（LRM）存在系统性效率问题：简单问题过度推理浪费算力，复杂问题推理不足导致精度下降；现有静态token压缩、固定路由方法会产生「效率税」，简单问题节省的算力往往换来复杂问题的精度损失，亟需按实例难度动态分配计算资源的方案。

### 方法关键点
- When2Think后训练框架将推理转化为实例级自适应计算分配问题，融合SYSTEM1快速响应和SYSTEM2深度推理能力
- 设计Instance-level Difficulty-Aware Control（IDAC）奖励塑造机制，离线预计算每个样本的参考准确率（难度α）和平均推理token数（预算τ），动态调节不同难度样本的推理深度奖励
- 结合可验证正确性奖励、Batch-Wise Standardized Advantage（BWS），实现无需学习奖励模型、无需critic的稳定PPO优化，训练时无在线参考模型查询开销
- 引入重要性采样（IS）平衡THINK/NOTHINK模式的探索，加速收敛到更优的效率-精度权衡点

### 关键实验
在GSM-Plus、OlympiadBench、AIME24/25等数学推理基准上，以R1-Distill-Qwen为基准对比LC-R1、ThinkPrune、LASER、AdaptThink等效率优化基线：AIME24上Pass@3提升10.0%，token用量减少27.9%；AIME25上Pass@3达40.0%，优于所有压缩、纯路由基线；MATH-500简单题token用量降低580，难题保持精度同时减少2276冗余token。

### 核心结论
推理效率的核心是计算资源的自适应分配，而非单纯的推理长度压缩，效率税来自于不同难度样本的计算错配而非模型容量不足。
