---
title: 'Filtered Vector Search in a Disaggregated Lakehouse: Composing Table-Format
  Pruning with Per-File ANN'
title_zh: 存算分离湖仓下的过滤向量搜索：表剪枝与单文件ANN结合
authors:
- Rakesh Jain
- Thomas Griffin
- Syed Zawad
affiliations:
- IBM Research
arxiv_id: '2608.05441'
url: https://arxiv.org/abs/2608.05441
pdf_url: https://arxiv.org/pdf/2608.05441
published: '2026-08-05'
collected: '2026-08-07'
category: RAG
direction: RAG底层 · 湖仓原生向量检索
tags:
- Vector Search
- ANN
- Lakehouse
- Apache Iceberg
- Parquet
- RAG
one_liner: 复用湖仓原生文件剪枝与Parquet嵌入IVF索引，无需独立向量库实现高性能带过滤向量搜索
practical_value: '- 电商/生成式推荐场景可直接将商品/用户向量的IVF索引嵌入现有Iceberg/Parquet数仓，无需搭建独立向量库，避免数据多副本、权限不同步的运维成本

  - 带结构化过滤的向量召回（如限定品类、价格段、地域的语义搜索）可复用数仓原生的分区剪枝、zone map、bitmap索引，先剪去无关文件再跑ANN，大幅降低计算量

  - 存算分离架构下的向量检索工程优化：用rendezvous哈希做文件到计算节点的路由，搭配文件级索引+向量矩阵缓存，避免扩缩容导致的缓存失效，暖查询性能可提数十倍

  - 跨表过滤的向量查询可先做半连接reduction下推过滤条件，高频过滤维度可反规范化到向量表做分区，实测最多可提近百倍性能'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前RAG、语义搜索、生成式推荐均依赖带结构化过滤条件的向量检索，主流方案需将向量从湖仓复制到独立向量库，存在数据多副本、与源表不同步、需重复开发过滤逻辑、权限需二次配置的问题，而湖仓本身已具备成熟的文件剪枝能力，此前未被有效复用至向量检索场景。
### 方法关键点
- 把IVF向量索引嵌入每个Parquet文件页脚，分布式并行构建，仅修改Iceberg表元数据，不影响原有Parquet文件的多引擎读取兼容性
- 查询时先通过湖仓原生的分区剪枝、zone map、bitmap索引过滤不符合条件的文件，仅对剩余文件执行单文件ANN，融合搜索与列投影逻辑，无需二次扫描数据
- 仅对分区/物化聚簇这类“文件纯”列做谓词下推到ANN层，排除SORT/ZORDER列，避免边界数据错误
- 用rendezvous哈希做文件到计算节点的稳定路由，搭配文件级的索引+向量矩阵缓存，解决存算分离下的对象存储读延迟和扩缩容缓存失效问题
### 关键结果
在11.5M×768的向量表上，暖查询下带过滤的ANN比暴力搜索快32倍，recall@10≥0.9；在5M真实IBM Granite嵌入数据集上，将跨连接的过滤维度反规范化到向量表做分区后，查询延迟从14.7s降至157ms，提速约94倍；方案全程无需拷贝数据，自动继承湖仓原有权限控制能力。
### 核心结论
带过滤的向量搜索性能核心不是更复杂的ANN算法，而是过滤列的文件级局部性，复用湖仓已有的存储优化能力远比重构一套独立向量系统性价比高
