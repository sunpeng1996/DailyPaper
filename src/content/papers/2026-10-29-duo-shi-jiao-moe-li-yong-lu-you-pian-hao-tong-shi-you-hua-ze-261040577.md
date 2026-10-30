---
title: 'Multi-View MoE: Letting Every Router Shape Expert Computation'
title_zh: 多视角MoE：利用路由偏好同时优化专家选择与计算
authors:
- Zelin Zhao
- Tianchi Ma
- Junyuan Shang
- Shuohuan Wang
- Dianhai Yu
affiliations:
- ERNIE Team, Baidu
arxiv_id: '2610.40577'
url: https://arxiv.org/abs/2610.40577
pdf_url: https://arxiv.org/pdf/2610.40577
published: '2026-10-29'
collected: '2026-10-30'
category: Training
direction: MoE架构优化 · 路由设计
tags:
- MoE
- Router Optimization
- Sparse Model
- Multi-View
- LLM Training
one_liner: 提出多路由聚合与视角混合的MoE架构，固定专家算力预算下显著提升模型性能
practical_value: '- 推荐系统多兴趣MoE建模可复用Multi-Router设计：多个独立初始化路由头sigmoid得分求和后选TopK专家，仅增加0.06%参数即可提升路由与专家效用的匹配度，缓解单路由偏差问题

  - 推理侧MoE优化可复用视角混合逻辑：利用路由得分跨路由归一化结果混合多个隐层视角作为专家输入，不改变激活专家数、FLOPs和All-to-All通信量，无额外推理成本即可提升效果

  - 单路由MoE升级可复用热启动策略：保留原有路由和投影作为第一个视角，新增视角用小扰动初始化，避免训练冷启动带来的效果损失'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统稀疏MoE依赖单路由头选择专家，实验发现单路由得分排名与实际专家效用排名的相关性极低，中深层仅0.06左右，错误选择会因专家缺乏梯度反馈被自强化；现有引入多评估信号的方法要么需要预计算专家激活额外增加成本，要么重复专家计算，无法在固定激活专家预算下同时优化选择和计算两个环节。

### 方法关键点
- Multi-Router子模块：多个独立初始化的sigmoid路由头分别给专家打分，求和后做一次TopK选择，路由头训练时会自然形成差异化偏好，兼顾单个路由强偏好和多路由共同支持的专家
- Multi-View视角混合：每个路由头对应一个独立隐层投影（视角），选中的专家将各路由头的得分跨路由归一化作为权重，混合多个视角作为输入，每个专家仅执行一次前向传播
- 全程不改变激活专家数量、专家FLOPs和All-to-All通信量，总参数增量仅0.19%

### 关键结果
基于24层10B参数A1B模型，在708B Tokens训练量下对比LatentMoE基线：
1. 仅用Multi-Router子模块，9个下游任务平均提升0.6pp，路由得分与专家效用的全局秩相关相对提升8.1%，最低对齐层相对提升58%
2. 完整Multi-View MoE 9个下游任务平均提升1.18pp，训练损失相对降低7.38e-3

路由偏好不仅可以用来选专家，还可以作为免费信号调制专家的输入，在不增加推理成本的前提下充分挖掘MoE的性能潜力
