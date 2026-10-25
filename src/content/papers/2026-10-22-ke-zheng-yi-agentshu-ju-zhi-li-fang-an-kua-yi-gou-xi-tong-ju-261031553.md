---
title: 'Contestable Agents for Data Governance: Recording Human Stewardship of AI-Generated
  Metadata Across Structured and Unstructured Systems'
title_zh: 可争议Agent数据治理方案：跨异构系统留存AI生成元数据的人工管控记录
authors:
- Humza Akhtar
- Brian Freeman
affiliations:
- MongoDB, Inc.
- Trane Technologies
arxiv_id: '2610.31553'
url: https://arxiv.org/abs/2610.31553
pdf_url: https://arxiv.org/pdf/2610.31553
published: '2026-10-22'
collected: '2026-10-25'
category: Agent
direction: Agent · 元数据治理 人在回路设计
tags:
- AI Agent
- Data Governance
- Metadata Management
- Human-in-the-loop
- Data Lineage
one_liner: 提出带举证留痕、人在回路的可争议Agent元数据治理框架，适配跨异构数据场景
practical_value: '- 商品/内容/广告元数据打标场景可复用这套人在回路争议决策流程：Agent输出元数据的同时附引用证据，低置信提案走全量论证，高置信可快速过审，所有修改全留痕，避免错误元数据流入下游召回/排序链路

  - 可复用版本化领域术语表注入Agent的设计，解决电商/广告领域大量专有名词、缩写的LLM理解偏差问题，大幅提升领域场景下Agent的输出准确率

  - 已验证决策自动沉淀为先例的机制，可用来迭代Agent的决策逻辑，减少重复人工审核成本，适配商品类目打标、广告素材标签生成、内容合规审核等高频场景'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
工业场景结构化、非结构化数据分散管理，元数据分类、关联高度依赖少量领域专家；LLM Agent自动生成的元数据无审核留痕机制，错误易扩散到下游业务系统，常规审批无校验追溯依据。
### 方法关键点
1. 提出可争议治理框架：专业Agent对存疑的元数据决策生成带评分、引用来源的论证链
2. 设计人在回路审批流程：管理员可接受/拒绝/修改/补充论证后提交，全链路留存证据、人工干预记录、最终决策结果
3. 配套版本化领域术语表为Agent输入专有名词定义，设置分流路径仅低置信提案走全量论证，已验证决策可沉淀为先例复用
### 关键结果
在两个HVAC场景验证落地：一是基于Brick Schema的点位分类任务，已开源参考实现；二是保修故障模式决策，可自动关联索赔字段、遥测数据与服务记录。
