---
title: 'KGVoyager: Knowledge Graph Agnostic Question Answering via Agentic Navigation'
title_zh: KGVoyager：无需预定义本体的知识图谱问答Agent架构
authors:
- Essam Wisam
- Chengkai Li
affiliations:
- University of Texas at Arlington
arxiv_id: '2609.01780'
url: https://arxiv.org/abs/2609.01780
pdf_url: https://arxiv.org/pdf/2609.01780
published: '2026-09-01'
collected: '2026-09-03'
category: Agent
direction: Agent 知识图谱问答优化
tags:
- KGQA
- LLM Agent
- SPARQL Generation
- Zero-shot
- Knowledge Graph
one_liner: 仅通过SPARQL端点访问，实现无预定义本体、无标注样本的KGQA能力
practical_value: '- 可复用「混合BM25+稠密向量RRF融合排序+自适应过滤」的检索设计，解决电商商品图谱的实体/属性对齐问题，降低对固定schema的依赖

  - Agent的「搜索-探索-执行」三阶段流程可直接迁移到商品自然语言查询场景，将用户查询自动生成SPARQL检索商品库，适配商品属性频繁更新的场景

  - 轻量类级别索引替代全量实体索引的方案，可大幅降低领域图谱问答系统的部署成本，适配存量SPARQL端点'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有知识图谱问答（KGQA）系统高度依赖预定义本体与标注好的自然语言-SPARQL配对数据，但领域场景下普遍存在本体缺失、不透明、标注样本稀缺问题，过往SOTA方案依赖的全量实体索引部署可行性极低（QLever架构端点上成功率为0），无法适配仅能访问SPARQL端点的轻量化部署需求。
### 方法关键点
- 基于ReAct的think-act-observe迭代框架，设计三类完全KG无关的工具集：搜索工具（类/属性/实例搜索，采用BM25+稠密向量的RRF融合排序，自适应过滤低相关结果避免上下文 rot）、探索工具（属性使用探索/实体关系探索，直接从采样数据推断属性的domain/range，无需依赖本体标注）、执行工具（运行候选SPARQL获取结果反馈，迭代修正查询）。
- 仅需构建轻量级类级别索引，无需全量实体索引，大幅降低部署门槛。
### 关键实验
在4个领域KG基准数据集上对比SOTA方案GRASP，平均F1提升7.8个点，推理成本降低21.7%，运行耗时降低22.4%；ablation实验验证混合检索相比纯关键词检索F1提升2.7~6.1个点，同时显著减少Agent迭代次数。
### 核心结论
对于缺乏标注资源和完整schema的领域知识图谱，通过Agent动态探索图谱结构的方案，可实现性能更优、部署成本更低的问答能力。
