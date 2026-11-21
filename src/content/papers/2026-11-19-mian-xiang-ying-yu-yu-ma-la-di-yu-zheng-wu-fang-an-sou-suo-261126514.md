---
title: Hybrid Retrieval for Government Scheme Search in English and Marathi
title_zh: 面向英语与马拉地语政务方案搜索的混合检索方法
authors:
- Aishwarya Gunjal
- Kanchan Khemnar
- Pawan Poojary
- Pranav Kulkarni
- Raviraj Joshi
- Manish Khodaskar
affiliations:
- Pune Institute of Computer Technology, Pune, India
- L3Cube Labs, Pune, India
arxiv_id: '2611.26514'
url: https://arxiv.org/abs/2611.26514
pdf_url: https://arxiv.org/pdf/2611.26514
published: '2026-11-19'
collected: '2026-11-21'
category: RecSys
direction: 双语垂直搜索 · 混合召回优化
tags:
- Hybrid_Retrieval
- BM25
- Sentence_Embedding
- Multilingual_Search
- MRR
one_liner: 提出融合BM25与句嵌入的双语混合检索方案，验证垂直领域多语言检索的性能增益
practical_value: '- 垂直领域小语种搜索场景可优先用BM25搭建强基线，再叠加领域适配的句嵌入做等权分数融合，低成本获取精度增益

  - 多语言检索场景优先选择适配目标语种的预训练Embedding模型，可避免跨语种语义漂移，获得更高性能增益

  - 若业务核心指标为召回率，强BM25基线已能满足绝大多数需求，无需额外叠加语义检索的工程与算力成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
政务方案检索存在两类核心痛点：一是公民口语化查询与官方行政术语存在词汇 mismatch，二是多语言场景下用户查询与官方文档的语义对齐难度高，纯词汇匹配或纯语义检索均无法兼顾效果。
### 方法关键点
1. 构建英语-马拉地语对齐的政务方案索引，支持多语言检索、马拉地语优先、翻译中介三类检索配置；
2. 采用等权分数融合的混合检索策略，结合BM25的词汇匹配能力与领域预训练句嵌入的语义匹配能力。
### 关键结果数字
人工标注双语查询数据集上，BM25基线MRR达0.864、召回率0.946；融合MahaSBERT的混合检索MRR提升至0.879，精度从0.781提升至0.808，召回率与BM25持平；纯语义检索MRR仅约0.65，远低于基线。
