---
title: 'Harness-G: A Graph-Structured Harness for Search Agents'
title_zh: Harness-G：面向搜索Agent的图结构化检索框架
authors:
- Yanning Hou
- Haoyuan Chen
- Sihang Zhou
- Xiaoshu Chen
- Xirui Liu
- Duanyang Yuan
- Lingyuan Meng
- Quan Liu
- Jian Huang
affiliations:
- National University of Defense Technology
arxiv_id: '2607.27652'
url: https://arxiv.org/abs/2607.27652
pdf_url: https://arxiv.org/pdf/2607.27652
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: 搜索Agent · 检索动作空间优化
tags:
- Search Agent
- Graph RAG
- Reinforcement Learning
- Action Space Design
- Credit Assignment
one_liner: 将搜索Agent自由查询生成重构为图上有限动作选择，解决检索等价坍塌问题
practical_value: '- 电商导购/商品搜索Agent可复用有限动作菜单设计：将自由Query生成替换为预定义的商品属性/实体选择动作，解决同义Query多生成但召回结果重叠的无效探索问题，降低RL训练不稳定性

  - 多轮检索场景可直接借鉴SNC信用分配机制：用冻结的答案打分器做同状态动作对比，沿依赖链回传下游收益，无需额外Rollout就能给早期跳转动作分配延迟奖励，适合多跳商品关联推荐的RL训练

  - 大规模商品库图构建可复用无LLM轻量方案：仅用分句、NER、实体归一化和稠密编码构建段落-句子-实体三元图，成本远低于LLM提取的知识图谱，可线性扩展到亿级商品规模

  - 小模型场景收益更显著：1.5B规模模型相对SOTA提升10.74个F1点，算力有限的业务场景优先尝试结构化动作空间约束，ROI高于单纯优化奖励信号的方案'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前RL训练的搜索Agent采用自由查询生成模式，存在检索等价坍塌问题：同一问题下生成的Query表面形式多样，但召回的证据集高度重叠，导致同组轨迹奖励差异极小、RL优化梯度消失，现有仅优化奖励信号的方案无法从根源解决这个接口层面的结构性问题。

### 方法关键点
- 离线构建无LLM参与的轻量段落-句子-实体三元图，仅用分句、NER、实体归一化、稠密编码即可完成，线性时间复杂度可扩展
- 在线检索接口重构为有限动作菜单：Agent仅需从Select（选择证据句）、Lookup（跳转实体检索）、Answer（终止并回答）三类动作中选择ID，环境负责确定性执行Query生成、结果召回、状态更新，自动过滤重复/无效动作
- 提出Structured Non-myopic Credit（SNC）信用分配：用冻结答案打分器对比同状态下选中动作与其他可选动作的边际收益，再沿动作依赖链将下游收益回传给早期使能动作，无需额外Rollout即可获得低方差的步骤奖励

### 关键结果
在2Wiki、HotpotQA、MuSiQue等6个多跳/单跳QA基准上测试，1.5B规模Qwen2.5模型平均F1超过最强基线Graph-R1 10.74点，3B规模超过3.98点；训练过程中检索多样性保持率远高于自由查询方案，跨数据集OOD泛化平均F1提升3.29点，且图构建无LLM调用成本，单查询耗时仅5.1s，成本远低于LLM提取结构的GraphRAG类方案。

**最值得记住的一句话**：搜索Agent的优化不能只盯着奖励信号设计，动作空间的结构化约束是比奖励优化性价比更高的优化方向。
