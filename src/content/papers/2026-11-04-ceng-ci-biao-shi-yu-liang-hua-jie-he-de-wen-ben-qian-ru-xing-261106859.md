---
title: 'Balancing hierarchical representation and quantization: A performance trade-off
  in text embeddings'
title_zh: 层次表示与量化结合的文本嵌入性能权衡实证研究
authors:
- Kai Ponel
- Marco Polignano
- Erasmo Purificato
- Aylin Julia Temizkan
- Marco Levantesi
- Giovanni Semeraro
- Ernesto William De Luca
affiliations:
- Ludwig-Maximilian-University Munich
- University of Bari Aldo Moro
- European Commission Joint Research Centre
- IBM Germany
- Otto von Guericke University Magdeburg
arxiv_id: '2611.06859'
url: https://arxiv.org/abs/2611.06859
pdf_url: https://arxiv.org/pdf/2611.06859
published: '2026-11-04'
collected: '2026-11-05'
category: RAG
direction: RAG · 文本嵌入压缩优化
tags:
- TextEmbedding
- MatryoshkaRepresentation
- Quantization
- MTEB
- RAG
one_liner: 在38个MTEB任务上实测Matryoshka截断与量化组合的性能trade-off，给出落地配置指南
practical_value: '- 电商搜索、Agent RAG问答场景的向量库优化可优先采用「Matryoshka截断到128维+int8量化」配置，仅损失5.6%效果的前提下实现32倍存储压缩，适合亿级商品/文档向量库降本

  - 商品召回、搜索等排序类任务对嵌入压缩敏感度远高于聚类、分类任务，召回侧压缩需保守选择≥256维+int8配置，避免截断导致的细粒度语义区分能力下降

  - 速度优先的端侧/边缘推荐场景，可采用2D Matryoshka模型中间层输出+int8量化，实测仅损失18%效果即可将推理耗时减半，且无需额外拟合投影矩阵

  - 优先选择int8量化而非二进制量化，二进制量化即使用全维嵌入也会损失17%以上效果，仅适合带高精度重排的粗召回阶段使用'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大规模文本嵌入部署面临存储成本高、推理延迟高的痛点，Matryoshka层次截断和量化是两种无额外拟合成本的常用压缩手段，但二者结合的性能-效率trade-off缺乏系统性实证验证，行业没有可直接复用的落地配置参考。
### 方法关键点
- 测试4款基于Matryoshka损失训练的开源嵌入模型（含1D、2D MR两类），覆盖全组合配置：8档维度截断、3种量化精度（float32/int8/binary），2D MR额外测试4档输出层
- 在38个MTEB任务上完成168种配置的评测，采用Friedman+Nemenyi统计检验验证结果显著性，拆分理论存储、端到端推理耗时、任务效果三个维度的收益损耗
### 关键结果
- int8量化在配对分类、重排任务上与float32效果无统计差异，整体效果损失最高仅1.5pp；二进制量化在所有任务上效果显著下降，全维下效果损失超17%
- 单次维度减半在维度≥16时无统计显著损失，连续两次减半则损失显著；8倍维度截断+int8量化可实现32倍存储压缩，仅损失5.6%的整体效果
- 检索类任务对压缩敏感度远高于其他任务，128维+int8配置在小检索数据集上已损失11%效果，生产级大规模检索场景损失会进一步放大
### 核心结论
文本嵌入压缩的配置上限由检索类任务决定，优先选择int8+Matryoshka截断的组合，不要为了存储收益盲目使用二进制量化
