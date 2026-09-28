---
title: Segment-Level Agentic Topic Modeling for Improved Data Exploration and Resource
  Efficiency
title_zh: 面向数据探索与资源效率优化的段级智能体主题建模框架
authors:
- Myeongjun Erik Jang
- Antonios Georgiadis
- Sae Young Moon
- Fran Silavong
affiliations:
- J.P. Morgan Chase
arxiv_id: '2609.31460'
url: https://arxiv.org/abs/2609.31460
pdf_url: https://arxiv.org/pdf/2609.31460
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: Agent 多智能体主题建模优化
tags:
- Topic Modeling
- LLM Agent
- Text Clustering
- Resource Efficiency
- Iterative Refinement
one_liner: 基于文本段聚类与多智能体反馈迭代的主题建模框架，兼顾效果与资源效率
practical_value: '- 长文本处理流程可复用：电商客服对话、用户评论、商品详情页等长文本可先按句法切分为句子/段落级短片段再聚类，能避免长文本embedding塌陷、lost-in-the-middle问题，同时降低LLM调用成本

  - 多智能体迭代架构可迁移：将主题生成任务拆分为「评估Agent（检测质量问题）-操作Agent（执行拆分/合并）-规划Agent（判断迭代收益）」的分工模式，比单Prompt生成的主题/标签/类目质量更稳定，可迁移到用户标签体系生成、商品类目体系迭代场景

  - 成本优化技巧可落地：聚类后仅对每个簇采样固定数量的代表性样本调用LLM生成主题，无需遍历所有文档，零迭代时仅消耗同类LLM主题建模方案8%-25%的token，适合大规模语料的离线标签生产

  - 层级化主题生成方法可复用：基于「簇中心embedding+主题名embedding+主题描述embedding」的多视图聚类生成上层父主题，无需额外大量调用LLM，可低成本构建商品、内容的层级化标签体系'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM驱动的主题建模方案多在文档级别分配主题，无法量化多主题在单文档中的占比，且调用成本随文档数量、长度线性增长，生成的主题易出现过宽/过窄问题，缺乏有效迭代优化机制，难以适配工业级大规模文本处理需求。
### 方法关键点
- 段级主题建模：先将文档按句法切分为句子/段落级短片段，生成embedding后用层次聚类得到片段簇；每个簇仅采样最多nS个代表性片段调用LLM生成主题名与描述，再基于片段归属计算每个文档的多主题分布，无需逐文档调用LLM。
- 多智能体反馈迭代：由评估Agent分别检测单个主题的一致性、主题间的重复度，操作Agent执行主题拆分/合并，规划Agent判断迭代收益，最多迭代e轮或连续T轮无收益则停止。
- 层级化主题生成：拼接片段簇中心embedding、主题名embedding、主题描述embedding做多视图聚类，生成上层父主题，低成本构建主题层级体系。
### 关键结果
在3个公开数据集、3个金融行业内部数据集上对比BERTopic、TopicGPT、TIDE等7个基线：零迭代时主题准确率（TA）相对最优基线平均提升21%，LLM token消耗仅为TIDE的24.4%、TopicGPT的8.19%；3轮迭代后TA进一步提升3%-5%，token消耗仍低于TopicGPT。
### 核心结论
对于文本类分析任务，先做细粒度语义单元的无监督聚类再做上层LLM加工，往往能在降本的同时提升效果。
