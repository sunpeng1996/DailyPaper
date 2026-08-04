---
title: Do Static Embeddings Add Value to Hybrid Dutch Retrieval?
title_zh: 静态嵌入对荷兰语混合检索是否存在增量价值？
authors:
- António Pereira Barata
arxiv_id: '2608.02112'
url: https://arxiv.org/abs/2608.02112
pdf_url: https://arxiv.org/pdf/2608.02112
published: '2026-08-03'
collected: '2026-08-04'
category: RecSys
direction: 混合检索 · RRF融合策略评估
tags:
- Hybrid Retrieval
- RRF
- BM25
- Dense Embedding
- Static Embedding
- MTEB
one_liner: 通过荷兰语MTEB基准对照实验，证明静态嵌入无法为BM25+Transformer混合检索架构带来额外增益
practical_value: '- 混合检索/召回架构设计优先验证组件边际增益，不要仅凭单模型Benchmark性能新增组件，避免无效提升复杂度和成本

  - 无领域调优数据时，BM25与Transformer稠密检索的等权RRF是鲁棒默认配置，跨5类数据集转移效果优于最优单检索器，MRR平均高0.059

  - 小语种/垂类检索场景可复用10折交叉验证选权重+留一数据集跨域验证的评估范式，避免过拟合到单分布数据

  - 电商搜索/商品召回场景可参考全库全量query-doc打分方法，避免top-k截断带来的评估偏差，准确度量多路召回的互补性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有嵌入基准仅评估单模型standalone性能，无法衡量低开销检索器在已融合词汇检索+Transformer语义检索的混合架构中的边际互补价值，静态嵌入虽推理成本低，但缺乏在成熟混合架构中增量价值的严格验证，小语种场景相关结论更是空白。

### 方法关键点
- 采用加权RRF融合BM25、Qwen3-Embedding-0.6B、两款多语言静态嵌入的排序结果，权重以0.1步长在单纯形空间遍历搜索
- 执行10折query级交叉验证，仅用9折数据选权重，剩余1折做持出评估，通过配对自助法置信区间、符号随机检验量化性能差异的显著性
- 新增留一数据集跨域转移测试，验证融合权重的跨领域通用性
- 全库全量计算query-doc打分，避免top-k截断引入评估混淆变量

### 关键结果
在MTEB-NL的5个荷兰语检索数据集（共1.45万query、78.6万doc）上测试：
- 交叉验证选出的BM25+Qwen融合方案比同训练集选出的最优单检索器MRR最高提升0.061（荷兰新闻数据集），4个数据集有显著正向收益
- 所有50次折级权重选择均未给静态嵌入分配正权重，强制加入静态嵌入会使MRR下降0.01~0.036
- 跨域转移场景下，等权BM25+Qwen配置在所有5个数据集上都优于跨域选出的最优单检索器，macro平均MRR高0.059

**最值得记住的结论**：单模型基准表现好不等于在混合架构中有边际增益，引入新检索组件必须做严格的持出边际价值验证，不能仅凭直觉堆叠模块。
