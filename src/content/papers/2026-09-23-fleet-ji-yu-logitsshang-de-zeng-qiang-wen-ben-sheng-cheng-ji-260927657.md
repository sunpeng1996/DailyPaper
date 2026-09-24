---
title: 'FLEET: From Logits Entropy to Enhanced Trajectories in Text Generation'
title_zh: FLEET：基于Logits熵的增强文本生成轨迹搜索框架
authors:
- Oleksii Streltsov
- Oleksandra Vitko
affiliations:
- Kharkiv National University of Radio Electronics
arxiv_id: '2609.27657'
url: https://arxiv.org/abs/2609.27657
pdf_url: https://arxiv.org/pdf/2609.27657
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM测试时优化 · 解码策略
tags:
- LLM Decoding
- Test-Time Scaling
- Entropy Guided Exploration
- Memory Augmented Generation
- MCTS
one_liner: 提出带记忆的熵触发式文本生成框架FLEET，同预算下大幅提升多步任务准确率
practical_value: '- 生成式推荐/电商文案生成场景可复用熵+varentropy双阈值启发式逻辑，仅在高不确定性决策点做采样探索，避免全局加温度导致的生成内容偏离业务要求，同时降低不必要的计算开销

  - 可引入VectorDSU在线聚类机制，对LLM生成的推荐候选、Agent执行路径做语义去重，同采样预算下提升候选多样性，避免结果冗余

  - 在有可量化外部反馈的场景（如推荐点击率反馈、Agent工具调用结果校验），可复用pUCT动态logit惩罚机制，将历史奖励信号实时反馈到解码环节，提升优质结果的命中效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM温度采样为无记忆策略，随采样次数增加，语义重复的生成结果占比持续上升，导致边际收益递减；自适应温度采样仅能动态调整全局超参，无法解决关键决策点的采样低效问题，且超参调优成本高、跨任务泛化差，多步推理、Agent自主决策等场景的采样效率亟待优化。

### 方法关键点
- 采用熵+varentropy双指标识别高不确定性决策点，仅在这类节点启动探索逻辑，其余节点走常规解码流程，避免对低不确定性的语法/结构token引入无关扰动
- 提出VectorDSU在线数据结构，基于LLM中间层隐藏态的余弦相似度做聚类，映射为离散搜索状态，记录历史轨迹的token动作、下游奖励、访问次数等元数据，避免重复探索语义等价路径
- 引入pUCT公式计算每个候选token的效用，对已验证的次优token施加动态logit惩罚，引导生成向高reward路径收敛
- 仅需一次校准即可确定所有超参数，无需多轮网格搜索，对现有LLM pipeline的改造量极小

### 关键结果
在GSM8K数学推理、LiveCodeBench代码生成数据集上对比经过贝叶斯调优的温度采样基线：
- 同32次采样预算下，LiveCodeBench Pass@32从59.9%提升至66.2%，GSM8K Pass@32从97.27%提升至97.8%
- 达到相同准确率时，FLEET的速度是基线的3倍

> 最值得记住的结论：多步生成任务的效率提升核心不是盲目增加采样数，而是通过记忆机制避免重复探索、把计算资源集中到高价值决策点的定向探索上
