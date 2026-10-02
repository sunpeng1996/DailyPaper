---
title: 'Prompt2Skill: Unsupervised Skill Optimization From Natural Language Instructions'
title_zh: Prompt2Skill：仅用自然语言指令的无监督Agent技能优化框架
authors:
- Bo Ni
- Li Li
- Ryan A. Rossi
- Franck Dernoncourt
- Tyler Derr
affiliations:
- Vanderbilt University
- University of Southern California
- Adobe Systems
arxiv_id: '2609.38593'
url: https://arxiv.org/abs/2609.38593
pdf_url: https://arxiv.org/pdf/2609.38593
published: '2026-09-28'
collected: '2026-10-02'
category: Agent
direction: Agent 无监督技能自动生成与优化
tags:
- Agent Skill
- Unsupervised Optimization
- Multi-Agent
- Prompt Engineering
- Zero-shot Learning
one_liner: 无需标注训练数据，仅从自然语言任务描述生成适配目标模型的优化Agent技能
practical_value: '- 电商Agent场景下，针对客服应答、商品属性抽取、订单自动处理等垂直任务，无需人工标注样本，仅靠任务描述即可自动生成适配的专用技能，大幅降低技能开发成本

  - 技能迭代闭环方案可直接复用：通过代理自动采集/合成适配任务的验证数据，基于错误反馈迭代优化技能，用统计显著性检验筛选有效更新，避免无效修改导致的效果回落

  - 小参数LLM场景适配收益更高，针对端侧/轻量推荐Agent，用该框架生成的技能可带来最高90%+的相对效果提升，无需微调即可升级小模型垂直任务表现'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能多由人工撰写，成本高且无法适配不同模型的特性，已有的自动化技能优化方法依赖标注训练集，很多业务场景下无法快速获取，针对新任务的技能开发周期长、落地门槛高。

### 方法关键点
- 双Agent架构：Data Agent基于任务描述生成任务规范，从公开数据集检索或生成适配的验证样本，经过多轮校验后构建样本池；Skill Agent基于样本池做闭环迭代，通过模型执行错误反馈生成技能修改方案，在独立验证批次上做配对统计检验，仅保留能显著提升效果的修改。
- 最终筛选阶段用独立冻结的验证集从所有迭代版本中选最优技能，避免过拟合迭代数据，无需修改目标模型任何参数。

### 关键实验
覆盖问答、阅读理解、数学推理、表格操作4类任务，对比直接prompt、现成通用技能、LLM单次生成技能3个基线，在5个开源/商用LLM上平均相对提升10.8个百分点，Llama-3.2-1B小模型上相对提升最高达93.5%，无明显效果回落情况。

### 核心结论
仅靠自然语言任务描述就能生成适配目标模型的专用技能，无需标注数据即可实现Agent能力的低成本快速升级。
