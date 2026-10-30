---
title: Contextual Embeddings Beyond the Gold Chunk
title_zh: 无需黄金块标注的上下文嵌入模型pplx-embed-v2-context
authors:
- Sedigheh Eslami
- Markus Krimmel
- William Barber
- Antoine Chaffin
- Maximilian Schall
- Jonas Golde
- Louis Milliken
- Ekaterina Glazkova
- Denis Bykov
- Bo Wang
affiliations:
- Perplexity AI
- turbopuffer
arxiv_id: '2610.38854'
url: https://arxiv.org/abs/2610.38854
pdf_url: https://arxiv.org/pdf/2610.38854
published: '2026-10-28'
collected: '2026-10-30'
category: RAG
direction: RAG检索 · 上下文嵌入训练与评测
tags:
- Contextual Embedding
- RAG
- Knowledge Distillation
- Retrieval Benchmark
- Multimodal Retrieval
one_liner: 通过查询感知上下文压缩模型蒸馏分级chunk相关性，训练无黄金块标注的SOTA上下文嵌入
practical_value: '- 训练上下文嵌入时可复用现有上线的查询感知上下文压缩模型作为教师蒸馏分级chunk相关性，无需标注黄金chunk，训练不绑定chunk策略，大幅降低标注和迭代成本

  - 检索效果评测可新增证据chunk召回、完整覆盖所需token数等指标，替代单一黄金块召回，更贴合电商商品详情页、客服知识库等长文档RAG的实际落地效果

  - 多模态图文检索可借鉴图像水平分块+分隔符标记的chunk策略，复用视觉语言基座的预训练跨模态能力，无需额外多模态训练即可拿到不错的检索效果，适配电商图文商品检索场景

  - 大小模型蒸馏时对齐嵌入空间，线上可根据流量、latency要求灵活切换0.6B小模型和9B大模型，无需重建索引，降低部署和迭代成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有上下文嵌入训练依赖单黄金块标注，将支撑答案的关联chunk误判为负样本，效果受限且标注绑定固定chunk策略，难以规模化迭代；现有评测仅考核单黄金块召回，不符合RAG系统需要同时召回答案+验证证据的实际需求，长文档、多模态场景下评测结果和业务效果脱节。
### 方法关键点
- 训练范式：以线上部署的查询感知上下文压缩模型为教师，输出token级相关性得分，可聚合为任意chunk的分级标签，蒸馏训练学生嵌入模型，无需黄金块标注，训练不绑定chunk策略
- 损失设计：9B模型采用chunk级KL散度蒸馏损失+文档级InfoNCE对比损失加权组合，加入Matryoshka表示学习和int8量化感知训练；0.6B模型直接对齐9B模型的表示空间，二者嵌入空间完全兼容
- 多模态扩展：复用视觉语言基座预训练能力，图像采用水平分块+chunk分隔符标记方案，无需额外多模态训练即可支持视觉文档检索
- 评测基准：发布context-bench（受控诊断基准）和Q2D-Chunk（真实搜索流量基准），同时标注答案chunk和支撑证据chunk，更贴合实际RAG场景
### 关键结果
9B模型在context-bench Answer@10达45.5%，超第二名voyage-context-4 14.4个点；Q2D-Chunk Answer@10达86.4%，超第二名2.5个点；ConTEB平均nDCG@10达83.4%，刷新SOTA；多模态检索在ViDoRe-V3上仅用2块/页、1/4的索引大小，性能超过Nemotron-3.5-8B。

上下文嵌入的训练和评测都要跳出单黄金块的假设，只有能同时召回答案和支撑证据的检索模型，才能真正提升RAG系统的实际业务效果。
