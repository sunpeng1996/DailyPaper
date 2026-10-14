---
title: 'Vela: User Behavior as Supervision Sparks LLM Intelligence'
title_zh: Vela：以用户行为为监督信号激发大模型智能
authors:
- Yang Xiao
- Yusong Sun
- Haoyi Wu
- Wenyang Hui
- Weiqiang Hang
- Luqing Wang
- Zejian Wang
- Zirui Tu
- Jingsheng Mao
- Shaobo Hu
affiliations:
- AllSpark Team
- The Hong Kong Polytechnic University
arxiv_id: '2610.14709'
url: https://arxiv.org/abs/2610.14709
pdf_url: https://arxiv.org/pdf/2610.14709
published: '2026-10-09'
collected: '2026-10-14'
category: Training
direction: LLM训练 · 用户行为监督
tags:
- UserBehaviorSupervision
- LLMFineTuning
- PersonalizedRecommendation
- UserProfiling
- ReinforcementLearning
one_liner: 提出用户行为作为监督的训练范式与Vela框架，同步提升LLM用户认知与通用能力
practical_value: '- 可复用用户行为转训练任务的框架：将历史行为拆分为可见段/未来段，设计预测类+规则评估类两种任务模板，可低成本生成海量个性化训练样本，无需依赖人工标注

  - 训练样本过滤可借鉴难度筛选策略：仅保留基础模型得分在0.2~0.8区间的中等难度任务，能提升OOD场景泛化性能，减少无效训练开销

  - 做LLM个性化推荐/用户画像任务时，可先在通用用户行为数据集上做SFT预训练，再做下游RL微调，相同RL配置下可额外提升7个点左右性能，投入产出比更高

  - 基于用户行为的增量训练不会损害LLM通用能力，反而可平均提升4分，无需担心里程碑式遗忘，适合电商场景大模型的迭代训练'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM训练数据以静态文本、合成数据为主，无法捕捉用户行为的时序演化规律，在个性化推荐、用户画像、购买意图预测等用户相关任务上表现不佳，甚至存在长行为序列下准确率下降、输出偏向平均用户画像的问题；而各大平台已积累海量真实用户行为数据，是未被充分利用的优质训练信号，此前研究仅针对特定推荐任务做改造，未验证其对LLM通用能力的增益。

### 方法关键点
- 提出「用户行为作为监督」训练范式：将脱敏时序用户行为序列拆分为可见历史段和隐藏未来段，设计91个任务模板，分为预测类（用未来真实行为做标注）、规则评估类（用自定义rubric打分）两大类型，覆盖浏览、搜索、购买、发布等6类用户行为
- 训练样本经过双重筛选：先用基础模型跑4次预测，仅保留平均得分在0.2~0.8区间的中等难度任务，再为每个保留任务生成4条训练轨迹，仅选得分最高的1条纳入训练集，最终得到7.5万条Vela-Instruct样本、9375条Vela-RFT样本
- 训练流程可叠加RL优化：先做SFT微调，后续可针对特定下游任务叠加RL训练进一步提升性能

### 关键结果
基于Qwen3.6-35B-A3B微调，相比底座模型：VelaBench（用户相关域内任务）提升11.5分，用户相关OOD任务平均提升6.2分，其中广告推荐任务提升11.2分，通用OOD基准平均提升4分；叠加RL训练后，相比直接从底座启动RL，性能额外提升7.7分；数据量从4.7K扩展到75K时，用户相关能力与通用能力均持续上涨；难度过滤策略可额外提升用户OOD任务平均1.1分。

最值得记住的一句话：真实用户行为是可规模化的优质LLM训练信号，既能够强化用户理解类任务表现，也不会损害反而会提升模型通用能力。
