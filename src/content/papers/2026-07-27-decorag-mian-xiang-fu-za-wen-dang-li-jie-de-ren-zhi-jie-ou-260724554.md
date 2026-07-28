---
title: 'DeCoRAG: Cognitive Decoupling and Semantic-Aware Cropping for Complex Document
  Understanding'
title_zh: DeCoRAG：面向复杂文档理解的认知解耦与语义感知裁剪框架
authors:
- Shuo Wang
- Kai Zhang
- Wenyuan Huang
- Yizheng Yu
- Xia Liao
- Junming Su
- Qing Wang
- Fang Xi
affiliations:
- QiYuanLab
- Beijing University of Posts and Telecommunications
- University of Science and Technology Beijing
arxiv_id: '2607.24554'
url: https://arxiv.org/abs/2607.24554
pdf_url: https://arxiv.org/pdf/2607.24554
published: '2026-07-27'
collected: '2026-07-28'
category: RAG
direction: 多模态RAG · 复杂文档理解
tags:
- Multimodal-RAG
- GraphRAG
- Visual-Attention-Sink
- Cognitive-Decoupling
- Document-Understanding
one_liner: 提出认知解耦多模态Graph RAG框架，缓解视觉注意力sink，降40.8%建图token量提12.5%语义通过率
practical_value: '- 处理电商商品参数长图、运营活动规则图、行业财报等多模态文档时，可复用认知解耦范式：先基于低分辨率图生成全局Semantic
  Anchor引导注意力，再做高分辨率局部信息抽取，缓解VLM注意力漂移导致的抽取幻觉，适合文档类Agent的解析场景

  - RAP-Crop双流裁剪方案可直接迁移至多模态处理链路：用传统CV形态学操作提取视觉密集区+语义关键词OCR匹配提取语义相关区，合并后裁剪冗余背景，可降低约40%的VLM输入token量，不损失抽取精度，显著降低推理成本

  - 多模态Graph RAG建图时可拆分耦合任务：无需让VLM同时完成视觉定位、语义理解、关系抽取三个任务，分阶段执行能大幅提升复杂布局文档的知识三元组抽取准确率，提升下游RAG问答的事实一致性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多模态Graph RAG处理高密复杂文档（含图表、表格、非结构化布局的财报、论文、运营材料等）时存在双重困境：耦合的视觉定位、语义理解、关系抽取任务会触发「Visual Attention Sink」，VLM注意力漂移到无意义的边界区域导致语义丢失、幻觉；同时全页高分辨率处理的token开销极高，现有方案无法兼顾效果和成本。
### 方法关键点
- 采用认知解耦的三段式建图管线：第一阶段输入低分辨率全局视图生成Semantic Anchor，作为注意力引导信号，将VLM注意力从sink区域拉回语义相关区
- 设计双流RAP-Crop算法：融合视觉密度流（形态学操作提取视觉密集块）和语义Grounding流（从Semantic Anchor提取关键词做OCR坐标匹配），动态裁剪感兴趣区域，丢弃冗余背景
- 第三阶段结合全局Semantic Anchor和裁剪后的高分辨率局部块，做结构化知识抽取，生成多模态知识图谱，支持下游混合检索和问答
### 关键结果
在SPIQA、SlideVQA、PaperTab等复杂文档基准上，对比ColPali、MMGraphRAG等SOTA基线，Semantic Pass Rate最高提升12.5%；RAP-Crop降低离线建图prompt token量40.8%、总token量29.6%，不损失端到端精度；在DocVQA上泛化验证ANLS达0.968，语义通过率97%。
最值得记住的结论：多模态复杂场景下，将耦合的视觉-语义推理任务拆解为全局锚定、区域裁剪、局部抽取的分阶段流程，往往比盲目提升模型容量更能兼顾效果和效率。
