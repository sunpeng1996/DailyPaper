---
title: 'Socratic Skill Learning: Interleaving Teaching and Practice for Transferable
  Agent Skills'
title_zh: 苏格拉底式技能学习：交错教学与实践的可迁移Agent技能习得方法
authors:
- Letian Zhu
- Han Li
- Yifan Yao
- Xinping Lei
- Xinyu Che
- Jiahao Wang
- Dianyi Wang
- Yucheng Fu
- Jiakai Wang
- Zhiqi Bai
affiliations:
- Nanjing University
- Alibaba Group
arxiv_id: '2610.17860'
url: https://arxiv.org/abs/2610.17860
pdf_url: https://arxiv.org/pdf/2610.17860
published: '2026-10-12'
collected: '2026-10-22'
category: Agent
direction: Agent 可迁移技能学习优化
tags:
- Agent Skill Learning
- LLM Agent
- Skill Transfer
- Socratic Learning
- Agent Benchmark
one_liner: 提出交错专家教学与学生实践的Agent技能学习框架，低监督成本下实现更高跨任务技能迁移率
practical_value: '- 电商/广告场景自动化Agent（如运营流程执行、客服问题处理）技能沉淀可复用SSL框架逻辑：不用全流程跑完再复盘，每完成若干操作步引入专家/规则引导，技能跨场景迁移率可提升5-8pp，优于事后复盘方案

  - 大模型推理成本有限时，可复用Issue-Guided SSL的问题驱动引导机制，仅在未解决问题出现时调用高能力大模型/领域专家，可减少60%+的专家侧token消耗，技能迁移效果几乎无损失

  - 构建企业内部Agent技能评估体系时，可借鉴SKILLTRANSFERBENCH的设计思路：按任务家族定义不变约束与可变范围，用未见过的实例测试技能迁移性，避免技能仅适配训练场景的过拟合问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能学习多从执行轨迹蒸馏，或仅在任务失败后提供反馈，无法在技能构建过程中引导探索方向，导致习得技能跨任务迁移性差、专家/高能力大模型资源利用率低，同时缺乏统一的技能迁移效果评估基准。
### 方法关键点
- 框架分为Student、Educator双角色：Student全权负责环境交互、验证建议、编写技能包，Educator仅拥有工作区读权限，按需提供解释、诊断、挑战建议或保持静默，Student可自主适配或拒绝指导。
- 两种落地方案：Fixed-Window SSL每完成固定次数工具调用触发评审；Issue-Guided SSL跟踪未解决学习问题，仅在问题新增/变更时触发评审，聚焦相关上下文降低调用成本。
- 构建SKILLTRANSFERBENCH评估基准：覆盖6大领域35个任务家族、408个可执行案例，每个家族公开任务不变量与可变范围，用未见实例测试技能迁移性。
### 关键结果
主实验基于Qwen模型在22个任务家族155个案例的主 cohort 测试：Fixed-Window SSL效用达0.801，较无技能（0.723）、Trace2Skill（0.761）、SKILL-KD（0.751）分别提升7.8pp、4pp、5pp；Issue-Guided SSL效用达0.805，较Fixed-Window SSL减少61.7%的Educator token与16.9%的总习得token，单位专家token的迁移收益提升2.75倍。
### 核心结论
Agent技能习得过程中，交错式过程引导比事后复盘或直接专家编写技能的迁移效果更好，基于未解决问题的按需引导可在几乎无损效果的前提下大幅降低专家资源消耗
