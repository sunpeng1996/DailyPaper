---
title: 'From Search to Decision: How Post-Training Shapes Information-Seeking Capabilities
  in Large Language Models'
title_zh: 后训练如何塑造大模型的信息寻求与决策能力
authors:
- Haohang Huang
- Xuan Lu
- Mingjin Kuai
- Yuxuan Zhang
- Wei Ji
- Haiyang Zhang
affiliations:
- Xi'an Jiaotong-Liverpool University
- Shanghai Jiao Tong University
- Nanjing University
- University of British Columbia
arxiv_id: '2611.14149'
url: https://arxiv.org/abs/2611.14149
pdf_url: https://arxiv.org/pdf/2611.14149
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: Agent 信息寻求能力后训练优化
tags:
- LLM
- Post-training
- Information-seeking
- Agent
- RAG
- Evaluation
one_liner: 系统梳理大模型6类信息寻求能力的后训练机制、实证进展与评估框架
practical_value: '- 搭建电商导购/搜索Agent时，可参考6类信息寻求能力拆解框架，针对性优化检索触发、query改写、多源商品信息整合等模块，避免全链路盲目调优

  - 后训练策略可复用：针对特定能力（如商品检索query改写）优先选择模块化SFT+局部RL优化，无需全量微调大模型，兼顾效果与训练成本；多步检索场景可引入中间信息增益、冗余惩罚信号缓解长序列信用分配问题

  - 评估环节可复用能力对齐原则：除最终转化/答对率外，补充检索决策准确率、query召回增益、证据覆盖率等行为指标，结合受控干预实验定位性能瓶颈，避免归因错误'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM驱动的信息寻求系统已从固定前置检索转向自主决策何时检索、如何改写query、怎么整合多源证据，但各类后训练方法的优化目标、评估维度高度分散，现有综述多围绕系统架构或优化技术展开，缺乏以能力为中心的系统梳理，无法指导从业者针对性提升特定信息寻求行为。
### 方法关键点
- 拆解6类核心信息寻求能力：认知感知与检索效用评估、信息需求表达、信息空间探索、证据评估、证据整合与信念修正、自适应搜索控制
- 从4维度梳理后训练机制：学习信号（演示数据、交互轨迹、奖励/偏好）、优化方法（SFT、偏好优化、RL、混合策略）、更新范围（模块化组件、全量策略、外部记忆）、长程信用分配（中间信号、回溯评估、状态值估计）
- 提出3项评估原则：补充能力特定的行为指标、受控实验隔离目标决策、明确泛化场景边界
### 关键结果
汇总近年实证进展：后训练可使检索路由准确率提升15%~30%，query改写后证据覆盖率提升20%~40%，多工具探索的信息召回提升25%以上，长步长搜索效率提升30%；多数能力可跨模型骨干、跨任务泛化，仅检索后端感知类策略迁移后性能下降10%~15%。
### 核心结论
信息寻求能力优化的核心是对齐决策目标与监督信号，而非盲目堆叠复杂训练流程，简单的终端奖励在受控场景下效果不逊于复杂信用分配机制
