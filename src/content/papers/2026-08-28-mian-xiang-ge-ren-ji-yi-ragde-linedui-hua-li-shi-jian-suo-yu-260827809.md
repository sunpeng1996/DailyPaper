---
title: 'LINE Conversation History Retrieval for Personal Memory RAG: Evaluating Search
  Representations and Hybrid Retrieval'
title_zh: 面向个人记忆RAG的LINE对话历史检索：搜索表示与混合检索评估
authors:
- Akito Hattori
affiliations:
- Independent Researcher, Tokyo, Japan
arxiv_id: '2608.27809'
url: https://arxiv.org/abs/2608.27809
pdf_url: https://arxiv.org/pdf/2608.27809
published: '2026-08-28'
collected: '2026-08-31'
category: RAG
direction: 个人记忆RAG · 对话历史检索优化
tags:
- RAG
- Hybrid Retrieval
- Personal Memory
- BM25
- Dense Retrieval
- Conversational Search
one_liner: 基于单用户36万条LINE对话数据，对比搜索表示与混合检索方案，优化个人记忆RAG的检索性能
practical_value: '- 构建对话类检索索引时可采用「摘要+原文片段」的embedding_text表示，兼顾语义匹配与精确词汇匹配，单BM25检索就能比原始文本BM25提升约15%的Recall@5

  - 混合检索可采用BM25与向量检索的线性加权组合，权重β=0.4~0.5区间在对话场景下表现最优，比单检索器提升约11%的Recall@5

  - 针对跨多段对话的聚合类查询，平铺开块检索性能下降明显，可后续叠加query分解、多跳检索、分层时序记忆索引优化

  - 处理短对话/聊天记录类文本时，分块可采用180分钟会话间隔切分+滑动窗口（窗口42条，步长36条）的策略，保留上下文连贯性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM默认无法感知用户个人历史对话，难以提供基于过往经历的个性化服务；而LINE这类即时通讯对话多为短语句、碎片化、强依赖上下文，直接检索的词汇匹配度低，是个人记忆RAG落地的核心瓶颈。

### 方法关键点
- 数据分块：将35.8万条单用户LINE消息按180分钟间隔切分会话，再用42条消息窗口、36条步长滑动分块，得到2.2万个时序连贯的检索单元
- 搜索表示：对比三类方案：raw_text（原始对话转录）、summary（GPT-4o-mini生成的对话摘要）、embedding_text（固定前缀+摘要+前4000字原文片段组合）
- 检索策略：对比BM25稀疏检索、text-embedding-3-small稠密检索，以及两者的线性混合检索，遍历6种检索器组合、21组权重β

### 关键结果
- 单检索器中embedding_text_bm25最优，Recall@5=0.584，比raw_text_bm25提升0.157
- 最优混合方案为embedding_text_bm25 + embedding_text_vector，β=0.45时Recall@5=0.697，较最优单检索器提升0.113，MRR@5=0.595，nDCG@5=0.575
- 聚合类查询（需跨多段对话整合信息）的Recall@5仅0.345，远低于命名实体类（0.789）和上下文类（0.755）

### 核心结论
对话类检索场景下，「语义摘要+原文片段」的组合表示搭配BM25+稠密向量的中等权重混合检索，可实现远超单一方案的检索性能；跨会话聚合类查询需额外叠加分层记忆或多跳检索优化
