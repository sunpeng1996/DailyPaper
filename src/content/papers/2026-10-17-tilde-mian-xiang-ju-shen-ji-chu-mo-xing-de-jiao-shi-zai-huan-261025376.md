---
title: 'TILDE: Teacher-in-the-Loop Distillation from Embodied Foundation Models'
title_zh: TILDE：面向具身基础模型的教师在环蒸馏方法
authors:
- Yuxiang Lu
- Yantong Liu
- Jinghua Hou
- Xueli Sun
- Ruihua Han
- Zhe Liu
- Hengshuang Zhao
affiliations:
- The University of Hong Kong
arxiv_id: '2610.25376'
url: https://arxiv.org/abs/2610.25376
pdf_url: https://arxiv.org/pdf/2610.25376
published: '2026-10-17'
collected: '2026-10-25'
category: Training
direction: 具身Agent · 知识蒸馏训练优化
tags:
- Knowledge Distillation
- Embodied AI
- Foundation Model
- Data Aggregation
- Policy Learning
one_liner: 提出教师在环蒸馏框架TILDE与自动数据聚合管道AutoDAgger，低成本迁移具身大模型能力
practical_value: '- 知识蒸馏场景可复用TILDE的「学生诱导状态在环蒸馏+教师恢复轨迹学习」联合范式，解决离线蒸馏的分布失配问题

  - 数据采集/标注环节可借鉴AutoDAgger的自动监控触发干预机制，替代人工在环降低成本，实测效率提升2倍以上

  - 跨架构模型能力迁移可复用该框架，无需重复上游大规模预训练，即可将大模型能力迁移到轻量部署模型'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
具身基础模型（EFM）经大规模动作预训练后泛化性、闭环鲁棒性优异，但复现预训练需海量机器人数据与算力，难以低成本迁移能力到无预训练的小策略模型，现有蒸馏方案还存在分布失配、人工介入成本高的痛点。
### 方法关键点
1. 提出TILDE框架，融合学生诱导状态下的在环蒸馏、教师执行的恢复轨迹学习两类监督信号
2. 配套AutoDAgger自动数据聚合管道，用机器人奖励模型监控任务进度、触发教师干预，无需人工监控即可收集恢复数据
### 关键结果
- AutoDAgger相比人工在环方案的恢复轨迹收集速度提升2倍以上
- TILDE在3个真实世界任务上相比行为克隆性能最高提升4.1倍，支持跨架构有效蒸馏
