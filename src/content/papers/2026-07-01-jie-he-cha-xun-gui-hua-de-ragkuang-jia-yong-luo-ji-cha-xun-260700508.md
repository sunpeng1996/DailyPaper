---
title: 'When RAG Meets Query Planning: Logical Query Trees for Resolving Exploratory
  Reasoning Problems'
title_zh: 结合查询规划的RAG框架：用逻辑查询树解决探索性推理问题
authors:
- Ganlin Xu
- Linghao Zhang
- Zhitao Yin
- Hongda Xi
- Chen Yang
- Jiaqing Liang
- Weijia Lu
- Sihang Jiang
- Yanghua Xiao
- Deqing Yang
affiliations:
- 复旦大学
- 联合汽车电子有限公司
arxiv_id: '2607.00508'
url: https://arxiv.org/abs/2607.00508
pdf_url: https://arxiv.org/pdf/2607.00508
published: '2026-07-01'
collected: '2026-07-02'
category: RAG
direction: RAG · 复杂查询规划优化
tags:
- RAG
- Query Planning
- Logical Query Tree
- Exploratory Reasoning
- Dynamic Programming
one_liner: 借鉴数据库查询规划思路，提出PlanRAG框架，通过逻辑查询树优化高不确定性复杂查询的RAG效果
practical_value: '- 电商模糊导购query、Agent探索式信息查询的拆解可复用本文的原子查询拆分+语义关系分类逻辑，减少无关检索召回，降低噪声

  - RAG链路的query优化环节可复用多维度成本模型，引入结构属性、语义相似度等维度做query改写/排序的打分指标，提升检索与生成的对齐度

  - 逻辑查询树的并行执行策略可直接迁移到RAG多子任务调度场景，通过多线程处理独立子查询，降低链路延迟，适配电商、广告等低延时业务需求

  - 原子查询对的预分类剪枝技巧能大幅减少LLM调用次数和token消耗，在保障效果的同时降低RAG系统推理成本，适合大规模上线场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG在处理高不确定性、实体关系模糊的探索性推理问题（ERP）时，存在检索噪声高、错误沿推理链累积、缺乏端到端全局规划的痛点，传统迭代式/图式RAG仅适配有明确推理路径的多跳查询，无法解决这类无清晰结构的复杂查询问题。

### 方法关键点
- 借鉴数据库查询规划范式，框架分为查询解析、逻辑优化、物理执行三个阶段，全程无需额外训练；
- 查询解析阶段将复杂ERP拆分为对应单一关系三元组的原子查询，提前预分类所有原子查询对的语义关系（父子/兄弟/无关），无关对直接剪枝，大幅减少后续LLM调用量；
- 逻辑优化阶段基于带环检测、上下文感知合并的动态规划算法，采用包含树大小、结构密度、深度、平衡度、语义相似度5个维度的成本模型，生成最优逻辑查询树（LQT）；
- 物理执行阶段采用自底向上的并行执行策略，独立节点多线程调度，子节点结果向上聚合后改写父节点查询再执行检索生成，直到根节点输出最终结果。

### 关键结果
在自建WikiWeb-ERP数据集（3536条探索性查询、53682篇文档）上，相比SOTA的迭代式/图式RAG，PlanRAG的Acc最高提升7.09个百分点，Acc†最高提升4.54个百分点；开启关系预处理后LQT构建速度提升9.8倍，token成本降低63%，并行执行让推理速度提升2.56倍，效果兼容不同基座LLM和检索器，在通用多跳QA数据集上也取得了有竞争力的表现。

### 核心结论
借鉴数据库查询规划的结构化思路做RAG的全局查询优化，是解决复杂模糊查询问题的高性价比路径，无需额外训练即可同时提升效果和运行效率。
