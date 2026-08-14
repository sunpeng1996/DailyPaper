---
title: Test-Time Optimization of Query Embeddings with Ranking Aware Reward Maximization
title_zh: 基于排序感知奖励最大化的查询嵌入测试时优化框架
authors:
- Tianyu Chen
- Jiaxing Wu
affiliations:
- The University of Texas at Austin
- Google DeepMind
arxiv_id: '2608.12569'
url: https://arxiv.org/abs/2608.12569
pdf_url: https://arxiv.org/pdf/2608.12569
published: '2026-08-12'
collected: '2026-08-14'
category: RecSys
direction: 检索召回 · 测试时嵌入优化
tags:
- Test-Time Optimization
- Dense Retrieval
- Query Embedding
- Knowledge Distillation
- Ranking Reward
one_liner: 无需修改模型和索引，将排序奖励蒸馏为可复用的查询侧残差向量提升检索效果
practical_value: '- 针对闭源商用嵌入API的场景，可直接复用TTT-Embed的残差向量叠加方案，无需修改模型和索引即可快速提升电商搜索、RAG系统的检索效果

  - 可根据业务可投入的rerank/LLM judge预算动态选择共享范围：低预算用全局向量冷启动，中预算分业务域用task-wise向量，高预算对核心query做query-wise优化，平衡效果与成本

  - 可复用证据自适应缩放系数α_g = n_g/(n_g+1)，无需人工调参即可适配不同数据量下的残差向量权重，降低上线调优成本

  - 针对域微调后通用能力下降的模型，无需回刷训练数据，直接蒸馏通用域排序奖励即可恢复甚至超过原基线效果，解决灾难性遗忘问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有稠密检索依赖冻结编码器和预计算索引，测试时来自reranker/LLM judge的排序奖励通常单次使用即丢弃，直接更新编码器权重不仅需要参数权限（闭源API不可行），大模型下计算成本极高，无法高效复用跨query的排序信号。

### 方法关键点
- 提出TTT-Embed框架，仅在输出嵌入空间学习轻量残差向量v_g，将查询原始嵌入修正为x̃_q = unit(x_q + α_g v_g)，无需修改编码器权重和文档索引，兼容闭源API
- 支持三种共享范围：全局（全query共用1个向量）、任务级（同业务/任务域共用1个向量）、查询级（单个query私有向量），可根据预算灵活选择
- 采用知识蒸馏目标：以reranker/LLM judge输出的排序得分构造教师分布，以修正后查询嵌入与文档的相似度构造学生分布，优化KL散度学习残差向量
- 用证据自适应缩放系数α_g = n_g/(n_g+1)（n_g为学习该向量用到的奖励query数），无需人工调参即可适配不同数据量下的向量权重

### 关键实验结果
在5个嵌入模型（含2个闭源Gemini API）、15个MTEB检索任务上验证，对比原生检索、同预算直接rerank：
- 高预算下（平均每个query 100条奖励）query-wise方案nDCG@10最高提升8.36，超出同预算直接rerank 0.56
- 中预算下（每个query 10条奖励）task-wise方案平均提升6.36，超出同预算直接rerank 3.15，且对未见过的query最高提升8.57，跨零样本任务最高提升4.71
- 可解决灾难性遗忘：域微调后通用能力下降的模型，用该方案可恢复甚至超过原基线通用效果，最高提升8.00 nDCG@10

### 核心结论
测试时的排序奖励不需要用来更新模型权重，蒸馏为嵌入空间的轻量残差向量即可实现跨query复用，在不改动现有检索架构的前提下实现效果提升。
