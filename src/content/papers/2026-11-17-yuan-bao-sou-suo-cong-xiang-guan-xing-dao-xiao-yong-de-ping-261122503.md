---
title: 'From Relevance to Utility: Rubric Alignment in Yuanbao Search'
title_zh: 元宝搜索从相关性到效用的评分规则对齐框架
authors:
- Yu Lu
- Lixin Zou
- Yangqi Chen
- Hui Xu
- Qiaolin Xia
- Hao Wang
- Qianwen Ma
- Reed Li
- Shuang Zeng
- Haijin Liang
affiliations:
- Tencent Inc.
- Wuhan University
arxiv_id: '2611.22503'
url: https://arxiv.org/abs/2611.22503
pdf_url: https://arxiv.org/pdf/2611.22503
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Agent搜索 · 全链路效用对齐
tags:
- Agentic Search
- Rubric Alignment
- Retrieval
- Ranking
- Reinforcement Learning
- RAG
one_liner: 以查询专属评分规则为统一监督信号，全链路对齐Agent搜索各阶段至效用最优
practical_value: '- 可复用rubric粗到细生成方案：用多LLM生成检索增强答案抽粗标准，再结合召回候选生成可落地的细粒度正负加权规则，大幅降低RAG/Agent检索的效用对齐标注成本

  - 召回排序对齐技巧：将集合级rubric蒸馏为单文档效用标签，用分级标签微调dual-encoder召回，加辅助头多任务训练排序模型，几乎不增加推理成本即可提升下游生成质量

  - 集合选择RL优化：采用GRPO+最优rollout蒸馏的双分支RL结构，解决稀疏集合奖励的信用分配问题，训练更稳定收敛更快，可直接迁移到RAG上下文选段、推荐结果集组合场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Agent搜索面向下游LLM推理提供文档集合，而非传统面向人类浏览的相关性排序，现有方案仅单独优化单环节或顶层选集合，上游召回排序未与最终回答效用对齐，存在粒度不匹配、标注成本高、集合奖励稀疏三大痛点。
### 方法关键点
- 逐查询生成加权rubric：粗阶段用3个不同LLM生成检索增强答案，抽取合并为高维标准；细阶段结合top15召回候选生成可验证的正负子标准，正标准带权重、负标准带扣分阈值
- 轻量标签蒸馏：大模型标注少量(query, document, rubric)三元组，蒸馏到小模型标签器，再经RL优化输出4级单文档效用标签，解决集合级标注无法规模化的问题
- 全链路对齐：召回用dual-encoder分两阶段训练，先域内对比预训练再用效用标签微调；排序用4B多任务模型，主头对齐效用标签，辅助头接入权威、时效、质量信号做正则；选集合用7B双分支RL，GRPO优化正样本，最优rollout蒸馏解决稀疏奖励的信用分配问题
### 关键结果
基于腾讯元宝搜索生产环境实验，全链路上线后端到端回答质量GSB提升8.52%；其中选集合环节贡献最大4.82%，排序贡献3.94%，召回贡献0.40%；rubric让奖励模型和人类判断的一致性从68.7%提升至79.3%。
### 核心结论
Agent检索的核心评价标准已从「单文档相关性」转向「集合级下游效用」，用统一rubric作为全链路监督信号，可在不增加线上推理延迟的前提下大幅提升端到端质量。
