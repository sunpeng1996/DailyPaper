---
title: Where A Small Language Model Helps in Invoice Categorisation, Understood Through
  Embedding Geometry
title_zh: 嵌入几何视角下小语言模型的发票分类效果解析
authors:
- Emma Ceccherini
- Daniel Lawson
- Anjulika Salhan
affiliations:
- University of Bristol, U.K.
- System Holdings Limited
arxiv_id: '2608.18033'
url: https://arxiv.org/abs/2608.18033
pdf_url: https://arxiv.org/pdf/2608.18033
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: 小语言模型 · 垂直领域文本分类
tags:
- SLM
- SBERT
- DeBERTa
- Embedding Geometry
- Vertical NLP
- Text Classification
one_liner: 通过嵌入几何分析验证小规模语言模型可低成本高精度完成垂直领域发票分类任务
practical_value: '- 垂直场景低资源分类/匹配任务可优先尝试SBERT等轻量SLM单卡微调，成本远低于大模型零样本调用，同时满足数据安全合规要求

  - 垂直领域NLP任务落地前可先分析预训练嵌入空间的聚类特性，若天然存在和业务标签强相关的局部聚类，微调样本量要求会大幅降低

  - 垂直场景数据预处理无需盲目对齐人类阅读习惯增加结构化格式，可先测试纯文本输入的SLM效果，避免不必要的预处理开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
发票分类是财务合规核心任务，依赖专业会计判断，现有大模型方案存在成本高、数据安全风险大的问题，亟需低成本高可控的本地化落地方案。

### 方法关键点
分析金融语料下SBERT、DeBERTa两类SLM的预训练嵌入几何特性，验证嵌入空间结构与分类性能的关联，对比零样本LLM、供应商身份基准等方案的表现。

### 关键结果数字
单GPU微调的SBERT发票分类准确率达0.96，优于零样本LLM与供应商基准；仅需100条客户专属标注样本即可达到0.9的F1值；金融语料句子嵌入空间全局各向异性但局部各向同性，聚类与供应商身份强相关；对人类友好的结构化输入无法提升SLM分类性能。
