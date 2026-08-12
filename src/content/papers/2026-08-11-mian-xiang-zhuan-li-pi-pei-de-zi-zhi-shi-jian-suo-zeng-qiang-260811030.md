---
title: Self-Knowledge Retrieval Augmented Generation Framework for Patent Matching
title_zh: 面向专利匹配的自知识检索增强生成框架
authors:
- Jian Zhang
- Songlin Lei
- Zhuohao Yang
- Bangli Liu
- Ziwei Wang
- Xufeng Weng
- Gehan Amaratunga
- Yu Lin
- Hongwei Wang
affiliations:
- School of Computer Science and Technology, Zhejiang University
- ZJU-UIUC Institute, Zhejiang University
- Shaoxing K3i Technology Co. Ltd
- State Key Laboratory of CAD&CG, Zhejiang University
arxiv_id: '2608.11030'
url: https://arxiv.org/abs/2608.11030
pdf_url: https://arxiv.org/pdf/2608.11030
published: '2026-08-11'
collected: '2026-08-12'
category: RAG
direction: 检索增强生成 · 垂直领域语义匹配
tags:
- RAG
- LLM
- Patent Matching
- FAISS
- Knowledge Extraction
one_liner: 提出自知识RAG框架，引导LLM提取专利实体建层级本体，提升专利匹配精度
practical_value: '- 垂直领域（如电商标品/专利等属性强、术语多的场景）做RAG时，可先让LLM自主从query提取关键实体、构建层级本体做查询扩展，显著提升检索准确率

  - 检索链路可复用FAISS召回+生成式匹配的级联架构，先粗筛候选再做细粒度判序，平衡检索效率与匹配精度

  - 垂直领域匹配任务优先考虑自知识RAG替代领域微调，可大幅降低标注成本，同时避免微调带来的灾难性遗忘问题'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
专利文档结构复杂、专业术语密集、多模态信息混杂，传统匹配方法难以识别专利间细微技术差异；现有基于LLM的方案依赖领域微调，标注成本高且易出现灾难性遗忘；通用RAG方案未充分释放LLM自动解析专利、挖掘深层语义关联的能力。

### 方法关键点
1. 构建自知识RAG框架，引导LLM自主从匹配query中提取核心技术实体、构建层级本体结构，实现精准查询扩展
2. 采用FAISS向量检索+生成式匹配的级联架构，用LLM提取的自知识增强对专利创新点的理解，提升匹配准度

### 关键结果
在真实世界专利数据集上性能显著优于各类基线方案，验证了自知识RAG在垂直领域语义匹配场景的有效性与落地潜力
