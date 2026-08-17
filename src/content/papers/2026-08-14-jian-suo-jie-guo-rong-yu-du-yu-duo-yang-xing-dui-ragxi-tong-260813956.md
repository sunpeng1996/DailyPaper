---
title: How retriever redundancy and diversity impact RAG effectiveness
title_zh: 检索结果冗余度与多样性对RAG系统问答效果的影响研究
authors:
- Jonathan J Ross
- Bevan Koopman
- Anton van der Vegt
- Guido Zuccon
affiliations:
- The University of Queensland
- CSIRO
arxiv_id: '2608.13956'
url: https://arxiv.org/abs/2608.13956
pdf_url: https://arxiv.org/pdf/2608.13956
published: '2026-08-14'
collected: '2026-08-17'
category: RAG
direction: RAG系统检索端策略优化
tags:
- RAG
- Retrieval Diversity
- Redundancy
- Question Answering
- LLM Evaluation
one_liner: 通过无参数知识干扰的可控实验，明确RAG检索结果多样性的收益远高于冗余与改写
practical_value: '- 电商/客服类RAG召回不要为填充上下文窗口塞重复或改写的相似片段，纯冗余几乎无收益，还可能挤占有效内容位置

  - RAG召回/重排阶段增加跨来源（商品详情页、用户评价、官方公告、达人测评等）的多样性筛选，固定k值下答案准确率最高可提升20%+

  - RAG检索结果优先选择百科、官方公告类结构化高可信度体裁内容，相同信息密度下比社交媒体类内容准确率高20%以上'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG检索通常按单文档相关性排序，忽略检索结果整体的冗余、多样性特征对生成端的影响，过往研究结论矛盾，且未排除LLM参数知识的干扰，无法明确不同冗余/多样性策略的真实收益。

### 方法关键点
- 采用FictionalQA合成虚构数据集，确保问题答案不存在于LLM预训练语料，完全来自检索上下文，彻底排除参数知识干扰
- 控制变量设计三组对照：完全重复的相同文档、LLM改写后的相同内容文档、来自不同体裁的独立内容文档，所有文档均验证可独立推导正确答案
- 测试4个不同参数量的开源LLM（1B-12B），用LLM Judge评估答案正确性，对比不同检索结果数量k下的效果差异

### 关键实验结果
测试1900条覆盖5种体裁的虚构事实查询，以单条检索文档的回答准确率为基线：纯重复/改写文档相比基线无显著效果提升；跨体裁多样文档在k=5时相比纯重复策略准确率提升7.4%-24.7%，排除答案字符串匹配干扰后增益仍可达13.9%-23%；百科类内容准确率比社交媒体类高20%-30%。

### 核心结论
RAG检索端优化不要只看单文档相关性，优先选择跨来源的多样化高可信度内容，远比重复填充上下文收益更高。
