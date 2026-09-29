---
title: 'RenderRank: Learning to Rerank Text with Compressed Visual Tokens'
title_zh: RenderRank：基于压缩视觉Token的文本重排序方法
authors:
- Seongtae Hong
- Youngjoon Jang
- Jungseob Lee
- Hyeonseok Moon
- Heuiseok Lim
affiliations:
- Korea University
- Sookmyung Women's University
arxiv_id: '2609.35069'
url: https://arxiv.org/abs/2609.35069
pdf_url: https://arxiv.org/pdf/2609.35069
published: '2026-09-27'
collected: '2026-09-29'
category: RAG
direction: RAG链路优化 · 多模态文档重排序
tags:
- Reranker
- Visual Token
- Knowledge Distillation
- Long Document
- Inference Efficiency
one_liner: 将文本渲染为图像编码为压缩视觉Token，实现高性能低开销的文档重排序
practical_value: '- 电商搜索/商品详情页长文本重排场景，可复用文本转压缩视觉Token的思路，在同等序列长度限制下容纳更多商品信息提升精度，或在相同精度下降低Token消耗提升吞吐

  - 两阶段训练范式可直接迁移至多模态重排器的领域适配：先用跨模态蒸馏对齐文本教师模型分数，再用Query级正负样本对比学习优化排序效果

  - 离线预计算并缓存文档视觉Embedding的工程方案，适合静态商品库/知识库的检索重排场景，可大幅降低在线推理延迟

  - 渲染配置可按需调优：字体越小Token量越少速度越快、精度略降，可通过离线A/B测试平衡业务的精度与延迟要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有文本重排器输入Token长度随文档长度线性增长，长文档场景下计算开销高、序列长度限制易导致关键信息丢失，RAG链路中重排阶段的高延迟会拖累全链路响应速度，亟需在保证重排精度的前提下降低输入Token量、提升推理效率。
### 方法关键点
- 输入模态转换：将纯文本文档按优化后的渲染配置（12pt字体、1.0行间距）转成固定宽高的图像，用VLM视觉编码器编码为压缩视觉Token，仅Query保留文本输入，大幅降低总输入序列长度
- 两阶段训练：第一阶段跨模态相关性蒸馏，用文本重排教师模型的分数监督视觉输入的学生模型输出，对齐跨模态相关性认知；第二阶段Query级相关性判别，用同一Query下的正负样本做InfoNCE对比学习，优化相对排序效果
- 效率优化：文档视觉编码可离线预计算并缓存，推理阶段直接读取缓存与文本Query拼接计算相关性，进一步降低推理延迟
### 关键实验结果
在11个BEIR通用检索数据集上，平均NDCG@10达55.96，优于所有4B参数以下的文本重排基线，输入Token量降低16.5%~35.5%；在4个长文档数据集上，平均NDCG@10达88.27，输入Token量仅为文本基线的一半，推理吞吐量达基线最高值的1.7×；相同序列长度限制下（如4K Token），重排精度优于文本基线在8K长度下的表现。
### 核心结论
纯文本转压缩视觉Token的模态转换思路，可在几乎不损失精度的前提下大幅降低长文本处理的计算开销，为检索重排、长文档理解等场景提供了全新的效率优化路径。
