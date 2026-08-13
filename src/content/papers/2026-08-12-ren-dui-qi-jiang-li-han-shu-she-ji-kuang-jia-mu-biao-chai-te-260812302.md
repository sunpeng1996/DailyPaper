---
title: 'A Framework for Designing Reward Functions: From Objectives to Features to
  Human-Aligned Reward Functions'
title_zh: 人对齐奖励函数设计框架：目标拆解、特征选择到权重拟合
authors:
- Di Yang Shi
- W. Bradley Knox
affiliations:
- University of Texas at Austin
arxiv_id: '2608.12302'
url: https://arxiv.org/abs/2608.12302
pdf_url: https://arxiv.org/pdf/2608.12302
published: '2026-08-12'
collected: '2026-08-13'
category: Agent
direction: Agent奖励设计 · 人对齐强化学习
tags:
- Reward Design
- Reinforcement Learning
- Human Alignment
- Preference Elicitation
- Causal DAG
one_liner: 提出三步标准化流程，支持非专家生成无冲突的人类对齐线性奖励函数
practical_value: '- 电商/广告推荐Agent的多目标 reward 设计可复用三步流程：先拆解业务核心目标→转可测特征→基于因果DAG选低冗余特征，有效避免
  reward 项冗余和 reward hacking问题

  - 多目标权重调优可参考凸可行域收缩方法，通过主动查询专家对轨迹的偏好迭代缩小权重范围，比盲目调参效率更高，查询复杂度仅为O(nlogκ)

  - 无法拿到完整因果DAG时，可使用局部贪心方法做特征选择，优先替换高成本下游特征为低成本上游因果特征，控制 reward 计算的资源开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统RL奖励设计依赖专家试错，非专家难以落地，且普遍存在reward hacking、奖励项冗余、策略行为与人类偏好不匹配等问题，缺乏标准化的人对齐奖励生成流程。

### 方法关键点
- 目标拆解：将自然语言描述的任务迭代拆解为不可再分的基础目标，为每个目标匹配可测量的结果变量作为候选奖励项，针对无可用proxy、训练期不可观测、易被作弊等问题给出对应解法。
- 因果感知特征选择：将候选变量的因果关系构建为DAG，把奖励项选择转化为DAG上的最小成本部分覆盖问题，通过转化为最大流问题多项式时间求解，全局筛选低冗余、低成本的代表性奖励项；无全局因果信息时可使用局部贪心方法近似求解。
- 偏好驱动权重拟合：将权重求解转化为凸可行域收缩问题，通过合成轨迹对主动发起偏好查询，用切平面法迭代缩小可行权重区域，保证生成的权重天然无冲突。

### 关键结果
该工作为纯理论框架，无实证实验，给出严格复杂度保证：奖励项选择使用Dinic算法时间复杂度为O(|V'|²|E'|)；权重拟合仅需O(nlogκ)次偏好查询即可收敛到指定误差精度，查询效率渐近最优。

奖励设计需优先对齐最终业务目标而非人为设定的中间行为，才能从根源规避reward hacking问题。
