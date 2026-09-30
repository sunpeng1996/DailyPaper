---
title: 'Generated Query Expansion Still Helps Strong Sparse Retrieval: A Controlled
  Study with SPLADE-v3'
title_zh: 生成式查询扩展对强稀疏检索仍有效：基于SPLADE-v3的对照研究
authors:
- Ryan C. Barron
- Cade W. Trotter
- Maksim E. Eren
- Kim Ø. Rasmussen
- Liz D. Miller
- Benjamin J. Migliori
affiliations:
- Los Alamos National Laboratory
arxiv_id: '2609.37911'
url: https://arxiv.org/abs/2609.37911
pdf_url: https://arxiv.org/pdf/2609.37911
published: '2026-09-29'
collected: '2026-09-30'
category: QueryRec
direction: 查询扩展 · 稀疏检索优化
tags:
- Query Expansion
- SPLADE
- Sparse Retrieval
- LLM
- Information Retrieval
one_liner: 验证四类生成式查询扩展均可稳定提升强稀疏检索器SPLADE-v3的检索效果
practical_value: '- 电商/垂类搜索场景可复用「生成扩展内容+原始query加权融合」方案，原始query权重≥30%即可稳定获得收益，调参成本极低

  - 生成式QE无需追求生成文本通顺度，只要补充的领域词汇准确即可，可大幅降低生成侧prompt设计和内容校验成本

  - 稀疏检索场景可固定文档侧SPLADE索引，仅在query侧做扩展迭代，无需全量重建索引，工程落地成本极低

  - 不建议优先投入自建领域概念图谱做QE，同量级投入下生成式QE的收益远高于结构化概念扩展，投入产出比更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有研究普遍认为生成式查询扩展（QE）的收益会随检索器能力提升而下降，而SPLADE等强稀疏检索器本身已内置上下文词汇扩展能力，是否还能从外部生成式QE中获益尚不明确，且生成式QE的收益来源（词汇/语序/上下文）也缺乏严格对照验证。

### 方法关键点
- 固定冻结SPLADE-v3文档索引，仅修改query侧表示，所有实验组共享相同的256维稀疏向量预算，严格隔离扩展内容的真实收益
- 测试四种生成式QE方案：短关键词列表、单伪文档（Query2doc）、多伪参考文献（MuGI风格）、语料引导生成文本（CSQE），同时对比语料诱导概念图的结构化扩展方案
- 新增两类对照：生成文本打乱语序、生成文本转为非上下文词袋验证收益来源；遍历原始query权重α从0.1到0.9验证融合策略鲁棒性

### 关键结果
在NFCorpus、TREC-COVID、SciDocs三个科学检索数据集上，四种生成式QE全部提升nDCG@10，最优相对增益分别为4.81%、8.92%、9.47%，12组对比中11组统计显著；114组α参数设置中103组优于基线，所有α≥0.3的设置全部跑赢基线，生成文本打乱语序、转为词袋后仍保留90%以上收益，证明核心收益来自补充的领域词汇而非语序或上下文编码；基于语料概念图的结构化扩展无稳定显著收益，各类消融和门控策略均无法追平生成式QE效果。

**最值得记住的一句话**：生成式QE是强稀疏检索器的有效补充，只要保留至少30%的原始query权重，即可稳定获得检索收益，不需要复杂的融合策略。
