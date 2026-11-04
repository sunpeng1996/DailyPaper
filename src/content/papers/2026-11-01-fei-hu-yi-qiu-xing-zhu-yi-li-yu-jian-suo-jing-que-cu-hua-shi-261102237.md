---
title: 'Nonreciprocal Spherical Attention and Retrieval: Sharp Coarsening Clocks and
  Certified Score Correction'
title_zh: 非互易球形注意力与检索：精确粗化时钟与可证分数校正
authors:
- Faruk Alpay
- Taylan Alpay
affiliations:
- Bahçeşehir University
- University of Turkish Aeronautical Association
arxiv_id: '2611.02237'
url: https://arxiv.org/abs/2611.02237
pdf_url: https://arxiv.org/pdf/2611.02237
published: '2026-11-01'
collected: '2026-11-04'
category: Other
direction: 向量检索优化 · 可证量化校正
tags:
- Dense Retrieval
- Product Quantization
- Score Calibration
- Attention Compression
- Theoretical Guarantee
one_liner: 提出非互易球形注意力框架，给出压缩检索的可证分数校正方法与理论性能保证
practical_value: '- 电商向量召回的PQ压缩场景可复用本文的边际校准技巧，仅新增KB级存储开销、几乎不增加查询延迟，即可小幅提升召回率，适配百亿级向量库降本需求

  - 可借鉴本文的质量中心化聚合方法优化KV cache或粗召回聚类误差，抵消一阶压缩误差仅保留二阶误差，大幅降低压缩带来的精度损失

  - 本文的凸优化分数校正框架可直接复用到语义检索/商品搜索的query侧适配，无需改动现有向量索引结构，仅新增极轻量的query变换逻辑'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前密集向量检索的压缩方案普遍缺乏严格的理论误差保证，非对称校正易出现病态性问题，同时注意力聚类的表示塌陷会损伤检索精度，亟需兼顾理论可证性和实际性能的压缩校正方案。
### 方法关键点
- 非互易球形注意力流模型，推导得到双簇亚稳态指数和二阶注意力压缩误差界，通过质量中心化抵消一阶压缩误差
- 严格凸的斜分数校准问题，给出唯一矩阵正规方程和残差优化误差界，仅需存储矩量即可完成校正，无需存储全量查询-文档分数矩阵
- 低秩实现采用实Schur分解保留最大斜奇异值对，不改动现有PQ/IVF-PQ索引结构，仅新增极轻量的query侧变换，存储开销可通过缩小PQ码本完全抵消
### 关键结果
- SciFact语义检索数据集上，同字节预算下斜校正相比PQ64基线nDCG@10提升0.0086；SIFT1M数据集上，PQ+斜校正Hit@10提升0.0031，OPQ+斜校正Hit@10提升0.0081
- 1000万向量BIGANN数据集上，IVF-PQ索引在0.1794ms/query的延迟下达到0.8827的Hit@10，存储仅为原始float32向量的1/20
- 质量中心化聚合相比原始粗中心，1000万键注意力记忆的输出误差最大降低96%

最值得记住的结论：不存在通用的非对称检索方向优势，严格的误差证书比孤立的精度提升更能保障业务稳定性。
