---
title: 'Wizard: Manipulate Any World in Real Time via Agentic Control'
title_zh: 《Wizard：基于Agent控制实现任意虚拟世界实时操控》
authors:
- Yuzhe Wu
- Zijun Lin
- Yeying Jin
affiliations:
- Tencent
- NUS
- NTU
arxiv_id: '2610.40339'
url: https://arxiv.org/abs/2610.40339
pdf_url: https://arxiv.org/pdf/2610.40339
published: '2026-10-29'
collected: '2026-10-31'
category: Agent
direction: Agent 虚拟世界实时生成控制
tags:
- Agent Control
- World Model
- Video Generation
- Zero-shot Generalization
- Interactive System
one_liner: 提出结合结构化代理与自适应掩码的Agent游戏世界模型，支持零样本泛化的虚拟角色实时精准控制
practical_value: '- 电商虚拟试穿、虚拟直播间场景可复用「结构化中间代理（骨架/几何信息）+视频生成」的架构，降低实时可控内容生成的控制信号对齐成本

  - 自适应掩码机制可迁移到多模态生成任务中，提升控制信号与生成内容的匹配度，适合动态生成商品展示短视频、个性化营销素材的业务场景

  - Agent显式维护全局状态的设计可复用在交互式推荐Agent中，保障多轮交互下的上下文一致性，优化用户主动配置偏好类场景的体验'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频世界模型仅支持简单游戏设置与预定义动作模式，对未见场景、角色泛化性差，实时交互能力不足，无法支撑用户自定义的高自由度互动内容需求。
### 方法关键点
1. 构建覆盖750个场景、178个角色的多源数据集，引入骨架、几何信息作为结构化中间代理，作为视频生成模型的条件输入；
2. 设计自适应掩码机制，优化控制信号与生成视频序列的对齐效果；
3. 配套Agent框架显式维护更新游戏状态，保障虚拟世界配置、角色控制的逻辑一致性与视觉质量。
### 关键结果
实现零样本泛化到全新场景、角色与动作的同时，支持对角色动作的实时细粒度控制，保障互动过程的玩法逻辑一致性
