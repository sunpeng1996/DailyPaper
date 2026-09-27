---
title: Learning Better Reasoning for Generative Recommendation with Semantic IDs
title_zh: 面向语义ID生成式推荐的推理能力优化框架Evo-Rec
authors:
- Mengdan Zhu
- Yufan Zhao
- Sophie Di
- Yao Zhao
- Tao Di
- Yulan Yan
- Sridhar Iyer
- Liang Zhao
affiliations:
- Emory University
- Microsoft
- Cornell University
arxiv_id: '2609.29973'
url: https://arxiv.org/abs/2609.29973
pdf_url: https://arxiv.org/pdf/2609.29973
published: '2026-09-24'
collected: '2026-09-27'
category: GenRec
direction: 生成式推荐 · Semantic ID推理优化
tags:
- Generative Recommendation
- Semantic ID
- Chain-of-Thought
- Reinforcement Learning
- GRPO
one_liner: 提出三阶段Evo-Rec框架，通过推理轨迹选择与排序感知RL提升语义ID生成式推荐效果
practical_value: '- 做Semantic ID生成式推荐的推理增强时，不要直接用所有生成的CoT做SFT，可复用Best-of-N拒绝采样策略，仅保留能提升目标item预测概率的推理轨迹，能大幅降低噪声引入，无需额外数据即可提升SFT效果

  - RL优化推荐推理策略时，不要只用粗粒度的Exact Match奖励，改用基于真实排序的NDCG@K奖励，配合item catalog前缀trie约束的束搜索生成候选，能更精准对齐推理优化与排序业务目标，Top-N指标提升尤其明显

  - 小参数LLM做生成式推荐可复用三阶段训练范式：先做SID-文本多任务对齐打基础，再用优质推理数据SFT暖启动，最后用业务反馈RL精调，落地门槛低且效果增益稳定'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式推荐引入显式推理时，普遍未筛选推理质量，语义合理但无预测增益的推理会误导后续item生成，甚至降低推荐效果；同时传统RL优化仅用精确匹配的粗粒度奖励，无法区分排序提升的实际价值，推理优化目标与业务排序目标存在错位。
### 方法关键点
- 阶段1 SID-语言对齐：通过多任务混合训练（SID历史→SID、SID↔商品标题、SID与文本交叉预训练等）将Semantic ID的语义、用户行为信号对齐到LLM，为推理能力落地提供基础
- 阶段2 Best-of-N拒绝采样SFT：对每个用户交互历史采样N条候选推理轨迹，仅保留能提升目标item预测概率的最优轨迹做SFT，过滤无增益甚至负增益的推理噪声
- 阶段3 排序感知RL优化：基于当前策略生成推理轨迹，通过全量item catalog前缀trie约束的束搜索生成合法候选列表，用目标item在候选列表中的NDCG@10作为奖励，采用GRPO优化推理策略，直接对齐排序业务目标
### 关键实验
在Amazon Review的3个公开基准数据集（Games、Office、Industrial）上，对比判别式推荐、普通生成式推荐、推理增强推荐三类基线，在难度最高的Games数据集上，相比最优基线SIDReasoner，Recall@5相对提升19.3%，NDCG@10相对提升32.5%，排序类指标增益普遍高于召回类指标。
### 核心结论
推荐系统的推理价值不取决于推理的语义合理性或长度，而取决于其对下游推荐排序的实际增量效用。
