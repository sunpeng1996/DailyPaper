---
title: 'UniSkill: Learning Actor-Aligned Skill Proposals for an Evolving Policy'
title_zh: UniSkill：面向演化策略的智能体对齐技能提案学习框架
authors:
- Yifei Lu
- Cheng Liu
- Dianzhi Yu
- Hui Xiang
- Ji Zhang
- Yuanchu Xiao
- Rong Liang
affiliations:
- Ant Group
- The Chinese University of Hong Kong
- Qiantang Credit
arxiv_id: '2610.10164'
url: https://arxiv.org/abs/2610.10164
pdf_url: https://arxiv.org/pdf/2610.10164
published: '2026-10-06'
collected: '2026-10-08'
category: Agent
direction: Agent 自演化技能库优化
tags:
- Agent
- SkillBank
- Reinforcement Learning
- LLM Agent
- Policy Optimization
one_liner: 提出共享策略的自演化Agent框架，用对比动作反馈免额外rollout，稳定联合训练无性能崩塌
practical_value: '- 技能库迭代可复用已有成功/失败轨迹做对齐校验，无需额外线上/仿真rollout，大幅降低训练成本，适合电商导购Agent、客服Agent的技能沉淀

  - 加入操作级正则避免技能编辑操作（新增/更新/不操作）的坍缩，保障探索性，解决长期训练中技能库迭代僵化的问题

  - 共享同一个大模型做任务执行和技能提取，减少多模型部署开销，适合中小团队快速落地自演化Agent系统

  - 技能有效性要和当前策略绑定，避免旧技能不适配更新后模型导致的性能下降，可迁移到推荐系统的召回规则、用户画像迭代场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能库与策略联合训练方案，要么依赖后续任务的成功信号（存在策略更新后混淆技能收益与策略本身提升的问题），要么每个候选技能都要额外做环境rollout（成本极高），长期训练容易出现性能崩塌。

### 方法关键点
- 共享同一个策略同时承担Actor（任务执行）和Skill Proposer两个角色，从完成轨迹生成技能编辑提案（ADD/UPDATE/NOEDIT）
- 设计对比动作反馈：固定当前策略和历史轨迹，计算替换为候选技能后，成功/失败轨迹的动作对数似然差的变化，作为技能与当前Actor的对齐信号，无需额外rollout
- 新增技能编辑支持正则：避免提案内容的负反馈抑制合理的编辑操作，保障三种编辑操作的探索概率
- 技能库更新只有同时通过规则校验、对齐信号>0、成功轨迹似然提升>0三个条件才会生效

### 关键实验
在ALFWorld和WebShop（模拟电商购物交互基准）上测试，对比GRPO、Evolving-RL、SkillRL等基线：ALFWorld成功率达98.4%，比Evolving-RL高5.4pp，无训练后期性能崩塌；WebShop任务得分90.5，成功率84.7%，比SkillRL高12pp；单步训练总耗时仅为Evolving-RL的1/3左右，3B小模型也能稳定运行，成功率超过7B参数的GRPO基线。

### 核心结论
技能的有效性高度依赖使用它的当前策略，脱离策略状态评估技能收益没有意义。
