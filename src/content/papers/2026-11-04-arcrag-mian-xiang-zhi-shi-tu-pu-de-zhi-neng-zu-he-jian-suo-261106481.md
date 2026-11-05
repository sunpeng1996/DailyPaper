---
title: 'ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs'
title_zh: ArcRAG：面向知识图谱的智能组合检索框架
authors:
- Jyotin Goel
- Abhinav Arun
- Tejas Prakash Agarwal
- Bhaskarjit Sarmah
- Stefano Pasquali
affiliations:
- Domyn
arxiv_id: '2611.06481'
url: https://arxiv.org/abs/2611.06481
pdf_url: https://arxiv.org/pdf/2611.06481
published: '2026-11-04'
collected: '2026-11-05'
category: RAG
direction: GraphRAG · 跨结构KG适配
tags:
- GraphRAG
- Knowledge Graph
- Agentic RAG
- Cypher
- Cross-Construction Portability
one_liner: 提出跨图谱构建范式的无预配置Agentic GraphRAG，无需微调即可适配不同结构KG
practical_value: '- 电商多来源KG接入场景可借鉴查询本地接口诱导思路，无需预先固化schema映射规则，查询时动态探索实体周边关系，大幅降低异构KG适配成本

  - 多跳检索工程可复用探索-规划-执行-修复的迭代架构，模块化Cypher生成与修复逻辑，适配电商多约束查询（如「适合3岁儿童的纯棉外套品牌」）需求

  - 业务侧同时存在结构化KG和开放抽取无类型KG时，可复用同一套检索配置，无需分别开发适配逻辑，降低维护成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有GraphRAG检索策略与自身图谱构建流程强绑定，一旦KG构建方式变化（如从schema引导的结构化抽取切换为开放信息抽取），检索策略即失效，需重新适配schema、关系名甚至微调，跨构建范式可移植性差，无法满足业务侧多来源KG统一检索的需求。

### 方法关键点
- 推理时动态诱导查询本地图谱接口：围绕查询提及的实体，实时探索周边节点标签、关系描述、属性键，自动发现别名与同义关系，无需离线实体/关系归一化
- 采用探索-规划-执行的Agent流水线：Explorer先探索实体周边可用路径，Planner生成多跳遍历子计划，Generator将计划编译为Cypher查询执行，结果不满足要求时自动修复查询或重新探索
- 完全无需图谱专属prompt、关系映射规则或微调，仅通过内省读取KG存储结构即可适配

### 关键结果
在MuSiQue、HotpotQA、TriviaQA三个QA数据集上分别构建schema引导的结构化KG和开放信息抽取无类型KG两类图谱，对比实验显示：
- 对比直接生成Cypher的baseline，ArcRAG在5重试5 passes配置下EM提升38~82个百分点
- 同一套配置跨两类KG运行，在开放无类型KG上取得38.0（MuSiQue EM）、65.5（HotpotQA EM）、71.6（TriviaQA F1）的效果，超过HippoRAG，接近HippoRAG 2水平
- 在结构化KG上效果更优，达到44.0（MuSiQue EM）、74.5（HotpotQA EM）、87.9（TriviaQA F1），超过所有公开的GraphRAG系统结果

最值得记住的结论：GraphRAG检索无需与图谱构建强绑定，通过查询时动态诱导本地接口，同一套检索策略可适配不同构建方式的知识图谱。
