---
title: Discrete Beckmann Transport Models for One-Step Language Modeling and Reasoning
title_zh: 离散贝克曼传输模型实现单步语言建模与推理
authors:
- Sophia Tang
- Shiyi Wang
affiliations:
- University of Pennsylvania
- Harvard University
- Kempner Institute
- IAIFI
arxiv_id: '2609.15903'
url: https://arxiv.org/abs/2609.15903
pdf_url: https://arxiv.org/pdf/2609.15903
published: '2026-09-14'
collected: '2026-09-16'
category: LLM
direction: LLM少步生成 · 无蒸馏训练
tags:
- Discrete Generative Model
- Flow Matching
- Few-step Generation
- Autonomous Flow
- No Distillation
one_liner: 无需教师蒸馏的离散生成框架，单/少步生成效果超离散扩散与流基线
practical_value: '- 可借鉴少步无蒸馏生成的架构设计，优化电商场景下的商品文案、推荐理由生成任务，无需依赖大模型蒸馏即可降低推理延迟，适配高吞吐的生成式推荐需求

  - 置信度驱动的仅低质量token迭代修正策略，可复用到电商导购Agent的回复优化、多轮推理路径修正场景，在不损失效果的前提下减少计算开销

  - 基于phase transition的锚定时间设计，可迁移到生成式推荐的模型训练中，在commitment time后锚定核心生成目标（如商品核心属性、用户需求关键词），平衡生成多样性与相关性，避免模式崩溃'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有离散扩散、流模型作为自回归语言模型的替代方案，少步采样通常需要蒸馏预训练教师模型，效果上限受限于教师质量，且需要昂贵的两阶段训练流程；时间依赖的流轨迹弯曲，采样效率低，无法适配低延迟生成场景需求。
### 方法关键点
- 构建时间无关的自主流，可证明一步将任意输入点映射到单纯形顶点的不动点，无需时间条件输入，流轨迹更平直，采样效率更高
- 直接从原始数据训练，通过最小化守恒方程残差优化模型，完全移除教师蒸馏环节，未完全收敛的模型可通过迭代应用直到达到不动点
- 设计partial-context插值训练范式，支持置信度驱动的迭代优化，每次迭代仅修正低置信度token，无需重走完整采样流程
- 基于理论推导的commitment time设定锚定损失生效时间，在token决策确定后再锚定目标，平衡生成多样性与收敛速度，避免模式崩溃
### 关键结果
在LM1B、OpenWebText语言建模任务上，DBTM+ril在1NFE下比流基线FMLM降低生成PPL 58%（LM1B）、65%（OpenWebText）；在Sudoku推理任务上，16NFE下困难难度准确率达97.5%，超过同NFE的FMLM+基线16.1个百分点；GSM8K任务32NFE准确率达16.8%，超过同预算的流基线。
最值得记住的结论：无蒸馏自主流离散生成模型通过迭代修正低置信度token，即可在极少NFE下逼近自回归模型的生成效果，是高吞吐低延迟生成场景的可行替代。
