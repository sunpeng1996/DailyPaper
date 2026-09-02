---
title: Improving Information Extraction with Learned Queries
title_zh: 基于可学习查询的信息抽取性能优化方法
authors:
- Omar Sharif
- Soroush Vosoughi
- Nikhil Singh
affiliations:
- Dartmouth College, Department of Computer Science
arxiv_id: '2608.31058'
url: https://arxiv.org/abs/2608.31058
pdf_url: https://arxiv.org/pdf/2608.31058
published: '2026-08-31'
collected: '2026-09-02'
category: LLM
direction: LLM信息抽取 · 可学习查询优化
tags:
- Information Extraction
- Prompt Optimization
- Query Generation
- Feedback Tuning
- LLM
one_liner: LoQ与FeedQ可学习查询框架可仅通过优化提问让信息抽取F1提升18.6点，效果超过模型扩容
practical_value: '- 电商/广告场景做商品评论、详情页、客服对话的信息抽取时，可优先优化prompt查询而非直接扩容大模型，用更低成本获得效果提升

  - 可复用FeedQ的反馈驱动迭代逻辑，针对业务特定抽取任务自动迭代优化prompt集合，替代人工撰写调试prompt的低效流程

  - 用优化后的高质量query微调7B/4B级小参数LLM，可使其效果超过更大参数的未调优模型，适配低延迟、低成本的线上部署需求'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
过往信息抽取性能不达预期时，业界通常优先优化抽取模型本身（如参数扩容、增强推理能力），普遍忽略引导信息抽取的查询设计的核心价值。
### 方法关键点
- List of Questions (LoQ) 可生成单文档专属多维度查询集合，覆盖不同抽取目标
- FeedQ 作为反馈驱动优化方法，基于实际抽取结果迭代调整查询，提升匹配度
- 优化后的高质量查询可用于训练轻量查询生成模型，降低落地门槛
### 关键结果
- 跨4个临床基准数据集、5款不同LLM测试，仅优化查询设计即可让信息抽取F1提升18.6点，效果优于直接使用更大参数的抽取模型
- 用优化后的查询微调4B参数模型，效果匹配甚至超过专家编写的基线prompt，大幅优于未调优的更大参数模型
- 开源包含12820条优化后查询的数据集，支撑相关研究落地
