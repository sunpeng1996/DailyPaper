---
title: 'DataCanvas-EDU: An Agentic Framework for Instructor-Guided Synthetic Data
  Generation in Business Analytics Education'
title_zh: DataCanvas-EDU：商分教育场景教师引导式合成数据生成Agent框架
authors:
- Bang An
- Maria Hamdani
- Joseph Fox
affiliations:
- University of Akron
arxiv_id: '2609.19617'
url: https://arxiv.org/abs/2609.19617
pdf_url: https://arxiv.org/pdf/2609.19617
published: '2026-09-17'
collected: '2026-09-20'
category: Agent
direction: Agent 定制化合成数据生成
tags:
- Agent
- Synthetic Data
- LLM
- Data Generation
- Instructional Agent
one_liner: 提出四阶段Agent框架支持教师通过对话生成定制化商分教学合成数据与配套教案
practical_value: '- 四阶段Plan/Create/Verify/Evaluate的人在回路合成数据生成流程可直接复用，生成符合业务特定分布、带预设隐藏pattern的推荐/搜索评测数据集，规避公开数据集的模型训练污染问题，提升评测准确性

  - Agent自动编写数据生成代码、自动校验数据合规性的能力可迁移到电商AB测试所需的模拟用户行为数据集生成场景，大幅降低定制化数据集的准备成本

  - 将特定领域能力封装为可复用Agent Skill的工程实践可参考，用于搭建业务内部的Agent能力组件库，减少同类型需求的重复开发工作量'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
商分教育需适配不同教学目标、学生背景的多样化数据集，真实数据获取难度高、定制灵活性差，公开数据集普遍存在LLM训练污染问题，教师准备教案与参考方案耗时成本极高。
### 方法关键点
基于四阶段流程实现人在回路的合成数据生成：1）Plan阶段通过对话对齐教师的教学目标、数据预设pattern要求；2）Create阶段Agent自动编写代码生成符合要求的结构化数据集；3）Verify/Test Analysis阶段自动校验数据合理性、生成配套参考分析结果；4）Evaluate阶段支持教师人工审核修订，同步输出作业、评分标准等全套教案。
### 关键结果数字
落地外卖业务教学案例WindowDash，生成1.5万条订单数据，内置9个预设分析pattern，框架已封装为可复用Agent Skill开源。
