---
title: Co-adaptive Rule Routing and Constraining for Structured Knowledge Retrieval
title_zh: 面向结构化知识检索的协同自适应规则路由与约束框架
authors:
- Zhisheng Qi
- Haoyu Han
- Jiaxi Li
- Bing He
- Huiyuan Chen
- Franck Dernoncourt
- Ryan A. Rossi
- Mahantesh M. Halappanavar
- Jin Lu
- Yu Zhang
affiliations:
- University of Georgia
- Michigan State University
- Georgia Institute of Technology
- Amazon
- Adobe Systems
arxiv_id: '2610.14465'
url: https://arxiv.org/abs/2610.14465
pdf_url: https://arxiv.org/pdf/2610.14465
published: '2026-10-16'
collected: '2026-10-26'
category: Agent
direction: Agent 规则路由与检索器协同优化
tags:
- Structured Retrieval
- Agent Routing
- Reinforcement Learning
- Contrastive Learning
- Co-adaptation
- RAG
one_liner: 无需预定义查询-规则对监督，交替优化路由Agent与规则约束检索器提升结构化检索效果
practical_value: '- 电商商品/用户知识图谱检索场景可复用交替优化范式，无需人工标注查询-检索规则对，用检索反馈自动学习规则路由策略，可降低70%以上的规则标注成本

  - 规则约束检索器的设计可直接迁移到知识库RAG系统：先通过规则限定图遍历路径缩小候选集，再结合BM25路径特征+规则嵌入做相关性排序，兼顾召回率和检索效率

  - 生成式路由Agent可采用「多域预训练+目标域微调」范式，跨业务场景迁移路由知识，冷启动阶段可比零-shot LLM路由提升10%以上的检索H@1

  - 路由策略的分布统计可用于自动挖掘/剪枝业务规则：高复用率规则保留，连续3轮优化使用率低于1%的规则直接淘汰，降低规则维护成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有结构化知识检索方法要么无约束检索效率低、召回准确率差，要么依赖预定义查询-规则对监督，而人工标注规则对成本极高、泛化性差，无法适配电商、生物医药、科研等多领域知识库检索的灵活需求。
### 方法关键点
- CoRE框架将结构化检索拆分为规则路由Agent和规则约束检索器两个耦合模块，无需查询-规则对标注，仅用查询-证据对即可完成端到端训练
- 采用交替优化策略：固定路由Agent时，用对比学习训练每个规则对应的专用检索器；固定检索器时，用检索结果的Reciprocal Rank作为奖励，通过强化学习优化路由Agent的规则分配策略
- 支持三种路由实现：BERT编码+分类头、LLM编码+分类头、LLM生成式路由，其中生成式路由支持跨域知识迁移
### 关键结果
在STaRK-QA的三个数据集（AMAZON电商知识库、MAG科研文献库、PRIME生物医药库）上与14种基线（BM25、DPR、KAR、MoR等）对比，CoRE-BERT-C变体平均H@1达54.47%，比此前最优的MoR高出5.54个百分点；生成式路由跨域迁移可比零-shot Qwen路由提升3~17个百分点的H@1，采用多域预训练+目标域微调范式后性能可进一步提升8%以上。
### 核心结论
Agent与专用检索工具的协同自适应优化，是降低结构化检索标注依赖、提升跨域泛化性的核心路径
