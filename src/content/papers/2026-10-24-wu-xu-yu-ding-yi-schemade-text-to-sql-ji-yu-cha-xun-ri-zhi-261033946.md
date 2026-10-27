---
title: 'Schema-Free Text-to-SQL: Learning Enterprise Database Structure from Query
  Logs'
title_zh: 无需预定义Schema的Text-to-SQL：基于查询日志的企业库结构学习
authors:
- Ömer Faruk Akgül
- Nikhil Kapahi
- Prajit Reddy Muppidi
affiliations:
- University of Southern California
- Amazon
arxiv_id: '2610.33946'
url: https://arxiv.org/abs/2610.33946
pdf_url: https://arxiv.org/pdf/2610.33946
published: '2026-10-24'
collected: '2026-10-27'
category: RAG
direction: 大语言模型应用 · Text-to-SQL 优化
tags:
- Text-to-SQL
- GraphRAG
- Knowledge Graph
- Enterprise LLM
- Retrieval Augmented Generation
one_liner: 从企业历史查询日志构建知识图谱，通过实体驱动GraphRAG实现无Schema文档的高可用Text-to-SQL
practical_value: '- 落地企业级数据查询Agent时，可跳过维护成本极高的Schema文档，通过解析历史查询日志挖掘表关联、字段语义、业务实体映射，大幅降低NL2SQL的落地门槛，适合电商运营/分析师自助查数场景

  - RAG检索遇到业务术语与系统存储标识不匹配的问题时，可引入「实体对齐优先+嵌入相似度兜底+知识图谱遍历补全」的混合召回策略，相比纯语义相似度召回准确率提升明显，可复用在商品标签检索、用户画像查询等电商RAG场景

  - 评估开放域生成任务（如自定义报表生成、运营自然语言查询）时，摒弃单金标准匹配思路，采用「执行有效性+LLM盲评+专家抽样校验」的多维度评估框架，更贴合业务实际需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有SOTA Text-to-SQL系统高度依赖完整、可解释的数据库Schema文档，但企业级生产库普遍存在表/字段命名晦涩、无显式外键声明、Schema迭代快、文档缺失或过时的问题，纯嵌入相似度的RAG基线无法解决业务术语和库表命名的词汇鸿沟，导致工业落地准确率骤降。
### 方法关键点
- 离线阶段：解析历史查询日志构建知识图谱，节点为表（附带LLM生成的表/字段语义描述、关联业务实体），边为历史出现的表关联关系，权重为关联频次
- 在线检索阶段：先提取用户问题的业务实体，通过实体重叠度匹配核心表作为种子节点，再结合嵌入相似度、历史相似查询得分做多策略排序，通过BFS遍历知识图谱挖掘关联表，用Personalized PageRank做结构重排
- 生成阶段：召回结果按「表元数据+关联路径+历史相似查询」的结构化格式喂给LLM，约束仅使用召回的表和关联路径生成SQL，减少幻觉
### 关键实验
分别在Amazon内部240表、50万条历史查询的生产环境，和公开Beaver基准测试，对比基线为嵌入相似度RAG方案：Beaver数据集上执行准确率达95.7%，比基线的60.8%高34.9个百分点；内部部署中数据工程师偏好率达70%，基线仅为10%；消融实验显示移除实体匹配模块后得分下降5.4%，是核心贡献点。
### 核心结论
企业级LLM应用的核心壁垒往往不是模型能力，而是如何把散落的历史业务行为数据转化为结构化的领域知识，消除用户自然语言和系统内部标识的语义鸿沟。
