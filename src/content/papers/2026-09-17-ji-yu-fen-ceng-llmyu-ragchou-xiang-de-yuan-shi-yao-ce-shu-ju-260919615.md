---
title: Semantic Layer Induction from Raw Telemetry via Hierarchical LLM and RAG Abstraction
title_zh: 基于分层LLM与RAG抽象的原始遥测数据语义层自动构建方法
authors:
- Yuanzhe Jia
- Ali Anaissi
affiliations:
- University of Sydney, Australia
- University of Technology Sydney, Australia
arxiv_id: '2609.19615'
url: https://arxiv.org/abs/2609.19615
pdf_url: https://arxiv.org/pdf/2609.19615
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: 语义层自动构建 · 分层LLM+RAG抽象
tags:
- Semantic Layer
- RAG
- Hierarchical Abstraction
- LLM-as-Judge
- Telemetry Processing
one_liner: 无需标注数据与人工规则，通过两级LLM+RAG流程自动从原始日志构建业务语义层
practical_value: '- 处理电商用户行为、埋点日志等异构无标注数据时，可复用「先粗粒度匹配领域知识识别高维业务特征、再细粒度聚类降噪生成标准语义节点」的两级流程

  - 语义质量评估可直接复用LLM-as-Judge方案，无需大量人工标注即可实现规模化效果校验，大幅降低运营成本

  - 原始日志到业务语义的自动化映射方案可迁移到电商用户行为数据清洗、特征工程环节，预计减少80%左右的人工维护成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
海量异构带噪的原始遥测数据难以直接转化为业务洞察，人工维护原始数据到业务KPI的映射规则成本高、鲁棒性差，无标注场景下的自动化语义层构建存在空白。
### 方法
端到端语义层构建框架无需标注数据与人工规则，采用两级语义抽象流程：1. 结合领域知识的LLM推理识别粗粒度高层业务特征；2. 经数据精炼、混合检索、多级过滤、语义聚类、标准化命名的结构化管线生成细粒度业务节点。
### 关键结果
生产级遥测数据评测显示：人工评估语义质量百分制得分从50提升至80+，维护人力成本降低80%，噪声过滤率达74%，LLM-as-Judge评估的Cohen's kappa系数为0.87。
