---
title: 'Beyond Placement and Articulation: Usage-Driven Code Scenes for Embodied Interaction'
title_zh: 《超越布局与结构建模：面向具身交互的使用驱动代码化3D场景生成》
authors:
- Zijian Xiao
- Zipeng Ye
- Jinkun Hao
- Xiong Yang
- Yuchen Xie
- Ran Yi
affiliations:
- Shanghai Jiao Tong University
- Meituan
arxiv_id: '2608.18840'
url: https://arxiv.org/abs/2608.18840
pdf_url: https://arxiv.org/pdf/2608.18840
published: '2026-08-19'
collected: '2026-08-20'
category: Agent
direction: 具身Agent · 3D交互场景生成
tags:
- Embodied AI
- Agent
- 3D Scene Synthesis
- Code-based Representation
- Simulation Environment
one_liner: 提出使用驱动的具身Agent代码化3D场景生成框架RoomWright，支撑交互场景功能可用性与因果逻辑建模
practical_value: '- 电商AR家装/AR试穿场景可复用使用驱动的物体affordance推理逻辑，提升虚拟场景交互合理性

  - Agent交互仿真环境搭建可借鉴触发-条件-效果（TCE）规则建模跨物体因果依赖，降低仿真开发成本

  - AR商品摆放等涉及3D物体姿态还原的业务，可复用标注引导的使用导向姿态校准方法，解决像素姿态歧义问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有代码化3D场景生成方法仅关注视觉构建与物体级结构，未建模场景功能使用逻辑，无法支撑具身AI交互、机器人操控等仿真需求。

### 方法关键点
1. 设计使用驱动的物体推理模块，将每个锚点作为任务中心，自动匹配任务所需物体及对应功能可供性（affordance）；
2. 引入代码Agent，将每类交互编译为触发-条件-效果（TCE）规则更新物体结构化状态，建模跨物体因果依赖；
3. 采用标注感知的使用导向姿态校准方法，解决仅从像素还原可操作物体姿态的歧义问题。

### 关键结果
生成的场景完全可执行、可编辑、可直接接入仿真，在具身交互场景可用性、交互逻辑合理性等指标上优于现有基线，可直接支撑具身AI策略训练。
