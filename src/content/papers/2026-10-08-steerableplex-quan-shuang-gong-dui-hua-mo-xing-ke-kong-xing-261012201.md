---
title: 'SteerablePlex: Can We Steer Full-Duplex Models?'
title_zh: SteerablePlex：全双工对话模型可控性优化方法与评估
authors:
- Haolong Zheng
- Maike Züfle
- Dominik Macháček
- Peter Polák
- Xulin Fan
- Xavier Sumba
- Siyin Wang
- Ondřej Klejch
- Mark Hasegawa-Johnson
affiliations:
- University of Illinois Urbana-Champaign
- Karlsruhe Institute of Technology
- Charles University
- Imperial College London
- Tsinghua University
arxiv_id: '2610.12201'
url: https://arxiv.org/abs/2610.12201
pdf_url: https://arxiv.org/pdf/2610.12201
published: '2026-10-08'
collected: '2026-10-10'
category: Agent
direction: 对话Agent 可控性训练与评估
tags:
- Full-duplex Model
- Instruction Following
- Reinforcement Learning
- User Simulator
- Controllable LLM
one_liner: 提出全双工对话模型可控性评估基准与GDPO训练方案，实现更稳定的多阶段约束遵循效果
practical_value: '- 搭建电商/推荐Agent的用户模拟评测体系时，可参考GDPO训练方案约束模拟器行为，避免偏离预设场景导致测评结果失真

  - 多轮对话类业务Agent（如导购、客服Agent）的可控性优化可复用奖励解耦RL训练思路，保证多任务按序完成的同时保留自然交互能力

  - 异步后端LLM监控+动态下发指令的架构，可直接迁移到需要动态调整对话路径的业务Agent（如售后问题处理Agent）开发中'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
全双工语音对话模型可实现类人自然交互，但对话历史变长后可控性大幅下降，用作用户模拟器时易偏离预设场景，导致评测结果不可靠，当前缺乏针对性的评估基准与可控优化方案。
### 方法关键点
1. 构建SimIF-Bench评估基准，专门测试对话模型是否能在交互中遵循预设场景、按要求顺序完成多项目标
2. 提出GDPO（Group Reward-Decoupled Normalization Policy Optimization）训练策略，保证全双工模型在对话中可遵循文本指令，同时保留原有的话轮转换能力
3. 搭配异步后端LLM架构，实时监控对话状态、按需下发指令，最终实现可控的全双工用户模拟器SteerablePlex
### 关键结果
SteerablePlex在多阶段约束遵循的稳定性上，显著优于现有开源全双工模型以及GPT-Realtime。
