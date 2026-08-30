---
title: 'CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators'
title_zh: CLAP：跨具身视频世界模型实现零样本物理仿真
authors:
- Kechen Liu
- Ola Shorinwa
affiliations:
- Princeton University
arxiv_id: '2608.27406'
url: https://arxiv.org/abs/2608.27406
pdf_url: https://arxiv.org/pdf/2608.27406
published: '2026-08-27'
collected: '2026-08-30'
category: Other
direction: 跨具身世界模型 · 零样本物理仿真
tags:
- World Model
- Cross-Embodiment
- Zero-Shot Transfer
- Curriculum Learning
- Video Generation
one_liner: 提出跨具身动作条件视频生成框架CLAP，可学习通用物理先验，零样本适配多机器人形态
practical_value: '- 课程式学习策略可迁移至多源异构数据训练场景：推荐系统可先在全域无标签数据学习通用用户行为先验，再在单业务小样本finetune，大幅降低冷启动成本

  - 异构空间对齐思路可复用：可参考三类动作表征对齐方案，构建多来源用户行为、搜索query、商品特征的统一表征，解决不同业务线特征不互通问题

  - 做实体/家居电商AR试摆、交互式Agent物理场景模拟的团队，可直接复用CLAP开源模型作为底层仿真引擎，减少从零开发的成本'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有动作条件视频模型仅支持单机器人具身，无法利用异构视频数据中的通用物理规律，且不同机器人平台动作表征差异大、人类视频普遍无动作标注，跨具身学习落地难度极高。

### 方法关键点
1. 采用末端执行器位姿、语言指令、隐式动作三类表征，对齐不同具身的异构动作空间；
2. 设计课程式跨具身学习流程：先基于无标注视频用隐式动作学习通用物理先验，再对齐到末端执行器动作空间，支持零样本部署；
3. 支持少样本适配快速定制单具身视频世界模型。

### 关键结果
在DROID等复杂环境下性能追平或超越SOTA单具身视频模型，可适配DROID、Bridge、双机械臂、人形机器人等多形态硬件，同时可提升π0.5等现有机器人策略的现实任务表现。
