---
title: 'DUPAR: Dual-Path Conversational Retrieval via Speech Retriever with Cross-Turn
  Evidence Caching'
title_zh: DUPAR：带跨轮证据缓存的双路径语音对话检索框架
authors:
- Yuanjun Li
- Yiwen Liu
- Dapeng Li
- Zhiwei Xu
- Bin Zhang
- Shengtao Zhang
- Rong Shen
affiliations:
- 山东大学
- 理想汽车
- 清华大学
- 中国科学院自动化研究所复杂系统认知与决策智能国家重点实验室
arxiv_id: '2609.18042'
url: https://arxiv.org/abs/2609.18042
pdf_url: https://arxiv.org/pdf/2609.18042
published: '2026-09-16'
collected: '2026-09-17'
category: RAG
direction: 对话RAG · 跨模态语音检索优化
tags:
- RAG
- Cross-Modal Retrieval
- Conversational Retrieval
- Low-Latency
- Speech Retrieval
- Cache Optimization
one_liner: 提出双路径语音对话检索框架，融合跨轮缓存与跨模态对齐，降延迟提鲁棒性
practical_value: '- 快慢双路径架构可直接复用在电商语音客服、车载语音导购等语音交互Agent场景，快路径查缓存降延迟，慢路径兜底保召回，平衡用户体验与检索准确率

  - 跨轮缓存基于当前轮检索结果+1跳图邻居预生成下一轮候选集的思路，可迁移到多轮对话推荐、多轮搜索场景，无需预测下一轮Query，大幅降低预检索开销

  - 语音编码器对齐冻结通用文本embedding（如BGE-M3）的训练方案，可无缝兼容现有存量文本向量索引，无需重构知识库，降低语音检索能力落地成本

  - 语音直接检索相比ASR+文本检索在低信噪比、方言/口音场景下鲁棒性更优的结论，可指导嘈杂环境下语音搜索、语音导购业务的技术选型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
语音助手RAG现有方案分为两类：ASR转文本再检索的级联链路延迟高，且ASR错误（尤其领域术语、口音、噪音场景）会向下传播导致检索失效；直接语音跨模态检索存在模态对齐gap，全库检索精度不足。多轮对话场景下轮次间语义高度相关，现有方案未利用历史检索结果减少重复计算。
### 方法关键点
- 双路径检索架构：快路径直接将语音Query编码为与BGE-M3对齐的向量，检索上一轮生成的跨轮证据缓存，满足置信度阈值直接返回，与ASR并行运行可提前出结果；不满足则触发慢路径，融合语音向量全库检索结果与ASR转文本的检索结果返回。
- 跨轮缓存更新：每轮返回的检索结果，基于预构建的Chunk关联图扩展1跳邻居作为下一轮缓存候选集，无需预测下一轮Query。
- 语音编码器训练：基于Qwen3-Omni语音权重，前24层冻结加Q/K/V LoRA，后8层全微调，用多尺度池化输出1024维向量，对齐冻结的BGE-M3文本embedding，损失融合余弦相似度损失与InfoNCE对比损失。
### 关键结果
- 干净语音场景下，语音编码器检索精度接近ASR+文本检索基线，R@1达67.6%（基线67.7%），Query端延迟降低3.75倍，TTFT/TTFA分别减少146.3/144.0ms。
- 噪音场景下平均Recall@10达0.875，比基线0.771提升10.4个百分点，5dB低噪下Recall@10达0.862，是基线0.608的1.42倍。
- 多说话风格/方言场景下整体R@1提升4.2个百分点，四川方言场景R@1提升8.43个百分点。
- 跨轮缓存检索相比全库检索，R@1从35.48%提升至67.74%，R@3从54.84%提升至90.32%。
### 核心结论
语音交互类RAG系统可通过快慢路径架构+跨轮局部缓存，在几乎不损失精度的前提下大幅降低延迟，同时规避ASR错误传播问题。
