---
title: 'Graph Memory for LLM Agents: At What Cost? A Comparative Evaluation of Query,
  Ingest, and Update Performance Across Graph Database Engines'
title_zh: LLM Agent 图内存成本分析：多图数据库引擎查询/导入/更新性能对比
authors:
- Donald Nguyen
- Gurbinder Gill
- Hadi Ahmadi
- Christopher J. Rossbach
affiliations:
- Corvic AI Research
- University of Texas at Austin
arxiv_id: '2609.23315'
url: https://arxiv.org/abs/2609.23315
pdf_url: https://arxiv.org/pdf/2609.23315
published: '2026-09-20'
collected: '2026-09-22'
category: Agent
direction: LLM Agent 图记忆存储选型评测
tags:
- LLM Agent
- Graph Memory
- Graph Database
- Benchmark
- TCO
one_liner: 对8款图数据库引擎的三类核心性能做横向对比，给出面向不同 workload 的选型成本模型
practical_value: '- 搭建电商用户行为图谱、商品知识图谱作为Agent记忆组件时，不要只看单查询latency，要结合业务的查询量、数据刷新频率，用论文给出的TCO公式计算交叉点q*选型，日更类图谱优先选高ingest吞吐量的引擎

  - 如果业务的图查询以局部邻域遍历为主（比如商品关联路径、用户社交关系查询），优先选原生图引擎；如果以全图扫描、join、聚合为主（比如用户行为归因、全量标签统计），优先选列式OLAP引擎

  - 用SQL/PGQ等图查询语法时，要注意检查生成的执行计划，避免不必要的多表join带来的性能损耗，必要时手写SQL替代自动生成的图查询计划

  - 图存储更新频率低于10^5次/刷新周期的场景，ingest吞吐量是远大于查询latency的核心成本项，优先选型高吞吐写入的引擎'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent落地中普遍采用图数据库作为结构化长时记忆载体（如用户行为图谱、商品知识图谱），但现有图数据库benchmark普遍仅关注查询延迟，忽略导入、更新成本与业务workload特征的匹配，无法支撑生产环境的选型决策。
### 方法关键点
- 构造类生物医学知识图谱结构的合成测试集，覆盖1K、10K、1.02M节点三个量级，最大规模含5.34M节点+边行
- 设计20类覆盖生产常见图查询模式的workload，包括邻域查询、受限路径查询、集合交、反连接、分组聚合、top-k、时间过滤、全表扫描、关系join等
- 测度覆盖查询延迟几何均值、批量导入吞吐量、点更新延迟、批量更新吞吐量、结果正确率5类核心维度，构建总拥有成本（TCO）模型量化导入与查询的trade-off
### 关键结果
对比8款主流图引擎的核心性能：
1. 1.02M节点规模下，全查询集正确率100%的引擎中，Corvic AI查询延迟几何均值最低（2.19ms），批量导入吞吐量最高（4.3M行/s），比最低的LoraDB高860倍
2. 原生图引擎Ladybug在受限局部路径查询上比Corvic AI快48%，但全图join类查询慢7.1倍
3. 基于TCO模型，导入成本的交叉点约为10^5次查询/刷新周期，低于该量级时导入吞吐量是远大于查询延迟的核心成本项
### 核心结论
没有通用最优的图数据库，查询模式、查询量与数据刷新频率的组合才是选型的核心依据，单一的查询延迟benchmark会误导生产决策
