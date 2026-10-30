---
title: 'xPRT: Cross-Passage Retrieval Pretraining'
title_zh: xPRT：面向密集检索器的无监督跨段落预训练框架
authors:
- Danush Khanna
- Himanshu Singhal
- Pranjal A. Chitale
- Bishal Santra
affiliations:
- Microsoft Research
arxiv_id: '2610.40122'
url: https://arxiv.org/abs/2610.40122
pdf_url: https://arxiv.org/pdf/2610.40122
published: '2026-10-29'
collected: '2026-10-30'
category: RAG
direction: 检索预训练 · 密集检索器优化
tags:
- Dense Retriever
- Unsupervised Pretraining
- Cross-Passage
- MTEB
- RAG
one_liner: 提出无监督跨段落检索预训练框架xPRT，显著提升密集检索器性能，超SOTA基线3.2%
practical_value: '- 垂直域检索器训练可复用xPRT的跨段落信号挖掘逻辑：先用已有基准编码器+TF-IDF过滤文档噪声片段，筛选核心段落作为anchor，再匹配同文档相关段落作为正例，无需标注即可提升检索效果

  - 已上线检索模型增量预训练可复用衰减式retention正则器：前期大权重保留原模型能力避免灾难性遗忘，后期降低权重让新目标主导，平衡原有效果和增量增益

  - 垂直域RAG系统检索器优化可直接采用xPRT的损失组合：对比损失对齐相关段落embedding + 轻量解码器跨段落预测Masked token，小体量无标注语料即可获得显著增益，降低标注成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
当前密集检索器是RAG、搜索系统的核心组件，传统训练依赖标注query-文档对，成本极高，仅头部领域有成熟标注数据；现有无监督预训练方法要么基于同段落自编码，要么基于随机同文档片段做对比学习，未利用单文档内段落间的语义关联信号，增益有限甚至会导致原有模型性能退化。

**方法关键点**
- 段落筛选：用冻结的基准编码器（如E5）+TF-IDF，先筛选同文档中靠近全局embedding中心的核心段落作为anchor，排除导航、广告等噪声片段；再通过RRF融合稠密和词法相似度，为每个anchor匹配top4相关同文档段落作为sibling
- 损失组合：核心损失包含跨段落对比损失（对齐anchor和top sibling的embedding）、跨段落内容监督损失（用anchor的embedding预测sibling的高比例Masked token），搭配自预测、MLM、uniformity正则项，训练完成后仅保留编码器，推理成本无增量
- 增量训练适配：加入衰减式retention正则器，前期用大权重保留预训练模型已有能力，避免灾难性遗忘，后期降低权重让新预训练目标主导

**关键实验**
基于FineWeb无标注语料训练，在MTEB English v2共41个任务上评测，对比E5、RetroMAE、SimLM、Revela等5个SOTA无监督预训练目标，控制预训练语料、schedule、初始化完全一致：从E5做增量预训练时，xPRT是唯一稳定带来增益的方法，MTEB平均得分提升1.8-1.9分，比最强基线高3.2%，检索任务nDCG@10提升6.1%；从BERT从零预训练时，比最强基线高4.4分，检索nDCG@10提升41%。

**核心结论**
单份无标注文档的跨段落语义关联是远未被充分利用的检索预训练信号，经过筛选的相关段落对能带来远高于随机配对或同段落自编码的增益。
