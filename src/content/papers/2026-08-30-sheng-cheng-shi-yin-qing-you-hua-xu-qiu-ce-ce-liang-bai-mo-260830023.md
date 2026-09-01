---
title: 'Demand-Side Measurement for Generative Engine Optimization: Constructing and
  Validating a Million-Persona, Intent-Annotated Buyer Corpus'
title_zh: 生成式引擎优化需求侧测量：百万级意图标注买家语料库构建与验证
authors:
- Dmitrij Żatuchin
- Daniil Dzemesjuk
affiliations:
- Estonian Entrepreneurship University of Applied Sciences
- Rankfor.AI OÜ
arxiv_id: '2608.30023'
url: https://arxiv.org/abs/2608.30023
pdf_url: https://arxiv.org/pdf/2608.30023
published: '2026-08-30'
collected: '2026-09-01'
category: Eval
direction: 生成式推荐 · 评估数据集构建
tags:
- GEO
- Persona Corpus
- Synthetic Data
- Search Intent
- Generative Recommendation
- Evaluation Dataset
one_liner: 构建并验证包含103万买家persona、带分层意图与偏好来源标注的PersonaGen-1M语料库
practical_value: '- 可复用MinHash LSH + 语义嵌入的两步persona去重pipeline，先词法去重再语义去重，大幅降低冗余同时保留多样性，适合构建用户画像、测试query库的场景

  - 可直接使用公开的PersonaGen-15K子集作为生成式推荐/GEO效果评估的query源，替代人工构造query，降低人工prompt带来的26.5%结果方差

  - 参考其persona schema设计，在自有用户画像体系中新增分层搜索意图（信息/商业/交易）、偏好信息来源字段，打通需求侧与生成式推荐供给侧的关联分析

  - 做生成式推荐/AI导购的prompt效果验证时，可借鉴「同一persona多query覆盖不同需求」的测试范式，避免单query评估的结果偏差'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式引擎已成为用户获取消费决策信息的核心入口，其回答中直接提及的品牌会获得绝大部分用户注意力，生成式引擎优化（GEO）成为品牌方的核心新需求。当前GEO研究仅依赖供给侧的引擎返回结果数据，缺乏匹配的需求侧数据支撑：现有大规模persona语料仅面向训练数据增强设计，未携带分层搜索意图标注与用户信任的信息来源字段，无法和供给侧的品牌推荐结果做关联分析；同时人工构造的测试query会带来26.5%的结果方差，远高于品牌本身的影响（1.5%），无法真实反映用户的实际提问特征。
### 方法关键点
- 数据源：聚合4个公开HuggingFace persona语料，共获得4000万条原始描述
- 两级去重pipeline：首先用GPU加速MinHash LSH做词法去重（Jaccard阈值0.9），压缩至420万条；再用KaLM-Embedding-Gemma3-12B生成语义嵌入，过滤余弦相似度>0.9的语义重复样本，压缩至约100万条
- 结构化富集：采用Grok-4-1-fast强制JSON输出模式，按固定schema生成每个persona的全量属性，包含分层搜索意图、典型搜索query、偏好信息来源等核心字段
- 质量验证：从完整性、维度多样性、维度关联性三个维度完成语料校验
### 关键结果
最终产出1,031,732条有效persona，覆盖511个行业、4种市场场景，共包含516万条搜索query，其中17.4%的商业意图persona可直接用于GEO评估；语料完整性100%，行业与意图的Cramer's V达0.299，验证了意图标注符合行业特性；试点测试中，150条FinTech商业意图query调用生成式引擎，97.3%的回答返回了具体品牌，平均每条回答提及5.01个品牌。
### 核心结论
人工构造的测试query会带来生成式引擎回答26.5%的结果方差，远高于品牌本身的影响，用真实用户视角的query库做评估才具备可信度。
