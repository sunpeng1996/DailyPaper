---
title: Agent as Policy for Robotic Manipulation
title_zh: Agent即策略：面向机器人操纵的通用智能体执行框架
authors:
- Mengzhao Jia
- Yang Lin
- Xixin Zhang
- Zhihan Zhang
- Xiaobai Liu
- Meng Jiang
affiliations:
- University of Notre Dame
- University of California San Diego
- San Diego State University
arxiv_id: '2609.12541'
url: https://arxiv.org/abs/2609.12541
pdf_url: https://arxiv.org/pdf/2609.12541
published: '2026-09-10'
collected: '2026-09-16'
category: Agent
direction: 通用Agent · 物理场景执行策略
tags:
- General Agent
- Runtime Reasoning
- Program Generation
- Zero-shot Execution
- Physical Manipulation
one_liner: 提出无需任务/环境专项训练的AGP框架，让通用Agent直接驱动实体机器人完成多类操纵任务
practical_value: '- 可复用「感知-代码生成-执行-反馈迭代」的Agent闭环架构，用于电商场景自动上新、线下门店价签调整等实体作业Agent开发

  - 任务执行中沉淀可复用的历史程序库，重复任务直接调用缩短耗时，可迁移到电商客服应答、推荐规则生成等高频场景降本

  - 无需场景专项训练的零样本执行思路，可借鉴到多品类/多场景的通用电商运营Agent快速落地'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有机器人操纵方案要么依赖预先生成的固定程序，要么需要调用预训练的专属策略，需针对特定任务/环境做专项训练，泛化性差，无法适配复杂多变的物理场景。
### 方法关键点
提出AGP（Agent as Policy）框架，将任务规划与执行全流程交由通用Agent管控：基于多模态输入（视觉证据、任务指令、机器人接口）完成感知解读、可执行控制程序生成、运动指令下发，同时根据物理执行结果实时迭代调整动作，实现推理、编程能力与物理环境的持续交互。
### 关键结果
在组装、积木搭建、骰子翻转、投掷、毛巾折叠等多个真实操纵任务中，每种任务配置下10次试验至少成功8次，其中三类积木搭建任务成功率分别达100%、100%、80%；复用沉淀的历史程序可大幅缩短重复任务的执行耗时。
