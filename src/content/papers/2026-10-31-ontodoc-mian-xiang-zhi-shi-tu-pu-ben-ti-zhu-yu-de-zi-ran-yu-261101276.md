---
title: 'OntoDoc: Automatically Generating Ontology Resource Descriptions'
title_zh: OntoDoc：面向知识图谱本体术语的自然语言描述自动生成框架
authors:
- Juan Guajardo Gutierrez
- Mike Tran
- Nasim Shirvani Mahdavi
- Chengkai Li
affiliations:
- University of Texas at Arlington
arxiv_id: '2611.01276'
url: https://arxiv.org/abs/2611.01276
pdf_url: https://arxiv.org/pdf/2611.01276
published: '2026-10-31'
collected: '2026-11-03'
category: Agent
direction: 多Agent协作 · 知识图谱本体文档生成
tags:
- MultiAgent
- KnowledgeGraph
- Ontology
- LLM
- TextGeneration
one_liner: 提出四阶段多Agent框架，自动生成知识图谱本体术语的高准确性高完整性自然语言描述
practical_value: '- 电商场景下可复用该框架生成商品类目、属性、SPU/OPU的官方释义，解决内部知识图谱术语无统一解释、人工标注成本高的问题，降低上下游业务对齐成本

  - 做结构化数据到文本生成任务（如商品卖点生成、属性文案生成）时，可新增「基于检索事实生成结构化可溯源中间假设」的步骤，大幅降低LLM hallucination，提升事实准确性

  - 多Agent解耦设计可直接复用：各Agent仅读写共享KV状态的指定Key，不直接调用其他Agent，可单独替换模块（如将公开网页检索替换为内部业务知识库检索），适配业务快速迭代需求

  - 垂直领域生成任务的评估可借鉴「LLM自动评分+小范围专家标注校准」的范式，在保证评估效率的同时对齐专业领域的判断标准'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
知识图谱是电商、科研、政务等领域的核心结构化知识载体，但大量本体术语（类目、属性、关系IRI）缺少自然语言释义，手工标注成本高、扩展性差。传统规则/模板式本体生成方法仅能处理显式schema公理，无法覆盖实例层面隐含语义，朴素LLM直接生成则存在信息不全、幻觉率高的问题。

### 方法关键点
- 四阶段多Agent流水线：数据库上下文Agent与网页上下文Agent并行执行，结果汇总后输入假设生成Agent，最后由描述生成Agent输出最终文本，各Agent通过共享KV状态解耦，可单独迭代替换
- 数据库上下文Agent：自适应SPARQL探索，根据IRI类型（类/属性/实例）自动规划查询，优先采集实例层面语义信息而非纯schema公理，控制token预算避免冗余
- 网页上下文Agent：过滤通用停用词后，根据术语领域特性选择维基百科/专业技术搜索引擎检索背景知识，经重排后保留高相关结果
- 假设生成Agent：参考CoT思路，先基于双路上下文生成带溯源依据的结构化假设，明确图谱上下文为权威信息，网页内容仅作补充，降低幻觉

### 关键实验结果
在生物医学、农业、开放领域3个知识图谱共151个术语上测试，对比朴素单跳检索+LLM基线、模板式本体生成工具：完整性平均提升12%，相对模板式基线在5分制下最高提升2.8分，专业领域下准确率持平甚至超过朴素基线；11名标注者的人工评估显示各领域评分均在3.65分/5分以上，生物医学领域准确率达4.51分，LLM自动评分和人工评估趋势高度一致。

### 核心结论
结构化知识到文本的生成任务中，增加「基于检索事实生成结构化中间假设」的步骤，能在几乎不损失生成质量的前提下大幅提升事实准确性和完整性，尤其适合垂直专业领域。
