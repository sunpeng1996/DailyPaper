---
title: 'ProtoVis-Nav: Prototypical Visual Imagination for Visual-Spatial Aligned UAV
  Navigation'
title_zh: ProtoVis-Nav：用于视觉空间对齐无人机导航的原型视觉想象框架
authors:
- Guangyuan Sui
- Yunzhong Hou
- Chi Harold Liu
affiliations:
- Beijing Institute of Technology
arxiv_id: '2611.17330'
url: https://arxiv.org/abs/2611.17330
pdf_url: https://arxiv.org/pdf/2611.17330
published: '2026-11-12'
collected: '2026-11-15'
category: Agent
direction: 具身Agent · 视语导航空间对齐
tags:
- VLN
- Embodied Agent
- UAV Navigation
- Prototype Learning
- Visual Alignment
one_liner: 提出原型视觉想象框架，通过特征原型组合预估目标视觉特征，优化无人机视语导航的视觉空间对齐
practical_value: '- 多模态Agent决策任务可借鉴「先预估动作对应的目标场景表征再输出动作」的两阶段范式，提升动作与环境感知的对齐度

  - 特征原型线性组合生成目标高维表征的方法可迁移至多模态召回、生成式推荐等任务，降低直接生成的误差

  - 训练时将动作输出与动作结果表征做绑定的优化思路，可用于电商导购Agent的决策逻辑优化，降低决策偏差'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
无人机视语导航(VLN)的3D运动预测容错率极低，现有方法直接从语言指令和视觉观测生成航点，无法预判动作执行结果，易出现导航偏差甚至碰撞。
### 方法关键点
引入原型视觉想象范式，首先预测多个视觉特征原型，通过原型线性组合预估下一步目标位置的局部视觉表征；再将预测得到的原型及目标表征作为上下文输入动作生成模块，强制视觉感知与航点输出的空间对齐，训练阶段同步优化视觉想象损失与航点预测损失。
### 关键结果
多组公开无人机VLN基准实验验证有效性，相比现有基线在导航成功率、轨迹对齐度等核心指标上取得显著提升。
