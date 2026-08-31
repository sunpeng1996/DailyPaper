---
title: 'J-Zero: Unified Challenger--Solver--Judge Co-Evolution from Zero Data'
title_zh: J-Zero：零数据下挑战者-求解器-裁判协同进化框架
authors:
- Gyouk Chu
- Myeongho Jeon
- Eunho Yang
affiliations:
- KAIST
arxiv_id: '2608.26582'
url: https://arxiv.org/abs/2608.26582
pdf_url: https://arxiv.org/pdf/2608.26582
published: '2026-08-26'
collected: '2026-08-31'
category: Training
direction: 大模型自进化 · 零数据训练
tags:
- Self-Evolution
- Zero-Data-Training
- Reward-Model
- Adversarial-Training
- GRPO
one_liner: 提出零数据下三角色协同进化框架，突破固定裁判瓶颈，适配两类任务域
practical_value: '- 可复用三角色协同框架优化推荐/广告系统冷启动：用Challenger生成高难度用户场景/query，Solver生成候选推荐结果/文案，Judge做偏好排序，无需人工标注即可完成小样本迭代

  - 两个零成本偏好对构造trick可直接落地：角色不对称偏好（专门优化的生成结果优于任务生成模型的结果）、分治增强偏好（拆分子问题聚合的结果优于直接生成结果），可低成本训练推荐场景的Reward
  Model

  - 训练样本过滤方法可提升迭代效率：筛选Solver输出得分方差最大的任务作为训练集，这类样本处于模型能力边界，训练收益远高于随机采样，适合新类目、新活动上线后的快速适配

  - 避免Reward Model天花板问题：不要用固定Reward Model，让Judge随业务迭代同步进化，可有效减少Reward Hacking，适配电商大促、用户偏好变化快的场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有零数据LLM自进化方案大多依赖固定裁判（Reward Model），仅能适配有客观标准答案的可验证域（如数学、代码），在依赖人类偏好的不可验证域（如文案生成、咨询回答、推荐理由生成）会快速碰到性能天花板，通常迭代2轮后性能就开始退化，无法持续提升。

### 方法关键点
- 三角色对抗进化闭环：Challenger生成高难度任务，训练目标是让Solver在该任务上得分最低；Solver训练目标是在Challenger生成的任务上拿到最高Judge得分，两者用GRPO优化，同时给Challenger增加重复任务惩罚、格式校验，避免生成无效任务。
- Judge协同进化：无需外部标注，基于两种结构不对称规则构造偏好对训练Judge：①角色不对称对：Solver的回答默认优于Challenger对自身生成任务的回答；②分治增强对：任务拆解为子问题分别求解再聚合的回答，默认优于Solver直接生成的回答，用Bradley-Terry损失更新Judge。
- 高价值训练样本筛选：选择Solver输出得分方差最大的Top-K任务训练，这类样本刚好处于模型能力边界，理论上可获得最高训练收益。

### 关键结果
实验覆盖11个可验证域基准（数学推理、通用推理、指令跟随）、3个不可验证域基准（AlpacaEval 2.0、Arena-Hard、创意写作），对比R-Zero、G-Zero等主流零数据自进化基线。可验证域平均得分超基线4.2分，不可验证域平均超基线8.0分，可持续迭代10轮性能持续提升，而基线迭代2轮后就出现性能退化。

> 最值得记住的结论：自进化模型的能力上限，永远等于其 evaluator 能识别的质量边界。
