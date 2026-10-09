---
title: 'Gated Memory: Admission-Controlled Memory Formation for Conversational AI'
title_zh: 门控记忆：面向对话AI的准入控制记忆生成框架
authors:
- Preeti Saraswat
- Divya Neelagiri
- Ajay Manoj
affiliations:
- Samsung Research America
arxiv_id: '2610.11270'
url: https://arxiv.org/abs/2610.11270
pdf_url: https://arxiv.org/pdf/2610.11270
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: 对话Agent · 长期记忆准入控制
tags:
- ConversationalAI
- LongTermMemory
- GatedMemory
- AdmissionControl
- MemoryFormation
one_liner: 在记忆提取前新增准入控制门与隐私感知富集层，提升对话Agent长期记忆质量
practical_value: '- 可迁移到电商客服/导购Agent的用户画像记忆模块：在提取用户偏好前保留原对话上下文，避免把临时场景（如代朋友买商品、试用产品）错当成长期用户属性，减少推荐误判

  - 4类实体作用域的隐私合规富集策略可直接复用：USER_PII类信息（手机号、地址）不做外部富集，商品等EXTERNAL类实体调用知识图谱补充品类、参数等属性，平衡记忆语义深度和合规要求

  - 对话拆分当前轮+参考历史的模式可复用：仅从当前轮提取新事实，历史轮仅用于指代消解，避免重复存储相同用户属性，降低向量库存储成本和检索噪声'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有对话AI长期记忆系统普遍只关注存储后的检索、去重、生命周期管理，默认进入存储的事实都有价值，忽略了记忆生成阶段的质量问题：提取三元组时会永久丢失原对话中区分临时状态和长期属性的上下文信号（比如用户说租的SUV会被错当成用户有SUV），无意义的空泛内容会污染向量库，占用top-k检索槽位，导致下游回答准确率下降，且这类错误下游无法修复。

### 方法关键点
- 提出3阶段门控记忆框架，可作为即插即用层对接任意现有记忆后端，完全不改动现有检索、生成逻辑
- 对话拆分当前轮（唯一新事实来源）+ 历史参考轮（仅用于指代消解），避免重复存储已存事实、虚构未提及实体
- 准入门在提取三元组前基于完整原对话评估候选事实，仅保留长期属性、稳定偏好、跨会话可复用的内容，拒绝临时状态、空泛情绪内容；同时做多意图拆分，给每个原子事实打分类标签、直接陈述/推断来源标签
- 4类实体作用域分类+条件富集：按隐私级别匹配富集策略，同时在生成阶段把相对时间/地点指代落地为绝对信息

### 关键实验
在LoCoMo-10长时记忆benchmark上对比mem0基线，仅新增门控记忆层的情况下，整体LLM-judge准确率相对提升2.6%，单跳查询提升4.4%，开放域查询提升3.3%，仅多跳查询因剪枝了关联节点出现4.2%的精度下降；准入门过滤了6%的低价值内容。

### 核心结论
记忆系统的上限在写入时刻就被决定了，存储什么、以什么形式存储，比后续的检索优化更能决定下游性能。
