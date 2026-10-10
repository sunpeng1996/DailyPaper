---
title: 'RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world
  environments'
title_zh: RoboRSI：复杂真实环境下稳定高效可复用的机器人自进化系统
authors:
- Zimo Wen
- Yijin Chen
- Yuxuan Cao
- Wendi Chen
- Yanwen Zou
- Wenye Yu
- Fuhang Kuang
- Han Xue
- Jun Lv
- Chuan Wen
arxiv_id: '2610.12424'
url: https://arxiv.org/abs/2610.12424
pdf_url: https://arxiv.org/pdf/2610.12424
published: '2026-10-08'
collected: '2026-10-10'
category: MultiAgent
direction: 多智体协作 · 技能迭代自进化
tags:
- MultiAgent
- Self-Evolution
- Skill-Learning
- Task-Decomposition
- Agent-Collaboration
one_liner: 提出基于自上而下技能精炼的多智体机器人自进化框架，实现稳定可复用的能力迭代
practical_value: '- 多智体分工（规划/执行/诊断/审核）的技能迭代框架可直接复用在电商推荐策略自迭代场景，比如动态调价、商品文案生成的错误归因与修复，避免盲目全链路调整

  - 自上而下任务分层+明确各层IO契约+错误归因到对应分支的思路，可用于推荐全链路故障定位，如召回/粗排/精排各层故障仅修改对应模块，保障迭代稳定性

  - 稳定技能序列沉淀为可复用复合技能的机制，可复用在电商Agent工具调用流程固化，比如客服Agent常见问题处理链路沉淀，减少重复推理开销'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有代码驱动的机器人Agent仅能基于执行反馈修复程序，无法围绕任务结构组织经验，导致修复的能力难以复用、迭代过程不稳定。
### 方法关键点
1. 提出Top-Down Skill Refinement（TSR）机制，将任务分解为复合、原子、基础三层技能，各层定义明确权责范围与IO契约，执行结果直接归因到对应分支，修复仅作用于出错分支
2. 设计Manager/Planner/Engineer/Reviewer四智体协作流程，协同完成规划、执行、诊断、新技能验证发布，稳定技能序列自动沉淀为可复用复合技能，支持人工介入校正方向
### 关键结果
- 真实环境下移动机械臂经过104轮迭代即可实现多物体家庭清洁能力
- 仿真环境下在LIBERO系列、RoboTwin数据集上成功率超出最强基线2.7~11.0个百分点，同时token使用量降低29.4%、VLM调用耗时降低27.2%
