---
title: 'Embeddings vs. Grep: Rethinking the Dense Advantage in Code Search'
title_zh: 向量检索 vs 关键词检索：重新审视代码搜索中的稠密向量优势
authors:
- Siqiao Xue
- Ziyin Zhang
- Zihan Liao
- Jin Qin
- Yixiang Mu
- Hang Yu
affiliations:
- Ant Group
- Shanghai Jiao Tong University
arxiv_id: '2611.20455'
url: https://arxiv.org/abs/2611.20455
pdf_url: https://arxiv.org/pdf/2611.20455
published: '2026-11-15'
collected: '2026-11-20'
category: RAG
direction: RAG检索优化 · 稠密检索效果评估
tags:
- Code Search
- Dense Retrieval
- BM25
- Query Expansion
- Benchmark
- RAG
one_liner: 构建真实仓库级代码搜索基准，厘清稠密检索优势来源，给出检索系统优化指南
practical_value: '- 检索效果对比需设置公平基线：BM25优先采用全文档索引而非复用稠密检索的短chunk规则，提前明确定义相关文档判定标准，避免高估稠密检索的实际增益

  - 工业级检索系统优先采用稠密检索+全文件BM25的Reciprocal Rank Fusion方案，实测nDCG@10可较单路稠密检索提升0.06以上，效果优于所有动态路由方案

  - 对缺失领域关键词的模糊query，先调用LLM做Query Expansion补充相关术语/标识符，BM25效果即可追平甚至超过稠密检索，适合低频次检索场景降低向量索引运维成本

  - 代码/知识库类Agent的定位能力核心取决于基座LLM水平，检索工具选型的影响不足0.04，研发资源优先投入LLM选型与Prompt优化而非检索模块迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有代码搜索基准普遍显示稠密编码器大幅领先BM25，但工程实践中基于grep的代码Agent效果也很好，两者矛盾源于现有基准存在系统性偏差：采用人工构造query、老旧代码、给BM25配置不友好的短chunk拆分、将编辑的测试文件算为相关文档，无法真实反映工业场景的检索效果。

### 方法关键点
- 构建REPOPREMIUM真实仓库级代码搜索基准，覆盖Python/JS/TS/Go/Rust/Java 6种语言、91个仓库、2825条query，包含人工构造query和2022-2026年真实PR文本，相关标签仅统计非测试代码文件
- 控制变量对比13款稠密编码器、SPLADE、ColBERTv2和不同配置的BM25，拆解稠密检索优势的真实来源
- 测试generate-then-grep、检索融合、动态路由等优化方案的落地效果

### 关键结果
默认短chunk配置下稠密检索nDCG@10领先BM25 0.121~0.191；将BM25改为全文件索引后优势收缩到0.034~0.125；给BM25加上LLM query expansion后，其效果追平甚至超过稠密检索，在人工构造query集上领先0.081。
固定的稠密+BM25 reciprocal rank fusion比单路稠密检索nDCG@10高0.06，所有尝试的动态路由方案都无法超过固定融合效果。代码Agent场景下，更换检索工具带来的准确率波动不到0.04，远小于更换LLM带来的0.27波动。

> 最值得记住的一句话：多数场景下稠密检索的优势来自评估基准的偏差，公平对比下BM25加简单优化即可媲美稠密检索，固定融合两类检索是性价比最高的方案
