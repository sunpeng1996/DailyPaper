---
title: 'ConRub-Med: Reinforcement Learning with Consensus Rubrics for Open-Ended Medical
  Question Answering'
title_zh: ConRub-Med：基于共识评分准则强化学习的开放式医疗问答方法
authors:
- Taojie Zhu
- Yuan Xia
- Tao Sun
- Yizhi Wang
- Yan Chen
- Qunshan He
- Tian Guan
- Jian Wang
- Jinjie Gu
- Junwei Liu
affiliations:
- Tsinghua University
- Ant Group
- Zhejiang University
arxiv_id: '2608.10996'
url: https://arxiv.org/abs/2608.10996
pdf_url: https://arxiv.org/pdf/2608.10996
published: '2026-08-11'
collected: '2026-08-12'
category: Training
direction: LLM训练 · 共识式RL奖励机制优化
tags:
- Reinforcement Learning
- GRPO
- Reward Modeling
- Consensus Mechanism
- Medical LLM
one_liner: 提出基于多模型共识评分规则的RL框架，低成本优化开放式医疗问答效果
practical_value: '- 多异构模型生成评价准则再取共识的方法，可迁移到生成式推荐/Agent回复的自动奖励设计，大幅降低人工标注成本

  - 三态评分（正确/缺失/错误）给错误打负分而非零分的规则，可优化RLHF的奖励区分度，避免无效/有害生成混过

  - GRPO分组出现奖励平局时引入双排序一致的pairwise判优机制，可直接复用在推荐排序的RL优化流程，减少平局噪声'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
数学、代码领域RL可依托自动校验生成奖励信号，但开放式医疗问答无低成本自动校验能力，人工编写评分规则（rubrics）成本过高，单模型生成规则可靠性不足，难以支撑规模化RL训练。
### 方法关键点
1. 3个异构LLM独立生成原子评分准则，仅保留三者均语义支持的共识准则，降低规则噪声；
2. 采用三态评分区分「正确覆盖/信息缺失/错误声明」，错误项给负分而非零分，强化对有害生成的惩罚；
3. GRPO训练时若组内样本奖励全部平局，引入双pairwise判优生成序列优势，无平局则沿用原生GRPO。
### 关键结果
9个基准测试中6项排名第一，医疗能力与泛化性平均分最高；仅用5166条prompt的规则数据集，HealthBench-Hard得分38.98±1.04，优于用8000样本的InfiMed-ORBIT（33.60）和28000样本版本（37.30），双盲专家评测临床相关性优于单模型生成规则方案。
