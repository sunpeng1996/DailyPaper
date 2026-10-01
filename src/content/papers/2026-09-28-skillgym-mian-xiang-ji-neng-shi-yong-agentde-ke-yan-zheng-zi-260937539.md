---
title: 'SkillGym: Training Skill-Use Agents with Automatic Verifiable Environment
  Generation'
title_zh: SkillGym：面向技能使用Agent的可验证训练环境自动生成框架
authors:
- Renxi Wang
- Mingshan Hee
- Fajri Koto
- Timothy Baldwin
- Haonan Li
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2609.37539'
url: https://arxiv.org/abs/2609.37539
pdf_url: https://arxiv.org/pdf/2609.37539
published: '2026-09-28'
collected: '2026-10-01'
category: Agent
direction: Agent 技能使用训练数据自动合成
tags:
- SkillGym
- Agent Training
- Skill Use
- SFT
- Environment Generation
one_liner: 提出自动生成可验证技能训练环境的SkillGym，SFT后9B模型性能超过397B未训练模型
practical_value: '- 可复用builder-reviewer双Agent流程生成业务专属训练数据：比如电商Agent的工具调用、运营流程技能的训练任务，自动做有效性校验和质量审核，减少人工标注成本

  - 技能关键任务设计思路可迁移：生成必须调用给定业务技能（如优惠券计算、商品上架规则）才能高效完成的训练任务，避免Agent绕开技能硬解

  - 小模型SFT增益可复用：用业务场景的真实技能轨迹SFT小模型，就能获得接近超大模型的技能调用效果，降低线上推理成本

  - 训练数据质量审核的价值：经reviewer校验的高质量轨迹比仅通过执行校验的轨迹带来的效果增益高4.7~9.3个点，业务数据生产环节要加质量门控'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent技能使用训练多依赖固定环境下的自有经验，覆盖域窄；公开社区技能覆盖软件、营销、金融等10+领域，但无配套任务、执行环境和结果校验机制，无法直接用于训练，且缺少标准化的高质量训练数据生成流程。

### 方法关键点
- 三阶段pipeline：爬取184k公开社区技能，经去重、离线可执行性校验后得到11897个可复用技能池
- builder-reviewer双Agent流程构建任务：基于流程执行、溯因诊断、约束满足、偏序规划4类推理结构生成任务，自动校验任务的技能关键性、验证逻辑合理性，过滤信息泄露、校验过严/过松的低质量任务
- 多模型多Agent harness轨迹采集：用3个大模型、4种主流Agent框架生成19k验证通过的成功交互轨迹，直接用于SFT

### 关键结果
- 构建6.8k覆盖19个领域的可验证任务，SFT后2B~122B全尺寸模型在4个技能使用基准上平均提升9.7~41.2分
- 9B SFT模型在SkillGym测试集、SkillEval上性能超过397B未训练Qwen3.5模型
- 训练后Agent相关技能调用率从28%提升至96%，增益可迁移到训练未见过的全新技能上

### 核心结论
训练Agent使用外部技能的核心是让它先学会主动调用技能，而非直接掌握技能本身的知识。
