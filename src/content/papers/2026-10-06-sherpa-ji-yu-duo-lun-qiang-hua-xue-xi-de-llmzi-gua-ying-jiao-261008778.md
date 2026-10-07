---
title: 'Sherpa: Teaching LLMs to Teach Adaptively'
title_zh: Sherpa：基于多轮强化学习的LLM自适应教学能力训练框架
authors:
- Weixian Xu
- Yanzhe Zhang
- Zora Zhiruo Wang
- Changyu Chen
- Diyi Yang
affiliations:
- Stanford University
- Georgia Tech
- Carnegie Mellon University
arxiv_id: '2610.08778'
url: https://arxiv.org/abs/2610.08778
pdf_url: https://arxiv.org/pdf/2610.08778
published: '2026-10-06'
collected: '2026-10-07'
category: Training
direction: LLM自适应教学 · 强化学习训练
tags:
- Reinforcement Learning
- LLM Tutoring
- Adaptive Teaching
- Student Archetype
- PPO
one_liner: 提出多轮RL框架SHERPA，通过模拟差异化学生偏好训练LLM自适应教学能力
practical_value: '- 多轮RL直接锚定最终业务目标（如用户转化、学习效果）的训练思路，可迁移到电商个性化导购Agent、生成式推荐话术的微调，避免依赖大量人工标注的偏好数据，适配不同用户的需求差异

  - 双Gate过滤机制可复用在Agent交互链路中：只放行符合用户偏好的内容，不符合的返回明确负反馈，倒逼Agent自适应调整输出策略，同时减少无效交互提升用户体验

  - 仅对有效交互回合分配最终奖励的优化方式，能大幅提升生成式模型的泛化性，可直接用于GenRec的RL微调，避免过拟合到人工制定的过程性规则'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM教学能力训练依赖示范数据、偏好标注或预设教学规则，未锚定不同学习者的真实学习效果，无法适配个性化需求，甚至会降低学习者的主动思考能力，难以实现真正有效的自适应教学。
### 方法关键点
- 多轮RL框架SHERPA的教学流程分为准备（教师提前解题留存草稿，避免对话漂移）、多轮交互tutoring、测试三个阶段，奖励直接绑定学生测试成绩的提升幅度，不预设任何教学规则
- 设计6种来自教育学的学生偏好archetype，通过双Gate机制控制交互：Guidance Gate过滤直接泄露答案的教师回复，Adaptive Gate仅接收符合当前学生偏好的指导，不符合的返回脚本化明确报错，倒逼教师从交互中推断用户需求
- 基于PPO优化教师策略，仅对通过双Gate的有效交互回合分配最终奖励，引入留一法中心化、回合级归一化提升训练稳定性，仅用LoRA微调教师模型，训练成本低
### 关键实验
在MATH数学题数据集、MathTutorBench教学基准上测试，对比基线为Qwen3-8B base、PedagogicalRL：学生平均成绩提升20.5个百分点；MathTutorBench整体教学得分从52.5%提升至79.2%；人类教师pairwise比较中79.6%偏好SHERPA生成的回复，泛化到训练未见过的学生偏好也有显著提升。
### 核心结论
基于用户最终效果的无预设规则RL训练，配合差异化用户archetype设计，能显著提升LLM的自适应交互能力，泛化性远优于基于人工预设规则的训练方式
