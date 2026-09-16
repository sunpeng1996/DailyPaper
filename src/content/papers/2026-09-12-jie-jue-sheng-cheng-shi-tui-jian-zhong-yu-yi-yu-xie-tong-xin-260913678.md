---
title: Addressing Cross-Stage Decoupling of Semantic and Collaborative Signals in
  Generative Recommendation
title_zh: 解决生成式推荐中语义与协同信号的跨阶段解耦问题
authors:
- Jiayi Dan
affiliations:
- Kuaishou Technology
arxiv_id: '2609.13678'
url: https://arxiv.org/abs/2609.13678
pdf_url: https://arxiv.org/pdf/2609.13678
published: '2026-09-12'
collected: '2026-09-16'
category: GenRec
direction: 生成式推荐 · 语义-协同信号跨阶段对齐
tags:
- Generative Recommendation
- Semantic ID
- Collaborative Filtering
- Manifold Alignment
- Tokenization
one_liner: 提出轻量SCRec框架双向对齐生成式推荐两阶段语义与协同信号，相对SOTA最高提升27%
practical_value: '- 做Semantic ID tokenization时，可直接将item的协同相似邻域的title转为文本prompt，和主item文本一起输入PLM编码，无需额外对齐任务就能高效注入协同信号，避免直接拼接CF
  embedding导致的空间畸变

  - 生成阶段可复用语义引导的动态门控融合逻辑，将冻结的PLM语义先验与学习到的code embedding自适应加权，仅增加极微小计算开销就能缓解语义信息丢失

  - 不同模态/分布的表征对齐可优先尝试双曲流形对齐方案，相比L2、MMD等欧氏空间对齐方法，对层次化语义ID表征的对齐效果更好，且复杂度低于batch InfoNCE损失

  - 整个框架可封装为可插拔模块，直接接入现有TIGER、LIGER等主流生成式推荐骨架，仅需不到7%的额外训练/推理开销就能获得10%+的性能提升'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式推荐普遍采用两阶段pipeline：tokenization阶段仅靠文本语义编码，协同信号注入不足导致code分配和下游生成任务错配；生成阶段重训code embedding又会丢失原始语义信息，跨阶段信息解耦严重限制推荐准确率和语义一致性，过往注入方案要么增加额外训练成本，要么信号注入不充分。

### 方法关键点
- **协同增强tokenization**：用预训练序列推荐模型召回item的top-k协同相似邻域，将邻域title转为文本prompt，和item自身属性文本一起输入PLM编码，加权融合后再经RQ-VAE量化为同时包含语义和协同信息的code序列，无额外在线开销
- **语义引导生成**：对code序列的embedding做item级加权聚合，通过动态门控自适应融合冻结的PLM语义先验与学习到的code embedding，搭配batch InfoNCE损失做实例级对齐
- **双曲流形对齐**：将code embedding和语义embedding都投影到同一个双曲空间，最小化两者测地线距离解决表征空间几何结构不匹配问题，复杂度仅为O(Nd)低于InfoNCE的O(N²d)

### 关键结果
在Amazon三个公开数据集（Beauty、Sports and Outdoors、Toys and Games）上对比20+基线，相比当前SOTA的RPG、PIT等模型，Recall@5/10、NDCG@5/10四个指标相对提升13%-27%；模块可插拔接入TIGER、LIGER骨架，相对提升10%-19%，仅增加不到7%的训练/推理开销。

**最值得记住的一句话**：生成式推荐的两阶段信号对齐不能只做实例级特征融合，还要从tokenization输入设计、表征空间几何一致性两个层面做系统性优化，才能用极低开销获得明显收益。
