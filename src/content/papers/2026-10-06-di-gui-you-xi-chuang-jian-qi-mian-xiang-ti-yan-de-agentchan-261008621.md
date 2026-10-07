---
title: 'Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game
  Harness'
title_zh: 递归游戏创建器：面向体验的Agent产品级游戏开发框架
authors:
- Jiajun Chen
- Haoyu Wu
- Mingda Jia
- Xihui Liu
affiliations:
- HKU MMLab
- The University of Hong Kong
- Shenzhen Loop Area Institute
arxiv_id: '2610.08621'
url: https://arxiv.org/abs/2610.08621
pdf_url: https://arxiv.org/pdf/2610.08621
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: 多Agent协作 · 体验导向迭代优化
tags:
- MultiAgent
- Recursive Optimization
- Experience-driven
- Agent Framework
- Automated Content Generation
one_liner: 提出Designer/Builder/Player/Reviewer四角色递归迭代的Agent游戏开发框架，兼顾代码正确性与玩家体验
practical_value: '- 可复用「设计/实现/测试/评估」四角色递归迭代Agent架构，适配电商营销物料生成、推荐策略调优、商品创意迭代等场景，大幅提升闭环反馈效率

  - 采用编程接口原生的测试Agent收集行为轨迹，替代人工/GUI测试，可迁移到推荐系统离线A/B测试的模拟用户采样环节，降低评估偏差与测试成本

  - 基于行为轨迹+显式偏好的多维度评估方法，可直接用到电商内容/商品的用户体验评估，补充单一点击率指标的体验感知缺陷'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有游戏设计Agent仅能保障生成内容的代码正确性，无法兼顾玩家体验，缺乏从原型到成熟产品的系统化迭代优化框架。
### 方法关键点
构建四角色协作的递归迭代链路：Designer承接用户需求与评估反馈输出开发计划；Builder生成候选游戏版本；Player通过原生编程接口自动执行可复用策略，高效收集多样化游玩轨迹，避免GUI测试的低效与偏差；Reviewer结合轨迹指标、视觉证据、用户显式偏好输出评估结果与优化建议，闭环驱动下一轮迭代。
### 关键结果
GameCraft-Bench上取得SOTA总分77.89；GameASG-Bench上任务成功率达53.2%，较同模型基线提升34.1%，运行时通过率93.4%为所有对比方法最高，用户研究显示玩家游玩时长与评分显著更高。
