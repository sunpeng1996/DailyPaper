---
title: 'RoutingTrie: Metadata Routing for Constrained Generative Retrieval'
title_zh: RoutingTrie：面向约束生成式检索的元数据路由方案
authors:
- Darshan Fofadiya
- Yang Liu
- Shuying Sun
- Kyumin Park
- Juhana Kangaspunta
affiliations:
- Shopify
arxiv_id: '2611.11016'
url: https://arxiv.org/abs/2611.11016
pdf_url: https://arxiv.org/pdf/2611.11016
published: '2026-11-07'
collected: '2026-11-10'
category: GenRec
direction: 生成式推荐 · SID约束解码
tags:
- Generative Retrieval
- Semantic ID
- Trie
- Metadata Filtering
- Beam Search
one_liner: 在生成式检索SID解码阶段前置元数据约束过滤，大幅提升召回率仅增加1.1ms延迟
practical_value: '- 可直接复用「元数据约束前置到beam selection前」的设计思路，替代现有生成后过滤的方案，解决电商场景多属性（库存、地域、店铺）过滤时beam容量浪费的问题，大幅提升符合约束的商品召回率

  - 分字段选择索引的方案可直接落地：低基数高密字段（如是否在售、国家）用Dense Bitset，高基数稀疏字段（如店铺ID、类目ID）用Sparse List，配套的存储成本计算公式可直接用来优化现有过滤索引的存储和查询效率

  - GPU端Triton实现多字段并行probe的工程方案可复用，probe延迟几乎不随beam宽度和字段基数上涨，适合生成式检索工业落地时控制端到端延迟

  - 可复用开源ShopTrie合成基准测试集，覆盖不同元数据分布的测试场景，快速验证生成式检索约束过滤方案的性能'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID（SID）的生成式检索系统，仅靠SID trie保证生成ID合法性，元数据约束（如地域、库存、店铺归属）全部放在SID生成后过滤，既浪费计算资源，还会占用有限的beam容量导致符合约束的item被提前剪枝，召回率偏低，难以满足工业场景多约束检索需求。

### 方法关键点
- 共享SID trie+分字段元数据索引架构：离线阶段从trie叶子向上聚合每个边下的所有元数据取值，为每个字段单独构建索引，无需修改原SID trie结构
- 双索引适配不同字段分布：低基数高值密度字段（如是否在售、国家）用Dense Bitset，去重存储重复bitset行，O(1)时间完成probe；高基数低值密度字段（如店铺ID、类目ID）用Sparse List，仅存储每个边下实际存在的排序取值数组，通过二分查找完成probe
- 推导存储成本计算公式，可自动为每个字段选择最优索引类型；在线解码阶段，多字段并行probe结果按查询的布尔逻辑合并为掩码，在beam selection前剪掉不可能满足约束的前缀，节省beam容量

### 关键实验
- 自研ShopTrie合成基准测试：覆盖基数从2到2M的8类典型元数据字段，GPU probe总延迟仅0.08ms左右，比CPU快1.3~14.5倍，且延迟几乎不随beam宽度变化
- 电商生产回放测试：对比生成后过滤的baseline，Hit@100从67.5%提升到96.1%，涨幅28.6个百分点，端到端延迟仅增加1.1ms

### 核心结论
生成式检索的元数据约束完全可以前置到解码阶段，以极微的延迟和存储成本换召回率的大幅提升，无需改动上游模型。
