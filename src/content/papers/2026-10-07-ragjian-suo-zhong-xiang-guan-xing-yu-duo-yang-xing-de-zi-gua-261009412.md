---
title: 'Finding the Right Balance: Relevance and Diversity in LLM Retrieval'
title_zh: RAG检索中相关性与多样性的自适应平衡方法
authors:
- Guillaume Brouillette
- Faustin Kagabo
- Usef Faghihi
- Nadia Ghazzali
affiliations:
- Université du Québec à Trois-Rivières
- Laboratoire d'intelligence artificielle appliquée (LI2A)
- INSTINT
arxiv_id: '2610.09412'
url: https://arxiv.org/abs/2610.09412
pdf_url: https://arxiv.org/pdf/2610.09412
published: '2026-10-07'
collected: '2026-10-08'
category: RAG
direction: RAG检索优化 · 相关性多样性平衡
tags:
- RAG
- Retrieval Diversification
- Re-ranking
- MMR
- Embedding
- Nearest Neighbor
one_liner: 设计自适应检索多样化决策规则与RNG-Score重排器，兼顾RAG检索相关性与多样性
practical_value: '- 业务RAG系统不要默认开启MMR等多样化功能：先统计候选池近重复对占比，低于0.0012时直接用k-NN即可，避免相关性损失，该阈值适配BGE、Qwen等主流编码器

  - 可复用自适应触发逻辑：用现有embedding计算top-k检索结果的Vendi score，当该值低于query所需证据数（如多跳问答设为2，单知识问答设为1）时才触发多样化，单query计算耗时仅20μs，无额外标注需求可直接上线

  - RNG-Score可替代MMR作为多样化重排器：其参数可在两端完全回退到k-NN，最坏场景下比k-NN掉点不超过4个S-Recall点，远低于MMR的最大30点损失，适合冗余度不稳定的业务场景灰度上线

  - 电商推荐/搜索场景可复用该逻辑：当召回候选池重复款/相似款占比高时才触发多样性重排，否则优先保证相关性，平衡用户个性化需求与探索需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG框架普遍内置MMR等检索多样化能力，但现有研究对其效果结论分歧极大，核心原因是未考虑候选池冗余度和查询的证据需求差异：盲目开启多样化会浪费LLM上下文窗口、降低检索相关性，业务场景缺乏无标注的低成本判断方法明确何时该启用多样化。
### 方法关键点
- 设计PoolRedundancy指标：基于已有embedding统计候选池内余弦相似度>0.95的近重复对占比，量化冗余度，无需标注
- 单query有效文档数T(q)：取k-NN检索结果embedding的Vendi score，衡量top-k中实际包含的语义不同文档数量，单query耗时仅20μs
- 自适应决策规则：仅当T(q)低于查询所需证据数h时触发多样化，否则直接返回k-NN结果，单证据查询自动禁用多样化，跨数据集、编码器无需重新调优
- RNG-Score几何重排器：基于相对邻域图构造，参数γ在正负极端可完全回退到k-NN，调参风险低，单query重排耗时仅230μs
### 关键实验
在HotpotQA、BEIR等主流基准上对比k-NN、MMR、DPP等基线：
- 干净候选池（冗余度<0.0012）下，MMR等固定多样化方法最多损失33个S-Recall@5点，RNG-Score波动不超过±0.2点
- 冗余度超过0.0012交叉阈值时，固定多样化方法最高较k-NN提升22个S-Recall@5点
- 自适应决策规则覆盖90%以上的可实现增益
### 核心结论
RAG检索不要盲目开启多样化，仅当候选池冗余度超过阈值或top-k有效文档数低于查询所需证据数时启用，否则会严重损害相关性
