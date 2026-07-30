---
title: 'AgentMap: Joint Equivalence and Subsumption Discovery for Ontology Matching'
title_zh: AgentMap：面向本体匹配的等价与从属关系联合发现
authors:
- Yiping Song
- Jiaoyan Chen
- Renate Schmidt
- Hui Yang
- Wen Zhang
affiliations:
- The University of Manchester, UK
- Zhejiang University, China
arxiv_id: '2607.27130'
url: https://arxiv.org/abs/2607.27130
pdf_url: https://arxiv.org/pdf/2607.27130
published: '2026-07-29'
collected: '2026-07-30'
category: MultiAgent
direction: 多智能体协作 · 本体语义匹配
tags:
- Ontology Matching
- MultiAgent
- LLM
- Semantic Alignment
- Knowledge Integration
one_liner: 提出统一等价与从属发现的混合本体匹配任务，以及多智能体语义匹配框架AgentMap
practical_value: '- 电商品类、商品属性的分层语义对齐可复用这套等价/从属关系联合发现逻辑，解决不同商家/平台类目映射痛点

  - 语义检索+层级搜索+多Agent协同推理的架构，可迁移到知识图谱对齐、标签体系归一、商品标准化等业务场景

  - 混合匹配的基准构建方法，可用于优化推荐系统语义召回的正负样本构造流程，提升语义匹配精度'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
传统本体匹配仅能单独识别等价或从属关系，无法同时发现两类语义映射，跨本体知识整合受概念粒度差异影响，匹配精度受限。
### 方法关键点
1. 定义混合本体匹配（HOM）新任务，统一等价与从属关系发现目标；
2. 多Agent框架AgentMap融合语义检索、层级搜索、多Agent协同推理模块，对源本体概念逐层探索目标本体，优先匹配等价概念，无匹配时输出最细粒度从属父概念。
### 关键结果
扩展4个现有本体匹配数据集构建HOM基准，混合设置下性能表现优异，同时在纯等价、纯从属匹配任务上分别超过对应基线模型。
