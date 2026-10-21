---
title: 'GARRET: Generative Feedback for Region Retrieval in Visual Documents'
title_zh: GARRET：基于生成反馈的视觉文档区域检索框架
authors:
- Weijian Jian
- Siyang Chen
- Yuguang Yang
- Yajun Zhang
- Chunyu Xie
- Dawei Leng
- Yuhui Yin
affiliations:
- 360 AI Research
- SAIS, UCAS
- CASIA
- SEIE, BUAA
arxiv_id: '2610.27829'
url: https://arxiv.org/abs/2610.27829
pdf_url: https://arxiv.org/pdf/2610.27829
published: '2026-10-20'
collected: '2026-10-21'
category: RAG
direction: 多模态RAG · 细粒度区域检索
tags:
- Multimodal RAG
- Region Retrieval
- Generative Feedback
- Weak Supervision
- Visual Document
one_liner: 无需查询-区域标注，基于生成反馈训练的高存储效率视觉文档区域检索SOTA框架
practical_value: '- 弱监督训练范式迁移：电商多模态商品/广告检索场景中，无需标注用户query到商品属性块的对应关系，可复用「(query, 物料页,
  成交/回答)三元组+下游生成NTP loss反向监督检索模块」的训练范式，大幅降低细粒度检索的标注成本

  - 多粒度表示工程优化：可借鉴「全局上下文注入+区域独立编码+丢弃基础页冗余向量」的视觉late chunking方案，同时支持页级和块级检索，可降低40%+的索引存储开销，适配大规模物料库的离线索引需求

  - 多模态RAG落地优化：电商智能客服、商品导购等多模态RAG系统，可替换原有页级检索为区域检索，仅用原60%的上下文面积即可提升2pp+的回答准确率，同时降低推理成本、减少幻觉'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多模态RAG对视觉富文档的检索大多返回整页，冗余度高、推高推理成本还容易引发幻觉；训练细粒度区域检索模型需要昂贵的query-区域人工标注，大模型生成伪标签的方案噪声大、计算成本高，现有动态区域生成方案无法支持高效离线索引，是多模态RAG落地的核心瓶颈。

### 方法关键点
- 上下文保留的多粒度检索架构（视觉late chunking）：区域编码时注入整页全局上下文，同时通过注意力掩码隔离不同区域避免互相干扰；索引时仅保留区域嵌入和少量页摘要向量，丢弃整页冗余嵌入，大幅压缩索引体积
- 无标注训练范式：仅用(page, question, answer)三元组训练，用辅助VLM的NTP loss作为生成反馈，通过可微软路由把梯度回传给检索模块，无需任何query-区域标注
- 推理时直接丢弃辅助VLM，仅用训练好的检索器即可同时支持页级和区域级检索，区域打分融合区域本身相关性和父页相关性，解决相似区域的消歧义问题

### 关键实验
在自建的VIDORE-V3-REGION基准（覆盖8个领域共200682个候选区域）上，对比ColQwen2.5、RegionRAG等SOTA基线，区域检索nDCG@10达0.4126，超出最强基线2.94个点；页级检索性能与ColQwen2.5相当，索引向量数减少47.8%；下游RAG任务仅用原66%的上下文面积，回答准确率比页级检索方案高2.12个点。

### 核心结论
没有细粒度标注的检索任务，用下游生成任务的端到端反馈做弱监督，往往比用大模型打伪标签的效果更好、落地成本更低
