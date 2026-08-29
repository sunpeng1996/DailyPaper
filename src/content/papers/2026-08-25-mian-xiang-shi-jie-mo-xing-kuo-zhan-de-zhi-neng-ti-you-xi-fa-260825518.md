---
title: Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling
  World Models
title_zh: 面向世界模型扩展的智能体游戏开发可验证轨迹数据引擎
authors:
- Pengfei Zhou
- Hexin Wang
- Zhengfeiyang Zhang
- Yixing Ma
- Zhenglin Wan
- Kaipeng Zhang
- Wangbo Zhao
- Yang You
affiliations:
- National University of Singapore
- InfRec, Cardinal AI Lab
- University of California, Berkeley
- Hong Kong University of Science and Technology
- Independent Researcher
arxiv_id: '2608.25518'
url: https://arxiv.org/abs/2608.25518
pdf_url: https://arxiv.org/pdf/2608.25518
published: '2026-08-25'
collected: '2026-08-29'
category: Agent
direction: 智能体训练 · 世界模型可验证数据引擎
tags:
- Agent
- World Model
- Reinforcement Learning
- Data Engine
- Verification
one_liner: 提出RLHEV训练范式与AWoMo世界模型，借游戏引擎+人类反馈构建可验证数据引擎优化世界模型训练
practical_value: '- 可复用「机器自动校验+人类全局反馈」的RL后训练范式，替代纯CLIP等模糊奖励信号，优化电商场景商品3D展示生成、虚拟导购场景构建效果

  - 可借鉴「可执行环境自动生成轨迹数据」的思路，在电商仿真推荐、广告投放模拟环境中生成高质量训练数据，降低人工标注成本

  - 跨引擎泛化的迁移学习思路可复用到多平台推荐策略迁移场景，降低新场景冷启动成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
当前世界模型主流训练依赖爬取视频+大算力，效率低下；空间生成任务依赖CLIP等模糊代理奖励信号，误差大、有偏，无法支撑高质量RL后训练，缺乏可落地的grounded奖励机制。
### 方法关键点
1. 提出RLHEV（Reinforcement Learning with Human-Engine Verification）后训练范式，结合游戏引擎输出的碰撞、物理特性、可导航性等稠密自动校验信号，叠加游戏开发流程中的人类隐式接受反馈作为全局奖励。
2. 配套提出Agentic World Model（AWoMo）世界构建智能体，可自主生成场景编辑方案，接收人机双路验证信号，将接受/修复后的多模态轨迹转化为训练数据，构建闭环递归数据引擎。
### 关键结果
在UnitySceneBench 200个样本的资产编辑评估中，RLHEV得分最高；跨Unreal、Godot引擎的泛化实验验证迁移学习可有效应对分布偏移；AWoMo增强训练可提升R2R、Gymnasium MuJoCo等多个具身任务的策略性能
