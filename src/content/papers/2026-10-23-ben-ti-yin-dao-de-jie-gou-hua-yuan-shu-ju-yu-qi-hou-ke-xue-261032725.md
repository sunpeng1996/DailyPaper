---
title: Ontology-Guided Knowledge Graph Construction from Structured Metadata and Climate
  Science Publications
title_zh: 本体引导的结构化元数据与气候科学出版物知识图谱构建
authors:
- Aayush Acharya
- Qi Zhang
- Eduard Dragut
- Longin Jan Latecki
affiliations:
- Temple University
arxiv_id: '2610.32725'
url: https://arxiv.org/abs/2610.32725
pdf_url: https://arxiv.org/pdf/2610.32725
published: '2026-10-23'
collected: '2026-10-26'
category: MultiAgent
direction: 多智体协作 领域知识图谱构建
tags:
- Knowledge Graph
- Multi-Agent
- Ontology
- Information Extraction
- LLM
one_liner: 提出本体引导的多Agent知识图谱构建框架，实现带溯源的高准确率领域知识抽取
practical_value: '- 多Agent分层校验架构可直接复用：先做低成本确定性校验（本体约束、字符串匹配）过滤大部分劣质候选，再调用高成本大模型做语义校验，能在精度提升4%+的前提下仅增加1%的额外成本，适合电商领域商品/用户知识图谱构建、商品信息抽取场景

  - 抽取结果强制绑定原文明文证据的设计可大幅降低大模型幻觉：在电商评论、商品详情页的信息抽取场景中，要求抽取的三元组必须匹配原文片段，可解决目前LLM抽取中常见的无中生有、属性错配问题，同时支持结果可溯源

  - 混合实体链接方案适配长尾领域实体：针对标准化术语（电商SPU/SKU编码、品牌名）用精确字符串匹配，针对长尾语义概念用语义相似度匹配+LLM兜底，能兼顾链接准确率和召回率，适合电商商品实体归一、类目对齐场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
科学文献量级爆发远超人工梳理效率，通用大模型领域信息抽取存在术语认知不足、schema不统一、幻觉严重、结果不可溯源等痛点，气候等垂直领域缺乏高可信度、可落地的大规模知识图谱构建方案。
## 方法关键点
- 多Agent分层流水线架构：分别负责三元组+原文证据抽取、本体一致性校验、证据真实性校验、语义合理性校验、混合实体链接，确定性低成本校验前置，高成本大模型校验后置
- 基于权威领域标准构建两层本体，约束实体类型、关系的定义域/值域，从结构化元数据初始化KG骨架，避免抽取结果schema漂移
- 强制所有三元组绑定原文明文证据，校验证据是否真实存在于原文，确保所有结果可溯源
- 混合实体链接：标准化术语用精确字符串匹配，长尾概念用语义embedding匹配，相似度处于阈值区间的候选调用LLM兜底判断
## 关键实验
在2000篇气候科学出版物上验证，Gemini-2.5-flash校验的Cohen's κ达0.640~0.700，与人与人标注的一致性水平（0.616~0.689）相当；最终产出的气候KG包含133990个节点、755308条关系，文献抽取的23327条三元组准确率达98.96%；对比通用多Agent基线KARMA，三元组数量提升4.49倍，准确率提升6.8个百分点；对比气候领域IE基线ClimateIE，准确率提升17.9个百分点。
## 核心结论
领域知识抽取的精度、schema一致性、可溯源性三个目标可通过分层多Agent架构同时实现，额外校验成本仅为抽取成本的1%
