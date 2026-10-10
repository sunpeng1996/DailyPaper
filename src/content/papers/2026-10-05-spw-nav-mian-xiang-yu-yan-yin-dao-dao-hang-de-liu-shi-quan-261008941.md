---
title: 'SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation'
title_zh: SPW-Nav：面向语言引导导航的流式全景世界模型
authors:
- Yunheng Liu
- Ziqi Cai
- Siqi Yang
- Yimu Wang
- Minggui Teng
- Jiaming Tan
- Shuchen Weng
- Erwin Wu
- Kaipeng Zhang
- Boxin Shi
affiliations:
- Alaya Lab
- Peking University
- Institute of Science Tokyo
arxiv_id: '2610.08941'
url: https://arxiv.org/abs/2610.08941
pdf_url: https://arxiv.org/pdf/2610.08941
published: '2026-10-05'
collected: '2026-10-10'
category: Agent
direction: 具身Agent · 语言引导导航世界模型
tags:
- EmbodiedAgent
- WorldModel
- PanoramicGeneration
- LanguageGuidedNavigation
- TextToVideo
one_liner: 提出支持自然语言移动指令、可实时生成2K 360°视频的流式全景世界模型SPW-Nav
practical_value: '- 电商虚拟逛店/VR看房场景：可复用球面旋转解耦、姿态对齐条件控制方法，实现语言引导的3D场景全景流实时生成，提升用户交互体验

  - 具身导航Agent训练：可复用多阶记忆+少步生成器设计，解决长序列交互下的状态漂移问题，降低标注训练数据的成本

  - 动态多模态生成业务：可借鉴指令动态切换的技术方案，落地支持用户实时调整需求的生成类服务，比如虚拟场景路线动态调整'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有全景生成器仅支持遵循预定义轨迹生成内容，交互世界模型仅能接收透视视图下的低级动作输入，无法理解关联场景内容的自然语言移动指令，无法满足长序列、动态调整路线的全景交互探索需求。
### 方法关键点
1. 引入球面旋转解耦机制，将自然语言指令对应的运动精确映射为球面相机操作；
2. 采用姿态对齐条件约束，保证长流式生成下平移输入的边界稳定，避免内容漂移；
3. 设计多阶记忆+少步生成器结构，支持导航指令动态切换时的场景一致性；
4. 构建带标注相机轨迹、验证后导航指令的SPW-NavSet数据集。
### 关键结果
仅输入单张全景图即可实时生成1分钟2K 360°视频，相机跟随精度、视频质量均优于此前SOTA全景生成器，原生支持中途动态切换导航指令。
