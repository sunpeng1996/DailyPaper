---
title: 'SciSchema.org: A Multidisciplinary Collection of Schemas for Structured Scientific
  Process Descriptions'
title_zh: SciSchema.org：多学科结构化科学流程描述Schema集合
authors:
- Jennifer D'Souza
- Sameer Sadruddin
- Anisa Rula
- Ana Bossler
- Andrés Fullana
- Enric Bas
- Syed Ather
- Defne Circi
- Anlan Chen
- L. Catherine Brinson
affiliations:
- TIB Leibniz Information Centre for Science and Technology
- University of Brescia
- University of Alicante
- Georgia Institute of Technology
- Duke University
arxiv_id: '2607.27955'
url: https://arxiv.org/abs/2607.27955
pdf_url: https://arxiv.org/pdf/2607.27955
published: '2026-07-30'
collected: '2026-08-03'
category: Other
direction: 科研知识图谱 · 结构化Schema构建
tags:
- SchemaMining
- Human-in-the-Loop
- LLM
- KnowledgeGraph
- StructuredData
one_liner: 开源覆盖5大学科的16个专家标注科学流程Schema，配套人在回路LLM挖掘构建流程
practical_value: '- 人在回路+LLM生成候选Schema再专家校准的工作流，可直接迁移到电商领域商品/用户/交易领域知识Schema的构建场景，降低人工梳理成本

  - 多格式Schema输出（JSON Schema/SHACL）的设计思路，可复用到业务中需兼容多系统的元数据规范制定环节

  - Schema质量验证的四维框架（结构合规/来源可追溯/专家评审/语法一致性），可直接复用为业务知识图谱Schema的验收标准'
score: 3
source: arxiv-cs.IR
depth: abstract
---

### 动机
科研流程相关信息分散在论文的正文、表格、图、协议、补充文件等异构载体中，难以支撑跨研究对比、实验复现、流程复用、自动化处理等需求。
### 方法关键点
1. 采用人在回路的Schema挖掘工作流：先由LLM从流程规范、科研论文、专家反馈生成候选结构，再由领域专家校准输出最终主Schema
2. 首期发布16个专家标注Schema，覆盖生物与生物技术、材料与化学、成像与测量、物理、心理学5大学科，每个Schema定义输入输出、材料、仪器/软件、参数、步骤等可复用字段
3. 开放全链路资源：包含JSON Schema、SHACL格式的最终Schema，中间生成结果、专家反馈记录、源论文元数据、分析脚本等，配套技术验证覆盖结构、来源、专家评审、语法合规性4个维度
### 关键结果
可直接支持结构化标注、元数据增强、科研知识图谱构建、信息抽取、语义出版、跨研究对比等场景
