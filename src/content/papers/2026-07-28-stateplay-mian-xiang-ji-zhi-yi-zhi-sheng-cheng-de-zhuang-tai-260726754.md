---
title: 'StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation'
title_zh: StatePlay：面向机制一致生成的状态感知游戏世界模型
authors:
- Zijun Lin
- Zeqing Wang
- Cheston Tan
- Bihan Wen
- Yeying Jin
affiliations:
- Tencent
- Nanyang Technological University
- National University of Singapore
- Centre for Frontier AI Research, A*STAR
arxiv_id: '2607.26754'
url: https://arxiv.org/abs/2607.26754
pdf_url: https://arxiv.org/pdf/2607.26754
published: '2026-07-28'
collected: '2026-08-01'
category: Agent
direction: Agent 环境世界模型机制一致性生成
tags:
- World Model
- Mixture-of-Transformers
- State Modeling
- Cross-Modal Interaction
- Multimodal Generation
one_liner: 提出MoT架构的状态感知游戏世界模型，联合预测视觉与状态，提升生成内容机制保真度
practical_value: '- 多模态联合生成场景可复用MoT式双分支架构，分别保留模态专属表征再做跨模态交互，兼顾生成准确性与模态特性

  - 规则约束型生成任务可新增显式状态建模分支，用状态预测结果引导生成，避免仅追求感官合理性却违反底层业务规则

  - 多模态多任务优化时，不同分支可采用适配自身特性的独立损失函数，有效降低任务间优化冲突'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有游戏世界模型仅能生成视觉逼真的交互环境，未建模血量、技能条、计时器等与玩法强耦合的隐式内部状态，导致生成内容视觉合理但违背游戏底层机制规则，无法适配闭环交互需求。
### 方法关键点
采用Mixture-of-Transformers（MoT）架构，分设视觉、状态两个专属表征分支，保留各自模态特性的同时支持跨模态交互，用预测得到的游戏状态引导后续帧生成；两个分支分别采用适配自身模态的独立优化目标训练。
### 关键结果
状态预测平均归一化L1距离低于0.06；相比无显式状态建模的基线模型，生成游戏序列的机制保真度提升18.6%。
