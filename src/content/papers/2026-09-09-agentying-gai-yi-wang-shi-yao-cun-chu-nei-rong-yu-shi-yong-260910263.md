---
title: What Should an Agent Forget? Separating What Is Stored from What Is Used
title_zh: Agent应该遗忘什么：存储内容与使用内容的分离机制
authors:
- Yuhang Li
- Yuchen Li
affiliations:
- Beihang University
- East China Normal University
arxiv_id: '2609.10263'
url: https://arxiv.org/abs/2609.10263
pdf_url: https://arxiv.org/pdf/2609.10263
published: '2026-09-09'
collected: '2026-09-10'
category: Agent
direction: Agent记忆管理 · 选择性遗忘
tags:
- LLM Agent
- Selective Forgetting
- Memory Management
- Query-aware Retrieval
- Persistent Memory
one_liner: 提出训练无关的RD-Forget框架，分离Agent记忆存储与查询条件化使用，解决过时事实干扰问题
practical_value: '- 电商个性化Agent可复用语义槽分组机制：将用户偏好按<主体|关系|范围>打槽，新偏好仅覆盖同槽旧值，既保证当前推荐准确性，又保留历史偏好供回溯类查询使用

  - 可直接复用无训练架构：无需微调LLM，仅靠prompt引导的curator做事实提取、槽分组，配合同槽替换规则，即可快速升级现有Agent记忆系统，降低落地成本

  - 长会话客服/推荐Agent可借鉴率失真打包逻辑：在token预算约束下，优先保留当前query相关的事实链和最新槽值，最大化回答准确率的同时控制推理成本

  - 用户画像更新可借鉴历史召回开关：识别到用户查询为历史相关意图时，自动释放被标记为过时的同槽旧值，避免遗漏历史相关结果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
持久化LLM Agent面临核心矛盾：直接删除过时事实会导致历史类查询无法回答，全量保留所有事实又会干扰当前状态的回答准确性，现有记忆管理方法要么全量保留要么物理删除，无法适配动态变化的查询意图。

### 方法关键点
- 完全训练无关架构：全量历史观察永久存储在源归档库不删除，仅针对当前query生成动态记忆视图，用冻结LLM作为curator处理事实提取
- 语义槽分组机制：事实按<主体|关系|范围>格式打槽，同槽下新值自动标记旧值为被取代，当前状态查询默认屏蔽旧值，历史意图查询可重新召回
- 率失真优化视图构建：在token预算约束下，优先选择最小化回答失真的事实集合，同时保留多跳推理所需的关联事实链

### 关键实验结果
在对话记忆、知识更新、事实整合、长上下文推理、个性化5类任务上，对比ACE、ReasoningBank等SOTA基线，4种LLM backbone均获得一致提升：事实整合任务相对最优基线提升11~26pp，BEAM长记忆任务提升8.47~15.67pp，PersonaMem个性化任务提升10.88~20.72pp；消融实验显示关闭遗忘机制带来的性能降幅最大（最高33.33pp），其次是关闭查询条件化。

最值得记住的一句话：Agent该遗忘什么的本质，不是删除存储的事实，而是决定哪些事实适合用于当前查询。
