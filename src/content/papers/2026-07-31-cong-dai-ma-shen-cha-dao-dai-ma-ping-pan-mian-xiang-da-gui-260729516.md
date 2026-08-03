---
title: 'From Code Review to Code Critique: Intent, Drift, and Spotlight for AI-Generated
  Diffs at Scale'
title_zh: 《从代码审查到代码评判：面向大规模AI生成diff的意图与偏差检测框架》
authors:
- Chandra Maddila
- Mashrur Rashik
- Euna Mehnaz Khan
- Smriti Jha
- James Saindon
- Nachi Nagappan
- Peter C. Rigby
affiliations:
- Meta, USA
- Concordia University, Montreal, Canada
arxiv_id: '2607.29516'
url: https://arxiv.org/abs/2607.29516
pdf_url: https://arxiv.org/pdf/2607.29516
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: AI Coding Agent 代码质量管控优化
tags:
- Coding Agent
- Code Review
- Intent Prediction
- Drift Detection
- Human-in-the-loop
one_liner: 提出ARCTIC代码评判系统，通过三大核心能力大幅提升大规模AI生成diff的审查效率与质量
practical_value: '- 做Agent输出对齐用户需求的场景，可复用「意图推理+输出回译做漂移检测」的范式，可直接迁移到生成式推荐文案/物料的需求一致性校验场景

  - 大模型长输出质检场景，可借鉴spotlight思路，仅对高风险片段做human-in-the-loop审核，大幅降低token消耗和人力成本

  - 垂域大模型落地前，先基于大规模真实人工标注数据构建需求优先级分类体系，避免模型输出大量低价值建议'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
AI coding Agent生成代码的速度和规模远超传统人工代码评审的承载能力，现有AI代码审查工具过度关注风格等低价值建议，忽略开发者最关心的正确性、安全性、性能问题。

### 方法关键点
基于1.8万份真实代码评审提炼的6类主题分类体系，搭建ARCTIC代码评判系统：1）从对话日志和元数据推理代码变更的用户真实意图；2）通过回译机制度量Agent输出与开发者意图的偏差程度；3）对diff中最需要人工检查的高风险片段做优先级排序。

### 关键结果
离线评估：意图预测F1=0.86，漂移检测与人工标注的加权卡帕系数QWK=0.907，高风险片段排序质量比基线AI评审高2.4倍，token消耗仅为基线的1/5；线上实验：漂移检测额外降低5.76%的代码对齐偏差，意图预测结果获得90.2%的开发者认可，上线后自评审diff零缺陷。
