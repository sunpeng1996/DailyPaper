---
title: How BERT-based Cross-Encoders Model Relevance in Information Retrieval?
title_zh: 基于BERT的交叉编码器信息检索相关性建模机制研究
authors:
- Mathias Vast
- Basile Van Cooten
- Laure Soulier
- Benjamin Piwowarski
affiliations:
- Sinequa by ChapsVision, France
- Sorbonne Université, CNRS, ISIR, France
arxiv_id: '2610.41425'
url: https://arxiv.org/abs/2610.41425
pdf_url: https://arxiv.org/pdf/2610.41425
published: '2026-10-30'
collected: '2026-11-02'
category: RecSys
direction: 信息检索 · 交叉编码器可解释性研究
tags:
- Cross-Encoder
- BERT
- Relevance Matching
- Interpretability
- Information Retrieval
one_liner: 通过可解释性实验揭示BERT类交叉编码器的匹配信号流动规律与跨域行为特征
practical_value: '- 电商搜索/推荐精排场景优化Cross-encoder时，可参考本文信息流动追踪方法定位冗余匹配信号，裁剪参数提升推理效率

  - 跨品类/跨场景检索推荐落地时，可基于本文揭示的跨域行为特征设计域自适应微调策略，缓解跨域效果衰减

  - RAG系统的相关性排序模块调优时，可参考匹配信号分析结论调整query与chunk的匹配权重，提升召回准确率'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
Cross-encoder是当前信息检索领域效果最优的相关性建模范式，但推理效率极低，且query-doc匹配机制不透明、可解释性差，极大限制了模型优化、跨域落地，易产生次优检索结果，过参数化的模型也带来额外效率损耗。
### 方法关键点
从两个核心维度展开可解释性研究：1）追踪Cross-encoder推理各阶段、query与doc输入段间的信息流动路径，拆解支撑相关性预测的核心匹配信号构成；2）对比3种不同规模、不同预训练策略的BERT系Cross-encoder在域内、跨域数据集上的行为差异。
### 关键结果
厘清了Cross-encoder相关性建模的已有共识，明确了query-doc语义匹配信号在相关性预测中的核心作用，为后续模型压缩、跨域适配等优化方向提供了可解释性理论支撑。
