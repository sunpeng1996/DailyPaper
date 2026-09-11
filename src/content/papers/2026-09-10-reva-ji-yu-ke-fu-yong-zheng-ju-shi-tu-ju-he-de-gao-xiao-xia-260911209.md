---
title: 'REVA: Reusable Evidence View Aggregation for Context-Efficient RAG Serving'
title_zh: REVA：基于可复用证据视图聚合的高效RAG上下文压缩框架
authors:
- Tuan Nguyen
- Qiran Hu
- Banruo Liu
- Khoa D. Doan
- Kok-Seng Wong
- Fan Lai
affiliations:
- VinUniversity
- University of Illinois Urbana-Champaign
- VinUni-Illinois Smart Health Center
arxiv_id: '2609.11209'
url: https://arxiv.org/abs/2609.11209
pdf_url: https://arxiv.org/pdf/2609.11209
published: '2026-09-10'
collected: '2026-09-11'
category: RAG
direction: RAG服务优化 · 上下文压缩
tags:
- RAG
- Context Compression
- Attention Mining
- LLM Serving
- Prompt Compression
one_liner: 基于历史LLM注意力聚合构建可复用文档压缩视图，降低RAG压缩开销同时提升生成质量
practical_value: '- 电商/推荐场景的RAG服务可复用REVA的离线注意力聚合逻辑，把高频查询关联的商品/攻略/规则文档的重要片段离线预计算，在线压缩开销从数百ms降到<40ms，大幅提升用户查询响应速度

  - 可复用「token注意力→单词单元聚合→按原始顺序渲染」的trick，避免压缩后文本碎片化影响LLM理解，适配商品详情、客服知识库这类结构化文本的压缩场景

  - 针对RAG场景的高频重复检索文档（如爆品详情、大促规则）可优先构建压缩视图，85%+的查询能命中至少一个已缓存视图，无需每个请求独立运行压缩模型，降低API
  token和算力成本

  - 跨查询的历史交互信号复用思路可迁移到生成式推荐的prompt优化，把用户历史点击/停留对应的item描述重要性预计算，减少生成推荐理由的prompt长度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG后检索压缩方法普遍存在两个痛点：一是每个查询独立处理，依赖额外辅助模型带来数百ms的在线开销，甚至超过压缩带来的效率收益；二是压缩逻辑与目标LLM无关，效果不稳定，部分场景下甚至不如简单前缀截断。同时RAG场景下85%-92%的查询会重复检索历史文档，大量历史query-document-LLM的交互信号未被有效利用。

### 方法关键点
- 离线/异步流程：从历史请求的LLM注意力trace中提取token级重要性，合并为可读的单词单元（自动保留日期、数字、专有名词等结构化片段），按文档维度聚合多次访问的平均重要性，存储到以文档ID+模型+tokenizer为复合key的分数库
- 在线流程：新请求检索到文档后，直接从分数库拉取预计算的重要性，按预算选最高得分的单词单元，保持原始文档顺序输出，未覆盖的文档用前缀截断兜底
- 支持两种配额分配策略：本地策略给每个检索文档均分配额，全局策略按文档历史效用动态分配配额，避免高价值文档配额不足

### 关键实验
在NQ、TriviaQA、HotpotQA、2Wiki四个QA基准，Llama-3.1-8B、Qwen3.5-9B、Gemma-4-E4B三个LLM上测试：
- 相比现有SOTA压缩方法，REVA生成质量提升1.0-5.8个点，压缩开销降低5.3-15.6倍，在线延迟<40ms
- 混合覆盖场景下（部分文档有预计算分数），相比前缀截断基线F1提升3.72个点，EM提升2.88个点
- 全命中场景下质量接近甚至超过RECOMP等有监督压缩方法，在线开销仅为其1/5-1/10

### 核心结论
RAG压缩不需要每个请求独立运行模型，复用历史交互的注意力信号可以实现质量和效率的双重收益。
