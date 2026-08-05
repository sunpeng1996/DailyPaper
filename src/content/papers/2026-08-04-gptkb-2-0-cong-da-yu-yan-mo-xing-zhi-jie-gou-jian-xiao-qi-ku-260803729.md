---
title: 'GPTKB 2.0: Direct Construction of Disambiguated Knowledge Bases from Large
  Language Models'
title_zh: GPTKB 2.0：从大语言模型直接构建消歧知识库
authors:
- Yujia Hu
- Tuan-Phong Nguyen
- Simon Razniewski
affiliations:
- ScaDS.AI Dresden/Leipzig & TU Dresden, Germany
- VNU University of Engineering and Technology, Hanoi, Vietnam
arxiv_id: '2608.03729'
url: https://arxiv.org/abs/2608.03729
pdf_url: https://arxiv.org/pdf/2608.03729
published: '2026-08-04'
collected: '2026-08-05'
category: LLM
direction: LLM原生知识库自动化构建
tags:
- LLM
- Knowledge Base
- Entity Disambiguation
- AKBC
- Knowledge Graph
one_liner: 可扩展的LLM原生消歧知识库构建方法，支撑产出首个百万级带实体关系规范化的公开KB
practical_value: '- 可复用on-the-fly实体/关系/类消歧方法，优化电商商品知识图谱、用户标签体系的去重与规范化，减少歧义导致的推荐/搜索误差

  - 参考其精度、规模、成本的权衡设计方案，指导业务侧自定义领域知识库构建的资源分配，平衡效果与投入

  - 可直接引入该百万级公开消歧知识库，扩充RAG场景的通用事实知识，提升电商客服Agent、推荐理由生成的事实准确性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有直接从LLM生成知识库的方案无原生实体表示，易出现重复条目、实体混淆问题；过往自动化知识库构建（AKBC）方案多依赖Wikimedia等外部资源，缺乏LLM原生的大规模无歧义知识库。
### 方法关键点
GPTKB 2.0构建框架内置实体、关系、类的实时消歧模块，针对规模化构建效率与消歧精度做专项优化，系统性量化精度、规模、成本三者的权衡关系。
### 关键结果
规模化运行后产出含超100万消歧实体、38.4M三元组的知识库，是首个实现实体、关系、类显式内部规范化的百万级LLM原生KB，已对外开源。
