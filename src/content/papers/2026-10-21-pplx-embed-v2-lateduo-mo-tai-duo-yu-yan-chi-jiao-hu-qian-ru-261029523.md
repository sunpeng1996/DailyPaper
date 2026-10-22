---
title: pplx-embed-v2-late Technical Report
title_zh: pplx-embed-v2-late多模态多语言迟交互嵌入模型技术报告
authors:
- Markus Krimmel
- Louis Milliken
- Ekaterina Glazkova
- Maximilian Schall
- Antoine Chaffin
- Sedigheh Eslami
- Jonas Golde
- Denis Bykov
- Claire Beamer
- Jeremy Yang
affiliations:
- Perplexity AI
arxiv_id: '2610.29523'
url: https://arxiv.org/abs/2610.29523
pdf_url: https://arxiv.org/pdf/2610.29523
published: '2026-10-21'
collected: '2026-10-22'
category: RAG
direction: RAG检索 · 多模态迟交互嵌入模型
tags:
- Late Interaction
- Multimodal Embedding
- Knowledge Distillation
- RAG
- Efficient Retrieval
one_liner: 推出0.6B/9B两款多模态多语言迟交互嵌入模型，支持跨模型混合部署，各尺寸段性能达SOTA
practical_value: '- 可复用「大参数教师蒸馏+大小学生共享embedding空间」的架构，离线用大模型建索引、在线用小模型做query编码，兼顾检索精度与查询
  latency，适配电商商品检索、Agent搜索等在线场景

  - 训练数据采样可借鉴基于黄金比例Kronecker序列的低偏差采样策略，保证多数据集/多模态样本均匀分布，避免数据偏置，提升跨域检索性能

  - 工程上可复用自定义Triton MaxSim核+梯度缓存的优化方案，解决迟交互模型大batch训练的内存瓶颈，降低训练成本

  - 电商多模态检索（文本搜图、图文商品检索）场景可直接试用这两款开源模型，同尺寸下检索精度优于现有主流基线，0.6B版本可部署端侧'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有检索系统存在效率与交互深度的矛盾：稠密嵌入检索快但语义交互弱，交叉编码器精度高但推理延迟过高，迟交互模型虽平衡二者，但现有方案在多模态支持、跨模型复用、小模型性能上仍有缺口，无法满足Agent搜索、多模态检索等场景低延迟高准确率的需求。

### 方法关键点
- 先训练18B迟交互教师模型：基于Qwen3.5-27B剪枝得到，采用两阶段对比训练（第一阶段186M多模态query-doc对，第二阶段加入hard negative三元组），结合LoRA、梯度缓存、自定义Triton MaxSim核支持16384超大batch训练。
- 采用token级表示蒸馏训练0.6B/9B两款学生模型，二者共享同一embedding空间，支持非对称部署：离线用9B模型建索引，在线用低延迟0.6B模型做query编码。
- 训练采样采用基于黄金比例Kronecker序列的低偏差采样策略，保证多模态、多领域、多语言样本均匀分布，避免训练偏置。

### 关键实验结果
- 文本检索：72个跨领域任务上，9B模型nDCG@10达81.3%，超次优基线1.6pp；0.6B模型达78.0%，为1B以下模型最优。Q2D-Web Agent检索数据集上，9B/0.6B的Recall@1000分别达74.8%/73.6%，超最优基线5.5pp/4.3pp。
- 多模态检索：ViDoRe-V3视觉文档检索任务上，9B/0.6B模型nDCG@10分别达65.2%/62.3%，为同尺寸vision-language模型最优。
- 混合部署：0.6B query + 9B索引的方案比纯0.6B部署nDCG@10高1.6pp，query延迟无变化。

### 核心结论
大小模型蒸馏对齐同一embedding空间的非对称部署方案，可在不增加在线延迟的前提下显著提升检索精度，是工业级检索系统兼顾效率与效果的高性价比路径。
