---
title: 'RewardVerse: Rubric-Guided Policy Optimization for Video Reward Modeling'
title_zh: RewardVerse：评分规则引导的视频奖励建模策略优化
authors:
- Zhenchen Tang
- Yang Li
- Songlin Yang
- Bo Peng
- Xiaotong Zhao
- Shuai Li
- Haotian Fan
- Alan Zhao
- Jing Dong
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Hong Kong University of Science and Technology
- Tencent
arxiv_id: '2609.22947'
url: https://arxiv.org/abs/2609.22947
pdf_url: https://arxiv.org/pdf/2609.22947
published: '2026-09-18'
collected: '2026-09-24'
category: Training
direction: 视频生成奖励建模 · 偏好对齐训练
tags:
- Reward Model
- RLHF
- Policy Optimization
- Preference Alignment
- Video Generation
one_liner: 引入动态评分规则中间表征，结合两阶段RGPO算法解决视频奖励模型标量漂移问题
practical_value: '- 针对电商/广告场景生成式内容（短视频、文案）的偏好打分，可引入动态评分规则作为中间锚点，解决跨query打分标量漂移问题，提升RM稳定性

  - 两阶段RGPO训练范式可复用：先基于种子规则预训练打分器，再联合优化规则生成器与打分器，降低标注成本同时提升打分与人类偏好的对齐度

  - 跨场景RM设计可参考该思路，将模糊的主观评价拆解为可解释的明确规则，既提升结果可解释性也便于业务规则干预'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有视频奖励模型（RM）直接将复杂主观的视频质量映射为单一标量分数，无明确评估准则，易出现跨prompt的标量漂移问题，导致RL优化时奖励信号不可靠。
### 方法关键点
1. RewardVerse框架引入动态评分规则作为评估查询与打分器之间的中间表征，先生成显式评估准则再做规则引导的打分，提供稳定语义锚点缓解标量漂移；
2. 两阶段Rubric-Guided Policy Optimization（RGPO）训练算法：第一阶段用自进化的种子评分规则预热打分器，第二阶段联合优化评分规则生成器产出适配查询的评估准则，同时持续对齐打分器与人类偏好。
### 关键结果
在16维EvalVerse基准及外部数据集上，RewardVerse有效缓解标量漂移，在pointwise和pairwise评估任务上均达到SOTA，可为视频生成的RL优化提供鲁棒可解释的奖励信号。
