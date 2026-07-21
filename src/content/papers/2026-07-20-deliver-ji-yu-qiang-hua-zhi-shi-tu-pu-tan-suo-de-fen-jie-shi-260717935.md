---
title: 'DeLIVeR: Decomposed Learning for Information-grounded Veracity Recognition
  via Reinforced Knowledge Graph Exploration'
title_zh: DeLIVeR：基于强化知识图谱探索的分解式事实真实性识别框架
authors:
- Cong Hoan Nguyen
- Thomas Hoang
- Hieu Minh Duong
- Long Nguyen
affiliations:
- University of Louisville
- Denison University
arxiv_id: '2607.17935'
url: https://arxiv.org/abs/2607.17935
pdf_url: https://arxiv.org/pdf/2607.17935
published: '2026-07-20'
collected: '2026-07-21'
category: RAG
direction: RAG优化 · 强化学习+知识图谱事实校验
tags:
- RAG
- Knowledge Graph
- GRPO
- Fact Checking
- Question Generation
one_liner: 通过GRPO优化的LLM规划器生成多维度问题集，结合KG检索实现高精度可解释事实校验，较SOTA提升10-15%F1
practical_value: '- 电商内容风控、虚假营销识别场景可直接复用框架：将商品宣传内容作为claim，构建商品/资质KG，用GRPO优化查询生成召回相关资质信息，判断内容真实性，效果优于普通RAG

  - RAG系统的多query生成优化可复用GRPO训练方案：采用格式/结构/准确性三维reward优化小参数LLM的query生成，实测4个query时达到最优性价比，避免过多query增加检索成本

  - 高风险推荐、内容审核等需可解释性的场景可借鉴KG+多query检索的可追溯链路：每个结论都能对应到KG来源路径和查询问题，满足合规、审核溯源要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统RAG做事实校验存在多跳推理缺口、静态query歧义大、检索策略固定无法适配复杂声明的问题，LLM直接校验 hallucination 率高，普通RAG召回证据相关性差，无法满足高准确率、可解释的事实校验需求。

### 方法关键点
- 框架分为KG构建、问题生成、检索校验、GRPO优化四部分：先基于证据语料用OpenIE抽取三元组构建带溯源的KG，过滤孤立节点保证多跳连通性
- 轻量二级LLM作为Planner，将输入声明分解为4-8个覆盖实体、时间、关系、矛盾等多维度的问题，最大化问题覆盖熵避免冗余
- 多问题embedding匹配KG节点/边embedding召回结构化证据，输入冻结的主LLM生成真实性判决（True/False/NEI）
- 用GRPO优化Planner参数，reward由格式合规（15%权重）、问题维度覆盖（60%权重）、证据准确性（25%权重）组成，无需critic训练更稳定

### 关键实验
在LIAR、FEVER、PolitiFact三个事实校验基准上对比Vanilla LLM、Naive RAG、LightRAG、ReAct、HippoRAG2五个基线，采用Qwen2.5-7B时峰值F1分别为83.73、84.57、79.70，较次优的HippoRAG2提升10-15%；ablation验证4个问题时达到最优性能，过多问题会引入冗余噪声降低效果。

### 核心结论
用轻量强化学习优化RAG的查询生成策略，配合结构化KG检索，能以很低的额外成本大幅提升事实类任务的准确率和可解释性
