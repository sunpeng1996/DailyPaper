---
title: Learning Design Taste through Verifiable Synthetic Environments and Agentic
  Reinforcement Learning
title_zh: 基于可验证合成环境与智能体强化学习的设计审美学习
authors:
- Sujay choubey
- Siddhant Saxena
- Sarthak Kapil
- Suhas Motwani
affiliations:
- Basethesis
arxiv_id: '2611.20612'
url: https://arxiv.org/abs/2611.20612
pdf_url: https://arxiv.org/pdf/2611.20612
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: Agent 强化学习 UI 生成优化
tags:
- Reinforcement Learning
- Synthetic Environment
- Reward Engineering
- Curriculum Learning
- Code Generation
one_liner: 提出分层验证奖励+合成环境+多轮智能体RL方案，让4B小代码模型掌握UI设计审美
practical_value: '- 奖励工程可复用分层验证思路：先过硬规则门槛，再做metric校验、专家偏好对齐，最后加入奖励池，避免奖励被hack，适合推荐系统排序目标、Agent行为约束的奖励设计

  - 合成训练环境构建可迁移：基于基础样例做语法树扰动+约束采样，搭配自适应课程学习，适合低资源场景下Agent/生成式推荐模型的训练数据增强

  - 多轮交互训练增益高于单轮：在电商文案生成、商品页UI生成等场景，可加入多轮自校验+隐式奖励反馈环，提升生成结果的人类偏好对齐度'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有代码大模型生成的UI页面虽可正常运行，但层级、间距、排版、构图等设计审美能力普遍偏弱，缺乏可靠的对齐训练方案。

### 方法关键点
1. 分层验证奖励框架：将设计质量拆解为硬规则、渲染指标、评分rubric、组间偏好、盲审专家面板5层，仅通过专家一致性、因果敏感性、抗hack、稳定性校验的信号才计入奖励；
2. 合成训练环境：基于智能体生成的基础页面，通过语法树扰动、约束采样生成不同难度的训练样例，搭配自适应课程+过优化隔离规则；
3. 4B小代码模型做多轮Agentic RL训练：交互过程中支持代码编辑、仓库构建、渲染报告读取，由隐藏评分器计算奖励。

### 关键结果
16项渲染信号仅7项、10项评分维度仅6项通过准入校验；TD-Bench上Taste Index在分布内从0.630升至0.795，分布外从0.598升至0.700；盲审专家对比中60%概率优于基线模型，56.9%概率优于单轮对照；仅跨需求独特性略低于基线。
