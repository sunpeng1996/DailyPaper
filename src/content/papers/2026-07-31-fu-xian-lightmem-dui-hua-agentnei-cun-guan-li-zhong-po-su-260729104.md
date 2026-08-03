---
title: 'Reproducing LightMem: Naive RAG Is Just as Good for Memory Management'
title_zh: 复现LightMem：对话Agent内存管理中朴素RAG效果相当
authors:
- Yongjie Zhou
- Shuai Wang
- Bevan Koopman
- Guido Zuccon
affiliations:
- The University of Queensland
- CSIRO
- Google
arxiv_id: '2607.29104'
url: https://arxiv.org/abs/2607.29104
pdf_url: https://arxiv.org/pdf/2607.29104
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: Agent长时内存管理 · RAG方案对比
tags:
- LLM Agent
- Memory Management
- RAG
- LightMem
- Conversational Retrieval
one_liner: 复现对话Agent轻量内存方案LightMem，验证朴素RAG多数场景效果相当，仅紧token预算下LightMem占优
practical_value: '- 电商导购/客服Agent选型优先选朴素RAG直接检索原始对话，避免额外内存构造开销与信息损失，仅token预算极紧张时再考虑结构化内存方案

  - Agent内存系统优化不要盲目迷信复杂构造方案，优先迭代retriever：同内存库下换retriever可带来58.1%到75.5%的准确率波动，大尺寸Dense
  Embedding（如Qwen3-Embedding-4B）效果最优

  - 若必须用结构化内存压缩token，需做成本收益核算：LightMem的预构造开销需约321次问答才能抵消，仅适合长周期固定用户的会话场景

  - 结构化内存场景下混合检索（BM25+Dense）无增益，无需额外开发，直接用强Dense retriever即可'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长时对话Agent需复用历史交互信息，现有结构化内存方案（如LightMem）宣称轻量高效，但此前仅用单一retriever评估，内存构造是否损失信息、对比直接检索原始对话的朴素RAG是否有真实优势尚不明确，亟需可复现的对比验证。

### 方法关键点
- 复现LightMem完整流水线：包含LLMLingua-2 token压缩、主题分组、批处理LLM构造结构化内存、离线更新4个阶段，测试3组官方配置
- 固定内存库测试11种retriever：覆盖稀疏（BM25、SPLADE-v3）、稠密（all-MiniLM-L6-v2、Qwen3-Embedding系列等）、混合三类
- 两组对照实验：匹配检索深度（top-3/5/10）、匹配回答token预算（约330/500/935 tok/q），对比LightMem与朴素RAG效果
- 增加Oracle评测，分离检索误差与内存构造的信息损失

### 关键结果
数据集采用LongMemEval-S的444个长时对话问答，生成模型用Qwen3-30B，评测用GPT-5.5 Judge。核心结果：①同内存库下换retriever可让LightMem准确率从58.1%升至75.5%，retriever是核心影响因子；②匹配检索深度时，朴素RAG平均准确率比LightMem高2.4~4.8个点；③匹配紧token预算（330 tok/q）时LightMem平均领先5.5个点，预算放宽到935 tok/q时朴素RAG反超0.9个点；④Oracle评测显示内存构造损失11.3个点的准确率，构造开销需约321次问答才能抵消。

**最值得记住的一句话**：复杂的结构化内存方案没有通用优势，其价值完全取决于retriever选型和可用token预算，多数场景下朴素RAG是更具性价比的选择。
