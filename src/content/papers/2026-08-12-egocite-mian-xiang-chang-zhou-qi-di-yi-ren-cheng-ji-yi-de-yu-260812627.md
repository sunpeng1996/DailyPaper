---
title: 'EgoCITE: Context-Augmented Indexing and Time-Aware Retrieval for Long-Horizon
  Egocentric Memory'
title_zh: EgoCITE：面向长周期第一人称记忆的上下文增强索引与时序感知检索
authors:
- Le Zhang
- Ke Sun
affiliations:
- University of Michigan, Ann Arbor
arxiv_id: '2608.12627'
url: https://arxiv.org/abs/2608.12627
pdf_url: https://arxiv.org/pdf/2608.12627
published: '2026-08-12'
collected: '2026-08-14'
category: Agent
direction: Agent 长时序记忆架构优化
tags:
- Agent Memory
- Time-aware Retrieval
- Multimodal Indexing
- RAG
- Egocentric QA
one_liner: 提出上下文增强多视角索引与双Agent时序感知检索框架，提升长周期第一人称记忆QA精度并降低36倍成本
practical_value: '- 做用户行为/会话记忆索引时，可复用EgoScheme的上下文补全思路，用相邻5分钟窗口的上下文补全单条记录的指代、省略信息，生成自包含的原子索引，避免后续检索因缺上下文失效

  - 处理带时序意图的用户query（如「上次买的XX」「最近常看的XX」）时，不要纯靠语义检索，可叠加query感知的时序衰减评分（默认λ=0.99效果最优），再用专门的采样Agent做时序意图对齐的证据筛选，比硬时间过滤鲁棒性更强

  - 长时序Agent记忆系统可参考多视角多粒度索引设计，拆分动作/活动/单条发言/会话不同粒度的索引，对应不同抽象层级的查询需求，提升召回准确性同时降低检索成本

  - 长时序记忆场景不要硬堆长上下文LLM，采用「多轮检索+小上下文推理」的方案，可在精度超过长上下文LLM的同时降低20倍以上的token成本，延迟也更可控'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有长周期第一人称记忆系统存在两大核心瓶颈：一是基于短上下文生成的视频字幕、语音转录构建的索引缺失局部上下文，存在大量未解决的指代、省略问题，10%的现有系统实体索引存在未解析代词，17%的会话索引保留无上下文的省略表述，无法支撑可靠检索；二是检索仅依赖语义相似度，忽略query的时序意图，76%的EgoLifeQA、48%的EgoMem问题都带时序限定（如「上次」「通常」「昨天上午」），现有方案时序相关问题准确率比非时序问题低9.8-13.3%。
### 方法关键点
- EgoScheme：用5分钟局部多模态上下文补全原始记录的指代、省略信息，生成自包含的原子记忆索引，避免信息缺失
- EgoIndex：按粒度和交互类型拆分为动作/活动/单条发言/会话四个互补视角的多粒度索引，适配不同抽象层级的查询需求
- EgoRetrv：双Agent时序感知检索，drafting Agent多轮生成语义+时序范围的混合查询，采用时序衰减评分合并语义和时序相关性召回候选；采样Agent基于query的时序意图从候选池中筛选对齐的证据
### 关键结果
在EgoLifeQA、EgoMem、EgoR1-Bench三个基准测试，对比长上下文LLM、EgoRAG、VideoRAG、WorldMM等基线：EgoCITE-GPT比现有Agent记忆基线准确率高4.4-14.2%，比长上下文GPT-5.4 Agent高3.6-8.9%，同时成本低36倍；时序相关问题准确率比最强Agent记忆基线高15.5%；记忆周期从1天扩展到7天时准确率仅下降4.8%，远优于长上下文LLM的11.9%降幅。
### 核心结论
记忆索引的有效性取决于索引本身的信息完整性，以及检索阶段对时序意图的显式建模，不需要堆百万token长上下文就能实现低成本的高性能长时序记忆
