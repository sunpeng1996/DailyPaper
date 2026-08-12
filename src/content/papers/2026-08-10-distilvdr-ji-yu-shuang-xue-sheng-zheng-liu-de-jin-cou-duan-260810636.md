---
title: 'DistilVDR: A Compact End-to-End Visual Document Retriever via Dual-Student
  Distillation'
title_zh: DistilVDR：基于双学生蒸馏的紧凑端到端视觉文档检索器
authors:
- Zhuchenyang Liu
- Ziyi Wang
- Yao Zhang
- Yu Xiao
affiliations:
- Aalto University, Finland
- Independent Researcher, Netherlands
arxiv_id: '2608.10636'
url: https://arxiv.org/abs/2608.10636
pdf_url: https://arxiv.org/pdf/2608.10636
published: '2026-08-10'
collected: '2026-08-12'
category: RAG
direction: RAG 视觉文档检索蒸馏压缩
tags:
- VDR
- Knowledge Distillation
- Vision-Language
- Embedding Retrieval
- RAG
one_liner: 基于双学生双边蒸馏的524M端到端视觉文档检索器，性能达8B教师的86.9%，索引速度提升10倍
practical_value: '- 非对称编码器设计可复用在多模态商品/内容检索场景，资源向高开销的文档/商品侧倾斜，查询侧轻量化，兼顾效果和推理速度

  - 双边蒸馏+点wise余弦对齐训练范式无需负采样、人工标注，可直接用于大模型蒸馏小多模态检索模型，降低训练成本

  - 单向量检索压缩方案可落地多模态RAG索引层，百万级文档索引体积缩小15.6倍，索引速度提升10倍，适配线上高吞吐场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有SOTA视觉文档检索（VDR）模型多为数十亿参数，全库索引速度慢、部署成本高；此前压缩方案要么从头训练小多向量编码器，要么仅蒸馏查询侧，无法实现端到端紧凑单向量检索。
### 方法关键点
以冻结8B视觉语言大模型为教师，通过双边蒸馏+点wise余弦对齐损失训练524M端到端学生模型DistilVDR，无需相关性标注、负采样和对比项；采用非对称编码器设计，视觉能力集中在文档侧，查询侧仅70M参数；推出HiRes、Fast两个版本，仅文档编码器视觉块预算有差异。
### 关键结果
HiRes版在ViDoRe v1+v2+v3上平均NDCG@5达61.74，为8B教师模型的86.9%，在高分辨率敏感的v3基准上领先所有1B以下基线；Fast版NDCG@5为59.98，视觉token预算仅为HiRes的1/3；两个版本百万文档索引体积比最强1B以下多向量基线小15.6倍，索引速度快1个量级
