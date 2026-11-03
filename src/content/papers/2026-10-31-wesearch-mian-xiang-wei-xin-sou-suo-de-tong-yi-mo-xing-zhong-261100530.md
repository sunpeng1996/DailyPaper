---
title: 'WeSearch: A Unified Model-Centric Retrieval Framework for WeChat Search'
title_zh: WeSearch：面向微信搜索的统一模型中心检索框架
authors:
- Kepu Zhang
- Yuzhe Cai
- Yue Shu
- Dawei Chen
- Jinhai Zhu
- Yuan Xu
- Zehua Dai
- Tongke Ni
- Ziyao Chen
- Chen Fu
affiliations:
- Tencent Inc. WeChat Search Group
arxiv_id: '2611.00530'
url: https://arxiv.org/abs/2611.00530
pdf_url: https://arxiv.org/pdf/2611.00530
published: '2026-10-31'
collected: '2026-11-03'
category: RecSys
direction: 工业级搜索 · 模型中心检索框架
tags:
- Semantic Retrieval
- Clustering
- OPQ
- Generative Retrieval
- Industrial Deployment
one_liner: 提出无固定层级Semantic ID的两阶段集群约束检索框架，落地微信搜索全流量
practical_value: '- 针对多主题商品/内容的检索场景，无需强行适配固定层级Semantic ID的生成式检索方案，可直接复用「集群召回+原子文档细粒度排序」的两阶段架构，规避早期解码错误、单语义路径适配性差的问题

  - 工程侧大库召回可直接复用OPQ量化+ADC加速的组合方案，在百亿级语料下既能大幅压缩内存占用，又能保证语义排序精度，同时降低检索 latency

  - 训练侧可复用多源正样本（标注/满意度/行为）+ 分级难负样本的采样策略，配合「集群覆盖损失+文档排序损失+pairwise损失」的联合训练目标，兼顾召回率和排序精度

  - 增量内容更新可采用滚动挂载方案：新文档直接匹配现有集群、复用现有量化码本，无需全量重建索引，大幅提升新品/新内容的上架效率'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式检索依赖固定层级Semantic ID，假设单文档仅对应一条语义路径，完全不适配多主题图文/内容类语料，且早期解码错误会导致相关文档被永久过滤；同时工业级搜索通常维护多路稀疏+稠密检索并行，存在计算冗余、资源成本高、模型迭代效率低的痛点，急需统一的语义检索架构同时兼顾效果、效率和迭代速度。

### 方法关键点
- 两阶段检索架构：第一阶段召回Top N相关集群，取集群内文档并集作为候选集，不要求集群语义完全同质，优先保证召回率；第二阶段先通过OPQ量化+ADC加速做粗排，再融合文档质量、用户行为、时序特征做细粒度FFN排序，兼顾精度和效率
- 训练策略：采用集群覆盖损失+文档排序损失+pairwise margin损失的联合训练目标，正样本融合人工标注、用户满意度、深度行为三类信号，负样本采用跨relevance等级、曝光未点击、检索高评分负例三类难负样本
- 工程优化：支持新文档滚动挂载（无需全量重建索引），模型+索引按版本原子更新，支持周级/按需日级模型迭代，配合vLLM加速query编码、分布式训练优化降低算力成本

### 关键结果
在微信搜索的亿级到百亿级语料上测试，对比原生产多路检索基线：1个月全流量A/B测试获CTR+0.68%、人均文章点击+2.27%、检索资源成本降低41%、图文检索latency降低19ms，目前已全量上线服务100%流量；对比固定Semantic ID的生成式检索，召回率显著更高，适配性更强。

### 核心结论
面向多主题内容的大规模工业检索，无需强求文档绑定固定层级Semantic ID，集群候选裁剪+原子文档细粒度排序的方案，在效果、成本、迭代效率上综合优势更突出。
