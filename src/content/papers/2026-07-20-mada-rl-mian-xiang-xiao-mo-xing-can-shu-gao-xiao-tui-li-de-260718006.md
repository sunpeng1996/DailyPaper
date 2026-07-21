---
title: 'MADA-RL: Multi-Agent Debate-Aware Reinforcement Learning for Parameter-Efficient
  Reasoning in Compact Models'
title_zh: MADA-RL：面向小模型参数高效推理的多智能体辩论感知强化学习
authors:
- Martino M. L. Pulici
- Cuong Xuan Chu
- Evgeny Kharlamov
- Zifeng Ding
- Volker Tresp
- Yunpu Ma
affiliations:
- Bosch Center for Artificial Intelligence
- LMU Munich
- University of Oslo
- University of Cambridge
- Munich Center for Machine Learning
arxiv_id: '2607.18006'
url: https://arxiv.org/abs/2607.18006
pdf_url: https://arxiv.org/pdf/2607.18006
published: '2026-07-20'
collected: '2026-07-21'
category: MultiAgent
direction: 多智能体协作 · 小模型推理优化
tags:
- LoRA
- Multi-Agent
- GRPO
- Reinforcement Learning
- Parameter Efficient
- Reasoning
one_liner: 基于LoRA与反事实优势的多智能体RL框架，低成本提升小模型推理能力
practical_value: '- 可复用「生成器+批评家」的角色拆分LoRA训练范式，低成本优化搜索推荐场景下的Query理解、文案生成等小模型效果，无需全量微调

  - 反事实优势的奖励设计可迁移到排序/多轮推荐场景：将优化模型的奖励与现有基线（如旧排序模型效果）做差，针对性提升纠错能力，避免输出同质化

  - 轻量多轮辩论协议可用于电商客服Agent、商品属性校验等场景，用多个小模型低成本集成提升准确率，平衡效果与部署成本

  - 奖励函数2:1（正确性:简洁性）的权重设计可直接用到商品标题生成、推荐理由生成等生成类任务的RL微调，平衡效果与输出长度，降低推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大模型推理能力突出但训练、推理成本过高，4B参数以下小模型在有限预算下的推理能力提升是产业落地的核心痛点；现有RL结合多智能体辩论的方案普遍存在需全量微调、信用分配不稳定、推理开销过高等问题，亟需低成本的小模型推理优化路径。

### 方法关键点
- 两阶段角色拆分训练：将模型分为生成器、批评家两类角色，仅用LoRA微调少量参数，基模型完全冻结，基于GRPO实现无价值模型的RL优化
- 反事实批评家优势设计：将批评家的奖励减去生成器集合的单样本平均准确率作为优势信号，针对性优化批评家纠正生成器共识错误的能力，避免单纯复制正确答案
- 轻量多轮推理协议：首回合生成器并行输出答案，后续回合批评家基于所有前序输出迭代修正，无额外摘要模型，尽可能降低内存开销
- 双目标奖励函数：正确性奖励与长度奖励权重为2:1，优先保证输出正确，同时鼓励简洁输出以降低推理成本

### 关键结果
基于DeepSeek-R1-Distill-Qwen-1.5B基座训练，在5个数学推理基准上测试，平均准确率从39.9%提升至41.9%（+2.0pp，p<0.001），可训练参数仅为全量微调基线的1/16，单位可训练参数的准确率增益为所有评估模型最高；推理时批评家纠错率达19.6%，为同类方案最优。

最值得记住的结论：小模型推理优化场景下，针对性的角色拆分和奖励设计带来的效率收益，远高于单纯增加训练参数或推理计算量。
