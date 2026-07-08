---
title: 'Learn to Pool: Lightweight Fine-Tuning for Flexible Multi-Vector Compression'
title_zh: Learn to Pool：面向多向量检索灵活压缩的轻量微调方法
authors:
- Stefan Josef
affiliations:
- Independent Researcher
arxiv_id: '2607.06036'
url: https://arxiv.org/abs/2607.06036
pdf_url: https://arxiv.org/pdf/2607.06036
published: '2026-07-07'
collected: '2026-07-08'
category: RecSys
direction: 多向量检索 · Pooling感知轻量微调
tags:
- ColBERT
- Multi-Vector Retrieval
- Vector Compression
- Lightweight Fine-tuning
- Token Pooling
one_liner: 通过轻量Pooling感知微调实现多向量检索模型高压缩率下精度持平甚至提升
practical_value: '- 优化电商搜索/商品召回的ColBERT类多向量模型时，可直接引入k-means Pooling感知轻量微调，在83%向量压缩率下实现精度不降，大幅降低向量存储与检索延迟

  - 若业务需要灵活调整压缩率，可采用多因子训练策略（每批随机采样1-6的Pool因子），单个模型即可适配不同压缩级别的索引需求，无需为每个压缩率单独训练

  - 负例采样可复用论文方案：先用小Embedding模型挖100个硬负例+30个随机负例，再用Reranker过滤得分过高的假负例，平衡难中易负例比例提升微调效果

  - 不要对预训练ColBERT做无Pooling的域内微调，会大幅破坏模型原生的Pooling兼容性，导致压缩后精度暴跌70%以上'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
ColBERT等晚交互多向量检索模型泛化性显著优于单向量Embedding，但单文档生成数十个Token向量导致存储、内存占用高，推理延迟大，限制大规模部署。现有无训练推理Pooling可压缩2-3倍但更高压缩率下精度下降快，全量Pooling感知预训练对中小团队算力要求过高，亟需低成本优化方案。

### 方法关键点
- 对比3种Pooling策略：顺序Span Pooling、k-means聚类Pooling、层次聚类Pooling，仅对文档侧Token做压缩，Query侧保持不变
- 轻量微调设计：仅需域内千级规模Query训练数据，将Pooling操作嵌入前向传播过程，基于Reranker得分做KL散度蒸馏损失训练，聚类类Pooling通过detach聚类分配保证梯度回传
- 多因子训练：每批随机采样1-6的Pool因子，让单个模型适配不同压缩率，同时p=1的无压缩样本作为正则项保留原生精度

### 关键结果
- 数据集：NanoBEIR、全量BEIR的FiQA、SciFact等5个公开检索数据集，基线为mxbai-edge-colbert-v0-32m无训练推理Pooling方案
- 核心数字：k-means Pooling感知微调后的模型在BEIR SciFact数据集上Pool因子1-6（最高83%压缩率）下NDCG@10均优于未压缩基线；跨数据集迁移下，单数据集微调后其他数据集Pooling场景精度平均提升5%-18%；仅做无Pooling域内微调的模型在Pool因子4下精度暴跌70%以上

### 核心结论
轻量Pooling感知微调是多向量检索模型降本提效的高性价比方案，k-means是微调阶段最优的Pooling策略，多因子训练可实现单个模型适配多压缩级别的灵活部署
