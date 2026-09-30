---
title: 'Follow the Entities: A Corpus Map for Agentic Search'
title_zh: 面向智能体搜索的实体中心语料导航层CORPUSMAP
authors:
- Soyeong Jeong
- Sujay Kumar Jauhar
- Sung Ju Hwang
- Andrew Joohun Nam
affiliations:
- KAIST
- Microsoft
arxiv_id: '2609.37226'
url: https://arxiv.org/abs/2609.37226
pdf_url: https://arxiv.org/pdf/2609.37226
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 智能体搜索 · 实体导航层
tags:
- Agentic Search
- Entity Linking
- RAG
- Corpus Navigation
- LLM Agent
one_liner: 提出离线构建的实体中心语料导航层CORPUSMAP，优化智能体搜索的效果与效率
practical_value: '- 电商知识库、订单/商品查询类Agent搜索场景，可复用CORPUSMAP的离线实体对齐+Entity Page设计，替代纯向量RAG，降低多文档证据拼接的token消耗，高频实体查询的收益尤其明显

  - 语料频繁更新的场景（如电商上新、运营规则迭代），可借鉴其增量更新逻辑，仅修改关联实体的Entity Page，无需全量重建导航层，大幅降低维护成本

  - 资源有限的场景可优先用低成本小模型/开源实体链接工具（如GLiNER）构建导航层，验证显示跨模型复用导航层仍有稳定效果，无需用大模型全流程构建'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前智能体搜索直接遍历扁平结构的语料库，每次查询都需要重新推断文档间的关联关系，不仅容易遗漏分散在多份文档中的互补证据，还会产生大量冗余token消耗；现有GraphRAG等实体增强检索方案仅在检索侧使用实体关系，未将关联关系暴露给智能体自主导航，仍受限于初始检索的召回天花板。
### 方法关键点
- 离线构建实体-文档二部导航图，仅保留关联至少2份文档的跨文档实体，每个实体对应**Entity Page**，聚合该实体的核心事实并标注来源，同时关联所有提及该实体的原始文档
- 构建流程分4步：从语料抽样诱导适配业务的实体类型目录→逐文档提取局部实体→跨文档对齐同指实体完成注册→渲染保留实体的Entity Page
- 推理时智能体无需适配新工具，可直接通过标准文件操作访问Entity Page，从查询关联实体出发遍历相关文档
### 关键实验
在EnterpriseRAG-Bench、WixQA、HERB三个多文档问答基准上，对比Raw Corpus、LLM Wiki、Corpus2Skill等5个基线，覆盖7款不同架构的LLM测试：
- 相比Raw Corpus基线，CORPUSMAP整体回答质量提升6.4~11.7个百分点，输入token平均减少34%~57%
- 用开源GLiNER构建的无LLM版本效果与LLM构建版相当，增量更新可节省70%左右的全量重建token
### 核心结论
优化语料的组织方式，而非仅优化智能体的搜索策略，是提升大语料下智能体搜索效果的高性价比方向
