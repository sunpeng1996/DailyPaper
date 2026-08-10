---
title: 'CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and
  Diversity'
title_zh: CreativeInstruct：可扩展训练LLM平衡生成质量、创意与多样性
authors:
- Ananya Sahu
- Mohit Bansal
- Elias Stengel-Eskin
affiliations:
- Columbia
- UNC Chapel Hill
- University of Texas at Austin
arxiv_id: '2608.07460'
url: https://arxiv.org/abs/2608.07460
pdf_url: https://arxiv.org/pdf/2608.07460
published: '2026-08-07'
collected: '2026-08-10'
category: Training
direction: 指令微调 · LLM创意生成优化
tags:
- Instruction Tuning
- LoRA
- Creativity Generation
- Diversity Metric
- Reinforcement Learning
one_liner: 通过带创意触发token的指令微调，单LLM兼顾对齐质量与基模型创意，配套结构多样性评估指标
practical_value: '- 电商营销文案、商品描述、推荐理由生成场景可直接复用创意token注入方案，在保证内容合规、符合业务要求的前提下提升多样性，避免同质化内容引起用户审美疲劳，仅需单模型推理，成本远低于双模型路由方案

  - 生成类任务的效果评估可复用LLM-GED结构多样性指标，比传统词汇、语义相似度指标更能捕捉叙事层面的差异，更贴合用户对内容新颖度的感知

  - 基于LLM的智能导购Agent、对话系统需要做RL优化时，可先做创意指令微调提升初始模型的多样性，再开展RL训练，能有效提升OOD场景的泛化性能，减少RL探索不足的问题

  - 没有对应公开基模型的场景下，可跨模型族用其他基模型生成带创意标签的训练数据做迁移微调，降低数据制备门槛'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM经过对齐后指令遵循能力、合规性显著提升，但生成多样性与创意大幅下降，导致创意类生成任务输出同质化，同时在RL训练时因探索不足出现性能瓶颈；现有双模型路由的创意增强方案推理时需加载两个模型，成本高且依赖公开基模型，落地门槛高。

### 方法关键点
- 数据制备：基于双模型路由方法BACo生成响应，对其中来自基模型的高创意span前后插入[StartCreativity]、[EndCreativity]特殊token，仅需筛选通用写作类指令数据即可构造训练集，可扩展性强。
- 训练：用LoRA微调对齐后的LLM，让模型自主学习判断何时注入创意span，推理时仅需单模型，无需额外路由逻辑或多模型加载。
- 评估：提出LLM-GED结构多样性指标，将生成内容抽象为包含实体、事件、时序关系的事件图，通过归一化图编辑距离衡量叙事层面的多样性，比传统词汇、语义指标更贴合人类对创意的判断。

### 关键结果
在叙事生成任务上测试7B~32B多个模型族，对比Instruct基线、双模型路由BACo、无标签蒸馏等方案：
- LLaMA-3.1 8B版本相较Instruct基线，语义多样性提升48%，结构多样性提升63%，70.3%的人类评估案例被认为更具创意，同时生成质量无下降。
- 效果优于双模型路由方法BACo，语义多样性平均提升29%、结构多样性提升28%，推理成本仅为BACo的一半。
- 作为RL训练基底时，在MATH数据集上精度提升5%，OOD的AMC数据集上精度提升4%。

### 核心结论
通过引入细粒度的创意切换标识做微调，无需改动推理架构，即可同时保留LLM对齐后的质量与基模型的多样性，还能为下游RL任务带来泛化增益
