---
title: Riemannian Geometry for Pre-trained Language Model Embeddings
title_zh: 面向预训练语言模型嵌入的黎曼几何方法
authors:
- Szczepan Konior
- Alexandre Quemy
- Przemysław Klocek
- Grégoire Cattan
- Bartłomiej Sobieski
affiliations:
- IBM Automation and AI, Krakow, Poland
- Hother, Krakow, Poland
- University of Warsaw
- Centre for Credible AI, Warsaw University of Technology
arxiv_id: '2607.07047'
url: https://arxiv.org/abs/2607.07047
pdf_url: https://arxiv.org/pdf/2607.07047
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: LLM嵌入几何 · 池化方法优化
tags:
- Riemannian Geometry
- Pooling
- SPD Manifold
- LLM Embedding
- Sentence Classification
one_liner: 提出黎曼均值池化RMP，基于SPD流形Fréchet均值聚合token嵌入提升句子分类性能
practical_value: '- 做文本语义表征聚合（如用户Query、商品标题/评论 embedding pooling）时，可尝试替换传统欧氏平均池化为RMP，适配LLM嵌入各向异性特性提升表征质量

  - 知识密集型文本分类任务（如电商虚假评论识别、商品合规校验）可优先尝试预训练编码器+黎曼几何聚合方案，增益更显著

  - 评估新池化策略时，可引入无标注噪声的对照数据集校验鲁棒性，避免拟合标注伪影'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM嵌入分析多默认欧氏空间假设，未考虑语言层级结构、表征各向异性等特性，池化方法易损失语义信号，限制下游任务性能与可解释性。

### 方法关键点
1. 从编码器解析雅可比矩阵提取每个token的拉回度量，将token嵌入映射到对称正定（SPD）流形空间；
2. 提出黎曼均值池化（RMP），通过SPD流形上的Fréchet均值聚合多token度量得到句子级表征。

### 关键结果
在CoLA、CREAK、RTE三个含复杂语言结构的数据集上，RMP效果全面优于欧氏平均池化；在去除标注人工伪影的FEVER-Symmetric数据集上性能符合随机概率，无过拟合问题；消融实验显示仅随机初始化编码器+Fréchet聚合就可在2个数据集上超过欧氏池化，增益核心来自几何聚合而非预训练流形结构，预训练编码器仅在知识最密集的CREAK数据集上有额外增益。
