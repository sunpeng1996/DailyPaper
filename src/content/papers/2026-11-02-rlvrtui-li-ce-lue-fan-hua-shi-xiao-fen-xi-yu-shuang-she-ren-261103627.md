---
title: 'Not All Reasoning Generalizes: A Case Study on Learning Generalizable Reasoning
  Strategies in RLVR'
title_zh: RLVR推理策略泛化失效分析与双射任务联合训练优化方法
authors:
- Ziqi Pang
- Yu-Xiong Wang
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2611.03627'
url: https://arxiv.org/abs/2611.03627
pdf_url: https://arxiv.org/pdf/2611.03627
published: '2026-11-02'
collected: '2026-11-03'
category: Reasoning
direction: LLM推理 · RLVR泛化优化
tags:
- RLVR
- OOD Generalization
- Reasoning Strategy
- Reinforcement Learning
- LLM
one_liner: 揭示RLVR推理策略OOD坍缩现象，提出双射任务联合训练方案大幅提升泛化能力
practical_value: '- 做电商Agent/商品规则推理的RL微调时，可加入低不确定性单解辅助任务联合训练，强化结构化推导策略，避免OOD场景（如冷启动、跨类目）退化为暴力枚举，提升泛化性

  - RL训练时可通过限制输出长度、缩小解空间等方式提升每token有效信息量，倒逼模型选择高效推理策略，减少无效采样，适合query语义解析、复杂营销规则匹配等场景

  - 评估RL微调效果不能仅看域内精度，需额外审计推理策略分布，避免域内表现达标但OOD策略坍缩的问题，适配跨域推荐、个性化推理等高泛化要求场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RLVR是当前提升LLM推理能力的核心技术之一，但现有实践中常出现域内精度达标、OOD场景精度暴跌的问题，且已排除基模型能力不足、奖励作弊等常见诱因，需从推理策略层面揭示失效机制并给出可落地的优化方案。
### 方法关键点
- 构建可控字符串函数反演实验框架：定义非双射函数多解反演任务，明确划分ID/OOD场景（OOD包含更多解要求、更长输出、输入输出长度变化等维度），可清晰区分结构化推导、暴力枚举两类可观测推理策略。
- 提出双射任务联合训练方案：在原非双射多解任务训练基础上，混入1:1比例的单解双射反演任务，无需过程监督，仅通过结果奖励即可强化模型对高泛化性推导策略的偏好。
- 建立信息论层面的理论解释：每token输出的有效信息量（比特率）决定推理策略的泛化能力，结果型RLVR会隐式给高比特率的推导策略分配更高奖励，双射任务放大了不同策略的奖励差，进一步强化高效策略的学习。
### 关键结果
基于Qwen2.5-7B-Instruct基模型实验：仅用非双射任务训练的MONO模型ID场景推导策略占比85%、精度92%，但OOD长输出+多解场景推导占比仅27%、精度仅18%，长度变化OOD场景精度仅6%；加入1:1双射任务的MIXED模型ID精度与MONO相当，OOD长输出+多解场景推导占比提升至69%，长度变化场景精度达25%，较MONO提升3倍以上，零样本迁移到数学竞赛数据集平均精度较基模型提升4.7个百分点。

**最值得记住的结论**：RLVR泛化的核心不是训练任务和目标任务的相似度，而是是否激励了高比特率的通用推理策略。
