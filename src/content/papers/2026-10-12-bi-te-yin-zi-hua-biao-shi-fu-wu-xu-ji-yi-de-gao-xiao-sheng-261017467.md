---
title: 'Computed, not Memorized: Bit-Factorized Identifiers for Efficient Generative
  Retrieval'
title_zh: 比特因子化标识符：无需记忆的高效生成式检索方案
authors:
- I-Fan Lin
- Zhen Zhang
- Faegheh Hasibi
- Suzan Verberne
affiliations:
- Leiden University
- Shandong University
- Radboud University
arxiv_id: '2610.17467'
url: https://arxiv.org/abs/2610.17467
pdf_url: https://arxiv.org/pdf/2610.17467
published: '2026-10-12'
collected: '2026-10-14'
category: GenRec
direction: 生成式检索 · Semantic ID 动态适配
tags:
- Generative Retrieval
- Semantic ID
- DocID
- Dynamic Corpus
- Bit Factorization
one_liner: 提出比特因子化可计算DocID，无需重训即可适配生成式检索动态语料，兼顾效果与效率
practical_value: '- 电商搜索/商品推荐的动态SKU库可复用该DocID设计，新商品无需重新训练检索模型即可被召回，大幅降低频繁上新的模型迭代成本

  - 生成式检索的解码环节可复用多树约束束搜索优化，通过比特排列生成多个前缀树并行搜索，用极小算力开销提升未见过样本的召回率

  - 跨域/冷启动场景可复用DocID编码器与检索编码器的权重插值策略，平衡分布内效果和分布外泛化性，无需额外标注数据即可提升冷启动指标'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式检索的数值型DocID依赖训练阶段记忆绑定语义，新增文档必须全量重训或做模型编辑，泛化性差、更新成本高，无法适配电商、搜索等动态文档/商品库的业务需求。
### 方法关键点
- DocID直接从预训练编码器输出计算得到：将文档embedding经过投影、层归一化、tanh激活后取符号，得到k比特二进制码，无需索引阶段的记忆性训练，新增文档可实时生成有效DocID
- 检索阶段训练按比特加权的查询编码器，通过InfoNCE损失优化查询和文档比特向量的匹配得分，无需自回归解码器，得分可拆分为独立的token级贡献
- 采用DocID编码器与检索编码器的权重插值平衡分布内性能和分布外泛化，推理阶段将多比特分组为token、用多前缀树并行束搜索降低早期剪枝误差
### 关键实验结果
在NQ320K、TriviaQA、MS MARCO三个基准数据集上对比NCI、SEAL、MEVI等主流生成式检索方案：未见过文档的Hit@10提升20pp以上，推理 latency 比现有数值DocID方案低7×以上，仅比全量重训方案低3pp的MS MARCO效果，存储开销仅0.015KB/doc，远低于BM25、GTR等传统检索方案。
> 最值得记住的结论：生成式检索的Semantic ID设计可以从「预定义+训练记忆」转向「从语义表示直接计算」，从根源上降低动态库适配的重训成本。
