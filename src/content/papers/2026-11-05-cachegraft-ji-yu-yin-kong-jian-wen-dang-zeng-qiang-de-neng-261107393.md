---
title: 'CacheGraft: Enhancing Retrieval-Augmented Generation via Latent-Space Document
  Enrichment'
title_zh: CacheGraft：基于隐空间文档增强的RAG性能优化方法
authors:
- Vihan Lakshman
- Peter Baile Chen
- Zhuohan Gu
- Michael Cafarella
affiliations:
- MIT CSAIL
arxiv_id: '2611.07393'
url: https://arxiv.org/abs/2611.07393
pdf_url: https://arxiv.org/pdf/2611.07393
published: '2026-11-05'
collected: '2026-11-06'
category: RAG
direction: 检索增强生成 · KV cache 离线优化
tags:
- RAG
- KV cache
- Document Enrichment
- Latent Space
- Model Collaboration
one_liner: 将跨模型KV cache融合技术迁移到RAG离线索引，用大模型信号增强小模型在线RAG性能
practical_value: '- 电商客服/商品问答场景的轻量RAG部署可复用该思路：离线用大模型预处理商品/FAQ文档生成融合KV cache，在线仅跑小模型就能获得接近大模型的问答质量，降低推理成本

  - 计算资源受限的端侧/边缘侧Agent RAG场景，可直接复用现成C2C融合器无需额外训练，不增加在线算力开销即可提升知识召回后的回答准确率

  - 可结合现有KV cache压缩技术解决存储开销问题，离线预生成的融合KV cache可按文档ID索引，检索后直接注入小模型KV空间，省去在线文本转KV的prefill耗时'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG离线优化多集中在文本层面的文档增强，预计算单模型KV cache仅能降低延迟无法提升小模型效果；跨模型KV cache融合技术此前仅用于实时多Agent通信，未被应用到RAG的非实时离线索引场景，小模型部署场景下RAG效果与算力成本的矛盾无法解决。

### 方法关键点
- 离线阶段针对每个文档，用大模型（4B参数sharer）和小模型（0.6B参数receiver）分别生成文档的KV cache，通过现成的C2C融合器生成小模型空间下的融合KV cache并持久化存储，无需感知用户query
- 在线阶段仅部署小模型，检索到相关文档后直接加载对应融合KV cache，拼接用户query的原生KV即可生成回答，全程不需要大模型和融合器参与
- 针对因果注意力特性，系统提示词+文档的融合KV与query无关，无需RoPE重旋转即可直接注入

### 关键实验
在SQuAD、AdversarialQA等5个QA基准上测试，用phi-4和Gemma-2-9B两个本地大模型做裁判，CacheGraft在30组对比中29组优于纯小模型文本RAG基线，其中17组统计显著，最高提升8个百分点；在线推理仅用1.27GB显存，比直接部署4B大模型节省83%显存，仅比纯小模型RAG高0.05GB。

### 核心结论
跨模型KV cache融合不仅可用于多Agent实时通信，更适合RAG离线索引场景，零额外训练就能用大模型的知识信号低成本增强小模型RAG效果。
