---
title: 'Advancing Open and Reproducible Relational Learning: RelArena-α, TabPFN-Rel
  and RPI'
title_zh: 推进开放可复现关系学习：RelArena-α、TabPFN-Rel与RPI
authors:
- Adrian Hayler
- Klemens Flöge
- Alan Arazi
- Rishabh Ranjan
- Jure Leskovec
- Felix Birkel
- Brendan Roof
- Anurag Garg
- Kristina Collins
- Lydia Sidhoum
affiliations:
- Prior Labs
- Stanford University
- NVIDIA
- University of Freiburg
- ELLIS Institute Tübingen
arxiv_id: '2608.16319'
url: https://arxiv.org/abs/2608.16319
pdf_url: https://arxiv.org/pdf/2608.16319
published: '2026-08-16'
collected: '2026-08-18'
category: Eval
direction: 关系学习 · 统一评测与开源工具
tags:
- Relational Learning
- Open Source
- Benchmark
- Baseline
- Tabular Learning
one_liner: 开源三款关系学习工具，覆盖统一评测、强基线、通用预测接口
practical_value: '- 电商场景下多表用户/商品/行为数据建模，可优先尝试多表打平为单表的方案，开发成本低且效果不弱于专用关系架构

  - 内部算法迭代的评测体系可参考RelArena-α设计，标准化数据加载、评估协议、调参规则，大幅提升方法对比的可复现性

  - 业务侧多表预测需求可复用RPI的模型无关接口设计，降低不同预测模型切换对接的开发成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
过去几年关系学习领域涌现大量数据集与任务，但社区始终未形成可靠、可复现的方法对比标准，同时工业界落地关系学习的门槛较高。
### 方法关键点
1. 开源RelArena-α统一评测框架，基于RelBench v1标准化数据加载、评估协议、调参机制，支持自定义调优
2. 开源TabPFN-Rel，为TabPFN-3定制的关系学习适配层，在RDBLearn基础上完成核心优化
3. 开源模型无关的关系预测接口RPI，支持用户在新数据库上快速定义任务，一键调用RelArena-α内的所有模型
### 关键结果
TabPFN-Rel在RelArena-α评测中排名第一，验证了将关系数据库打平为单表的方案，在真实任务上效果与专用关系架构相当
