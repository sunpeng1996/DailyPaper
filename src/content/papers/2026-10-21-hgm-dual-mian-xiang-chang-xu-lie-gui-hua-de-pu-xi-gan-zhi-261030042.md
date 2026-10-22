---
title: 'HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon
  Planning'
title_zh: HGM-Dual：面向长序列规划的谱系感知引导Agent Harness优化框架
authors:
- Sudipta Paul
- Pengrui Quan
- Aounon Kumar
- Nicholas Tzou
- Vivek Kulkarni
- Srinivas Chappidi
affiliations:
- Samsung Research America
arxiv_id: '2610.30042'
url: https://arxiv.org/abs/2610.30042
pdf_url: https://arxiv.org/pdf/2610.30042
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent自优化 · Harness无参数迭代
tags:
- Agent Self-Optimization
- Harness Optimization
- Long-Horizon Planning
- Evolutionary Search
- LLM Agent
one_liner: 通过结构化进化上下文和错误感知双路径生成，大幅降低长序列规划Agent Harness优化的评估成本
practical_value: '- 优化Agent的prompt、工具、workflow时可复用结构化谱系上下文机制：记录每一次修改的内容、性能影响、错误变化，避免重复无效修改，可将有效修改占比提升30%以上。

  - 迭代时可采用双路径生成策略：保留无限制探索分支的同时，针对当前Top2高频错误生成定向修复分支，仅保留最优子代入归档，在电商导购、履约规划等约束复杂的场景下可减少2-4倍评估成本。

  - 对于约束密集的任务（如电商凑单、优惠券核销、多商品组合推荐），可先通过预测试判断错误信号的稳定性，仅在错误分类一致性≥0.4、主导错误稳定性≥0.7时开启定向修复分支，避免噪声误导优化方向。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于递归自优化的Agent Harness优化方案（如HGM、DGM）主要适配编码场景，在长序列规划任务中（如电商购物规划、旅行规划）存在严重的修改冗余、修改与错误错配问题：41.8%的修改重复已尝试过的无效模式，19.4%的修改针对父Agent从未出现的错误，64.2%的修改无法解决父Agent的核心错误，导致评估预算浪费严重，优化效率极低。

### 方法关键点
- 结构化谱系进化上下文：为每个Agent维护修改记录，包含修改内容、功能变化、性能波动、错误分布变化、行为影响5个维度，编辑器仅接收父Agent谱系的压缩上下文，无需遍历全量历史Agent。
- 错误感知双路径子代生成：当预测试验证错误信号稳定（分类一致性≥0.4、主导错误稳定性≥0.7）时，同时生成两类子代：1个通用探索子代保留无限制优化能力，2个定向修复子代分别针对当前Top2高频错误修改对应Harness组件，最终仅保留得分最高的子代入归档。

### 关键实验
在DeepPlanning基准的旅行规划、电商购物两个长序列任务上测试，对比HGM、HGM-CA、HGM-CF等SOTA基线：4000评估预算下，相对最强基线HGM-CF的case accuracy提升8.13%（旅行）、5.84%（购物）；购物场景下仅用1/4的预算即可达到HGM-CF的最终性能，整体评估成本降低2-4倍；谱系上下文可将有效修改占比从31.3%提升至41.0%，重复修改率降低22.7%。

### 核心结论
Agent自优化的核心不是无限制探索，而是结构化沉淀历史修改的因果关系，并在探索和定向修复之间做好动态平衡。
