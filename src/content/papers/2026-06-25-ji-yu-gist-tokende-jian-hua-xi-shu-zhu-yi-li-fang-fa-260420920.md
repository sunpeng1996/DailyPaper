---
title: Simplified Sparse Attention via Gist Tokens
title_zh: 基于Gist Token的简化稀疏注意力方法
authors:
- Yuzhen Mao
- Michael Y. Li
- Emily B. Fox
affiliations:
- Stanford University
arxiv_id: '2604.20920'
url: https://arxiv.org/abs/2604.20920
pdf_url: https://arxiv.org/pdf/2604.20920
published: '2026-06-25'
collected: '2026-06-30'
category: LLM
direction: 长上下文LLM · 稀疏注意力优化
tags:
- Sparse Attention
- KV cache
- Long Context
- LLM
- RAG
one_liner: 无需修改模型架构，基于gist token实现长上下文高效稀疏注意力，兼顾精度与推理速度
practical_value: '- 电商RAG导购、多文档商品知识库场景，可复用gist token思路对每个文档做压缩摘要，能过滤无关文档噪声，实验显示RAG准确率比全注意力还高5.7+分，同时大幅降低KV
  cache占用

  - Agent长对话记忆场景，分层H-SSA的多级gist索引能让解码延迟保持平稳，44K上下文下相对Flash-Decoding实现最高3.37×解码加速，解决长会话卡顿问题

  - 该方案无需修改原有LLM架构，仅需对现有业务模型做继续预训练即可适配，落地改造成本远低于需要架构修改的稀疏注意力方案

  - 支持KV cache复用，预编码文档/历史对话后可重复响应多轮查询，无需重复prefill，能显著提升大模型推荐/导购服务的QPS'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文建模是LLM支撑Agent、RAG、多文档推理的核心能力，但KV缓存访问和注意力计算成本随上下文长度线性增长，现有稀疏注意力方案要么需要修改原生Transformer架构，要么仅做推理后处理的近似压缩，难以兼顾精度、效率和落地成本，因此需要一种无需架构修改、端到端可训练的稀疏注意力方案。

### 方法关键点
- 将长序列分块，每块末尾插入可学习gist token，通过注意力掩码约束强制模型将本块核心信息压缩到gist token中，全程无需修改模型结构或新增参数
- 推理时以当前解码query与各gist token的注意力点积作为分块相关性得分，仅展开top-k相关分块的原始token做注意力，实现查询自适应的稀疏计算
- 扩展出分层H-SSA方案：递归对gist分块插入高层meta-gist，推理时做从粗到细的分块选择，将单步解码复杂度降为对数级
- 仅需对原有LLM做继续预训练即可生效，可选做选择性微调进一步提升性能，训练使用标准next-token损失，无额外开销

### 关键结果
在LongBench、多文档RAG、KV缓存复用任务上实验：相同压缩比下，SSA比现有gist压缩基线高2.8~5.9个点；RAG场景下仅继续预训练的SSA就超过全注意力基线5.7个点；44K上下文下相对Flash-Decoding实现最高3.37×端到端解码加速，解码延迟几乎不随上下文增长；32×高压缩比下，分层H-SSA比单级SSA再提升1.6个点精度。

最值得记住的一句话：选择性展开过滤无关噪声，让压缩稀疏注意力在RAG场景精度反超全注意力
