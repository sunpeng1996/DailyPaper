---
title: 'From Delivery to Stateful Exploration: Rethinking the Index for Agentic Search'
title_zh: 面向智能体搜索的索引原生交互框架INDEXACT
authors:
- Deogyong Kim
- Sunghwan Kim
- Sangam Lee
- Wonjae Lee
- Dongha Lee
affiliations:
- Yonsei University
arxiv_id: '2610.07960'
url: https://arxiv.org/abs/2610.07960
pdf_url: https://arxiv.org/pdf/2610.07960
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: 智能体搜索 · 索引原生交互优化
tags:
- Agentic Search
- Retrieval Interface
- Inverted Index
- Context Optimization
- Multi-hop QA
one_liner: 提出索引原生交互接口INDEXACT，解耦智能体搜索的候选集精炼与文本读取流程
practical_value: '- 电商导购/搜索Agent可复用候选集状态下沉设计：将布尔筛选、集合运算、短语匹配等候选过滤逻辑下沉到倒排索引侧，仅返回统计信息而非完整文本，可降低50%以上LLM上下文占用，减少API调用成本

  - 多轮RAG系统可借鉴统计反馈机制：给智能体暴露候选集匹配数量、条件命中占比等统计信号，替代传统直接返回TopK结果的模式，提升检索路径决策合理性，降低无效检索占比

  - 大规模商品/内容库探索类任务可参考扩容优化思路：索引侧执行所有过滤运算，避免反复拉取全量候选文本，语料扩容8倍时性能与成本几乎无波动，适配千万级以上语料场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有智能体搜索接口每次检索直接返回匹配文本，大量非证据类无效内容挤占LLM上下文空间，拉高推理成本；终端式直接语料交互方案随语料规模扩容，上下文占用与调用成本指数级上升，无法适配百万级以上大规模业务语料场景。

### 方法关键点
- 候选集精炼逻辑完全下沉至倒排索引侧：支持布尔过滤、短语/近邻匹配、集合交并差运算、自定义加权排序等操作，执行后仅返回可复用的候选集引用、匹配数量等统计信息，不返回任何文本内容
- 候选集状态持久化可复用：所有历史生成的候选集状态保留在索引侧，智能体可随时回溯任意历史状态进行二次筛选、组合，无需重复执行全量检索
- 文本读取完全由智能体主动触发：仅当智能体调用READ接口时，才返回指定候选集的指定范围文本片段，从机制上避免非必要文本进入上下文

### 关键实验
覆盖智能体搜索、多跳QA两类任务共5个基准数据集，对比7个主流基线方案：在BrowseComp-Plus数据集上准确率达73.5%，较最强基线RARG提升4.1个百分点，证据覆盖率提升3.5个百分点，平均上下文仅13960token，为RARG的50%；4个多跳QA数据集上准确率全部登顶；语料规模从100K扩容至800K时，准确率稳定维持在70%以上，上下文占用与API调用成本几乎无波动。

### 核心结论
智能体搜索的性能提升核心不是单纯缩短上下文长度或减少检索步数，而是给智能体提供充分的候选集统计反馈 + 可复用的检索状态，让其自主决定何时读取文本。
