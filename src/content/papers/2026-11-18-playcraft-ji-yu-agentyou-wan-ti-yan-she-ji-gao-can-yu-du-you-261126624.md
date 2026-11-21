---
title: 'PlayCraft: Designing Engaging Games from Agent Play Experience'
title_zh: PlayCraft：基于Agent游玩体验设计高参与度游戏
authors:
- Weihao Cheng
arxiv_id: '2611.26624'
url: https://arxiv.org/abs/2611.26624
pdf_url: https://arxiv.org/pdf/2611.26624
published: '2026-11-18'
collected: '2026-11-21'
category: Agent
direction: 双Agent协作的内容体验迭代优化
tags:
- Agent
- Multi-Agent
- Automated Content Generation
- User Engagement
- Iterative Optimization
one_liner: 提出双Agent交替迭代的PlayCraft框架，基于游玩反馈优化游戏的掌握感提升参与度
practical_value: '- 可复用「执行Agent+优化Agent交替迭代」架构，用于电商内容/活动自动调优：先由模拟用户Agent交互上报体验，再由优化Agent迭代内容策略

  - 借鉴「基于交互反馈拟合用户能力曲线匹配目标进度」思路，可用于推荐系统新手成长路径设计、难度分层的任务/权益推送

  - 单轮交互后收集决策、反思、结果三类反馈的机制，可迁移到A/B测试自动归因模块，降低人工标注成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有AI Agent生成的游戏可玩但参与度不足，设计支持玩家技能掌握的内容需要大量人工游玩调优，成本极高。

### 方法关键点
PlayCraft采用双Agent交替迭代框架：
1. 游玩阶段：视觉输入的玩家Agent反复体验游戏，保留记忆，每轮结束上报进度、决策、结果、反思四类数据；
2. 创作阶段：创作者Agent基于上报数据评估玩家能力，预测不同熟练度下的表现，和预设目标学习曲线对比，诊断游戏缺陷并迭代修改，为玩家提供合理的技能提升空间。

### 关键结果数字
在三种智能等级的测试Agent上验证，相比初始游戏，PlayCraft生成的游戏在多数场景下学习增益更高、学习斜率更陡，所有智能等级下的各指标宏观均值均优于基线。
