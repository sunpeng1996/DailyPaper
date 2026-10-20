---
title: 'Designing for Imperfect Prompts: A Simulation-Based Evaluation of an LLM-Based
  Enterprise Data Assistant Using Knowledge Graphs'
title_zh: 面向不完美提示的知识图谱增强LLM企业数据助手仿真评估
authors:
- Niklas Wagner
- Alexander Mädche
affiliations:
- Karlsruhe Institute of Technology (KIT)
arxiv_id: '2610.23304'
url: https://arxiv.org/abs/2610.23304
pdf_url: https://arxiv.org/pdf/2610.23304
published: '2026-10-16'
collected: '2026-10-20'
category: Agent
direction: LLM Agent 企业数据查询语义适配优化
tags:
- LLM
- Knowledge Graph
- Semantic Mediation
- Prompt Optimization
- Text-to-SQL
- Enterprise Agent
one_liner: 对比两种语义中介层方案，验证知识图谱可有效解决企业场景LLM数据助手的不完美提示问题
practical_value: '- 电商运营后台、商家数据查询类Agent面对用户不规范query（含行业黑话、缩略词）时，可优先采用KG驱动的语义中介层，替代纯语义相似度匹配方案，提升意图识别准确率

  - 企业级数据类Agent的效果评估可复用「仿真数据集测试+LLM-as-a-Judge+人工校验」的三级框架，兼顾评估效率与结果可信度

  - 可复用从业务数仓自动构建领域KG的思路，快速适配不同业务线的用户查询意图对齐需求，避免重复开发schema适配规则'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
企业真实部署的LLM数据助手面临大量不完美用户prompt：普遍包含领域专属词汇、缺失数据库schema关联信息，导致Text-to-SQL等数据查询能力准确率大幅下降。
### 方法关键点
设计两类语义中介层方案做对照：① 基于语义相似度的schema直接匹配方案；② 基于数仓自动构建的知识图谱做语义映射的中介方案；采用仿真测试+LLM-as-a-Judge评估+人工校验的三级评估范式。
### 关键结果
KG驱动的语义中介层在Precision、Recall、F1三类核心指标上全面优于纯schema匹配方案，对不同技能水平用户的查询意图保留度均有显著提升，场景适配性更强
