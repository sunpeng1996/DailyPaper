---
title: 'UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability
  Dilemma'
title_zh: UP：无界正非对称优化破解RL训练探索-稳定性两难问题
authors:
- Chongyu Fan
- Pengfei Liu
- Jingjia Huang
- Sijia Liu
- Yi Lin
affiliations:
- ByteDance Seed
- Michigan State University
arxiv_id: '2607.06987'
url: https://arxiv.org/abs/2607.06987
pdf_url: https://arxiv.org/pdf/2607.06987
published: '2026-07-07'
collected: '2026-07-10'
category: Training
direction: LLM RL训练 · 探索稳定性优化
tags:
- RLHF
- Policy Optimization
- GRPO
- LLM Reasoning
- Training Stability
one_liner: 提出可插拔的非对称RL优化目标UP，在保证训练稳定的同时最大化LLM推理探索能力
practical_value: '- 现有基于GRPO/DAPO做Agent、生成式推荐RL对齐的业务，可直接将UP作为插件替换正优势分支的损失计算，无需改动其他流程即可提升长尾路径探索能力，且无训练稳定性风险

  - 正优势分支用stop-gradient自锚定替换传统ISπold锚点的设计，可迁移到推荐系统离策略更新场景，解决冷门优质商品/内容的梯度被提前截断、无法有效提权的问题

  - 「正样本无界强化、负样本保留截断约束」的非对称损失范式，可复用到电商/推荐的RL排序、召回模块的损失设计中，平衡探索效率与训练稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前基于重要性采样（IS）的RL算法是LLM推理对齐的主流方案，但存在固有探索-稳定性两难：纯无截断IS易引发梯度爆炸导致训练崩溃，而通用的截断机制会严格限制低置信度正确推理路径的更新预算，尤其是长尾优质轨迹的强化会被提前截断，严重抑制模型探索能力。

### 方法关键点
- 定义Probability Capacity（Cap）量化截断机制对策略更新幅度的约束，证明传统截断的Cap线性依赖历史策略πold，天然存在长尾路径更新上限的结构缺陷
- 非对称优化设计：正优势（正确轨迹）用stop-gradient算子将策略锚定到当前策略sg(πθ)而非πold，推导可知该结构等价于无截断REINFORCE梯度，完全解除正更新的Cap限制
- 负优势（错误轨迹）保留原有截断机制作为安全冗余，避免过度惩罚导致训练不稳定
- 可作为通用插件直接接入GRPO、DAPO、GSPO等所有GxPO族算法，兼容token级、序列级优化粒度，适配Dense、MoE、多模态各类模型架构

### 关键结果
- 对比11种SOTA RL基线，UP-GRPO在5个推理基准上平均Pass@1达61.31%，超出第二名GSPO 1.16个百分点
- UP-DAPO在AIME24数据集上Avg@32达51.15，较原生DAPO提升3.44，同时梯度范数、KL散度与基线持平，无训练不稳定问题
- 跨架构/模态适配性优异：UP-GSPO在MoE模型上AIME24 Avg@32提升3.02，UP-GRPO在多模态几何推理数据集上精度提升3.3

### 核心结论
正优势无界强化+负优势截断约束的非对称设计，是同时提升RL训练探索能力和稳定性的通用范式
