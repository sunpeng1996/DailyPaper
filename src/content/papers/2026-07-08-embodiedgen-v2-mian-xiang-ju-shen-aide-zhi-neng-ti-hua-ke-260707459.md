---
title: 'EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied
  AI'
title_zh: EmbodiedGen V2：面向具身AI的智能体化可直接仿真3D世界引擎
authors:
- Xinjie Wang
- Liu Liu
- Taojun Ding
- Andrew Choi
- Chaodong Huang
- Mengao Zhao
- Ziang Li
- Jackson Jiang
- Chunlei Yu
- Shengxiang Liu
affiliations:
- Horizon Robotics
- WuwenAI
arxiv_id: '2607.07459'
url: https://arxiv.org/abs/2607.07459
pdf_url: https://arxiv.org/pdf/2607.07459
published: '2026-07-08'
collected: '2026-07-10'
category: Agent
direction: 具身Agent · 仿真环境自动生成
tags:
- Embodied AI
- 3D Generation
- Simulation Environment
- Agent Training
- Reinforcement Learning
one_liner: 提出基于统一可仿真表示的3D世界生成引擎，自动化构建具身AI训练所需的各类任务仿真环境
practical_value: '- 跨模拟器统一表示的设计思路可直接复用给多框架部署的Agent训练系统，解决不同仿真/推理框架下资产、场景的兼容性问题，减少重复适配开发

  - 任务驱动的场景生成逻辑可迁移到电商家居布置/虚拟试穿类Agent的仿真数据集构建，自动生成符合任务要求的3D场景，大幅降低人工标注与场景制作成本

  - 「生成-校验-修复」的闭环pipeline设计可迁移到生成式推荐的内容生成链路，保障生成的推荐内容（如文案、3D展示素材）符合业务约束，提升可落地性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D可仿真资产生成技术发展快速，但将资产组装为可直接用于策略训练的任务环境仍以人工为主，严重限制具身AI规模化闭环学习。
### 方法关键点
1. 设计统一可仿真表示框架，打通跨模拟器资产、交互可供性、任务驱动场景、大规模多房间场景、有状态Vibe Coding，构建生成式、可编辑、可复用的仿真pipeline
2. 配套智能体化世界编译器，实现意图解析、场景图生成、资产生成、仿真校验的全流程自动化，支持操作、导航、移动操作等多类型具身任务与跨模拟器部署
### 关键结果
- 资产流水线人类接受度96.5%，碰撞检测成功率98.6%；83.3%的任务驱动场景无需人工修改即可直接用于下游仿真
- 基于生成环境开展在线RL训练，仿真任务成功率从9.7%提升至79.8%，迁移到真实机器人后任务成功率从21.7%提升至75.0%
