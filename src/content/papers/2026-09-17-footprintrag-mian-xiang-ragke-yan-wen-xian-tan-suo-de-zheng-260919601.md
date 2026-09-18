---
title: 'FootprintRAG: Visual Analytics for Evidence Context Refinement in RAG-based
  Scientific Literature Exploration'
title_zh: FootprintRAG：面向RAG科研文献探索的证据上下文细化可视化系统
authors:
- Xingyu Liu
- Yu Dong
- Qizhen Yu
- Shiyu Cheng
- Zhe Wang
- Guan Li
- Guihua Shan
- Dong Tian
- Christy Jie Liang
- Quang Vinh Nguyen
affiliations:
- Computer Network Information Center, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Hangzhou Institute for Advanced Study, UCAS
- University of Technology Sydney
- Western Sydney University
arxiv_id: '2609.19601'
url: https://arxiv.org/abs/2609.19601
pdf_url: https://arxiv.org/pdf/2609.19601
published: '2026-09-17'
collected: '2026-09-18'
category: RAG
direction: RAG 证据上下文优化 · 人机协同可视化
tags:
- RAG
- LLM Agent
- Visual Analytics
- Human-AI Collaboration
- Scientific Literature Mining
one_liner: 提出LLM-Agent驱动的可视化分析系统，支持RAG科研文献探索场景下生成前证据上下文可干预调整
practical_value: '- 可复用「预生成阶段证据上下文可干预」的设计思路，优化电商RAG客服、合规性商品推荐的召回结果校验流程，提前过滤低质量证据，降低生成幻觉风险

  - 可迁移ERS多维度排序逻辑，融合关联度、来源多样性、查询相关性三个维度优化召回候选集排序，平衡推荐/搜索结果的相关性和品类丰富度

  - 可借鉴「并行多Query扩展+多轮检索结果对比」的设计，优化搜索Query改写的可解释性，支持运营人员快速对比不同Query变体的召回效果，调整搜索策略'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统在开放域探索任务中，检索、重排序、过滤等上下文构建过程完全黑盒，用户无法感知证据单元的取舍逻辑，易遗漏高价值但语义相关性较低的证据，生成结果可信度差、可追溯性弱，在科研文献综述等对准确性要求极高的场景下痛点尤为突出。

### 方法关键点
- 证据单元统一建模：将文献拆分为文本、图文混合两类证据单元，图文单元通过LLM生成描述实现与文本单元的统一检索范式，所有单元嵌入后存入向量库
- 多轮并行检索机制：Query Agent基于初始Query生成多个并行查询变体，分语义答案查询、精确术语匹配两类意图分别检索，返回结果由Assessment Agent标记高/中/低支持度
- 补充证据召回策略：设计ERS（Evidence Relation Score）融合关联度（与已选高价值证据相似度）、来源多样性（降低单篇文献依赖）、查询相关性三个维度，从全库和当前检索截断集中召回可能遗漏的高价值证据
- 人机协同交互界面：提供四视图联动界面，支持用户对比多轮多策略检索结果、手动增删证据单元、生成带溯源链接的总结内容

### 关键实验
在包含10~48篇领域文献的多个测试 corpus 上验证，对比基线为传统单轮RAG、现有RAG可视化调试工具；用户研究显示候选证据修订、上下文确认功能的满意度达4.9/5分，90%参与者认为系统可显著提升生成结果可信度，证据级操作占用户交互总量的60%以上。

### 核心结论
RAG系统的用户干预可从生成后内容校正提前到生成前证据上下文优化阶段，通过透明化中间过程、引入人机协同可大幅提升高要求场景下的生成质量与可信度。
