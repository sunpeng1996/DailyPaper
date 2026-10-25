---
title: Action Learning for Scientific Simulations
title_zh: 面向科学仿真的动作学习框架
authors:
- Sarah Liaw
- Yuanqi Du
- Yilun Du
affiliations:
- Kempner Institute
- Harvard University
- Microsoft Research New England
arxiv_id: '2610.31585'
url: https://arxiv.org/abs/2610.31585
pdf_url: https://arxiv.org/pdf/2610.31585
published: '2026-10-22'
collected: '2026-10-25'
category: Other
direction: 科学仿真 · 轨迹动作学习与推理
tags:
- ActionLearning
- DynamicalSystem
- TrajectoryModeling
- EnergyBasedModel
- ScientificSimulation
one_liner: 提出LEAP动作学习框架，从轨迹观测恢复随机动作，支撑多场景科学推理与控制
practical_value: '- 长序列建模可借鉴「锚定参考过程+学习差异修正」范式，避免单步转移建模丢失长时依赖，可用于用户全链路行为轨迹建模

  - 路径空间可微目标的构造思路可迁移到推荐全链路转化优化、Agent多步决策的统一目标设计，解决分步优化目标不一致问题

  - 可复用动作表征的设计思路可用于多任务Agent的通用决策表征学习，降低跨场景、跨任务的迁移成本'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有动力学建模方法要么学习局部转移规则丢失跨时间依赖，要么生成轨迹无统一可处理的优化目标，无法支撑任意路径的评估与优化需求。
### 方法关键点
提出动作学习范式，从轨迹观测中恢复随机动作作为动力学系统推理的统一目标；设计LEAP（Learned Energy on Action Paths）框架，将未知动作锚定到可处理的参考过程，通过对比观测轨迹与参考轨迹学习修正项，得到路径空间可微目标，同时捕获局部动力学结构与非加性长时依赖；训练后的动作表征可复用在路径排序、机制调控、约束优化、采样等多任务。
### 关键结果
在随机物理系统、多体轨道动力学、分子仿真场景下，LEAP可精准恢复底层动力学，有效捕获跨时间依赖，支持推理目标与物理条件的跨场景迁移
