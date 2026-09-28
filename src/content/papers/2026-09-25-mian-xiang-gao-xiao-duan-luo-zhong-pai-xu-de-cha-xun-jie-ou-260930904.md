---
title: 'QReason: Query-Focused Decoupled Chain-of-Thought for Efficient Passage Reranking'
title_zh: 面向高效段落重排序的查询解耦思维链框架QReason
authors:
- Yang Zhang
- Wenhan Liu
- Qiannan Zhu
- Mingming Li
- Yuanfei Huang
affiliations:
- 北京师范大学人工智能学院
- 北京教育人工智能重点实验室
- 教育部智能技术与教育应用工程研究中心
- 中国人民大学高瓴人工智能学院
- 中国科学院信息工程研究所
arxiv_id: '2609.30904'
url: https://arxiv.org/abs/2609.30904
pdf_url: https://arxiv.org/pdf/2609.30904
published: '2026-09-25'
collected: '2026-09-28'
category: QueryRec
direction: 查询改写 · 重排序效率优化
tags:
- Query Rewriting
- Chain-of-Thought
- Passage Reranking
- Reinforcement Learning
- Efficiency
one_liner: 解耦全局查询推理与窗口级重排序，仅生成1次可复用推理查询大幅降低冗余计算
practical_value: '- 解耦推理架构可直接迁移到电商搜索/推荐排序场景：若业务用到CoT辅助排序，可将全局用户/Query意图推理与窗口内物品排序解耦，1次生成推理结果跨窗口复用，实测可降低70%以上端到端推理延迟，同时不损失排序效果。

  - 两阶段训练范式可复用：第一阶段用黄金正样本做SFT让生成内容接地，第二阶段用「下游业务指标+语义一致性」双奖励做RL对齐，既能保证改写内容的相关性，又能直接优化NDCG等业务核心指标，效果比通用query改写模型更稳定。

  - 工程落地选型参考：推理密集型检索场景（如电商复杂语义Query、Agent工具调用检索）可选用小参数模型做推理查询生成，搭配大参数非推理重排器，效果优于同规模端到端推理重排模型，推理成本更低。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有带CoT的listwise LLM重排器依赖滑动窗口处理长候选集，每个窗口都要重复生成相似的Query侧推理链，平均语义相似度超90%，产生大量计算冗余、提升响应延迟；通用检索阶段的query改写方法直接用到重排场景效果不稳定，易引入错误信号降低排序质量。

### 方法关键点
- 提出解耦框架QReason，将全局Query推理与窗口级重排分离：先用轻量rewriter生成1次CoT风格的排序导向推理查询，后续所有滑动窗口的非推理重排器直接复用该查询，无需重复生成CoT。
- 两阶段训练rewriter：第一阶段为Relevance-Grounded Supervised Tuning（RGST），输入Query+黄金正例段落对，用大模型教师生成的推理查询做监督SFT，保证生成内容有明确相关性依据；第二阶段为Rank-Aligned Dual-Reward Refinement（RADR），基于GRPO做RL优化，列表式奖励直接对齐NDCG@10排序指标，点式奖励约束推理查询与黄金正例的语义一致性，避免生成内容漂移。

### 关键实验
在BRIGHT推理密集型检索基准测试，对比ReasonRank、Rank1等SOTA推理重排器：搭配Qwen3.5-35B-A3B重排器的QReason平均NDCG@10达36.93，超过ReasonRank 32B的36.45；相比ReasonRank 32B，端到端 latency 降低7.9倍（搭配MoE重排器）或2.6倍（搭配同规模密集重排器）；在3款不同基础重排器上均稳定提升NDCG@10 1.05~2.43个点，效果远优于GPT-4、TongSearch等通用改写方案。

### 核心结论
排序场景下重复推理的成本远高于预填充阶段的输入长度增加成本，将可复用的全局推理提前单次生成，是兼顾效果与效率的核心优化思路。
