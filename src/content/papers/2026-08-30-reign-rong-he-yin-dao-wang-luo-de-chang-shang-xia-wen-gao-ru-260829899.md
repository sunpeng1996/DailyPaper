---
title: 'REIGN: Refurbished Embeddings with Integrated Guidance Networks for Efficient
  Context-Length Scaling'
title_zh: REIGN：融合引导网络的长上下文高效嵌入扩展框架
authors:
- Devrim Çavuşoğlu
- Emre Akbaş
affiliations:
- Middle East Technical University
- OBSS AI
arxiv_id: '2608.29899'
url: https://arxiv.org/abs/2608.29899
pdf_url: https://arxiv.org/pdf/2608.29899
published: '2026-08-30'
collected: '2026-09-01'
category: RAG
direction: RAG长文档检索 · 高效嵌入优化
tags:
- Long-Context Retrieval
- Dense Embedding
- Contrastive Learning
- Bi-encoder
- Efficient Training
one_liner: 基于冻结引导网络的分块嵌入训练轻量编码器，大幅降低长文档检索的训练推理成本
practical_value: '- 长文本类召回场景可直接复用架构：冻结已落地的短文本嵌入模型（如GTE、E5）作为引导网络，仅训练上层轻量分块聚合Transformer，无需重新训练大模型，适配电商商品详情页检索、用户长评论语义匹配、Agent长记忆检索等场景

  - 成本优化trick可直接落地：预计算并缓存引导网络的分块嵌入到磁盘，训练阶段仅运行上层小模型，单文档训练成本比传统分块Transformer微调低4个数量级，大幅降低大规模长文本数据集的训练门槛

  - 数据集构造方法可迁移：用LLM改写长文本生成正样本、语义相似文本作为分级负样本的方式，可快速构造领域专属的长文本对比训练数据集，无需人工标注长文本对

  - 场景适配经验：仅在需要跨块语义聚合的长文档检索场景引入该架构，短文本/query匹配场景直接用原生嵌入模型即可，避免冗余计算消耗'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有长上下文嵌入模型要么需要修改Transformer注意力架构，要么要微调十亿级大模型，训练推理成本极高；同时公开数据集中缺乏标注完善的长文档对比训练对，导致长文档密集检索落地门槛高，难以适配业务中大规模长文本处理需求。
### 方法关键点
- 架构采用双阶段设计：冻结成熟短文本嵌入模型作为Guidance Network（GN），将长文档分块编码为嵌入序列，上层仅训练轻量Transformer聚合跨块语义，平均池化得到文档级嵌入
- 效率优化：预计算并缓存GN的分块嵌入，训练时仅运行REIGN小模型，计算复杂度从token级O(M²d)降至chunk级O(N²d)，单chunk输入直接返回GN结果避免冗余
- 训练策略：采用SimCLR风格对比学习，设计三级余弦损失适配正样本、分级负样本、batch负样本，比InfoNCE在小batch下训练更稳定
- 开源GoodWiki-Long-Synthetic数据集：用GPT-4o-mini改写维基百科长文生成正样本，语义相似文本作为分级负样本，单文档最长达35K token
### 关键结果
- 分布内GoodWiki-Long数据集：55M参数的REIGN+GTE-small nDCG@10超过568M的BGE-M3，参数量仅为1/10
- OOD LoCo长上下文基准：357M的REIGN+GTE-large nDCG@10达70.77，仅比20倍参数的E5-Mistral低0.65
- 真实专利检索场景：357M REIGN与1.6~4.3倍参数的Jina-v3、Stella-1.5B效果统计无显著差异

长文本嵌入不需要从头训练大模型，冻结成熟短文本嵌入模型做分块聚合的轻量化方案，在大部分场景下性价比更高
