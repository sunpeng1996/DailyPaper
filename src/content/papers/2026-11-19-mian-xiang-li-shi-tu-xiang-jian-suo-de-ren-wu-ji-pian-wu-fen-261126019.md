---
title: A Task-Level Bias Taxonomy for Historical Image Retrieval
title_zh: 面向历史图像检索的任务级偏误分类体系
authors:
- Omkar Gavali
- Ratan Sebastian
- Christoph Rippe
- Ralph Ewerth
- Anett Hoppe
affiliations:
- Philipps-Universität Marburg, Germany
- TIB – Leibniz Information Centre for Science and Technology, Hannover, Germany
- L3S Research Center, Leibniz University Hannover, Germany
- Goethe University Frankfurt, University Library, Germany
- Hessian Center for Artificial Intelligence (hessian.AI), Germany
arxiv_id: '2611.26019'
url: https://arxiv.org/abs/2611.26019
pdf_url: https://arxiv.org/pdf/2611.26019
published: '2026-11-19'
collected: '2026-11-21'
category: Multimodal
direction: 多模态检索 · 偏误治理
tags:
- Bias Mitigation
- Multimodal Retrieval
- Historical Image
- Metadata Enrichment
- GLAM
one_liner: 梳理历史图像检索全链路偏误的类型、成因与影响，总结现有偏误缓解方案
practical_value: '- 处理电商存量低质/老旧商品素材（如复古品类图、早期无标注上架素材）时，可参考本文偏误成因框架，排查跨域标注生成、检索链路的bias来源，避免低质召回

  - 针对标注稀疏/缺失的存量内容库做metadata自动富集时，需重点校验训练数据与目标存量数据的分布差、原始标注自带的历史偏误，提前做分布对齐降低对推荐/检索效果的影响

  - 做垂类内容检索系统的合规性/公平性优化时，可复用本文任务级偏误分类逻辑，分层拆解全链路bias点做逐个治理'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
GLAM（画廊、图书馆、档案馆、博物馆）机构已完成海量历史图像的数字化，但这类图像普遍存在元数据稀疏、缺失甚至自带时代性偏误的问题。当前依赖ML生成/富集元数据提升检索可及性的方案，容易因训练数据与历史图像分布差异、图像降质、原始标注偏误等问题，放大检索结果的不公平性，缺乏全链路的偏误系统分析框架。
### 方法关键点
从任务全链路维度搭建任务级偏误分类体系，逐一明确不同偏误的产生路径、对AI辅助检索系统的影响逻辑，同时系统性回顾现有偏误缓解的技术方案，覆盖数据预处理、模型训练、结果校准全环节。
### 关键结论
形成了覆盖数据层、模型层、任务层的统一偏误分析框架，明确了历史标注偏误、跨域分布偏移偏误、图像质量降质偏误等核心问题的影响机制，为历史图像检索系统的公平性优化提供了标准化分析依据。
