---
title: 'SPEAR: A Simulator for Photorealistic Embodied AI Research'
title_zh: SPEAR：面向照片级具身AI研究的交互仿真模拟器
authors:
- Mike Roberts
- Renhan Wang
- Rushikesh Zawar
- Rachith Dey-Prakash
- Quentin Leboutet
- Stephan R. Richter
- Matthias Müller
- German Ros
- Rui Tang
- Stefan Leutenegger
affiliations:
- Adobe Research
- Intel Labs
- Manycore Tech Inc
- NVIDIA
- ETH Zurich
arxiv_id: '2607.06701'
url: https://arxiv.org/abs/2607.06701
pdf_url: https://arxiv.org/pdf/2607.06701
published: '2026-07-06'
collected: '2026-07-18'
category: Agent
direction: 具身Agent训练 · 照片级仿真模拟器
tags:
- Embodied Agent
- Simulation
- Unreal Engine
- Synthetic Data
- Python API
one_liner: 基于Unreal Engine的高可编程高速仿真器，支持具身Agent训练与多模态合成数据生成
practical_value: '- 做电商3D商品展示、数字人交互Agent训练时，可复用SPEAR的UE-Python互调架构，快速生成照片级多视角商品/场景合成训练数据，降低真实数据采集成本

  - 开发具身导购Agent、虚拟试穿Agent时，可基于SPEAR快速搭建仿真环境，完成人机交互策略的预训练，减少线上真机调试成本

  - 需批量生成商品渲染素材、SEM落地页可视化素材的场景，可复用其73FPS 1080P高速渲染能力，批量生成带材质ID标注的高质量素材'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有照片级具身AI仿真器存在通用性差、可编程能力弱、渲染速度慢三类核心缺陷，无法支撑复杂具身Agent训练与多模态合成数据生成需求。
### 方法关键点
1. 核心为Python库，通过模块化插件架构可编程控制任意Unreal Engine应用，暴露超14K个UE原生函数给Python调用；
2. 设计高层编程模型，支持定义带任意数据依赖的UE任务图，可在单帧内确定性执行；
3. 支持渲染结果直接输出为NumPy数组，同步提供材质ID、物理着色参数等独家真值模态。
### 关键结果
单实例渲染1080P照片级图像速度达73FPS，可编程能力、渲染速度均比现有UE类仿真器高一个数量级，已验证支持多Agent控制、城市级场景渲染、自然语言场景编辑等多类场景。
