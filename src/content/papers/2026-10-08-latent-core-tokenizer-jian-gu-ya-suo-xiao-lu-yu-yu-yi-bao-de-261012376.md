---
title: 'Latent Core Tokenizer: Compress, but Meaningfully'
title_zh: Latent Core Tokenizer：兼顾压缩效率与语义保留的无语言依赖分词器
authors:
- Felermino D. M. A. Ali
- Millicent Ochieng
- Ogbemi Ekwejunor-Etchie
- Ade Famoti
- Jacki O'Neill
- Debjit Paul
affiliations:
- Microsoft Research Africa
- Microsoft Research Accelerator
- Microsoft Research India
arxiv_id: '2610.12376'
url: https://arxiv.org/abs/2610.12376
pdf_url: https://arxiv.org/pdf/2610.12376
published: '2026-10-08'
collected: '2026-10-09'
category: LLM
direction: LLM多语言分词 · 词表压缩优化
tags:
- Tokenizer
- Multilingual
- BPE
- VocabularyCompression
- Morphology
one_liner: 拆分结构发现与词表构建流程，104语言下分词效率与下游效果全面优于BPE等基线
practical_value: '- 跨语种电商/广告语义理解场景可复用LCT的语言频率加权策略，缓解小语种分词效果差的问题，提升多语种召回/排序的小语种表现

  - 业务若需优化LLM推理序列长度（如多轮Agent会话、长商品描述理解），可参考LCT低fertility分词逻辑，降低KV cache开销，提升推理速度

  - 做Semantic ID生成、商品标题/query语义单元拆分时，可借鉴MDL+分支熵+形态约束的结构发现方法，得到更贴合语义的切分单元'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有主流分词器（BPE、Unigram等）以压缩率为核心优化目标，多语言场景下会天然偏向高资源语言，且分词单元与语义/词法结构脱节，压缩率高不代表下游任务表现好，亟需兼顾压缩效率与语义保留的分词方案。

### 方法关键点
- 拆分latent结构发现与表层词表构建两个独立阶段，挖掘到的结构单元不直接作为最终输出分词
- 先对各语言词频做加权平衡，避免高资源语言主导词表分配；再通过Minimum Description Length（MDL）、分支熵、形态约束三阶段无监督挖掘可复用的语义/词法结构单元
- 表层词表构建阶段按合并收益高低选择性合并latent单元，填满指定词表预算，同时支持UTF-8字节fallback保证编码可逆

### 关键结果
实验在104语言、200K词表规模下开展，对比BPE、Unigram、Parity-Aware BPE三类基线：
- 内在指标：fertility低至1.999（比BPE低10.8%），MorphScore F1达0.5209（比BPE高18.1%），跨语言分词成本基尼系数与BPE持平
- 下游指标：在XNLI、Belebele等4个多语言基准上，总分比BPE高1.48，比Unigram高1.83，比Parity-Aware BPE高2.00

### 核心结论
压缩率不是分词器选择的唯一标准，兼顾语义结构保留的分词设计能在不增加推理成本的前提下显著提升下游任务效果。
