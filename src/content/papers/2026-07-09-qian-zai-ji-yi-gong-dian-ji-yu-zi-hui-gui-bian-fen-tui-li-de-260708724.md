---
title: 'Latent Memory Palace: Reasoning for Control as Autoregressive Variational
  Inference'
title_zh: 《潜在记忆宫殿：基于自回归变分推理的控制推理方法》
authors:
- Chuning Zhu
- Eva Xu
- Jose Barreiros
- Krishnan Srinivasan
- Paarth Shah
- Abhishek Gupta
affiliations:
- University of Washington
- Toyota Research Institute
arxiv_id: '2607.08724'
url: https://arxiv.org/abs/2607.08724
pdf_url: https://arxiv.org/pdf/2607.08724
published: '2026-07-09'
collected: '2026-07-11'
category: Reasoning
direction: 潜空间推理 · 连续控制策略优化
tags:
- Latent Reasoning
- Variational Inference
- Autoregressive Model
- Continuous Control
- Reinforcement Learning
one_liner: 提出基于自回归潜空间变分推理的潜在记忆宫殿框架，实现连续控制任务的自适应推理与性能提升
practical_value: '- 可将自回归潜空间的自适应迭代推理思路迁移到Agent决策模块，替代固定步数的推理链，动态分配计算资源，降低复杂任务的推理延迟

  - 变分推断优化下界的训练方法可复用在生成式推荐的离散/连续潜变量建模中，提升Semantic ID序列生成的稳定性

  - 可变长tokenizer的设计思路可用于推荐系统动作（如营销触达时机、出价策略）的编码，适配下游自回归排序模型的输入需求'
score: 5
source: arxiv-cs.LG
depth: abstract
---

### 动机
LLM自适应推理能力难以迁移至连续控制场景，语言空间推理粒度不足，无法支撑空间理解与精准动作决策，现有连续控制策略缺乏动态调整推理成本的能力。
### 方法关键点
将控制推理建模为自回归潜分布下的变分推理任务，提出Latent Memory Palace (LMP)框架，设计潜空间强化学习方法可高效优化变分下界，同时衍生得到可变长动作编码器LMP-tok。
### 关键结果
LMP-π策略在仿真与真实世界控制任务上实现SOTA性能，支持测试时计算资源的可解释自适应分配；LMP-tok大幅优于固定长度动作编码方案，显著提升下游自回归控制策略性能。
