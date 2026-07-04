---
title: Building a Multimodal Dataset of Academic Paper for Keyword Extraction
title_zh: 面向关键词提取任务的学术论文多模态数据集构建
authors:
- Jingyu Zhang
- Xinyi Yan
- Yi Xiang
- Yingyi Zhang
- Chengzhi Zhang
affiliations:
- 南京理工大学信息管理系
- 苏州大学档案与电子政务系
arxiv_id: '2606.31069'
url: https://arxiv.org/abs/2606.31069
pdf_url: https://arxiv.org/pdf/2606.31069
published: '2026-06-30'
collected: '2026-07-04'
category: Other
direction: 多模态关键词提取 · 数据集构建
tags:
- Multimodal Dataset
- Keyword Extraction
- Information Extraction
- Text Mining
- Multimodal Fusion
one_liner: 构建含1000样本的学术论文多模态数据集，验证多模态文本拼接可提升关键词提取效果
practical_value: '- 电商商品关键词生成、搜索Query拓展场景可复用多模态文本拼接思路，融合商品详情文本、主图OCR文本、直播口播转写文本，提升关键词准确率

  - 知识类内容推荐场景可借鉴该数据集的标注框架，优化论文、课程等多模态内容的标签生成与召回特征构建流程

  - 多模态召回模型迭代时可参考本文的单/多模态效果对比方法，验证不同模态特征的增益贡献'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有关键词提取任务仅依赖单一文本数据，忽略图像、音频模态的隐藏信息，导致输入信息丰富度不足、跨模态关联被遗漏，直接限制模型表征学习能力与预测精度；同时面向关键词提取的公开多模态数据集极度稀缺，阻碍相关技术的落地迭代。

### 方法关键点
构建包含1000个标注样本的学术论文多模态数据集，每个样本覆盖论文原文、图像、音频、人工标注关键词四类数据；分别基于无监督、有监督两类关键词提取范式，对比单模态文本输入、多模态提取文本拼接输入两种方案的效果差异。

### 关键结果
不同模态提取的文本在模型中表现出显著差异化特征；直接拼接论文原文、图像OCR文本、音频转写文本的方案，可有效提升学术论文关键词提取的整体性能。
