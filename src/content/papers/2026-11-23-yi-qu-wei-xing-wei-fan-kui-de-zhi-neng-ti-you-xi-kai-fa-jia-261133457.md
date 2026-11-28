---
title: Playfulness as Feedback for Agentic Game Development
title_zh: 以趣味性为反馈的智能体游戏开发框架
authors:
- Weijia Mao
- Kevin Qinghong Lin
- Zhen Fang
- Danze Chen
- Dongxing Mao
- Mike Zheng Shou
affiliations:
- Show Lab, National University of Singapore
- University of Science and Technology of China
arxiv_id: '2611.33457'
url: https://arxiv.org/abs/2611.33457
pdf_url: https://arxiv.org/pdf/2611.33457
published: '2026-11-23'
collected: '2026-11-28'
category: Agent
direction: Agent 生成内容迭代优化
tags:
- Agent
- Code Generation
- Feedback Loop
- Generative Content
- Iterative Refinement
one_liner: 提出三阶段递归游戏开发框架Play2Evolve，以智能体游玩的趣味性反馈迭代优化游戏体验
practical_value: '- 可复用「智能体自测试+多维度体验反馈」的迭代框架，落地到电商营销小游戏、互动权益玩法的自动生成优化，无需大量人工标注即可完成多轮迭代

  - 可借鉴「功能-视觉-玩法」三维度反馈拆解逻辑，适配推荐系统的商品物料、文案、互动组件的多维度效果自动评估，降低人工审核成本

  - 多模态生成模型与代码生成结合的架构，可直接复用到电商商品动态展示素材、直播间互动玩法的自动生成链路中'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
编码智能体已可实现从自然语言描述生成可运行游戏，但可运行不代表玩家体验佳，趣味性需覆盖可靠核心功能、吸引人的视觉设计、支持探索的丰富玩法三大维度，现有方案对上述维度的优化研究存在空白。

### 方法关键点
Play2Evolve为三阶段递归框架：初始化阶段生成基础可运行游戏；优化阶段由智能体模拟游玩，输出功能、视觉、玩法三类趣味性反馈，指导bug修复与素材升级；进化阶段基于反馈提出新玩法与美学目标，实现持续迭代；同时结合视频生成模型与代码生成动静态素材，丰富互动可玩性。

### 关键结果
在GameCraft-Bench得分60.05，优于初始化阶段的50.81与基线Play2Code的52.46；人工整体质量评分达3.67，较两款基线提升50%以上。
