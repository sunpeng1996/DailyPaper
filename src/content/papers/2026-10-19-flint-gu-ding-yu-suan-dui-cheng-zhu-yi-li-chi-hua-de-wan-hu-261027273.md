---
title: 'FLINT: Fixed-budget Late Interaction'
title_zh: FLINT：固定预算对称注意力池化的晚交互检索架构
authors:
- Himank Handa
- Negar Arabzadeh
- Matei Zaharia
affiliations:
- University of Illinois Urbana-Champaign
- University of California, Berkeley
arxiv_id: '2610.27273'
url: https://arxiv.org/abs/2610.27273
pdf_url: https://arxiv.org/pdf/2610.27273
published: '2026-10-19'
collected: '2026-10-21'
category: RecSys
direction: 多向量召回 · 晚交互检索效率优化
tags:
- Multi-Vector Retrieval
- Late Interaction
- Dense Retrieval
- Attention Pooling
- Efficiency Optimization
one_liner: 对称池化query和doc到固定向量数，长复杂查询下检索效率远超ConstBERT
practical_value: '- 电商搜索、Agent RAG召回场景可复用FLINT对称注意力池化方案，将query和item均压缩为固定数量向量，避免长query（用户多约束搜品、模糊需求描述）下检索
  latency 随query长度线性上涨，兼容现有PLAID索引

  - 可借鉴向量预算V的调优思路：短query为主的场景选V=32即可平衡效果与成本，长复杂query占比高的场景可上调至V=64，也可尝试query和doc使用不同V值进一步控本

  - 现有ConstBERT/ColBERT类多向量检索系统升级时，可直接替换原有池化模块为FLINT的跨注意力池化，索引大小与ConstBERT持平，长query场景检索速度提升1.5~2.8倍，还能拿到效果增益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
ColBERT类token级晚交互检索模型效果优于同规模单向量bi-encoder，但存储成本、检索latency随doc、query长度线性增长，无法适配长复杂查询场景；此前ConstBERT仅对doc做固定数量向量池化，query仍保留token级向量，长query下检索成本仍不可控，亟需同时压缩query和doc的固定预算晚交互架构。
### 方法关键点
- 对称设计：对query和doc使用共享的跨注意力池化模块，分别基于各自独立的可学习latent向量，将变长token序列压缩为固定V个向量，解耦存储、检索成本与输入长度
- 池化结构：基于Perceiver Resampler的跨注意力机制加FFN层输出固定维度向量，沿用ColBERT的MaxSim打分函数做晚交互匹配
- 可控trade-off：通过调整向量数V，可直接在检索效果、存储、latency之间做自定义权衡
### 关键实验
数据集覆盖BEIR（短常规查询）、CRUMB、TREC ToT 2025、BrowseComp+（长复杂查询），对比baseline包括单向量bi-encoder、ColBERTv2、ConstBERT，兼容BERT和ModernBERT两种backbone：
- 效果：BEIR上与ConstBERT持平，接近ColBERTv2；长复杂查询场景NDCG@10优于ConstBERT，ModernBERT backbone下TREC ToT 2025上NDCG@10达ConstBERT的2倍以上
- 效率：索引比ColBERTv2小5.3~9.3倍，长query场景端到端检索速度比ConstBERT快1.5~2.8倍，搜索阶段速度快2.5~4.8倍，latency随query长度几乎无增长
### 核心结论
对query和doc同时做固定预算对称池化，是解决长复杂查询下多向量检索存储和latency瓶颈的高性价比方案
