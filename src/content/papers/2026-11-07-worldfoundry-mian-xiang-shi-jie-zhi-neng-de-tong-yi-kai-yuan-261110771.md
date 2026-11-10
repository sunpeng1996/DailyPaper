---
title: 'WorldFoundry: Towards Unified Infrastructure for World Intelligence'
title_zh: WorldFoundry：面向世界智能的统一开源基础设施
authors:
- Juanxi Tian
- Jiadong Hou
- Baiang Li
- Xin Lin
- Zhengbo Jiao
- Weijia Zhang
- Yeying Jin
- Truong Nguyen
- Haitian Zheng
- Zhifei Zhang
affiliations:
- OpenEnvision
arxiv_id: '2611.10771'
url: https://arxiv.org/abs/2611.10771
pdf_url: https://arxiv.org/pdf/2611.10771
published: '2026-11-07'
collected: '2026-11-10'
category: Eval
direction: 世界模型 · 统一评估与推理基础设施
tags:
- World Model
- Embodied Agent
- Evaluation Framework
- Multimodal
- Open Source
one_liner: 开源世界智能统一可复现推理与评估基础设施，覆盖视频3D、具身交互等场景
practical_value: '- 跨异构模型的模态适配器设计可直接复用：电商多模态推荐系统接入图文/视频/3D商品模型时，可通过该方案保留原生输入输出语义，大幅降低多模型集成的适配成本

  - 证据感知评分卡机制可迁移到推荐AB实验：将模型执行就绪度、指标计算证据与效果结论解耦，实现推荐策略迭代的全链路效果可追溯，减少无效实验结论

  - 持久化历史依赖状态建模思路可优化生成式推荐：在多轮交互推荐场景引入环境状态更新逻辑，提升推荐序列的时序一致性和因果合理性，降低用户困惑度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉生成模型仅追求视觉合理性，缺乏环境持久状态、物理动力学约束，输出无法保证交互后的因果一致性；同时世界模型领域缺少统一的执行与评估框架，异构模型的能力对比不可复现，难以区分感知生成与世界建模的能力差异。
### 方法关键点
明确定义生成式世界模型的5个核心能力维度：感知接地、持久状态建模、可控变换、动力学感知预测、闭环交互；推出WorldFoundry开源基础设施，通过模态专属适配器兼容多模态原生执行逻辑，统一模型/基准管理、执行编排、工件管理与可视化流程，引入显式清单、持久化工件契约、证据感知评分卡实现评估结论全链路可追溯。
### 关键结果
当前内置270个模型、74个基准、62个注册指标，支持视频/3D/4D、具身动作、交互世界系统的可复现推理与评估，可实现异构系统的可控动力学能力横向对比
