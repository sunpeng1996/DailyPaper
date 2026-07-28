---
title: Cross-Attention Calibrated Deduplication for Retrieval-Augmented Generation
  System
title_zh: 面向RAG系统的交叉注意力校准文档块去重方法
authors:
- Phuong Le Huy
- Nam H. Nguyen
- Quan V. Dang
affiliations:
- Full Stack Data Science
- University College London
arxiv_id: '2607.24332'
url: https://arxiv.org/abs/2607.24332
pdf_url: https://arxiv.org/pdf/2607.24332
published: '2026-07-27'
collected: '2026-07-28'
category: RAG
direction: RAG索引优化 · 文档块去重
tags:
- RAG
- Chunk Deduplication
- Cross-Encoder
- Attention Entropy
- Vector Database
one_liner: 提出结合交叉编码器、注意力熵新信息得分、多候选投票的RAG块去重方案，效率与去重率优于现有语义去重方法
practical_value: '- 可直接复用CACD的三级判断逻辑替换现有RAG系统的cosine相似度去重，尤其适合商品详情、客服知识库等重复内容多的场景，可降低向量库存储、提升检索速度

  - 基于交叉编码器注意力熵的新信息得分（NIS）计算方法可迁移到检索后上下文去重场景，避免LLM重复摄入相同信息，降低冗余prompt token消耗

  - 多候选多数投票的决策逻辑可复用在去重、过滤类任务中，降低单样本误判风险，适合电商SPU聚合、商品属性对齐等对误删敏感的场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG系统各类分块策略普遍生成冗余chunk，既膨胀向量库体积、拖慢检索速度，也可能因重复上下文降低LLM生成质量；现有cosine相似度去重依赖单池化向量，易丢失细粒度token信息，无法区分同主题非重复块和真重复块，误删有效内容风险高。
### 方法关键点
- 三阶段流水线：先检索内存中已存块的TopK近邻，再用交叉编码器联合编码新块与候选块对，最后通过多数投票决策是否保留
- 提出基于交叉编码器注意力熵的新信息得分（NIS），量化候选块无法解释的新块内容占比，避免池化向量的信息损失
- 设计三类防护规则：排除父子块的刻意重叠、移除上下文头避免评分干扰、长块优先保留降低误删风险
- 决策逻辑融合交叉编码器重复概率、NIS得分和多候选投票，单候选误判不会影响最终结果
### 关键实验结果
在SQuAD 1.1验证集上，对比5种基线去重方法、9种分块策略共18种配置：CACD平均去重率9.75%为所有方法最高；单配置平均处理耗时51.0s，比NERExact快27%，比cosine相似度去重快7倍；索引存储小于所有基线，精度、IoU均高于cosine相似度和NERExact去重。
### 核心结论
针对RAG分块去重任务，结合交叉编码器细粒度信号和多候选投票的方案，能在几乎不损失检索质量的前提下，实现比传统语义去重高得多的效率和去重率
