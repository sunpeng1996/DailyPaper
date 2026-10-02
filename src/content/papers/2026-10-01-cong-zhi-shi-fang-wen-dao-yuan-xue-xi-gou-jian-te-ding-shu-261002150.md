---
title: 'From Knowledge Access to Source Learning: Developing Source-Specific Competence'
title_zh: 从知识访问到源学习：构建特定数据源的可复用能力
authors:
- Lucheng Fu
- Kejing Xia
- Yiyang Wang
- Yiqiao Jin
- Jinjin He
- Xiyuan Yang
- Haoxin Liu
- Ye Yu
- Haibo Jin
- Yijia Xiao
affiliations:
- Georgia Institute of Technology
- University of Illinois at Urbana-Champaign
- University of California, Los Angeles
arxiv_id: '2610.02150'
url: https://arxiv.org/abs/2610.02150
pdf_url: https://arxiv.org/pdf/2610.02150
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: Agent 源知识学习与能力复用
tags:
- LLM Agent
- RAG
- Source Learning
- Agent Memory
- Knowledge Reuse
one_liner: 提出SourceLearn框架，通过双机制构建持久化源模型，大幅提升同源任务性能
practical_value: '- 针对电商商品库、规则库、API文档等固定权威数据源，可构建实体为中心的源模型，沉淀规则、依赖、适用条件等跨任务复用的结构化知识，减少重复检索成本

  - 双学习机制可直接复用：自主学习阶段主动排查源模型的知识缺口补全，任务引导阶段用业务bad case定位模型缺陷，再从权威数据源重构更新，避免记忆污染业务错误

  - 可采用源模型+RAG的互补推理架构：同时调用激活的源模型和实时检索结果，既提升检索不全时的鲁棒性，又保留权威数据源的事实准确性，适合电商合规类、规则类问答/推荐场景

  - 源模型不需要全量压缩数据源，仅保留跨任务复用的结构化知识，低阶可检索事实留在原数据源，平衡内存占用和效果，适合大商品库场景落地'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有RAG方法仅解决单次任务的知识访问问题，Agent记忆系统仅保留交互经验，当Agent频繁使用同一固定权威数据源（如API文档、商品库、规则集）时，重复检索不会积累对数据源的结构化理解，每次都要重新组织知识逻辑，效率和效果都存在瓶颈。

### 方法关键点
- 定义「源学习」范式，目标是构建可复用的特定源能力，用持久化可更新的源模型沉淀对数据源的结构化理解，包括知识结构、解释逻辑、适用条件、实体关联等，推理时和实时RAG检索结果互补，原数据源仍作为事实权威
- 双学习机制迭代源模型：① 自主源学习：基于当前模型主动排查知识缺口，针对性重读数据源补全碎片化知识、关联跨实体依赖；② 任务引导源学习：用下游任务的失败case定位局部表示缺陷，同时聚合多任务的共性需求优化知识组织粒度，所有更新都从权威数据源重构，不直接存储任务答案或经验
- 源模型激活机制：当模型超过上下文窗口时，按任务相关性激活对应区域的结构化知识，和实时检索结果一起输入LLM

### 关键实验
在5个基准（文档QA、代码QA、工具使用、交互环境）+3种LLM后端上测试，对比Hybrid RAG、RAPTOR、HippoRAG 2、AWM等基线，15个测试设置中13个取得SOTA，比Hybrid RAG最高提升22.6个点，平均提升4.9~14.3个点；源模型对任务所需知识的覆盖率从初始23.2%提升到40%，检索不全时效果下降远慢于纯RAG方法。

### 核心结论
针对高频复用的固定权威数据源，不要只做单次访问的RAG，要沉淀结构化的可复用源能力，学习信号只决定补什么，所有持久化知识必须从权威源重构，避免记忆污染。
