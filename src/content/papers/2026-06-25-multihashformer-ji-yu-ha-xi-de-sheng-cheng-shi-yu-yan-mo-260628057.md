---
title: 'MultiHashFormer: Hash-based Generative Language Models'
title_zh: MultiHashFormer：基于哈希的生成式语言模型
authors:
- Huiyin Xue
- Atsuki Yamaguchi
- Nikolaos Aletras
affiliations:
- University of Sheffield
arxiv_id: '2606.28057'
url: https://arxiv.org/abs/2606.28057
pdf_url: https://arxiv.org/pdf/2606.28057
published: '2026-06-25'
collected: '2026-06-30'
category: LLM
direction: LLM 结构优化 · 参数效率
tags:
- parameter efficiency
- hashing
- autoregressive LM
- multilingual NLP
- large language model
one_liner: 通过多独立哈希生成唯一token签名，解决因果LM哈希冲突，实现参数固定的词表扩展
practical_value: '- 电商推荐场景扩展长尾商品词、新类目词、多语言词表时，可复用该方案固定 embedding 总参数量，避免词表增大带来的线性参数膨胀，降低显存开销

  - 做生成式任务（如query推荐、商品文案生成）时，该多哈希签名方案解决了传统哈希压缩的冲突问题，可用于自回归生成场景的参数压缩

  - 跨境多语言电商场景，新增小语种词表无需修改模型结构、全量重训，直接复用原有参数承载新词表，降低迭代成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
传统大语言模型的token embedding矩阵参数随词表规模线性增长，会带来词表瓶颈，无法灵活适配新领域、新语言；传统基于哈希的词表示用多对一映射压缩参数，虽能节省参数，但哈希冲突问题导致其仅能用于encoder-only模型，无法适配因果自回归的生成式语言模型。

### 方法关键点
设计MultiHashFormer框架，每个token通过多个独立哈希函数生成唯一的离散哈希ID序列（哈希签名），通过Hash Encoder压缩为单个隐向量输入Transformer decoder；生成阶段由Hash Decoder预测下一个token的哈希签名，再映射回原文本token，从根本上避免多对一哈希冲突，支持自回归生成同时保持固定参数规模。

### 关键结果
在100M、1B、3B三个参数量级下，多个基准测试性能均超过标准Transformer LMs；多语言场景中，可在不修改模型、不增加参数的前提下支持词表扩展。
