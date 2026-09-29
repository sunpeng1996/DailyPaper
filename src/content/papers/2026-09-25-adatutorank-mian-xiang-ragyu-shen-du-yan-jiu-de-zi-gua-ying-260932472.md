---
title: 'AdaTutoRank: Learning to Rerank Document Sets via Adaptive Tutoring Optimization
  for RAG and Deep Research'
title_zh: AdaTutoRank：面向RAG与深度研究的自适应辅导优化文档集重排序方法
authors:
- Kailin Jiang
- Lei Liu
- Jian Xi
- Yangqi Chen
- Hui Xu
- Hongwei Zhao
- Bin Li
- Yu Lu
- Haibo Shi
affiliations:
- University of Science and Technology of China
- Tencent Yuanbao Team
arxiv_id: '2609.32472'
url: https://arxiv.org/abs/2609.32472
pdf_url: https://arxiv.org/pdf/2609.32472
published: '2026-09-25'
collected: '2026-09-29'
category: RAG
direction: RAG文档重排 · 集合级自适应优化
tags:
- Document Reranking
- RAG
- Deep Research Agent
- Setwise Optimization
- Reinforcement Learning
one_liner: 提出自适应辅导优化的集合级重排序方法，解决RAG重排的集合级信用分配稀疏问题，10个基准达SOTA
practical_value: '- 可直接复用3层9维的集合级评估体系：电商搜索/推荐/广告的候选集重排，可照搬文档、集合、全局三层评估维度（相关性、互补性、冗余度、完整性等），替代传统单点相关性排序，解决结果重复、信息覆盖不全的问题。

  - 自适应辅导优化(ATO)训练框架可迁移到集合类决策任务：对推荐选品、广告素材组合、搜索候选集生成等集合级预测场景，先做SFT冷启动，再按输出质量分档匹配不同强度hint（高分给规则、中分给修正建议、低分给参考样本），解决集合级reward稀疏、信用分配难的痛点。

  - 训练推理解耦设计适合低延迟业务落地：训练阶段使用的查询专属rubric、hint在推理时完全不依赖，不会增加推理耗时，可直接嵌入现有电商搜索、RAG智能客服、导购Agent等链路。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统RAG和深度研究Agent的文档重排多基于单文档相关性排序，返回结果易冗余、覆盖不全，无法满足复杂信息需求；现有集合级重排仅用统一标量奖励，存在信用分配稀疏问题：冗余文档可搭高质量集合的便车获得高奖励，关键文档也会被低质量集合牵连受惩罚，且固定形式的蒸馏指导对不同质量输出适配性差，过强限制优质输出，过弱对劣质输出无指导作用。

### 方法关键点
- 设计3层9维分层评估rubric：文档层（相关性、真实性、质量）、集合层（互补性、冗余度、冲突）、全局层（完整性、密度、可达性），全流程支撑冷启动银标生成、RL奖励计算、蒸馏hint生成。
- 两阶段训练：第一阶段用大模型生成的rubric对齐银标做Setwise SFT冷启动；第二阶段用自适应辅导优化(ATO)，将当前策略冻结生成3种不同强度hint，按输出reward分档匹配：高分输出仅给rubric规则、中分输出给修正反思、低分输出给参考最优集合，蒸馏生成token级优势信号，和GRPO的集合级优势加权组合优化。
- 训练推理解耦：推理时仅需输入查询和候选集，无需查询专属rubric和hint，无额外耗时。

### 关键结果
在10个覆盖RAG、深度研究、集合级评估的基准上测试，对比11种主流重排器，总体得分45.28，比此前SOTA RubricRanker高1.44，比初始检索高6.20；深度研究场景得分提升2.05，同时可减少Agent的检索调用次数；集合级评估总体得分48.97，比RubricRanker高2.17，在7个细粒度维度排名第一。

### 最值得记住的一句话
集合级优化任务无需局限于统一标量奖励，可通过分层评估体系+分档自适应hint将稀疏集合级奖励转化为密集token级监督，兼顾性能与推理效率。
