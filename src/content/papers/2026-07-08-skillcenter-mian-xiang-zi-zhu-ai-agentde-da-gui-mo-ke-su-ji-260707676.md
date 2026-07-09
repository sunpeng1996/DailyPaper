---
title: 'SkillCenter: A Large-Scale Source-Grounded Skill Library for Autonomous AI
  Agents'
title_zh: SkillCenter：面向自主AI Agent的大规模可溯源技能库
authors:
- Tianming Sha
- Yue Zhao
- Lichao Sun
- Yushun Dong
affiliations:
- Stony Brook University
- University of Southern California
- Lehigh University
- Florida State University
arxiv_id: '2607.07676'
url: https://arxiv.org/abs/2607.07676
pdf_url: https://arxiv.org/pdf/2607.07676
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent 可溯源技能库构建
tags:
- Agent
- Skill Library
- Source Grounding
- LLM
- Knowledge Retrieval
- Offline Search
one_liner: 开源包含21万+结构化可溯源技能的跨域Agent技能库及自动构建流水线
practical_value: '- 业务侧Agent搭建可直接复用SkillGate质量过滤+迭代溯源校验的流水线，从业务规则、运营文档、技术手册中批量生成结构化可落地技能，降低Agent生成内容的幻觉率，适配电商活动配置、推荐策略落地等场景

  - 低延迟/内网/离线场景的Agent检索可参考SQLite FTS5+BM25的无依赖检索方案，无需向量数据库、GPU及网络访问，可按需拆分领域包部署，适合商家端运营Agent、内网运维Agent等场景

  - 生成式推荐/Agent辅助决策系统可参考其结构化技能设计范式，替代普通RAG的无结构文档块，明确标注技能的适用范围、操作步骤、验证标准，减少大模型的理解成本，提升决策的可解释性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前AI Agent自主性快速提升，但生成结果仅能保证可执行，无法保障正确性、安全性与可维护性；传统人工审核扩展性差，普通RAG使用的无结构文档块缺少质量校验、可操作性弱，现有开源技能库多为人工构建，规模仅数千级，覆盖领域有限，无法支撑多场景Agent落地需求。

### 方法关键点
- 全流水线无人工干预：包含多源采集（学术期刊、ArXiv、GitHub、技术文档、社区论坛等）、SkillGate预过滤（提前筛除无实操性的低质量源，降低生成成本）、分场景模板生成、迭代优化+硬溯源校验（所有修改必须匹配源文档的精确子串，避免幻觉）、四重规则发布门五个环节
- 技能采用结构化Schema：包含适用场景、输入输出、操作步骤、验证标准、溯源信息、质量分，远优于普通RAG的无结构文本块
- 检索层基于SQLite FTS5实现离线BM25检索，无任何外部依赖，支持按领域拆分安装，检索延迟可忽略

### 关键结果
总技能量达216938条，覆盖24个领域，规模超过此前开源技能库10倍以上；其中114565条为流水线生成的可溯源技能，平均质量分3.91（满分5），仅3%生成内容被发布门过滤，跨领域包重复率<0.01%。

### 核心结论
Agent的自主性越高，越需要可溯源的结构化知识约束其行为，而非仅依赖大模型自身的世界知识。
