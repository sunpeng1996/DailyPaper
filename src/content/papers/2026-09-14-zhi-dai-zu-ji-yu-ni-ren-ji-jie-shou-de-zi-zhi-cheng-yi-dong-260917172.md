---
title: 'Fingers as Legs: Learning Self-Supported Locomotion and Manipulation with
  an Anthropomorphic Hand'
title_zh: 指代足：基于拟人机械手的自支撑移动与操作学习
authors:
- Amirhossein Kazemipour
- Hehui Zheng
- Robert Katzschmann
affiliations:
- Soft Robotics Lab, ETH Zurich
arxiv_id: '2609.17172'
url: https://arxiv.org/abs/2609.17172
pdf_url: https://arxiv.org/pdf/2609.17172
published: '2026-09-14'
collected: '2026-09-20'
category: Other
direction: 机器人多任务复用 · 强化学习落地
tags:
- Reinforcement Learning
- Mobile Manipulation
- Robotic Hand
- Sim2Real
- Locomotion
one_liner: 提出强化学习方案训练拟人机械手复用手指实现移动与操作，无需额外行走机构
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: huggingface-daily
depth: abstract
---

### 动机
现有移动操作机器人多需独立行走与操作机构，结构冗余，难以适配狭窄空间作业场景，复用拟人机械手手指同时实现移动与操作可大幅提升部署灵活性。
### 方法关键点
1. 保留原有拟人机械手的手指设计与位置控制器，搭载板载电源与计算单元实现完全自包含；
2. 采用基于硬件测量校准的仿真环境做强化学习训练，定制适配不等长手指特性的奖励函数，避免四足类奖励方案的适配问题；
3. 部署多套任务专用策略，分别适配移动、操作类不同任务需求。
### 关键结果数字
- 仿真中移动速度显著优于经调优的原生四足机器人奖励方案；
- 硬件端支持14种不同地面（橡胶垫、地毯、草地、砾石等）的无缆爬行、转向、跌倒恢复；
- 自重支撑下可实现无视觉连续12次键盘输入、带视觉反馈的物体推送任务。
