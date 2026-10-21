---
title: 'HarnessRL: Co-Evolving Policies with a Just-in-Time Training Harness for Open-Ended
  RL'
title_zh: HarnessRL：面向开放式强化学习的策略与即时训练套件协同进化方法
authors:
- Xiaoqiang Wang
- Ting-En Lin
- Yuchuan Wu
- Pinyi Zhang
- Caixin Kang
- Ling Li
- Bingxue Qiu
- Jieping Ye
- Yongbin Li
- Bang Liu
affiliations:
- Alibaba Group
- Université de Montréal
- Mila - Quebec AI Institute
arxiv_id: '2610.26426'
url: https://arxiv.org/abs/2610.26426
pdf_url: https://arxiv.org/pdf/2610.26426
published: '2026-10-18'
collected: '2026-10-21'
category: Training
direction: 开放式强化学习 · LLM训练优化
tags:
- Reinforcement Learning
- GRPO
- Reward Modeling
- Training Efficiency
- LLM Alignment
one_liner: 动态适配三类训练接口解决rubric奖励失效问题，大幅提升开放式RL训练效率与泛化性
practical_value: '- 做生成式推荐文案、智能客服Agent的RL对齐时，可直接复用其奖励失效归因框架：将无区分奖励、虚假奖励分别映射到任务采样、rollout引导、评分规则三个模块的更新，避免单模块调整导致的问题转移（比如加引导后奖励饱和、改评分后信号太弱）。

  - 多任务推荐/排序模型的动态训练采样可借鉴其带重要性权重的策略：给高学习价值的任务更高采样率，同时通过重要性采样修正保证原任务分布的目标不变，无需调整损失函数即可实现自适应课程学习。

  - 大模型RL训练的调优效率优化可复用JIT Critic机制：每个候选的规则、引导、采样调整都先在当前冻结策略上验证效果，落在预设接受区间才采纳，能减少近一半的无效训练步数，降低大算力场景的训练成本。'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
基于自然语言评分规则（rubric）的开放式RL是LLM对齐、Agent训练的主流方案，但存在两类核心奖励失效问题：非区分性奖励（分数全低或全高，无有效学习信号）、虚假奖励（高分不对应真实响应质量），固定训练配置的传统方法会导致奖励与真实效果脱节，训练效率低、泛化性差。
### 方法关键点
- 设计训练时动态套件\(H_t\)，包含三个可调接口：任务采样（动态调整任务权重，带重要性采样修正保证原目标分布不变）、rollout引导（根据训练阶段动态增减评分项提示、参考样例、历史反馈三类引导字段，推理时完全移除）、rubric规则（动态增删/拆分/合并评分项，调整权重）。
- 构建训练记忆库存储历史rollout、规则更新、训练动态，支持时间维度的任务历史检索和语义维度的跨任务相似规则证据检索。
- 套件进化器通过归因器定位奖励失效类型并匹配对应调整接口，提案器生成候选更新，JIT Critic在当前冻结策略上实测更新效果，落在预设接受区间才采纳，否则退回修订。
### 关键结果
自研覆盖医疗、科学、写作等5领域的Rubric-Mix-10k评测集，对比GRPO、EvoRubric等SOTA基线：4B/9B模型规模下域内得分领先2.8~3.1分，OOD得分领先2.8~3.1分，达到最优OOD checkpoint的训练步数接近GRPO的一半，单步算力开销仅为GRPO的1.6倍，实际总训练成本低于所有基线。
> 最值得记住的结论：开放式RL训练中固定配置无法适配策略的动态进化，只有协同调整任务、引导、评分三个维度并即时验证效果，才能同时提升训练效率和泛化性。
