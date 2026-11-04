---
title: Factorized MLLM Embeddings for Composed Image Retrieval
title_zh: 面向组合图像检索的因式分解多模态大模型嵌入方法
authors:
- WonJun Moon
- Seongchan Kim
- Dahun Kim
- Seungryong Kim
affiliations:
- KAIST AI
- Google DeepMind
arxiv_id: '2611.05193'
url: https://arxiv.org/abs/2611.05193
pdf_url: https://arxiv.org/pdf/2611.05193
published: '2026-11-02'
collected: '2026-11-04'
category: Multimodal
direction: 多模态检索 · MLLM嵌入优化
tags:
- MLLM
- Composed Image Retrieval
- Embedding
- Factorized Representation
- Multimodal Retrieval
one_liner: 提出FactEmbed因式分解MLLM嵌入框架，解耦查询理解与嵌入学习，实现组合图像检索SOTA
practical_value: '- 电商多模态搜货场景可直接复用FactEmbed双输出架构：用[EOS]单向量做粗召回，同前向生成的因子化隐向量均值对top100候选重排，仅增不到0.05%开销即可提升top精度

  - 训练多模态匹配模型时，可引入轻量目标重构辅助损失作为结构监督，无需额外稠密标注即可让隐向量捕获更细粒度的语义属性，提升匹配准确率

  - 组合任务训练数据增强可借鉴对比式caption策略：同时给MLLM输入参考、目标、难负例生成修改文本，大幅降低标注成本的同时减少假负例'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
组合图像检索（CIR）支持用户输入参考图+修改文本检索目标图，是电商以图搜货、多模态搜索的核心需求；现有MLLM-based CIR方法直接将组合查询映射为单一嵌入，没有显式利用MLLM的组合理解能力，无法区分要修改和保留的视觉属性，细粒度匹配精度受限。
### 方法关键点
- 引入K个可学习因子化隐向量作为信息瓶颈，插入MLLM输入序列的[EOS]前，解耦组合查询理解与判别性嵌入学习
- 新增目标想象辅助损失：在MLLM中间层接入轻量解码器，基于粗布局先验用隐向量重构目标图细粒度特征，迫使隐向量各自捕获语义一致的目标属性
- 训练采用双层对比损失：因子层面用最优运输做InfoNCE对齐查询与目标隐向量，实例层面用[EOS]输出的全局嵌入做常规InfoNCE，同时加蒸馏损失将解码器的空间分解信息传递到MLLM深层注意力层
- 推理仅需一次前向传播：[EOS]向量用于高效粗召回，因子化隐向量均值对top100候选做轻量重排，几乎无额外计算与存储开销
### 关键结果
在Refined-CIRR、Refined-FashionIQ两个标准CIR基准上测试，对比ReCALL、CSMCIR等SOTA基线，FactEmbed在Refined-CIRR上R@1达68.99，相对提升2.3~2.7个百分点；在Refined-FashionIQ上平均R@10达71.13，相对提升2.3~2.4个百分点。
### 核心结论
将生成式重构作为结构监督引入判别性嵌入学习，可在几乎不增加推理成本的前提下，大幅提升多模态组合检索的细粒度匹配精度
