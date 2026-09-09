---
title: 'REDSI: Addressing the Reproducibility and Evaluation Consistency of Differentiable
  Search Indexing for Document Retrieval'
title_zh: REDSI：解决可微搜索索引的复现性与评估一致性问题
authors:
- Vivien Nicolas
- Hicham Randrianarivo
- Pascale Sébillot
- Caio Corro
affiliations:
- Artefact Research Center
- INSA Rennes, IRISA, CNRS, Université de Rennes
- MICS, CentraleSupélec, Université Paris-Saclay
arxiv_id: '2609.08860'
url: https://arxiv.org/abs/2609.08860
pdf_url: https://arxiv.org/pdf/2609.08860
published: '2026-09-08'
collected: '2026-09-09'
category: GenRec
direction: 生成式检索 · DSI可复现框架
tags:
- DSI
- Generative Retrieval
- Semantic ID
- Reproducibility
- NQ320K
one_liner: 开源支持全三类文档ID的DSI实现与可配置NQ320K构建管线 验证原子ID的参数效率优势
practical_value: '- 电商站内搜索/商品生成式检索场景优先选择atomic ID方案，相同效果下参数量可降低60%以上，训练速度提升10倍，推理仅需1步解码，工程成本更低

  - 构建生成式检索训练数据集时，优先用全局唯一稳定ID（如商品SPU ID）作为去重主键，避免用标题/URL等易变字段导致数据冲突，提升模型效果一致性

  - DSI训练时索引任务与检索任务的采样比例不要盲目沿用原论文32:1，实测自然比例1:2.8效果最优，可直接复用减少调参成本

  - 多token ID解码无需复杂的约束解码，增加简单的后过滤步骤移除无效ID即可，效果几乎无损失，工程实现更简单'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
DSI是生成式检索领域的事实基线，但长期存在复现难题：无公开实现支持原子/朴素/语义三类文档ID，不同工作的NQ320K数据集预处理规则不透明、数据集差异极大，不同复现的效果无法公平对比，阻碍生成式检索的落地迭代。
### 方法关键点
- 开源REDSI统一框架：支持三类ID的训练、评估全流程，代码可直接复用
- 开源可配置NQ320K构建管线：拆分文档去重（TEXT4K/标题/URL/PAGEID共4种规则）和文本序列化（NCINORM/HTMLNORM共2种规则）模块，可复现已有所有NQ320K变体
- 提出HTMLNORM序列化方案：大幅降低文本中的UNK token比例，从18.7%降至1.6%
### 关键实验
在NQ320K数据集上对比三类ID在T5不同缩容版本（16M/60M/220M）的表现：
1. 原子ID在所有模型规模下效果最优，44M参数量的原子ID模型MRR@10达62.2，超过220M参数量的朴素ID（60.1）和语义ID（59.7）模型
2. 原子ID训练速度提升10倍以上，仅需6.8小时达到95%峰值效果，另外两类ID需要74.5小时以上
3. 多token ID的约束解码相比简单后过滤无明显收益，可省略
### 核心结论
静态百万级以内语料的生成式检索场景，优先选择原子ID方案，兼顾效果、效率和工程实现成本
