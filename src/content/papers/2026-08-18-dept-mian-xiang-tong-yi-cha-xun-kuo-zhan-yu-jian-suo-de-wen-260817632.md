---
title: 'DEPT: Document Embedding Preservation Tuning for Unified Query Expansion and
  Retrieval'
title_zh: DEPT：面向统一查询扩展与检索的文档嵌入保持微调
authors:
- Jingyuan Wang
- Richong Zhang
- Zhijie Nie
- Mingxin Li
- Yanzhao Zhang
affiliations:
- Beihang University
arxiv_id: '2608.17632'
url: https://arxiv.org/abs/2608.17632
pdf_url: https://arxiv.org/pdf/2608.17632
published: '2026-08-18'
collected: '2026-08-19'
category: QueryRec
direction: 查询扩展与检索 · LLM端到端统一优化
tags:
- Query Expansion
- Dense Retrieval
- LoRA
- Contrastive Learning
- LLM Fine-tuning
one_liner: 提出文档嵌入保持微调方案，实现单LLM端到端统一查询扩展与检索，兼容已有文档索引
practical_value: '- 电商搜索Query扩写场景可复用DEPT不对称微调思路：固定商品侧嵌入仅优化Query侧，避免每次模型迭代需重算全量商品向量的极高成本

  - LLM统一做生成+检索的场景，可复用straight-through梯度回传方案，让检索损失直接优化扩写内容，无需分阶段训练两个模块，降本提效

  - 嵌入各向异性问题可直接复用「预计算固定白化变换+嵌入保持正则」组合，无需额外后处理，还可兼容现有向量索引，适配已有检索架构

  - 训练阶段的在线难负例采样可复用固定预建索引方案，无需每次迭代更新索引，大幅降低训练算力开销'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Query扩展与稠密检索通常分模块、分阶段优化，扩写模块的生成效果与最终检索损失没有直接对齐；若用单LLM统一承担两个任务，普通对比学习会同时改变Query和文档侧嵌入，导致检索目标漂移、扩写质量下降，还会让原有文档索引失效，大语料场景下重训后重索引成本极高。

### 方法关键点
- 采用不对称微调设计，新增文档嵌入保持（DEP）损失，约束微调后文档嵌入与初始预计算缓存嵌入的余弦距离，避免文档侧嵌入漂移，兼容原有索引
- 预计算初始文档嵌入的固定白化变换，解决LLM嵌入各向异性问题，配合DEP损失保证变换在微调全程有效
- 用straight-through梯度回传机制，让检索损失可直接回传到扩写生成的token，实现端到端优化，无需切断生成与检索的梯度路径
- 基于固定缓存文档索引做在线难负例采样，无需每次训练迭代更新索引，大幅降低训练算力消耗

### 关键实验
在BEIR基准的5个检索数据集上，采用Qwen3-4B-Instruct、LLaMA-3.2-3B-Instruct两个backbone，对比Query2Doc、HyDE、ExpandR、UniRAG等基线：DEPT在Qwen3上平均nDCG@10达42.59，较最优基线ExpandR高1.5个点；短扩写版本DEPT-K仅用平均9个生成token，平均nDCG@10达41.45，也超过所有基线；微调后模型通用生成能力仅下降1.28个百分点，远好于普通对比学习68个百分点的下降幅度，原有缓存索引的检索效果仅比重新编码低0.64个点，几乎无损失。

最值得记住的一句话：统一生成与检索的LLM微调，最优策略是激进优化Query侧行为，同时尽可能保持文档侧嵌入可复用。
