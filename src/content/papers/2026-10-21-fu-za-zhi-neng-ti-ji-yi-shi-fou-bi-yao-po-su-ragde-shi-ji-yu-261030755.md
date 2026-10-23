---
title: Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought
title_zh: 复杂智能体记忆是否必要？朴素RAG的实际性能远超预期
authors:
- Zhengye Bao
- Shengtao Zhang
- Haokai Zhang
- Shiqi Lou
- Muning Wen
- Minnan Luo
affiliations:
- 西安交通大学
- 上海交通大学
- 浙江大学
- 香港中文大学
arxiv_id: '2610.30755'
url: https://arxiv.org/abs/2610.30755
pdf_url: https://arxiv.org/pdf/2610.30755
published: '2026-10-21'
collected: '2026-10-23'
category: Agent
direction: Agent 长时记忆系统优化
tags:
- Agentic Memory
- RAG
- Long-term Conversation
- Retrieval
- LLM Agent
one_liner: 仅含稠密检索+重排的朴素RAG在4个长对话记忆基准上超越多数主流复杂Agent记忆系统
practical_value: '- 做Agent长时记忆优先上朴素RAG基线：用「稠密检索+交叉编码器重排+原始历史片段索引」的方案，不需要先搞复杂的事实提取、图存储、状态更新，成本低性能还高，适合快速落地

  - 工程实现参数可直接复用：256token滑动窗口+32token重叠，先召回Top128候选再重排选Top15，chunk大小在128-1024范围对效果影响不大，不用纠结切分参数

  - 记忆系统设计核心优先级：优先保证据覆盖率，其次再优化利用率，原始历史的时序、依赖路径信息不能丢，不要为了省存储做过度的摘要、事实提取，会丢失推理需要的上下文导致效果下降'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent长时记忆系统普遍引入事实提取、状态突变、图构建等复杂操作，但业界缺少对这类复杂度必要性的验证，过往朴素RAG基线往往存在检索单元过粗、无重排等缺陷，导致性能被低估，无法作为合理的对比基线。

### 方法关键点
- 提出RAW-RAG基线：不对原始对话历史做任何LLM加工（无提取、无摘要、无突变），仅将对话带时间戳序列化后切为256token窗口（32token重叠），存入扁平向量索引
- 检索流程：query嵌入后先召回Top128相似窗口，用交叉编码器重排后选Top15喂给下游Reader LLM，由LLM自行处理时序、状态变更推理

### 关键实验
在LoCoMo、LongMemEval、MEME、MemoryAgentBench 4个公开长时对话记忆基准，7组Benchmark-模型配置下测试，对比EverMemOS、Mem0、Memora等12款主流Agent记忆系统：
- RAW-RAG在6组配置下得分第一，比最优复杂记忆系统高0.13~5.53分
- 100万token量级BEAM数据集上，RAW-RAG摄入耗时仅0.3h，是次优系统的1/10，最快比Memora快83倍
- 证据覆盖度比次优系统高5~40个百分点，靠高证据覆盖抵消了稍低的利用率

### 核心结论
对于绝大多数长时对话类记忆任务，设计良好的朴素RAG基线性能已经超过绝大多数复杂Agent记忆系统，新增复杂记忆操作前必须先和该基线对齐对比
