---
title: 'Twists and Turns: A Graph-Based Benchmark and Framework for Long-Term Memory
  in Exploration Tasks'
title_zh: 面向探索任务长时记忆的图基准数据集与图引导记忆框架
authors:
- Chongyuan Dai
- Yaling Shen
- Zirui Song
- Junfeng Liao
- Jinpeng Hu
- Xiuying Chen
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Monash University
- Hefei University of Technology
arxiv_id: '2611.06414'
url: https://arxiv.org/abs/2611.06414
pdf_url: https://arxiv.org/pdf/2611.06414
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent长时记忆 · 图结构存储与检索
tags:
- Long-term Memory
- Graph Memory
- LLM Agent
- Benchmark
- RAG
one_liner: 提出面向长期探索任务的图基准LExMem与图记忆框架LExGraph，性能优于现有RAG与记忆系统
practical_value: '- 电商/广告Agent的长时用户交互记忆系统可复用双类型边设计：用层级边跟踪用户需求迭代路径，用跨分支边关联历史相似需求/反馈，提升分散用户行为/反馈信息的召回准确率

  - RAG系统优化可借鉴「语义+ lexical匹配的RRF融合排序 + 邻接节点扩展检索」组合，在多轮交互query、长尾商品检索场景下能减少关联证据遗漏，提升召回全面性

  - 针对需跟踪迭代过程的场景（如大促活动策划Agent、定制化推荐需求跟踪），可直接复用LExGraph的增量建图方法，无需预先定义图谱Schema，即可从交互流自动构建结构化记忆'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长时记忆基准与框架多聚焦孤立事实召回，忽略了科研、软件开发、多轮用户需求迭代这类探索任务中信息的关联依赖与动态迭代特性，无法评估模型对分散、存在分支/修订/回溯关系的探索过程信息的推理能力，而基于语义相似性、聚类的传统记忆组织方式也难以捕捉探索过程中的复杂依赖。

### 方法关键点
- 构建LExMem基准：用有向图建模探索步骤与依赖，通过进化机制模拟非单调探索过程，实例化科研、软件开发2类共224个平均88K token的多轮对话，生成2018个分3类（密集子图、稀疏子图、同类型节点集）的QA实例，覆盖6类记忆推理能力
- 提出LExGraph记忆框架：无需预定义图谱Schema，增量将对话切分为主题一致的记忆节点，每个节点存储「内容摘要+关键事实」键值对；自动构建两类边：层级边跟踪对话演进路径，跨分支边关联不同探索分支的相似节点；检索阶段用RRF融合语义匹配与BM25排序，召回核心节点后扩展邻接节点做证据聚合

### 关键实验结果
在LExMem基准上，LExGraph仅需1.2~1.3倍vanilla方法的token开销，相比最强基线LightRAG，Qwen-3.8 27B backbone下整体F1提升4.3%、ACC提升2.25%，GPT-6 Luna backbone下整体F1提升3.9%、ACC提升0.54%，尤其在分散信息聚合、多跳关系追踪场景优势显著；在外部BEAM基准上也取得最高整体得分0.472，超现有各类RAG与记忆框架。

**最值得记住的一句话**：对于存在分支、迭代、回溯的长周期任务，基于图结构组织记忆、结合邻接扩展的检索方式，远优于纯语义相似性的记忆召回方案。
