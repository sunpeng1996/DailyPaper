---
title: 'ReLTEx: Reliable LLM-based Taxonomy Expansion'
title_zh: ReLTEx：基于大语言模型的可靠分类体系扩展框架
authors:
- Zeinab Ghamlouch
- Mehwish Alam
affiliations:
- Télécom Paris, Institut Polytechnique de Paris, France
arxiv_id: '2608.10970'
url: https://arxiv.org/abs/2608.10970
pdf_url: https://arxiv.org/pdf/2608.10970
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: LLM驱动分类体系自动扩展
tags:
- Taxonomy Expansion
- LLM
- Hallucination Mitigation
- Structure Validation
- Knowledge Organization
one_liner: 融合结构感知校验与递归扩展控制的LLM分类体系扩展框架ReLTEx，降低幻觉提升生成质量
practical_value: '- 电商商品类目/垂直领域知识分类体系的自动扩展，可直接复用「LLM候选生成+结构感知校验」两阶段架构，大幅降低人工维护成本

  - 结构感知校验思路可迁移到商品品类打标、类目层级关系校验、商品挂错类纠错等场景，减少LLM生成的层级不一致问题

  - 递归逐层扩展的控制策略可用于类目体系增量更新，避免新增类目出现冗余、跨层级错位等问题'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有直接调用LLM做分类体系扩展的方案易生成噪声、冗余内容，且存在层级结构不一致的幻觉问题；传统人工维护分类体系成本高、效率低，无法适配新概念快速迭代的业务需求。
### 方法关键点
ReLTEx采用三层架构：1）LLM驱动候选生成模块，基于现有分类体系的父节点生成待补充的子概念候选；2）结构感知校验模块，从语义相关性、层级隶属合理性两个维度对候选做过滤，筛除低质量内容；3）递归扩展控制模块，按分类层级逐层迭代扩展，避免跨层级错位。
### 关键结果
在基准分类体系的掩码扩展任务上，经适配评估指标与人工评估双重验证，生成结果的层级一致性、语义连贯性均显著优于纯LLM生成基线，结构错误与冗余问题得到大幅改善。
