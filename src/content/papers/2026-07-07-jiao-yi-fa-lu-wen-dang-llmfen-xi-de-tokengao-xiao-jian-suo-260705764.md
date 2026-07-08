---
title: Inject or Navigate? Token-Efficient Retrieval for LLM Analysis of Transactional
  Legal Documents
title_zh: 交易法律文档LLM分析的Token高效检索方案对比
authors:
- Mahmoud Hany
- Mourad ElSheraey
- Mahmoud Said
- Peter Naoum
affiliations:
- Syntheia Pty Ltd
arxiv_id: '2607.05764'
url: https://arxiv.org/abs/2607.05764
pdf_url: https://arxiv.org/pdf/2607.05764
published: '2026-07-07'
collected: '2026-07-08'
category: RAG
direction: RAG · 结构化检索效率优化
tags:
- RAG
- Retrieval Optimization
- Token Efficiency
- Structured Index
- LLM-as-Judge
one_liner: 对比全文档注入、向量检索、结构化索引导航三种RAG模式，给出法律QA的质量-成本权衡方案
practical_value: '- RAG系统可复用硬召回节点上限设计，如电商商品QA、导购Agent召回时固定最多返回10个相关chunk，避免过度召回浪费token、引入噪声，实测可降本20%且几乎不损失效果

  - 不要盲目叠加BM25等混合检索策略，需在业务域验证效果，本实验中BM25的长度偏置导致token开销翻倍甚至超过全量注入成本，短文本为主的电商场景更需注意

  - 核算RAG成本时需拆分token footprint（影响长上下文性能）和现金成本（受缓存折扣、访问频次影响），高频小知识库（如电商活动规则、售后政策）优先用全量注入缓存，低频大知识库优先用结构化检索

  - 优化RAG召回效果优先提升chunk的元数据丰富度而非更换嵌入模型，可给商品/内容的召回chunk新增品类、属性、时效等结构化标签，大幅提升检索准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
全文档注入（inject）是RAG的简单基线，召回率最高但token开销随语料规模线性增长，还会触发LLM长上下文性能衰减；法律文档存在大量跨条款引用、修正案优先级、术语定义等结构依赖，普通向量检索无法覆盖，亟需平衡检索质量、token效率、运行成本的方案。
### 方法关键点
- 固定结构感知分块作为统一前置步骤，对比三种RAG模式：全文档注入基线、向量检索+重排（navembed）、结构化索引导航（navindex）
- navindex采用双文件架构：索引文件存储布尔语义标签、交叉引用ID、术语定义标记等轻量化元数据，正文文件存储条款原文；检索时先让LLM扫描索引选出最多10个相关节点，自动跟随交叉引用边补全上下文后再生成回答
- 评估采用位置偏置控制的成对LLM judge，用标注参考答案锚定评分，明确区分token footprint（模型实际attention的token数，影响长上下文性能）和现金成本（受厂商缓存折扣、访问模式影响）两个独立指标
### 关键结果
在15份公开交易法律文档的20道带标注验证问题集上测试：
1. 带cross-encoder重排的navembed与inject在16/18道文档相关问题打平，token开销降低17.3×；GTE嵌入版本token开销降低29.9×，但打平率略低
2. navindex在全部20道问题上与inject打平，总token开销低1.61×，回答阶段上下文缩小56×，现金成本降低25%
3. 推导缓存 crossover 规则：仅当语料规模小于召回载荷的10倍时，缓存全量注入的现金成本更低
### 核心结论
结构化元数据对检索效果的提升远大于嵌入模型选型，硬召回数量上限是性价比最高的检索控制手段。
