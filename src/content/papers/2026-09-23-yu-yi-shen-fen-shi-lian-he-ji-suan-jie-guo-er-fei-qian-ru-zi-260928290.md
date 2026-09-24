---
title: 'Computation Over Geometry: Meaning Identity Is Computed, Not Shipped in the
  Embeddings'
title_zh: 语义身份是联合计算结果，而非嵌入自带的几何属性
authors:
- Jiaqi Deng
affiliations:
- Independent Researcher
arxiv_id: '2609.28290'
url: https://arxiv.org/abs/2609.28290
pdf_url: https://arxiv.org/pdf/2609.28290
published: '2026-09-23'
collected: '2026-09-24'
category: RAG
direction: RAG语义匹配 · 语义身份计算优化
tags:
- Semantic Matching
- Retrieval
- RAG
- Paraphrase Detection
- Embedding
one_liner: 证明语义一致性无法通过独立嵌入匹配获得，必须通过同一次前向传播联合计算得到
practical_value: '- 电商/客服FAQ、商品重复去重、广告文案撞库场景可采用「嵌入粗召回+联合推理校验」架构，无需改动存量向量索引，即可降低高词汇重叠样本的误判率

  - 可蒸馏跨模型共识的小参数联合判定器，1.5B规模即可达到7B模型的语义校验效果，比finetune bi-encoder泛化性更强，不会损失通用STS匹配性能

  - RAG/Agent检索阶段不要依赖嵌入余弦相似度做语义一致性强校验，高词汇重叠paraphrase场景下该方法AUC仅0.55-0.65，联合前向传播判定可达0.90+'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前RAG、检索、重复内容判定系统普遍假设语义一致性是句子嵌入的固有几何属性，可通过余弦相似度、late fusion等独立嵌入匹配方法获得，但在高词汇重叠的paraphrase硬样本（如词序调换但语义完全不同/相同的句子）上，这类方法性能极差，业务中频繁出现误判。

### 方法关键点
- 构建词汇重叠匹配的PAWS-X、QQP数据集，保证仅靠词汇重叠的分类器AUC接近0.5，排除混淆变量
- 设计4种对比读入方式：独立编码余弦匹配、独立嵌入线性探针、late fusion、同一次前向传播的联合探针，搭配打乱句子对的对照组
- 覆盖20+主流开源模型，参数规模从0.36B到32B，包含decoder-only、双向编码器、编码器-解码器三类架构

### 关键结果
- 在重叠匹配的PAWS-X数据集上，BGE、E5等主流专用编码器的余弦匹配AUC仅0.55-0.70，Llama3、Mistral等大模型独立编码匹配AUC仅0.47-0.61，均接近随机水平
- 同一次前向传播的联合探针AUC达0.90-0.96，打乱句子对后AUC回落至0.5左右，性能提升完全来自联合计算的语义一致性信号
- 蒸馏跨模型共识的1.5B联合判定器，在FAQ硬样本场景下，将cosine召回的Top-1准确率从0.468提升至0.842，和7B模型效果相当

**最值得记住的一句话**：语义身份是两个句子的联合计算关系，不是单个句子嵌入的固有属性，「嵌入粗召回+联合校验」是高准确率语义匹配的最优性价比架构。
