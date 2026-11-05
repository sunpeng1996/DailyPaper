---
title: 'Pairing Expert Critique with LLM-Driven Refinement: An Iterative Approach
  for Curating Quality AI Evaluation Datasets'
title_zh: 结合专家评审与LLM迭代优化的高质量AI评估数据集构建方法
authors:
- Honson Ling
- Kidus Admassu
- Stephanie Rosenthal
affiliations:
- Microsoft Corporation
arxiv_id: '2611.05749'
url: https://arxiv.org/abs/2611.05749
pdf_url: https://arxiv.org/pdf/2611.05749
published: '2026-11-03'
collected: '2026-11-05'
category: Eval
direction: 评估数据集构建 · 人在回路专家协作
tags:
- Human-in-the-loop
- Dataset Curation
- LLM Evaluation
- SME Critique
- Iterative Refinement
one_liner: 提出SME-C人在回路工作流，通过轻量专家评审+LLM优化低成本构建高质量领域专属评估数据集
practical_value: '- 搭建业务场景（如商品文案、推荐理由生成）的评估数据集时，可复用轻量专家评审替代专家从零撰写的模式，大幅降低数据集构建的时间与人力成本

  - 两类LLM优化策略可直接适配不同业务反馈场景：有用户/运营的详细评价文本时用critique-based策略生成更贴合领域的内容，仅能拿到点击/偏好类投票反馈时用vote-based策略过滤无关内容

  - 迭代式同步生成数据集与评估规则的流程，可复用在电商LLM应用（如智能客服、营销文案生成）的持续迭代优化链路中'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
领域专属LLM的效果评估需要高质量参考数据与评估规则，纯专家从零撰写的模式效率极低、成本高昂，纯合成数据集又难以贴合实际从业者偏好，无法满足可靠评估需求。
### 方法关键点
提出SME-C人在回路工作流：先让领域专家对候选响应做轻量评审，再搭配两种LLM驱动的优化策略，迭代产出高质量响应数据集与评估规则：
1. 基于专家书面评审内容引导的优化
2. 仅基于专家偏好投票推断评审逻辑的优化
### 关键结果数字
在金融简报场景验证，累计收集411位金融专家对520个query的3853条评审；100位新增专家盲测显示，两种策略生成的内容质量均显著超过专家排名最高的基线响应，其中critique-based策略生成内容更贴合领域特性，vote-based策略更擅长过滤无关内容，整体数据集构建效率远高于纯专家撰写模式，成本更低。
