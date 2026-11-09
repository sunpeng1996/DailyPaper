---
title: 'Compaction, decay and reinforcement in a two-tier conversational memory: a
  paired evaluation against retrieval-augmented generation'
title_zh: 两层对话记忆的压缩、衰减与强化：与RAG的配对对比评估
authors:
- Osamudiamen Edogun
- Joshua Obigwe
- Irfan Mehmood
affiliations:
- Independent researcher
- University of Bradford
arxiv_id: '2611.09807'
url: https://arxiv.org/abs/2611.09807
pdf_url: https://arxiv.org/pdf/2611.09807
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: Agent 对话记忆架构优化
tags:
- ConversationalMemory
- RAG
- AgentMemory
- McNemarTest
- ContextEfficiency
one_liner: 基于严格配对实验对比事实压缩式对话记忆与传统RAG的优劣势及适用边界
practical_value: '- 电商客服/购物助手Agent可分场景选型：查询订单时间、用户等级等短值类问题用事实压缩记忆，省34% prompt token且准确率更高；用户反馈原话、诉求细节等需要原始措辞的场景用传统RAG

  - 评估两个同任务LLM/Agent模块时，采用配对实验+McNemar检验，同一问题同时跑两个方案、结果存在同一行，可消除不同运行环境、模型漂移的干扰，比分开跑算准确率可靠得多

  - 对话记忆的指数衰减机制仅用于冷热存储分层即可，实测用衰减权重做检索排序会降低5.3个点的准确率

  - 长对话时间类问题的优化trick：写入记忆时直接将相对时间转成绝对时间存储，比RAG把相对时间丢给LLM运算的准确率高25个百分点'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长对话Agent的记忆方案目前分为两类：传统RAG存储完整对话 transcript 检索，存在上下文冗余、长上下文精度衰减问题；事实压缩式记忆将对话转成原子事实存储，省token但损失原始措辞。过往两类方案的对比均为分开运行，结果受环境干扰大，未明确优劣适用边界。

### 方法关键点
- 提出两层记忆架构NMAFC：写入时将对话转成带权重、有效期、关联实体的原子事实，去重后分为热存储（最近活跃事实向量库）和冷存储（全量事实SQLite+FTS5索引）
- 记忆权重按遗忘曲线指数衰减，被检索到则强化重置权重，权重低于阈值从热存储移至冷存储，不做物理删除
- 检索时同时搜索冷热两层，用Reciprocal Rank Fusion融合稠密、稀疏、图召回结果，返回前20条事实+前5条事实对应的原始对话片段
- 采用严格配对实验：同一问题、同一份存储、同一个生成器和评委，同时运行NMAFC与RAG基线，结果存同一行，用McNemar精确检验对比差异

### 关键结果
在LoCoMo长对话记忆基准的1985个问题上对比传统 transcript RAG：
1. 常用4类问题（不含对抗集）上，NMAFC准确率71.4% vs RAG 64.6%，领先6.8个点（p=5.5e-8），prompt token减少34%
2. 时间类问题领先25.5个点，核心收益来自写入时将相对时间转成绝对时间存储，避免RAG让LLM运算时间的误差
3. 优势随参考答案长度下降：参考答案1-2个词时领先9.6个点，超过8个词时落后3.1个点，需要原措辞的对抗集落后14.6个点

**最值得记住的一句话：事实压缩式记忆存的是「说了什么」，RAG存的是「怎么说的」，两者无绝对优劣，按答案需要的是事实值还是原措辞选型即可**
