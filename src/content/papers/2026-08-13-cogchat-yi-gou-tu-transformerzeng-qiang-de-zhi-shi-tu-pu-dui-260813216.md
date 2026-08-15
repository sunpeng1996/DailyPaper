---
title: 'CogChat: Knowledge Graph-Augmented Conversational AI with Heterogeneous Graph
  Transformer for Cognitive Grounding in Design Generation'
title_zh: CogChat：异构图Transformer增强的知识图谱对话AI 实现设计生成认知接地
authors:
- Jiin Choi
- Kyung Hoon Hyun
affiliations:
- Hanyang University
- Design AI Lab
- Human-Centered AI Design Institute
arxiv_id: '2608.13216'
url: https://arxiv.org/abs/2608.13216
pdf_url: https://arxiv.org/pdf/2608.13216
published: '2026-08-13'
collected: '2026-08-15'
category: Agent
direction: 对话Agent · 知识图谱增强多轮交互
tags:
- Knowledge Graph
- Heterogeneous Graph Transformer
- Conversational Agent
- Context Management
- LLM Grounding
one_liner: 基于用户专属异质知识图谱与HGT节点选择，优化LLM多轮对话的上下文保留与交互深度
practical_value: '- 电商导购/咨询Agent可复用「用户专属动态异质KG」架构，存储用户历史交互的实体（如浏览商品、偏好属性）与关联关系，解决多轮对话上下文衰减问题

  - 多轮召回/对话生成场景可采用HGT做结构化知识的节点选择，相比直接拼接全量KG或仅用近邻上下文，能降低噪声、提升相关知识召回准确率

  - 个性化推荐的用户建模可参考该方案，将用户行为的实体关系结构化存储，替代纯序列式的行为编码，提升长周期偏好识别准确率'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有LLM对话系统仅基于时序近邻信息维护上下文，没有建模用户知识组织逻辑，多轮交互中关系型上下文易衰减，存在同词歧义、对话循环无法深化等问题，难以满足设计等对上下文深度要求高的场景需求。

### 方法关键点
1. 实时从用户输入中提取带类型的实体与关系，构建用户专属动态异质知识图谱存储交互语义；
2. 采用Heterogeneous Graph Transformer（HGT）筛选结构相关的图谱节点，作为响应生成的grounding信息，同时生成匹配用户意图与探索性的引导问题；
3. 规避朴素KG增强直接拼接全量知识引入的噪声问题。

### 关键结果
技术评估显示HGT实体选择效果显著优于无接地LLM和朴素KG增强方案；9名专业设计师的内组实验表明，该方案可提升上下文保留率、个性化意图识别准确率与对话深度，同时降低用户认知负载。
